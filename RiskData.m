clear
clc
close all

filename = 'RiskData.csv';
CSVdata = readtable(filename);
TT = table2timetable(CSVdata);

plotting(TT)
xlabel('Time')
xtickangle(30)
ylabel('Risk score')

function plotting(TT)
    fh = figure;
    plotted = plot(TT.index,TT.Variables);
    %xticklabels(string(T.index))
    %xtickformat('dd-MM-yyyy HH:mm:ss')
    dcm = datacursormode(fh);
    datacursormode on
    set(dcm, 'updatefcn', {@myupdatefcn,TT,plotted})
end

function txt = myupdatefcn(~,event_obj,TT,plotted)
    for lines = 1:length(plotted)
        plotted(lines).LineWidth = 0.5;
    end
    % Customizes text of data tips
    pos = get(event_obj,'Position');
    I = get(event_obj, 'DataIndex');
    event_obj.Target.LineWidth = 3;
    columnData = event_obj.Target.YData;
    for index = 1:size(TT,2)
        data = TT{:,index}';
        if (data == columnData)
            break
        end
    end
    whichOne = char(TT.Properties.VariableNames(index));
    assignin('base','pos',pos)
    assignin('base','plotted',plotted)
    assignin('base','I',I)
    assignin('base','columnData',columnData)
    assignin('base','event_obj',event_obj)
    t = datenum(pos(1));
    new = addtodate(t,month(TT.index(1))-1, 'month');
    new = addtodate(new,year(TT.index(1)), 'year');
    new = datestr(addtodate(new,day(TT.index(1)), 'day'));
    txt = { ['ID: ',whichOne],...
            ['Date/Time: ',new],...
            ['Risk Score: ',num2str(pos(2))]};
end


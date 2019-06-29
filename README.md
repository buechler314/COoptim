# Weather Forcast & Distance Optimization

Last Updated: 2019-06-29 19:02:23.778248

Risk Parameters:

### probabilityOfPrecipitation
{'Weight': 0.8, 'Lower': 0, 'Upper': 20, 'NormUpper': 100, 'NormLower': 0}

### skyCover
{'Weight': 0.6, 'Lower': 0, 'Upper': 30, 'NormUpper': 100, 'NormLower': 0}

### windSpeed
{'Weight': 0.5, 'Lower': 0, 'Upper': 5, 'NormUpper': 40, 'NormLower': 0}

### temperature
{'Weight': 0.5, 'Lower': 5, 'Upper': 15, 'NormUpper': 32, 'NormLower': -10}

### lightningActivityLevel
{'Weight': 1, 'Lower': 0, 'Upper': 2, 'NormUpper': 6, 'NormLower': 0}

Location Used: NA,weight: 0.6

Cost Type: quad

## Risk Plot:

![Risks](https://buechler314.github.io/COoptim/risk.png)

## Trailheads risk scale: High to Low Risk

|                     | 0                          | 1                          | 2                          | 3                          | 4                          | 5                          | 6                  | 7                          | 8                          | 9                          | 10                 | 11                         | 12                         | 13                         | 14                 | 15                         | 16                 | 17                         | 18                 | 19                         | 20                         | 21                 | 22                         | 23                         | 24                         | 25                         | 26                         | 27                 | 28                 | 29                         | 30                 | 31                         | 32                         | 33                         | 34                 | 35                         |
|---------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|--------------------|----------------------------|----------------------------|----------------------------|--------------------|----------------------------|----------------------------|----------------------------|--------------------|----------------------------|--------------------|----------------------------|--------------------|----------------------------|----------------------------|--------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|--------------------|--------------------|----------------------------|--------------------|----------------------------|----------------------------|----------------------------|--------------------|----------------------------|
| 2019-06-29 08:00:00 | Castle Creek               | La Plata                   | Missouri Gulch             | North Elbert               | Mt Massive                 | Clear Creek                | Stewart Creek      | Longs Peak                 | Maroon Lake                | Baldwin Gulch              | Kite Lake          | Snowmass Creek             | Quandary                   | Mt Princeton Road          | Matterhorn Creek   | Lake Como                  | Fourmile Creek     | Half Moon                  | Shavano Tabeguache | Capitol Creek              | Yankee Boy Basin           | Grays Peak         | Denny Creek                | Rock of Ages               | Willow Creek               | Crags Campground           | Guanella Pass              | South Colony Lakes | Nellie Creek       | Silver Creek-Grizzly Gulch | N Cottonwood Creek | American Basin             | Culebra (main)             | Navajo Lake                | Needleton          | Huerfano-Lily Lake         |
| 2019-06-29 09:00:00 | Kite Lake                  | Quandary                   | Longs Peak                 | La Plata                   | Fourmile Creek             | Missouri Gulch             | Castle Creek       | Clear Creek                | Mt Massive                 | North Elbert               | Stewart Creek      | Grays Peak                 | Guanella Pass              | Lake Como                  | Baldwin Gulch      | Mt Princeton Road          | Maroon Lake        | Shavano Tabeguache         | Snowmass Creek     | Culebra (main)             | Huerfano-Lily Lake         | Willow Creek       | Matterhorn Creek           | Crags Campground           | Half Moon                  | Denny Creek                | South Colony Lakes         | Yankee Boy Basin   | Capitol Creek      | N Cottonwood Creek         | Rock of Ages       | Nellie Creek               | American Basin             | Silver Creek-Grizzly Gulch | Needleton          | Navajo Lake                |
| 2019-06-29 10:00:00 | Longs Peak                 | Kite Lake                  | Quandary                   | Fourmile Creek             | Grays Peak                 | Guanella Pass              | Castle Creek       | La Plata                   | Missouri Gulch             | Half Moon                  | Snowmass Creek     | Maroon Lake                | North Elbert               | Mt Massive                 | Stewart Creek      | Clear Creek                | Capitol Creek      | Lake Como                  | Willow Creek       | Mt Princeton Road          | Baldwin Gulch              | Shavano Tabeguache | Matterhorn Creek           | Crags Campground           | Culebra (main)             | Huerfano-Lily Lake         | South Colony Lakes         | Yankee Boy Basin   | Rock of Ages       | Denny Creek                | N Cottonwood Creek | Nellie Creek               | Navajo Lake                | Silver Creek-Grizzly Gulch | American Basin     | Needleton                  |
| 2019-06-29 11:00:00 | Longs Peak                 | Fourmile Creek             | Kite Lake                  | Quandary                   | Grays Peak                 | Guanella Pass              | North Elbert       | Mt Massive                 | La Plata                   | Missouri Gulch             | Castle Creek       | Stewart Creek              | Snowmass Creek             | Capitol Creek              | Maroon Lake        | Mt Princeton Road          | Crags Campground   | Willow Creek               | Lake Como          | Half Moon                  | Clear Creek                | Baldwin Gulch      | Shavano Tabeguache         | South Colony Lakes         | Matterhorn Creek           | N Cottonwood Creek         | Yankee Boy Basin           | Rock of Ages       | Culebra (main)     | Huerfano-Lily Lake         | Nellie Creek       | Denny Creek                | Navajo Lake                | Silver Creek-Grizzly Gulch | American Basin     | Needleton                  |
| 2019-06-29 12:00:00 | Guanella Pass              | Grays Peak                 | Quandary                   | Fourmile Creek             | Kite Lake                  | Longs Peak                 | Crags Campground   | Stewart Creek              | North Elbert               | Mt Massive                 | Yankee Boy Basin   | Matterhorn Creek           | Missouri Gulch             | Lake Como                  | American Basin     | Silver Creek-Grizzly Gulch | Nellie Creek       | La Plata                   | Half Moon          | Willow Creek               | Capitol Creek              | Clear Creek        | Snowmass Creek             | Mt Princeton Road          | N Cottonwood Creek         | Rock of Ages               | South Colony Lakes         | Shavano Tabeguache | Huerfano-Lily Lake | Baldwin Gulch              | Castle Creek       | Culebra (main)             | Denny Creek                | Maroon Lake                | Needleton          | Navajo Lake                |
| 2019-06-29 13:00:00 | Guanella Pass              | Grays Peak                 | Fourmile Creek             | Kite Lake                  | Silver Creek-Grizzly Gulch | American Basin             | Matterhorn Creek   | Nellie Creek               | Quandary                   | Stewart Creek              | Yankee Boy Basin   | Longs Peak                 | Crags Campground           | Missouri Gulch             | Denny Creek        | Culebra (main)             | North Elbert       | Mt Massive                 | La Plata           | Lake Como                  | Clear Creek                | Mt Princeton Road  | Willow Creek               | Baldwin Gulch              | N Cottonwood Creek         | South Colony Lakes         | Shavano Tabeguache         | Huerfano-Lily Lake | Snowmass Creek     | Half Moon                  | Rock of Ages       | Navajo Lake                | Capitol Creek              | Needleton                  | Castle Creek       | Maroon Lake                |
| 2019-06-29 14:00:00 | Silver Creek-Grizzly Gulch | American Basin             | Matterhorn Creek           | Nellie Creek               | Stewart Creek              | Guanella Pass              | Grays Peak         | Fourmile Creek             | Quandary                   | Kite Lake                  | Longs Peak         | Crags Campground           | Yankee Boy Basin           | Needleton                  | Culebra (main)     | North Elbert               | Mt Massive         | La Plata                   | Half Moon          | Rock of Ages               | Baldwin Gulch              | Clear Creek        | Mt Princeton Road          | Missouri Gulch             | N Cottonwood Creek         | Navajo Lake                | Shavano Tabeguache         | Denny Creek        | South Colony Lakes | Lake Como                  | Willow Creek       | Huerfano-Lily Lake         | Castle Creek               | Maroon Lake                | Capitol Creek      | Snowmass Creek             |
| 2019-06-29 15:00:00 | Silver Creek-Grizzly Gulch | American Basin             | Matterhorn Creek           | Stewart Creek              | Nellie Creek               | Crags Campground           | Baldwin Gulch      | N Cottonwood Creek         | Yankee Boy Basin           | Culebra (main)             | Guanella Pass      | Grays Peak                 | Quandary                   | Needleton                  | Fourmile Creek     | Longs Peak                 | Kite Lake          | Castle Creek               | Mt Massive         | North Elbert               | La Plata                   | Denny Creek        | Shavano Tabeguache         | Mt Princeton Road          | Clear Creek                | Half Moon                  | Rock of Ages               | Missouri Gulch     | South Colony Lakes | Snowmass Creek             | Navajo Lake        | Maroon Lake                | Willow Creek               | Huerfano-Lily Lake         | Capitol Creek      | Lake Como                  |
| 2019-06-29 16:00:00 | American Basin             | Silver Creek-Grizzly Gulch | Matterhorn Creek           | Nellie Creek               | Stewart Creek              | Guanella Pass              | Crags Campground   | Grays Peak                 | Quandary                   | Fourmile Creek             | Kite Lake          | Castle Creek               | Yankee Boy Basin           | Longs Peak                 | Needleton          | Baldwin Gulch              | N Cottonwood Creek | Culebra (main)             | La Plata           | Mt Massive                 | North Elbert               | Denny Creek        | Clear Creek                | Shavano Tabeguache         | Mt Princeton Road          | Missouri Gulch             | Half Moon                  | South Colony Lakes | Huerfano-Lily Lake | Navajo Lake                | Willow Creek       | Rock of Ages               | Lake Como                  | Maroon Lake                | Snowmass Creek     | Capitol Creek              |
| 2019-06-29 17:00:00 | Silver Creek-Grizzly Gulch | American Basin             | Matterhorn Creek           | Grays Peak                 | Guanella Pass              | Stewart Creek              | Quandary           | Fourmile Creek             | Kite Lake                  | Nellie Creek               | Crags Campground   | Culebra (main)             | Baldwin Gulch              | Longs Peak                 | N Cottonwood Creek | Needleton                  | South Colony Lakes | La Plata                   | Mt Massive         | North Elbert               | Denny Creek                | Clear Creek        | Mt Princeton Road          | Shavano Tabeguache         | Missouri Gulch             | Huerfano-Lily Lake         | Yankee Boy Basin           | Willow Creek       | Capitol Creek      | Navajo Lake                | Half Moon          | Snowmass Creek             | Lake Como                  | Rock of Ages               | Castle Creek       | Maroon Lake                |
| 2019-06-29 18:00:00 | Culebra (main)             | Grays Peak                 | Fourmile Creek             | Quandary                   | Guanella Pass              | Kite Lake                  | American Basin     | Crags Campground           | South Colony Lakes         | Willow Creek               | Matterhorn Creek   | Silver Creek-Grizzly Gulch | Huerfano-Lily Lake         | Baldwin Gulch              | N Cottonwood Creek | Stewart Creek              | La Plata           | Denny Creek                | Mt Princeton Road  | Mt Massive                 | North Elbert               | Clear Creek        | Lake Como                  | Missouri Gulch             | Half Moon                  | Longs Peak                 | Shavano Tabeguache         | Navajo Lake        | Nellie Creek       | Needleton                  | Snowmass Creek     | Castle Creek               | Capitol Creek              | Yankee Boy Basin           | Rock of Ages       | Maroon Lake                |
| 2019-06-29 19:00:00 | Grays Peak                 | Quandary                   | Fourmile Creek             | Culebra (main)             | Kite Lake                  | Guanella Pass              | Crags Campground   | Willow Creek               | Lake Como                  | South Colony Lakes         | American Basin     | Huerfano-Lily Lake         | N Cottonwood Creek         | Silver Creek-Grizzly Gulch | Mt Princeton Road  | Longs Peak                 | Baldwin Gulch      | Matterhorn Creek           | Denny Creek        | Shavano Tabeguache         | La Plata                   | Clear Creek        | Stewart Creek              | Missouri Gulch             | Mt Massive                 | North Elbert               | Needleton                  | Nellie Creek       | Yankee Boy Basin   | Castle Creek               | Half Moon          | Maroon Lake                | Navajo Lake                | Snowmass Creek             | Rock of Ages       | Capitol Creek              |
| 2019-06-29 20:00:00 | Grays Peak                 | Quandary                   | Fourmile Creek             | Kite Lake                  | Guanella Pass              | Culebra (main)             | Crags Campground   | Willow Creek               | Lake Como                  | Longs Peak                 | Huerfano-Lily Lake | Mt Princeton Road          | Baldwin Gulch              | South Colony Lakes         | N Cottonwood Creek | Shavano Tabeguache         | American Basin     | Denny Creek                | Missouri Gulch     | Silver Creek-Grizzly Gulch | Mt Massive                 | North Elbert       | La Plata                   | Clear Creek                | Matterhorn Creek           | Stewart Creek              | Needleton                  | Half Moon          | Nellie Creek       | Yankee Boy Basin           | Capitol Creek      | Navajo Lake                | Castle Creek               | Rock of Ages               | Snowmass Creek     | Maroon Lake                |
| 2019-06-29 21:00:00 | Grays Peak                 | Quandary                   | Fourmile Creek             | Kite Lake                  | Guanella Pass              | Lake Como                  | Crags Campground   | Culebra (main)             | Willow Creek               | Longs Peak                 | Huerfano-Lily Lake | Mt Princeton Road          | Baldwin Gulch              | Shavano Tabeguache         | South Colony Lakes | N Cottonwood Creek         | Denny Creek        | Missouri Gulch             | American Basin     | La Plata                   | Clear Creek                | Mt Massive         | North Elbert               | Silver Creek-Grizzly Gulch | Matterhorn Creek           | Half Moon                  | Stewart Creek              | Needleton          | Nellie Creek       | Maroon Lake                | Yankee Boy Basin   | Castle Creek               | Navajo Lake                | Rock of Ages               | Capitol Creek      | Snowmass Creek             |
| 2019-06-29 22:00:00 | Fourmile Creek             | Grays Peak                 | Quandary                   | Kite Lake                  | Guanella Pass              | Longs Peak                 | Lake Como          | Willow Creek               | Culebra (main)             | Crags Campground           | Huerfano-Lily Lake | American Basin             | Shavano Tabeguache         | Mt Princeton Road          | South Colony Lakes | Baldwin Gulch              | N Cottonwood Creek | Silver Creek-Grizzly Gulch | La Plata           | Denny Creek                | Missouri Gulch             | Mt Massive         | Clear Creek                | North Elbert               | Matterhorn Creek           | Stewart Creek              | Needleton                  | Half Moon          | Nellie Creek       | Yankee Boy Basin           | Navajo Lake        | Rock of Ages               | Castle Creek               | Maroon Lake                | Capitol Creek      | Snowmass Creek             |
| 2019-06-29 23:00:00 | Quandary                   | Fourmile Creek             | Grays Peak                 | Longs Peak                 | Kite Lake                  | Guanella Pass              | Lake Como          | Willow Creek               | Culebra (main)             | American Basin             | Crags Campground   | Huerfano-Lily Lake         | Silver Creek-Grizzly Gulch | South Colony Lakes         | Needleton          | Matterhorn Creek           | Nellie Creek       | Stewart Creek              | Yankee Boy Basin   | La Plata                   | Shavano Tabeguache         | Mt Princeton Road  | Rock of Ages               | N Cottonwood Creek         | Baldwin Gulch              | Denny Creek                | Navajo Lake                | Mt Massive         | Clear Creek        | Castle Creek               | Missouri Gulch     | North Elbert               | Half Moon                  | Maroon Lake                | Capitol Creek      | Snowmass Creek             |
| 2019-06-30 00:00:00 | Longs Peak                 | Fourmile Creek             | Kite Lake                  | Grays Peak                 | Quandary                   | Guanella Pass              | American Basin     | Matterhorn Creek           | Lake Como                  | Willow Creek               | Culebra (main)     | Silver Creek-Grizzly Gulch | Huerfano-Lily Lake         | South Colony Lakes         | Crags Campground   | Needleton                  | Stewart Creek      | Yankee Boy Basin           | Nellie Creek       | Rock of Ages               | Navajo Lake                | La Plata           | Half Moon                  | Castle Creek               | Shavano Tabeguache         | Maroon Lake                | Capitol Creek              | N Cottonwood Creek | Denny Creek        | Baldwin Gulch              | Mt Massive         | Clear Creek                | Mt Princeton Road          | Missouri Gulch             | North Elbert       | Snowmass Creek             |
| 2019-06-30 01:00:00 | Longs Peak                 | Fourmile Creek             | Kite Lake                  | Quandary                   | Grays Peak                 | American Basin             | Guanella Pass      | Silver Creek-Grizzly Gulch | Lake Como                  | Matterhorn Creek           | Huerfano-Lily Lake | Culebra (main)             | Needleton                  | Nellie Creek               | Yankee Boy Basin   | Willow Creek               | Crags Campground   | Rock of Ages               | Stewart Creek      | South Colony Lakes         | Navajo Lake                | Half Moon          | Castle Creek               | Maroon Lake                | Capitol Creek              | La Plata                   | Snowmass Creek             | Shavano Tabeguache | N Cottonwood Creek | Mt Massive                 | Clear Creek        | Mt Princeton Road          | Baldwin Gulch              | Missouri Gulch             | Denny Creek        | North Elbert               |
| 2019-06-30 02:00:00 | Longs Peak                 | Fourmile Creek             | Kite Lake                  | Grays Peak                 | Quandary                   | American Basin             | Guanella Pass      | Silver Creek-Grizzly Gulch | Matterhorn Creek           | Nellie Creek               | Yankee Boy Basin   | Huerfano-Lily Lake         | Needleton                  | Rock of Ages               | Lake Como          | Navajo Lake                | Culebra (main)     | Half Moon                  | Castle Creek       | Stewart Creek              | Crags Campground           | Maroon Lake        | Capitol Creek              | South Colony Lakes         | Willow Creek               | Snowmass Creek             | N Cottonwood Creek         | Mt Massive         | La Plata           | Clear Creek                | Mt Princeton Road  | Baldwin Gulch              | Shavano Tabeguache         | Missouri Gulch             | Denny Creek        | North Elbert               |
| 2019-06-30 03:00:00 | Longs Peak                 | Fourmile Creek             | American Basin             | Quandary                   | Kite Lake                  | Silver Creek-Grizzly Gulch | Matterhorn Creek   | Grays Peak                 | Nellie Creek               | Yankee Boy Basin           | Needleton          | Guanella Pass              | Rock of Ages               | Huerfano-Lily Lake         | Navajo Lake        | Half Moon                  | Castle Creek       | Maroon Lake                | Capitol Creek      | Lake Como                  | Snowmass Creek             | Stewart Creek      | Culebra (main)             | Crags Campground           | South Colony Lakes         | N Cottonwood Creek         | La Plata                   | Mt Massive         | Clear Creek        | Mt Princeton Road          | Baldwin Gulch      | Shavano Tabeguache         | Missouri Gulch             | Denny Creek                | Willow Creek       | North Elbert               |
| 2019-06-30 04:00:00 | Fourmile Creek             | Longs Peak                 | Kite Lake                  | Matterhorn Creek           | Silver Creek-Grizzly Gulch | American Basin             | Quandary           | Nellie Creek               | Yankee Boy Basin           | Grays Peak                 | Guanella Pass      | Needleton                  | Rock of Ages               | Navajo Lake                | Half Moon          | Maroon Lake                | Castle Creek       | Snowmass Creek             | Capitol Creek      | Stewart Creek              | Huerfano-Lily Lake         | South Colony Lakes | Crags Campground           | Lake Como                  | Culebra (main)             | Mt Massive                 | N Cottonwood Creek         | La Plata           | Clear Creek        | Mt Princeton Road          | Baldwin Gulch      | Shavano Tabeguache         | Missouri Gulch             | Denny Creek                | Willow Creek       | North Elbert               |
| 2019-06-30 05:00:00 | Fourmile Creek             | Matterhorn Creek           | Kite Lake                  | Longs Peak                 | American Basin             | Silver Creek-Grizzly Gulch | Nellie Creek       | Quandary                   | Yankee Boy Basin           | Grays Peak                 | Rock of Ages       | Guanella Pass              | Needleton                  | Castle Creek               | Navajo Lake        | Maroon Lake                | Half Moon          | Snowmass Creek             | Capitol Creek      | Stewart Creek              | South Colony Lakes         | La Plata           | Lake Como                  | N Cottonwood Creek         | Mt Massive                 | Clear Creek                | Mt Princeton Road          | Baldwin Gulch      | Shavano Tabeguache | Missouri Gulch             | Denny Creek        | Willow Creek               | Crags Campground           | Culebra (main)             | Huerfano-Lily Lake | North Elbert               |
| 2019-06-30 06:00:00 | American Basin             | Silver Creek-Grizzly Gulch | Matterhorn Creek           | Fourmile Creek             | Kite Lake                  | Nellie Creek               | Yankee Boy Basin   | Longs Peak                 | Quandary                   | Needleton                  | Rock of Ages       | Castle Creek               | Grays Peak                 | Maroon Lake                | Half Moon          | Navajo Lake                | Guanella Pass      | Snowmass Creek             | Capitol Creek      | South Colony Lakes         | Stewart Creek              | Shavano Tabeguache | Missouri Gulch             | Baldwin Gulch              | Clear Creek                | La Plata                   | Lake Como                  | N Cottonwood Creek | Mt Massive         | Mt Princeton Road          | Denny Creek        | Willow Creek               | Crags Campground           | Culebra (main)             | Huerfano-Lily Lake | North Elbert               |
| 2019-06-30 07:00:00 | Silver Creek-Grizzly Gulch | American Basin             | Matterhorn Creek           | Nellie Creek               | Fourmile Creek             | Yankee Boy Basin           | Longs Peak         | Kite Lake                  | Guanella Pass              | Needleton                  | Rock of Ages       | Castle Creek               | Navajo Lake                | Quandary                   | Maroon Lake        | Half Moon                  | South Colony Lakes | Snowmass Creek             | Grays Peak         | Stewart Creek              | Capitol Creek              | La Plata           | Denny Creek                | Shavano Tabeguache         | Missouri Gulch             | Mt Princeton Road          | Mt Massive                 | North Elbert       | Baldwin Gulch      | Willow Creek               | Crags Campground   | Culebra (main)             | Lake Como                  | N Cottonwood Creek         | Huerfano-Lily Lake | Clear Creek                |
| 2019-06-30 08:00:00 | Silver Creek-Grizzly Gulch | American Basin             | Matterhorn Creek           | Nellie Creek               | Guanella Pass              | Yankee Boy Basin           | Fourmile Creek     | Needleton                  | Castle Creek               | Navajo Lake                | Longs Peak         | Stewart Creek              | Kite Lake                  | Rock of Ages               | Maroon Lake        | South Colony Lakes         | Quandary           | Half Moon                  | Snowmass Creek     | Capitol Creek              | La Plata                   | Denny Creek        | Grays Peak                 | Mt Massive                 | North Elbert               | Mt Princeton Road          | Willow Creek               | Lake Como          | N Cottonwood Creek | Baldwin Gulch              | Crags Campground   | Missouri Gulch             | Huerfano-Lily Lake         | Shavano Tabeguache         | Culebra (main)     | Clear Creek                |
| 2019-06-30 09:00:00 | Silver Creek-Grizzly Gulch | American Basin             | Matterhorn Creek           | Nellie Creek               | Guanella Pass              | South Colony Lakes         | La Plata           | Longs Peak                 | Rock of Ages               | Mt Princeton Road          | Denny Creek        | Willow Creek               | Stewart Creek              | Lake Como                  | Baldwin Gulch      | Mt Massive                 | North Elbert       | Half Moon                  | Fourmile Creek     | N Cottonwood Creek         | Crags Campground           | Huerfano-Lily Lake | Needleton                  | Shavano Tabeguache         | Culebra (main)             | Missouri Gulch             | Clear Creek                | Castle Creek       | Navajo Lake        | Yankee Boy Basin           | Maroon Lake        | Snowmass Creek             | Capitol Creek              | Kite Lake                  | Quandary           | Grays Peak                 |
| 2019-06-30 10:00:00 | American Basin             | Silver Creek-Grizzly Gulch | Matterhorn Creek           | Nellie Creek               | Needleton                  | Castle Creek               | Navajo Lake        | Yankee Boy Basin           | Longs Peak                 | Stewart Creek              | Fourmile Creek     | Maroon Lake                | La Plata                   | Grays Peak                 | Rock of Ages       | Guanella Pass              | Kite Lake          | Mt Princeton Road          | Missouri Gulch     | Denny Creek                | South Colony Lakes         | Clear Creek        | Mt Massive                 | North Elbert               | Baldwin Gulch              | Willow Creek               | Lake Como                  | Culebra (main)     | Shavano Tabeguache | Huerfano-Lily Lake         | Crags Campground   | N Cottonwood Creek         | Half Moon                  | Snowmass Creek             | Quandary           | Capitol Creek              |
| 2019-06-30 11:00:00 | American Basin             | Silver Creek-Grizzly Gulch | Matterhorn Creek           | Nellie Creek               | Castle Creek               | Needleton                  | Navajo Lake        | Yankee Boy Basin           | Stewart Creek              | Maroon Lake                | Rock of Ages       | La Plata                   | Half Moon                  | Denny Creek                | Missouri Gulch     | Clear Creek                | Mt Massive         | North Elbert               | Longs Peak         | South Colony Lakes         | Huerfano-Lily Lake         | Culebra (main)     | Baldwin Gulch              | Fourmile Creek             | Shavano Tabeguache         | N Cottonwood Creek         | Mt Princeton Road          | Grays Peak         | Guanella Pass      | Willow Creek               | Crags Campground   | Snowmass Creek             | Lake Como                  | Capitol Creek              | Kite Lake          | Quandary                   |
| 2019-06-30 12:00:00 | American Basin             | Silver Creek-Grizzly Gulch | Matterhorn Creek           | Castle Creek               | Nellie Creek               | Needleton                  | Yankee Boy Basin   | Stewart Creek              | Navajo Lake                | Half Moon                  | Maroon Lake        | Rock of Ages               | Denny Creek                | La Plata                   | Clear Creek        | Missouri Gulch             | Mt Massive         | North Elbert               | Snowmass Creek     | Capitol Creek              | Huerfano-Lily Lake         | South Colony Lakes | Grays Peak                 | Longs Peak                 | Guanella Pass              | Culebra (main)             | Baldwin Gulch              | N Cottonwood Creek | Kite Lake          | Fourmile Creek             | Shavano Tabeguache | Crags Campground           | Willow Creek               | Mt Princeton Road          | Quandary           | Lake Como                  |
| 2019-06-30 13:00:00 | American Basin             | Silver Creek-Grizzly Gulch | Matterhorn Creek           | Nellie Creek               | Castle Creek               | Needleton                  | Yankee Boy Basin   | Stewart Creek              | Navajo Lake                | Half Moon                  | Rock of Ages       | Maroon Lake                | Denny Creek                | La Plata                   | Mt Massive         | North Elbert               | Missouri Gulch     | Clear Creek                | Grays Peak         | Guanella Pass              | Kite Lake                  | Fourmile Creek     | Baldwin Gulch              | Culebra (main)             | Huerfano-Lily Lake         | Snowmass Creek             | Shavano Tabeguache         | N Cottonwood Creek | Longs Peak         | South Colony Lakes         | Crags Campground   | Quandary                   | Mt Princeton Road          | Willow Creek               | Capitol Creek      | Lake Como                  |
| 2019-06-30 14:00:00 | Silver Creek-Grizzly Gulch | American Basin             | Nellie Creek               | Matterhorn Creek           | Castle Creek               | Needleton                  | Half Moon          | Yankee Boy Basin           | Maroon Lake                | Stewart Creek              | Navajo Lake        | Denny Creek                | Rock of Ages               | Kite Lake                  | Guanella Pass      | Grays Peak                 | Mt Massive         | North Elbert               | Fourmile Creek     | La Plata                   | Clear Creek                | Missouri Gulch     | Baldwin Gulch              | Shavano Tabeguache         | N Cottonwood Creek         | Longs Peak                 | Culebra (main)             | Snowmass Creek     | Crags Campground   | Huerfano-Lily Lake         | Quandary           | Mt Princeton Road          | South Colony Lakes         | Willow Creek               | Lake Como          | Capitol Creek              |
| 2019-06-30 15:00:00 | Silver Creek-Grizzly Gulch | American Basin             | Nellie Creek               | Matterhorn Creek           | Half Moon                  | Castle Creek               | Maroon Lake        | Denny Creek                | Stewart Creek              | Yankee Boy Basin           | North Elbert       | Mt Massive                 | Needleton                  | Kite Lake                  | Navajo Lake        | Baldwin Gulch              | Clear Creek        | Missouri Gulch             | Guanella Pass      | Shavano Tabeguache         | Fourmile Creek             | La Plata           | Quandary                   | Grays Peak                 | Longs Peak                 | N Cottonwood Creek         | Rock of Ages               | Culebra (main)     | Huerfano-Lily Lake | Crags Campground           | South Colony Lakes | Mt Princeton Road          | Snowmass Creek             | Willow Creek               | Lake Como          | Capitol Creek              |
| 2019-06-30 16:00:00 | Silver Creek-Grizzly Gulch | American Basin             | Matterhorn Creek           | Castle Creek               | Nellie Creek               | Half Moon                  | Maroon Lake        | Needleton                  | Denny Creek                | Yankee Boy Basin           | Kite Lake          | Grays Peak                 | Guanella Pass              | Stewart Creek              | Navajo Lake        | Quandary                   | Baldwin Gulch      | Fourmile Creek             | North Elbert       | Mt Massive                 | Shavano Tabeguache         | Clear Creek        | La Plata                   | Missouri Gulch             | N Cottonwood Creek         | Longs Peak                 | South Colony Lakes         | Huerfano-Lily Lake | Mt Princeton Road  | Rock of Ages               | Willow Creek       | Crags Campground           | Culebra (main)             | Lake Como                  | Snowmass Creek     | Capitol Creek              |
| 2019-06-30 17:00:00 | Castle Creek               | American Basin             | Guanella Pass              | Silver Creek-Grizzly Gulch | Grays Peak                 | Denny Creek                | Matterhorn Creek   | Kite Lake                  | Yankee Boy Basin           | Needleton                  | Baldwin Gulch      | Shavano Tabeguache         | South Colony Lakes         | Clear Creek                | Stewart Creek      | La Plata                   | Nellie Creek       | Quandary                   | Longs Peak         | Half Moon                  | Fourmile Creek             | Mt Massive         | North Elbert               | Maroon Lake                | N Cottonwood Creek         | Missouri Gulch             | Willow Creek               | Mt Princeton Road  | Huerfano-Lily Lake | Navajo Lake                | Lake Como          | Crags Campground           | Culebra (main)             | Rock of Ages               | Snowmass Creek     | Capitol Creek              |
| 2019-06-30 18:00:00 | South Colony Lakes         | American Basin             | Silver Creek-Grizzly Gulch | Castle Creek               | Denny Creek                | Grays Peak                 | Baldwin Gulch      | N Cottonwood Creek         | Matterhorn Creek           | Guanella Pass              | Mt Princeton Road  | Willow Creek               | Kite Lake                  | Clear Creek                | Shavano Tabeguache | Stewart Creek              | La Plata           | Culebra (main)             | Nellie Creek       | Huerfano-Lily Lake         | Missouri Gulch             | Quandary           | North Elbert               | Mt Massive                 | Fourmile Creek             | Maroon Lake                | Needleton                  | Yankee Boy Basin   | Lake Como          | Crags Campground           | Half Moon          | Longs Peak                 | Navajo Lake                | Capitol Creek              | Snowmass Creek     | Rock of Ages               |
| 2019-06-30 19:00:00 | South Colony Lakes         | American Basin             | Silver Creek-Grizzly Gulch | Grays Peak                 | Baldwin Gulch              | Castle Creek               | Mt Princeton Road  | Denny Creek                | Guanella Pass              | Matterhorn Creek           | Willow Creek       | N Cottonwood Creek         | Kite Lake                  | Shavano Tabeguache         | Culebra (main)     | Stewart Creek              | Clear Creek        | Huerfano-Lily Lake         | Nellie Creek       | La Plata                   | Quandary                   | Missouri Gulch     | Fourmile Creek             | North Elbert               | Mt Massive                 | Maroon Lake                | Yankee Boy Basin           | Lake Como          | Needleton          | Crags Campground           | Half Moon          | Longs Peak                 | Navajo Lake                | Capitol Creek              | Snowmass Creek     | Rock of Ages               |
| 2019-06-30 20:00:00 | South Colony Lakes         | Baldwin Gulch              | Grays Peak                 | American Basin             | Guanella Pass              | Mt Princeton Road          | Denny Creek        | Silver Creek-Grizzly Gulch | Castle Creek               | Shavano Tabeguache         | Matterhorn Creek   | Willow Creek               | Kite Lake                  | N Cottonwood Creek         | Culebra (main)     | Quandary                   | Stewart Creek      | Huerfano-Lily Lake         | Clear Creek        | Missouri Gulch             | Fourmile Creek             | Nellie Creek       | Mt Massive                 | North Elbert               | La Plata                   | Half Moon                  | Maroon Lake                | Yankee Boy Basin   | Crags Campground   | Lake Como                  | Needleton          | Longs Peak                 | Capitol Creek              | Snowmass Creek             | Navajo Lake        | Rock of Ages               |
| 2019-06-30 21:00:00 | South Colony Lakes         | Shavano Tabeguache         | Mt Princeton Road          | Grays Peak                 | Kite Lake                  | Half Moon                  | Castle Creek       | Guanella Pass              | Quandary                   | Willow Creek               | Denny Creek        | N Cottonwood Creek         | Baldwin Gulch              | Matterhorn Creek           | Culebra (main)     | Silver Creek-Grizzly Gulch | Huerfano-Lily Lake | Stewart Creek              | American Basin     | Crags Campground           | Clear Creek                | Maroon Lake        | Fourmile Creek             | Nellie Creek               | Missouri Gulch             | Mt Massive                 | North Elbert               | Capitol Creek      | La Plata           | Yankee Boy Basin           | Snowmass Creek     | Lake Como                  | Longs Peak                 | Needleton                  | Navajo Lake        | Rock of Ages               |
| 2019-06-30 22:00:00 | Half Moon                  | Grays Peak                 | Silver Creek-Grizzly Gulch | Castle Creek               | Matterhorn Creek           | South Colony Lakes         | American Basin     | Quandary                   | Culebra (main)             | Huerfano-Lily Lake         | Kite Lake          | Guanella Pass              | Nellie Creek               | Fourmile Creek             | Baldwin Gulch      | Willow Creek               | Mt Princeton Road  | Maroon Lake                | Crags Campground   | Shavano Tabeguache         | Yankee Boy Basin           | Denny Creek        | La Plata                   | Stewart Creek              | N Cottonwood Creek         | Mt Massive                 | North Elbert               | Missouri Gulch     | Capitol Creek      | Clear Creek                | Snowmass Creek     | Needleton                  | Lake Como                  | Longs Peak                 | Rock of Ages       | Navajo Lake                |
| 2019-06-30 23:00:00 | American Basin             | Silver Creek-Grizzly Gulch | Nellie Creek               | Matterhorn Creek           | Needleton                  | Half Moon                  | Grays Peak         | Yankee Boy Basin           | Castle Creek               | Quandary                   | Guanella Pass      | Rock of Ages               | Kite Lake                  | Fourmile Creek             | North Elbert       | La Plata                   | Culebra (main)     | Mt Massive                 | Crags Campground   | Navajo Lake                | Stewart Creek              | Longs Peak         | Clear Creek                | Missouri Gulch             | Willow Creek               | Huerfano-Lily Lake         | Maroon Lake                | South Colony Lakes | Denny Creek        | Baldwin Gulch              | Mt Princeton Road  | Snowmass Creek             | N Cottonwood Creek         | Lake Como                  | Capitol Creek      | Shavano Tabeguache         |
| 2019-07-01 00:00:00 | American Basin             | Needleton                  | Silver Creek-Grizzly Gulch | Nellie Creek               | Matterhorn Creek           | Yankee Boy Basin           | Grays Peak         | Half Moon                  | Castle Creek               | Rock of Ages               | Fourmile Creek     | Guanella Pass              | Quandary                   | Navajo Lake                | Longs Peak         | Kite Lake                  | Crags Campground   | La Plata                   | Mt Massive         | North Elbert               | Stewart Creek              | Clear Creek        | Missouri Gulch             | Willow Creek               | Maroon Lake                | Snowmass Creek             | Huerfano-Lily Lake         | Culebra (main)     | Denny Creek        | N Cottonwood Creek         | Mt Princeton Road  | Baldwin Gulch              | Capitol Creek              | Lake Como                  | South Colony Lakes | Shavano Tabeguache         |
| 2019-07-01 01:00:00 | American Basin             | Silver Creek-Grizzly Gulch | Nellie Creek               | Matterhorn Creek           | Needleton                  | Yankee Boy Basin           | Longs Peak         | Castle Creek               | Navajo Lake                | Half Moon                  | Rock of Ages       | Kite Lake                  | Fourmile Creek             | Quandary                   | Stewart Creek      | Guanella Pass              | Grays Peak         | Crags Campground           | Maroon Lake        | La Plata                   | Mt Massive                 | North Elbert       | Clear Creek                | Snowmass Creek             | Denny Creek                | Missouri Gulch             | Willow Creek               | Baldwin Gulch      | Huerfano-Lily Lake | Culebra (main)             | Mt Princeton Road  | Shavano Tabeguache         | Capitol Creek              | N Cottonwood Creek         | South Colony Lakes | Lake Como                  |
| 2019-07-01 02:00:00 | American Basin             | Silver Creek-Grizzly Gulch | Matterhorn Creek           | Nellie Creek               | Needleton                  | Longs Peak                 | Stewart Creek      | Yankee Boy Basin           | Castle Creek               | Crags Campground           | Kite Lake          | Fourmile Creek             | Quandary                   | Navajo Lake                | Half Moon          | Rock of Ages               | Shavano Tabeguache | Clear Creek                | Baldwin Gulch      | Mt Massive                 | North Elbert               | Maroon Lake        | Denny Creek                | La Plata                   | Guanella Pass              | Willow Creek               | Grays Peak                 | Mt Princeton Road  | Missouri Gulch     | Snowmass Creek             | N Cottonwood Creek | South Colony Lakes         | Huerfano-Lily Lake         | Lake Como                  | Capitol Creek      | Culebra (main)             |
| 2019-07-01 03:00:00 | Castle Creek               | Silver Creek-Grizzly Gulch | American Basin             | Matterhorn Creek           | Nellie Creek               | Stewart Creek              | Longs Peak         | Needleton                  | Yankee Boy Basin           | Crags Campground           | Shavano Tabeguache | Kite Lake                  | Fourmile Creek             | Quandary                   | Half Moon          | Baldwin Gulch              | Navajo Lake        | Clear Creek                | Denny Creek        | Maroon Lake                | Rock of Ages               | Mt Massive         | North Elbert               | Mt Princeton Road          | South Colony Lakes         | Willow Creek               | La Plata                   | Lake Como          | N Cottonwood Creek | Guanella Pass              | Capitol Creek      | Grays Peak                 | Snowmass Creek             | Huerfano-Lily Lake         | Missouri Gulch     | Culebra (main)             |
| 2019-07-01 04:00:00 | Castle Creek               | Stewart Creek              | Nellie Creek               | Silver Creek-Grizzly Gulch | American Basin             | Matterhorn Creek           | Longs Peak         | Needleton                  | Crags Campground           | Yankee Boy Basin           | Kite Lake          | Fourmile Creek             | Quandary                   | Navajo Lake                | Baldwin Gulch      | Shavano Tabeguache         | Rock of Ages       | Half Moon                  | Clear Creek        | Denny Creek                | Maroon Lake                | South Colony Lakes | Mt Massive                 | North Elbert               | Willow Creek               | La Plata                   | Capitol Creek              | Snowmass Creek     | Huerfano-Lily Lake | Mt Princeton Road          | Lake Como          | N Cottonwood Creek         | Guanella Pass              | Grays Peak                 | Missouri Gulch     | Culebra (main)             |
| 2019-07-01 05:00:00 | Castle Creek               | Stewart Creek              | Nellie Creek               | Crags Campground           | Silver Creek-Grizzly Gulch | American Basin             | Matterhorn Creek   | Needleton                  | Yankee Boy Basin           | Navajo Lake                | Rock of Ages       | Longs Peak                 | South Colony Lakes         | Baldwin Gulch              | Denny Creek        | Snowmass Creek             | Capitol Creek      | Huerfano-Lily Lake         | Clear Creek        | La Plata                   | Mt Massive                 | North Elbert       | Shavano Tabeguache         | Willow Creek               | Guanella Pass              | Fourmile Creek             | Kite Lake                  | Quandary           | Maroon Lake        | Lake Como                  | N Cottonwood Creek | Grays Peak                 | Missouri Gulch             | Mt Princeton Road          | Half Moon          | Culebra (main)             |
| 2019-07-01 06:00:00 | Castle Creek               | Stewart Creek              | Crags Campground           | Nellie Creek               | Grays Peak                 | South Colony Lakes         | Guanella Pass      | Huerfano-Lily Lake         | Denny Creek                | Maroon Lake                | Capitol Creek      | Half Moon                  | Snowmass Creek             | La Plata                   | Baldwin Gulch      | Mt Massive                 | North Elbert       | Clear Creek                | Fourmile Creek     | N Cottonwood Creek         | Kite Lake                  | Quandary           | Missouri Gulch             | Willow Creek               | Mt Princeton Road          | Shavano Tabeguache         | Lake Como                  | Culebra (main)     | Longs Peak         | Needleton                  | Navajo Lake        | American Basin             | Silver Creek-Grizzly Gulch | Yankee Boy Basin           | Rock of Ages       | Matterhorn Creek           |
| 2019-07-01 07:00:00 | Castle Creek               | Stewart Creek              | Crags Campground           | Nellie Creek               | Grays Peak                 | Guanella Pass              | La Plata           | North Elbert               | Mt Massive                 | Missouri Gulch             | Clear Creek        | Denny Creek                | South Colony Lakes         | N Cottonwood Creek         | Longs Peak         | Baldwin Gulch              | Huerfano-Lily Lake | Mt Princeton Road          | Quandary           | Willow Creek               | Fourmile Creek             | Shavano Tabeguache | Kite Lake                  | Half Moon                  | Culebra (main)             | Lake Como                  | Maroon Lake                | Snowmass Creek     | Capitol Creek      | Navajo Lake                | Needleton          | Yankee Boy Basin           | American Basin             | Matterhorn Creek           | Rock of Ages       | Silver Creek-Grizzly Gulch |
| 2019-07-01 08:00:00 | Castle Creek               | Stewart Creek              | Crags Campground           | Guanella Pass              | Grays Peak                 | Longs Peak                 | North Elbert       | Mt Massive                 | La Plata                   | Nellie Creek               | Clear Creek        | Missouri Gulch             | Denny Creek                | N Cottonwood Creek         | South Colony Lakes | Baldwin Gulch              | Mt Princeton Road  | Shavano Tabeguache         | Huerfano-Lily Lake | Kite Lake                  | Quandary                   | Willow Creek       | Culebra (main)             | Fourmile Creek             | Lake Como                  | Half Moon                  | Maroon Lake                | Snowmass Creek     | Capitol Creek      | Matterhorn Creek           | American Basin     | Silver Creek-Grizzly Gulch | Yankee Boy Basin           | Needleton                  | Rock of Ages       | Navajo Lake                |
| 2019-07-01 09:00:00 | Crags Campground           | Stewart Creek              | Guanella Pass              | Longs Peak                 | Grays Peak                 | Castle Creek               | North Elbert       | Mt Massive                 | La Plata                   | Clear Creek                | Missouri Gulch     | N Cottonwood Creek         | Denny Creek                | South Colony Lakes         | Mt Princeton Road  | Nellie Creek               | Baldwin Gulch      | Kite Lake                  | Shavano Tabeguache | Quandary                   | Huerfano-Lily Lake         | Fourmile Creek     | Willow Creek               | Culebra (main)             | Lake Como                  | Half Moon                  | Silver Creek-Grizzly Gulch | American Basin     | Matterhorn Creek   | Maroon Lake                | Yankee Boy Basin   | Needleton                  | Snowmass Creek             | Capitol Creek              | Rock of Ages       | Navajo Lake                |
| 2019-07-01 10:00:00 | Crags Campground           | Guanella Pass              | Longs Peak                 | Stewart Creek              | Grays Peak                 | South Colony Lakes         | Castle Creek       | North Elbert               | Mt Massive                 | Denny Creek                | Clear Creek        | Willow Creek               | N Cottonwood Creek         | La Plata                   | Huerfano-Lily Lake | Missouri Gulch             | Mt Princeton Road  | Baldwin Gulch              | Kite Lake          | Fourmile Creek             | Shavano Tabeguache         | Culebra (main)     | Lake Como                  | Quandary                   | Nellie Creek               | Silver Creek-Grizzly Gulch | American Basin             | Matterhorn Creek   | Half Moon          | Yankee Boy Basin           | Maroon Lake        | Needleton                  | Snowmass Creek             | Capitol Creek              | Rock of Ages       | Navajo Lake                |
| 2019-07-01 11:00:00 | South Colony Lakes         | Guanella Pass              | Crags Campground           | Grays Peak                 | Longs Peak                 | Stewart Creek              | Willow Creek       | Huerfano-Lily Lake         | Culebra (main)             | Castle Creek               | Fourmile Creek     | Mt Princeton Road          | Lake Como                  | Denny Creek                | Kite Lake          | Shavano Tabeguache         | Baldwin Gulch      | N Cottonwood Creek         | Mt Massive         | North Elbert               | Nellie Creek               | Clear Creek        | Silver Creek-Grizzly Gulch | American Basin             | Missouri Gulch             | La Plata                   | Quandary                   | Matterhorn Creek   | Yankee Boy Basin   | Maroon Lake                | Needleton          | Half Moon                  | Snowmass Creek             | Capitol Creek              | Rock of Ages       | Navajo Lake                |
| 2019-07-01 12:00:00 | South Colony Lakes         | Silver Creek-Grizzly Gulch | American Basin             | Willow Creek               | Matterhorn Creek           | Huerfano-Lily Lake         | Guanella Pass      | Culebra (main)             | Grays Peak                 | Nellie Creek               | Crags Campground   | Fourmile Creek             | Longs Peak                 | Lake Como                  | Castle Creek       | Kite Lake                  | Mt Princeton Road  | Stewart Creek              | Shavano Tabeguache | Denny Creek                | Baldwin Gulch              | Quandary           | N Cottonwood Creek         | Mt Massive                 | North Elbert               | Clear Creek                | Missouri Gulch             | Yankee Boy Basin   | La Plata           | Needleton                  | Maroon Lake        | Half Moon                  | Capitol Creek              | Snowmass Creek             | Rock of Ages       | Navajo Lake                |
| 2019-07-01 13:00:00 | South Colony Lakes         | Willow Creek               | Huerfano-Lily Lake         | Culebra (main)             | Silver Creek-Grizzly Gulch | Guanella Pass              | American Basin     | Crags Campground           | Lake Como                  | Grays Peak                 | Fourmile Creek     | Matterhorn Creek           | Kite Lake                  | Castle Creek               | Longs Peak         | Shavano Tabeguache         | Baldwin Gulch      | Stewart Creek              | Mt Princeton Road  | Nellie Creek               | Denny Creek                | N Cottonwood Creek | Quandary                   | Clear Creek                | Missouri Gulch             | La Plata                   | Mt Massive                 | North Elbert       | Maroon Lake        | Yankee Boy Basin           | Half Moon          | Needleton                  | Capitol Creek              | Snowmass Creek             | Rock of Ages       | Navajo Lake                |
| 2019-07-01 14:00:00 | South Colony Lakes         | Culebra (main)             | Willow Creek               | Huerfano-Lily Lake         | Lake Como                  | Crags Campground           | Guanella Pass      | Fourmile Creek             | Silver Creek-Grizzly Gulch | Kite Lake                  | American Basin     | Grays Peak                 | Castle Creek               | Baldwin Gulch              | Shavano Tabeguache | Stewart Creek              | Quandary           | Denny Creek                | Matterhorn Creek   | Mt Princeton Road          | N Cottonwood Creek         | Longs Peak         | Nellie Creek               | Clear Creek                | La Plata                   | Missouri Gulch             | Mt Massive                 | North Elbert       | Half Moon          | Maroon Lake                | Capitol Creek      | Snowmass Creek             | Needleton                  | Yankee Boy Basin           | Rock of Ages       | Navajo Lake                |
| 2019-07-01 15:00:00 | South Colony Lakes         | Culebra (main)             | Huerfano-Lily Lake         | Willow Creek               | Lake Como                  | Crags Campground           | Fourmile Creek     | Guanella Pass              | Kite Lake                  | Silver Creek-Grizzly Gulch | Grays Peak         | American Basin             | Baldwin Gulch              | Stewart Creek              | Shavano Tabeguache | Quandary                   | Half Moon          | Denny Creek                | Capitol Creek      | Mt Princeton Road          | Castle Creek               | Clear Creek        | N Cottonwood Creek         | La Plata                   | Missouri Gulch             | Snowmass Creek             | Mt Massive                 | North Elbert       | Matterhorn Creek   | Nellie Creek               | Longs Peak         | Maroon Lake                | Needleton                  | Yankee Boy Basin           | Rock of Ages       | Navajo Lake                |
| 2019-07-01 16:00:00 | South Colony Lakes         | Culebra (main)             | Huerfano-Lily Lake         | Willow Creek               | Crags Campground           | Lake Como                  | Fourmile Creek     | Guanella Pass              | Shavano Tabeguache         | Kite Lake                  | Baldwin Gulch      | Stewart Creek              | Mt Princeton Road          | Denny Creek                | N Cottonwood Creek | Grays Peak                 | Clear Creek        | La Plata                   | Missouri Gulch     | Quandary                   | Silver Creek-Grizzly Gulch | North Elbert       | Mt Massive                 | American Basin             | Castle Creek               | Capitol Creek              | Half Moon                  | Snowmass Creek     | Longs Peak         | Matterhorn Creek           | Nellie Creek       | Maroon Lake                | Needleton                  | Yankee Boy Basin           | Rock of Ages       | Navajo Lake                |
| 2019-07-01 17:00:00 | South Colony Lakes         | Culebra (main)             | Crags Campground           | Willow Creek               | Huerfano-Lily Lake         | Lake Como                  | Shavano Tabeguache | Guanella Pass              | Baldwin Gulch              | Stewart Creek              | Mt Princeton Road  | Fourmile Creek             | N Cottonwood Creek         | Denny Creek                | Clear Creek        | Missouri Gulch             | Grays Peak         | La Plata                   | Kite Lake          | North Elbert               | Mt Massive                 | Quandary           | Castle Creek               | Silver Creek-Grizzly Gulch | American Basin             | Longs Peak                 | Capitol Creek              | Half Moon          | Snowmass Creek     | Nellie Creek               | Matterhorn Creek   | Maroon Lake                | Needleton                  | Yankee Boy Basin           | Rock of Ages       | Navajo Lake                |
| 2019-07-01 18:00:00 | Culebra (main)             | South Colony Lakes         | Crags Campground           | Willow Creek               | Huerfano-Lily Lake         | Lake Como                  | Shavano Tabeguache | Mt Princeton Road          | Baldwin Gulch              | Stewart Creek              | N Cottonwood Creek | Guanella Pass              | Denny Creek                | Clear Creek                | Missouri Gulch     | La Plata                   | Fourmile Creek     | North Elbert               | Mt Massive         | Grays Peak                 | Kite Lake                  | Quandary           | Castle Creek               | Longs Peak                 | Silver Creek-Grizzly Gulch | Nellie Creek               | American Basin             | Matterhorn Creek   | Maroon Lake        | Half Moon                  | Capitol Creek      | Snowmass Creek             | Needleton                  | Yankee Boy Basin           | Rock of Ages       | Navajo Lake                |
| 2019-07-01 19:00:00 | South Colony Lakes         | Culebra (main)             | Crags Campground           | Huerfano-Lily Lake         | Willow Creek               | Lake Como                  | Shavano Tabeguache | Baldwin Gulch              | Mt Princeton Road          | N Cottonwood Creek         | Denny Creek        | Stewart Creek              | Missouri Gulch             | Clear Creek                | Guanella Pass      | La Plata                   | Fourmile Creek     | North Elbert               | Mt Massive         | Kite Lake                  | Grays Peak                 | Quandary           | Longs Peak                 | Castle Creek               | Silver Creek-Grizzly Gulch | American Basin             | Nellie Creek               | Matterhorn Creek   | Maroon Lake        | Snowmass Creek             | Half Moon          | Capitol Creek              | Needleton                  | Yankee Boy Basin           | Rock of Ages       | Navajo Lake                |
| 2019-07-01 20:00:00 | South Colony Lakes         | Culebra (main)             | Crags Campground           | Huerfano-Lily Lake         | Willow Creek               | Lake Como                  | Shavano Tabeguache | Baldwin Gulch              | Mt Princeton Road          | N Cottonwood Creek         | Denny Creek        | Missouri Gulch             | Clear Creek                | Stewart Creek              | La Plata           | North Elbert               | Mt Massive         | Guanella Pass              | Fourmile Creek     | Kite Lake                  | Grays Peak                 | Quandary           | Longs Peak                 | Castle Creek               | Silver Creek-Grizzly Gulch | American Basin             | Maroon Lake                | Nellie Creek       | Matterhorn Creek   | Snowmass Creek             | Capitol Creek      | Half Moon                  | Needleton                  | Yankee Boy Basin           | Rock of Ages       | Navajo Lake                |
| 2019-07-01 21:00:00 | Culebra (main)             | South Colony Lakes         | Crags Campground           | Huerfano-Lily Lake         | Willow Creek               | Lake Como                  | Shavano Tabeguache | Baldwin Gulch              | N Cottonwood Creek         | Denny Creek                | Mt Princeton Road  | Missouri Gulch             | Clear Creek                | Stewart Creek              | La Plata           | North Elbert               | Mt Massive         | Fourmile Creek             | Guanella Pass      | Kite Lake                  | Grays Peak                 | Longs Peak         | Quandary                   | Castle Creek               | Maroon Lake                | Silver Creek-Grizzly Gulch | American Basin             | Nellie Creek       | Matterhorn Creek   | Snowmass Creek             | Capitol Creek      | Half Moon                  | Yankee Boy Basin           | Needleton                  | Rock of Ages       | Navajo Lake                |
| 2019-07-01 22:00:00 | Culebra (main)             | South Colony Lakes         | Crags Campground           | Huerfano-Lily Lake         | Lake Como                  | Willow Creek               | Baldwin Gulch      | Shavano Tabeguache         | Denny Creek                | N Cottonwood Creek         | Mt Princeton Road  | Clear Creek                | Missouri Gulch             | Stewart Creek              | La Plata           | North Elbert               | Mt Massive         | Guanella Pass              | Fourmile Creek     | Kite Lake                  | Grays Peak                 | Longs Peak         | Quandary                   | Castle Creek               | Silver Creek-Grizzly Gulch | Maroon Lake                | American Basin             | Matterhorn Creek   | Nellie Creek       | Snowmass Creek             | Half Moon          | Capitol Creek              | Needleton                  | Yankee Boy Basin           | Rock of Ages       | Navajo Lake                |
| 2019-07-01 23:00:00 | Culebra (main)             | Crags Campground           | South Colony Lakes         | Huerfano-Lily Lake         | Lake Como                  | Willow Creek               | Baldwin Gulch      | Shavano Tabeguache         | Denny Creek                | N Cottonwood Creek         | Clear Creek        | Stewart Creek              | Mt Princeton Road          | Missouri Gulch             | Guanella Pass      | La Plata                   | Fourmile Creek     | Kite Lake                  | North Elbert       | Mt Massive                 | Grays Peak                 | Longs Peak         | Quandary                   | Castle Creek               | American Basin             | Silver Creek-Grizzly Gulch | Maroon Lake                | Matterhorn Creek   | Half Moon          | Nellie Creek               | Snowmass Creek     | Capitol Creek              | Needleton                  | Yankee Boy Basin           | Navajo Lake        | Rock of Ages               |

## North Elbert

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      2       |    46      |    0.514444 |      13.3333  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      3.5     |    49      |    1.02889  |      15       |                  1.33333 |
|  2 | 2019-06-29 10:00:00 |                      5       |    53      |    1.54333  |      17.7778  |                  1.5     |
|  3 | 2019-06-29 11:00:00 |                      7       |    58      |    3.08666  |      20       |                  1.66667 |
|  4 | 2019-06-29 12:00:00 |                     10       |    62      |    4.11555  |      18.8889  |                  2       |
|  5 | 2019-06-29 13:00:00 |                     24       |    64      |    4.63     |      20       |                  3       |
|  6 | 2019-06-29 14:00:00 |                     38       |    65      |    4.11555  |      21.1111  |                  4       |
|  7 | 2019-06-29 15:00:00 |                     52       |    67      |    3.85833  |      20.8333  |                  3.875   |
|  8 | 2019-06-29 16:00:00 |                     48       |    72      |    3.60111  |      20.5556  |                  3.75    |
|  9 | 2019-06-29 17:00:00 |                     44       |    78      |    3.34389  |      19.4444  |                  3.625   |
| 10 | 2019-06-29 18:00:00 |                     41       |    83      |    3.08666  |      18.8889  |                  3.5     |
| 11 | 2019-06-29 19:00:00 |                     36       |    78      |    2.57222  |      16.6667  |                  3.375   |
| 12 | 2019-06-29 20:00:00 |                     32       |    74      |    2.315    |      13.8889  |                  3.25    |
| 13 | 2019-06-29 21:00:00 |                     27       |    69      |    2.05778  |      11.6667  |                  3.125   |
| 14 | 2019-06-29 22:00:00 |                     19       |    57      |    1.54333  |      10.5556  |                  3       |
| 15 | 2019-06-29 23:00:00 |                     11       |    45      |    1.64622  |      10       |                  2       |
| 16 | 2019-06-30 00:00:00 |                      3       |    33      |    1.74911  |       9.44444 |                  1       |
| 17 | 2019-06-30 01:00:00 |                      2       |    27      |    1.852    |       9.16667 |                  1.6     |
| 18 | 2019-06-30 02:00:00 |                      1.5     |    20      |    1.95489  |       8.88889 |                  1.68571 |
| 19 | 2019-06-30 03:00:00 |                      1       |    14      |    2.05778  |       8.33333 |                  1.77143 |
| 20 | 2019-06-30 04:00:00 |                      2       |    19      |    1.80055  |       7.77778 |                  1.85714 |
| 21 | 2019-06-30 05:00:00 |                      3       |    23      |    1.54333  |       7.22222 |                  1.94286 |
| 22 | 2019-06-30 06:00:00 |                      4       |    28      |    1.37185  |       7.77778 |                  2.02857 |
| 23 | 2019-06-30 07:00:00 |                      5.66667 |    31.75   |    1.20037  |      10       |                  2.11429 |
| 24 | 2019-06-30 08:00:00 |                      7.33333 |    35.5    |    1.02889  |      13.3333  |                  2.2     |
| 25 | 2019-06-30 09:00:00 |                      9       |    39.25   |    1.11463  |      16.1111  |                  2.8     |
| 26 | 2019-06-30 10:00:00 |                     26.3333  |    43      |    1.20037  |      18.3333  |                  3.4     |
| 27 | 2019-06-30 11:00:00 |                     43.6667  |    58      |    1.28611  |      19.4444  |                  3.7     |
| 28 | 2019-06-30 12:00:00 |                     61       |    73      |    1.37185  |      20       |                  4       |
| 29 | 2019-06-30 13:00:00 |                     65.6667  |    79      |    1.45759  |      19.4444  |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                     70.3333  |    84      |    1.54333  |      18.8889  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     75       |    89      |    2.05778  |      17.2222  |                  5       |
| 32 | 2019-06-30 16:00:00 |                     69.6667  |    88.5    |    2.315    |      16.1111  |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                     64.3333  |    88      |    2.57222  |      15       |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                     59       |    87.6667 |    2.315    |      13.8889  |                  4       |
| 35 | 2019-06-30 19:00:00 |                     50.3333  |    87.3333 |    2.05778  |      16.6667  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     41.6667  |    87      |    1.80055  |      13.8889  |                  3       |
| 37 | 2019-06-30 21:00:00 |                     33       |    85.5    |    1.54333  |      10.5556  |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     24       |    84      |    1.02889  |       9.44444 |                  2       |
| 39 | 2019-06-30 23:00:00 |                     15       |    81      |    1.09319  |       8.88889 |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      6       |    78      |    1.1575   |       8.33333 |                  1       |
| 41 | 2019-07-01 01:00:00 |                      8.33333 |    74      |    1.2218   |       8.05556 |                  1.5     |
| 42 | 2019-07-01 02:00:00 |                     10.6667  |    71      |    1.28611  |       7.77778 |                  2       |
| 43 | 2019-07-01 03:00:00 |                     15.3333  |    68      |    1.35042  |       7.22222 |                  2.25    |
| 44 | 2019-07-01 04:00:00 |                     16.8889  |    66      |    1.41472  |       6.66667 |                  2.5     |
| 45 | 2019-07-01 05:00:00 |                     18.4444  |    65      |    1.47903  |       7.22222 |                  2.75    |
| 46 | 2019-07-01 06:00:00 |                     20       |    64      |    1.54333  |       7.77778 |                  3       |
| 47 | 2019-07-01 07:00:00 |                     31.3333  |    63      |    1.64622  |       8.33333 |                  3.16667 |
| 48 | 2019-07-01 08:00:00 |                     42.6667  |    62      |    1.74911  |      11.1111  |                  3.33333 |
| 49 | 2019-07-01 09:00:00 |                     54       |    60      |    1.852    |      13.8889  |                  3.5     |
| 50 | 2019-07-01 10:00:00 |                     65.3333  |    61      |    1.95489  |      15.5556  |                  3.66667 |
| 51 | 2019-07-01 11:00:00 |                     76.6667  |    62      |    2.05778  |      16.6667  |                  3.83333 |
| 52 | 2019-07-01 12:00:00 |                     88       |    63      |    2.315    |      17.2222  |                  4       |
| 53 | 2019-07-01 13:00:00 |                     81.5     |    64      |    2.57222  |      17.5     |                  4       |
| 54 | 2019-07-01 14:00:00 |                     75       |    67      |    2.46933  |      17.7778  |                  4       |
| 55 | 2019-07-01 15:00:00 |                     68.5     |    71      |    2.36644  |      17.5     |                  4       |
| 56 | 2019-07-01 16:00:00 |                     62       |    73      |    2.26355  |      17.2222  |                  4       |
| 57 | 2019-07-01 17:00:00 |                     55.5     |    76      |    2.16066  |      16.6667  |                  4       |
| 58 | 2019-07-01 18:00:00 |                     49       |    78      |    2.05778  |      16.1111  |                  4       |
| 59 | 2019-07-01 19:00:00 |                     49       |    74      |    1.80055  |      15       |                  4       |
| 60 | 2019-07-01 20:00:00 |                     49       |    70      |    1.54333  |      12.2222  |                  4       |
| 61 | 2019-07-01 21:00:00 |                     49       |    67      |    1.02889  |       9.44444 |                  4       |
| 62 | 2019-07-01 22:00:00 |                     49       |    63      |    0.514444 |       8.33333 |                  4       |
| 63 | 2019-07-01 23:00:00 |                     49       |    59      |    0.685925 |       7.77778 |                  4       |

## Mt Massive

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      2       |    46      |    0.514444 |      13.3333  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      3.5     |    49      |    1.02889  |      15       |                  1.33333 |
|  2 | 2019-06-29 10:00:00 |                      5       |    53      |    1.54333  |      17.7778  |                  1.5     |
|  3 | 2019-06-29 11:00:00 |                      7       |    58      |    3.08666  |      20       |                  1.66667 |
|  4 | 2019-06-29 12:00:00 |                     10       |    62      |    4.11555  |      18.8889  |                  2       |
|  5 | 2019-06-29 13:00:00 |                     24       |    64      |    4.63     |      20       |                  3       |
|  6 | 2019-06-29 14:00:00 |                     38       |    65      |    4.11555  |      21.1111  |                  4       |
|  7 | 2019-06-29 15:00:00 |                     52       |    67      |    3.85833  |      20.8333  |                  3.875   |
|  8 | 2019-06-29 16:00:00 |                     48       |    72      |    3.60111  |      20.5556  |                  3.75    |
|  9 | 2019-06-29 17:00:00 |                     44       |    78      |    3.34389  |      19.4444  |                  3.625   |
| 10 | 2019-06-29 18:00:00 |                     41       |    83      |    3.08666  |      18.8889  |                  3.5     |
| 11 | 2019-06-29 19:00:00 |                     36       |    78      |    2.57222  |      16.6667  |                  3.375   |
| 12 | 2019-06-29 20:00:00 |                     32       |    74      |    2.315    |      13.8889  |                  3.25    |
| 13 | 2019-06-29 21:00:00 |                     27       |    69      |    2.05778  |      11.6667  |                  3.125   |
| 14 | 2019-06-29 22:00:00 |                     19       |    57      |    1.54333  |      10.5556  |                  3       |
| 15 | 2019-06-29 23:00:00 |                     11       |    45      |    1.64622  |      10       |                  2       |
| 16 | 2019-06-30 00:00:00 |                      3       |    33      |    1.74911  |       9.44444 |                  1       |
| 17 | 2019-06-30 01:00:00 |                      2       |    27      |    1.852    |       9.16667 |                  1.6     |
| 18 | 2019-06-30 02:00:00 |                      1.5     |    20      |    1.95489  |       8.88889 |                  1.68571 |
| 19 | 2019-06-30 03:00:00 |                      1       |    14      |    2.05778  |       8.33333 |                  1.77143 |
| 20 | 2019-06-30 04:00:00 |                      2       |    19      |    1.80055  |       7.77778 |                  1.85714 |
| 21 | 2019-06-30 05:00:00 |                      3       |    23      |    1.54333  |       7.22222 |                  1.94286 |
| 22 | 2019-06-30 06:00:00 |                      4       |    28      |    1.37185  |       7.77778 |                  2.02857 |
| 23 | 2019-06-30 07:00:00 |                      5.66667 |    31.75   |    1.20037  |      10       |                  2.11429 |
| 24 | 2019-06-30 08:00:00 |                      7.33333 |    35.5    |    1.02889  |      13.3333  |                  2.2     |
| 25 | 2019-06-30 09:00:00 |                      9       |    39.25   |    1.11463  |      16.1111  |                  2.8     |
| 26 | 2019-06-30 10:00:00 |                     26.3333  |    43      |    1.20037  |      18.3333  |                  3.4     |
| 27 | 2019-06-30 11:00:00 |                     43.6667  |    58      |    1.28611  |      19.4444  |                  3.7     |
| 28 | 2019-06-30 12:00:00 |                     61       |    73      |    1.37185  |      20       |                  4       |
| 29 | 2019-06-30 13:00:00 |                     65.6667  |    79      |    1.45759  |      19.4444  |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                     70.3333  |    84      |    1.54333  |      18.8889  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     75       |    89      |    2.05778  |      17.2222  |                  5       |
| 32 | 2019-06-30 16:00:00 |                     69.6667  |    88.5    |    2.315    |      16.1111  |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                     64.3333  |    88      |    2.57222  |      15       |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                     59       |    87.6667 |    2.315    |      13.8889  |                  4       |
| 35 | 2019-06-30 19:00:00 |                     50.3333  |    87.3333 |    2.05778  |      16.6667  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     41.6667  |    87      |    1.80055  |      13.8889  |                  3       |
| 37 | 2019-06-30 21:00:00 |                     33       |    85.5    |    1.54333  |      10.5556  |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     24       |    84      |    1.02889  |       9.44444 |                  2       |
| 39 | 2019-06-30 23:00:00 |                     15       |    81      |    1.09319  |       8.88889 |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      6       |    78      |    1.1575   |       8.33333 |                  1       |
| 41 | 2019-07-01 01:00:00 |                      8.33333 |    74      |    1.2218   |       8.05556 |                  1.5     |
| 42 | 2019-07-01 02:00:00 |                     10.6667  |    71      |    1.28611  |       7.77778 |                  2       |
| 43 | 2019-07-01 03:00:00 |                     15.3333  |    68      |    1.35042  |       7.22222 |                  2.25    |
| 44 | 2019-07-01 04:00:00 |                     16.8889  |    66      |    1.41472  |       6.66667 |                  2.5     |
| 45 | 2019-07-01 05:00:00 |                     18.4444  |    65      |    1.47903  |       7.22222 |                  2.75    |
| 46 | 2019-07-01 06:00:00 |                     20       |    64      |    1.54333  |       7.77778 |                  3       |
| 47 | 2019-07-01 07:00:00 |                     31.3333  |    63      |    1.64622  |       8.33333 |                  3.16667 |
| 48 | 2019-07-01 08:00:00 |                     42.6667  |    62      |    1.74911  |      11.1111  |                  3.33333 |
| 49 | 2019-07-01 09:00:00 |                     54       |    60      |    1.852    |      13.8889  |                  3.5     |
| 50 | 2019-07-01 10:00:00 |                     65.3333  |    61      |    1.95489  |      15.5556  |                  3.66667 |
| 51 | 2019-07-01 11:00:00 |                     76.6667  |    62      |    2.05778  |      16.6667  |                  3.83333 |
| 52 | 2019-07-01 12:00:00 |                     88       |    63      |    2.315    |      17.2222  |                  4       |
| 53 | 2019-07-01 13:00:00 |                     81.5     |    64      |    2.57222  |      17.5     |                  4       |
| 54 | 2019-07-01 14:00:00 |                     75       |    67      |    2.46933  |      17.7778  |                  4       |
| 55 | 2019-07-01 15:00:00 |                     68.5     |    71      |    2.36644  |      17.5     |                  4       |
| 56 | 2019-07-01 16:00:00 |                     62       |    73      |    2.26355  |      17.2222  |                  4       |
| 57 | 2019-07-01 17:00:00 |                     55.5     |    76      |    2.16066  |      16.6667  |                  4       |
| 58 | 2019-07-01 18:00:00 |                     49       |    78      |    2.05778  |      16.1111  |                  4       |
| 59 | 2019-07-01 19:00:00 |                     49       |    74      |    1.80055  |      15       |                  4       |
| 60 | 2019-07-01 20:00:00 |                     49       |    70      |    1.54333  |      12.2222  |                  4       |
| 61 | 2019-07-01 21:00:00 |                     49       |    67      |    1.02889  |       9.44444 |                  4       |
| 62 | 2019-07-01 22:00:00 |                     49       |    63      |    0.514444 |       8.33333 |                  4       |
| 63 | 2019-07-01 23:00:00 |                     49       |    59      |    0.685925 |       7.77778 |                  4       |

## N Cottonwood Creek

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      1       |       31   |     2.57222 |      13.8889  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      2       |       33   |     2.05778 |      15.5556  |                  1.5     |
|  2 | 2019-06-29 10:00:00 |                      3       |       35   |     2.57222 |      17.2222  |                  1.75    |
|  3 | 2019-06-29 11:00:00 |                      6       |       39   |     3.60111 |      18.8889  |                  2       |
|  4 | 2019-06-29 12:00:00 |                      8       |       43   |     4.11555 |      19.1667  |                  2.5     |
|  5 | 2019-06-29 13:00:00 |                     24       |       49   |     4.63    |      19.4444  |                  3       |
|  6 | 2019-06-29 14:00:00 |                     39       |       55   |     4.45851 |      20       |                  4       |
|  7 | 2019-06-29 15:00:00 |                     55       |       61   |     4.28703 |      19.4444  |                  5       |
|  8 | 2019-06-29 16:00:00 |                     49       |       69   |     4.11555 |      18.8889  |                  4       |
|  9 | 2019-06-29 17:00:00 |                     44       |       77   |     3.60111 |      17.2222  |                  3.83333 |
| 10 | 2019-06-29 18:00:00 |                     38       |       85   |     3.08666 |      16.1111  |                  3.66667 |
| 11 | 2019-06-29 19:00:00 |                     35       |       82   |     2.57222 |      14.4444  |                  3.5     |
| 12 | 2019-06-29 20:00:00 |                     31       |       78   |     2.44361 |      12.7778  |                  3.33333 |
| 13 | 2019-06-29 21:00:00 |                     27       |       75   |     2.315   |      11.1111  |                  3.16667 |
| 14 | 2019-06-29 22:00:00 |                     20       |       62   |     2.18639 |      10.5556  |                  3       |
| 15 | 2019-06-29 23:00:00 |                     13       |       48   |     2.05778 |      10       |                  2       |
| 16 | 2019-06-30 00:00:00 |                      5       |       35   |     2.315   |       9.44444 |                  1       |
| 17 | 2019-06-30 01:00:00 |                      4       |       27   |     2.57222 |       9.16667 |                  1.6     |
| 18 | 2019-06-30 02:00:00 |                      2       |       20   |     2.82944 |       8.88889 |                  1.68571 |
| 19 | 2019-06-30 03:00:00 |                      1       |       13   |     3.08666 |       8.33333 |                  1.77143 |
| 20 | 2019-06-30 04:00:00 |                      2       |       18   |     2.95805 |       7.77778 |                  1.85714 |
| 21 | 2019-06-30 05:00:00 |                      3       |       22   |     2.82944 |       8.05556 |                  1.94286 |
| 22 | 2019-06-30 06:00:00 |                      4       |       27   |     2.70083 |       8.33333 |                  2.02857 |
| 23 | 2019-06-30 07:00:00 |                      5.33333 |       30   |     2.57222 |      10.5556  |                  2.11429 |
| 24 | 2019-06-30 08:00:00 |                      6.66667 |       33   |     2.05778 |      12.7778  |                  2.2     |
| 25 | 2019-06-30 09:00:00 |                      8       |       36   |     1.54333 |      15.5556  |                  2.8     |
| 26 | 2019-06-30 10:00:00 |                     25.3333  |       39   |     1.02889 |      17.2222  |                  3.4     |
| 27 | 2019-06-30 11:00:00 |                     42.6667  |       50   |     1.37185 |      18.8889  |                  3.7     |
| 28 | 2019-06-30 12:00:00 |                     60       |       62   |     1.71481 |      20       |                  4       |
| 29 | 2019-06-30 13:00:00 |                     64       |       69   |     2.05778 |      19.7222  |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                     68       |       75   |     3.08666 |      19.4444  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     72       |       82   |     3.60111 |      18.3333  |                  5       |
| 32 | 2019-06-30 16:00:00 |                     68       |       85   |     4.11555 |      16.6667  |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                     64       |       88   |     4.63    |      15       |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                     60       |       93   |     3.60111 |      12.7778  |                  4       |
| 35 | 2019-06-30 19:00:00 |                     51       |       91   |     3.08666 |      14.4444  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     42       |       90   |     2.05778 |      12.2222  |                  3       |
| 37 | 2019-06-30 21:00:00 |                     33       |       89   |     2.315   |      10.5556  |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     24       |       84   |     2.57222 |      10       |                  2       |
| 39 | 2019-06-30 23:00:00 |                     15       |       78   |     3.08666 |       8.88889 |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      6       |       73   |     3.60111 |       8.33333 |                  1       |
| 41 | 2019-07-01 01:00:00 |                      8       |       70   |     4.11555 |       7.77778 |                  1.5     |
| 42 | 2019-07-01 02:00:00 |                     10       |       68   |     4.01266 |       7.22222 |                  2       |
| 43 | 2019-07-01 03:00:00 |                     14       |       65   |     3.90977 |       7.08333 |                  2.25    |
| 44 | 2019-07-01 04:00:00 |                     15.3333  |       64.5 |     3.80689 |       6.94444 |                  2.5     |
| 45 | 2019-07-01 05:00:00 |                     16.6667  |       64   |     3.704   |       6.80556 |                  2.75    |
| 46 | 2019-07-01 06:00:00 |                     18       |       63   |     3.60111 |       6.66667 |                  3       |
| 47 | 2019-07-01 07:00:00 |                     29.6667  |       62   |     3.08666 |       7.77778 |                  3.16667 |
| 48 | 2019-07-01 08:00:00 |                     41.3333  |       60   |     2.57222 |      10.5556  |                  3.33333 |
| 49 | 2019-07-01 09:00:00 |                     53       |       58   |     2.67511 |      12.2222  |                  3.5     |
| 50 | 2019-07-01 10:00:00 |                     64.6667  |       61   |     2.778   |      13.3333  |                  3.66667 |
| 51 | 2019-07-01 11:00:00 |                     76.3333  |       63   |     2.88089 |      14.4444  |                  3.83333 |
| 52 | 2019-07-01 12:00:00 |                     88       |       66   |     2.98378 |      15.5556  |                  4       |
| 53 | 2019-07-01 13:00:00 |                     82       |       68   |     3.08666 |      15.7407  |                  4       |
| 54 | 2019-07-01 14:00:00 |                     76       |       70   |     2.98378 |      15.9259  |                  4       |
| 55 | 2019-07-01 15:00:00 |                     70       |       72   |     2.88089 |      16.1111  |                  4       |
| 56 | 2019-07-01 16:00:00 |                     64       |       76   |     2.778   |      15.5556  |                  4       |
| 57 | 2019-07-01 17:00:00 |                     58       |       79   |     2.67511 |      15       |                  4       |
| 58 | 2019-07-01 18:00:00 |                     52       |       82   |     2.57222 |      13.8889  |                  4       |
| 59 | 2019-07-01 19:00:00 |                     52       |       81   |     2.05778 |      13.3333  |                  4       |
| 60 | 2019-07-01 20:00:00 |                     52       |       79   |     1.54333 |      11.6667  |                  4       |
| 61 | 2019-07-01 21:00:00 |                     52       |       78   |     1.71481 |      10       |                  4       |
| 62 | 2019-07-01 22:00:00 |                     52       |       72   |     1.88629 |       8.88889 |                  4       |
| 63 | 2019-07-01 23:00:00 |                     52       |       66   |     2.05778 |       8.33333 |                  4       |

## Lake Como

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      0       |    18      |    2.05778  |       17.7778 |                  1       |
|  1 | 2019-06-29 09:00:00 |                      1       |    17      |    2.315    |       21.1111 |                  1.5     |
|  2 | 2019-06-29 10:00:00 |                      2       |    16      |    2.57222  |       22.7778 |                  1.75    |
|  3 | 2019-06-29 11:00:00 |                      3       |    14      |    2.65796  |       24.4444 |                  2       |
|  4 | 2019-06-29 12:00:00 |                      5       |    13      |    2.7437   |       25.5556 |                  2.5     |
|  5 | 2019-06-29 13:00:00 |                     16       |    18      |    2.82944  |       27.2222 |                  3       |
|  6 | 2019-06-29 14:00:00 |                     26       |    23      |    2.91518  |       28.3333 |                  4       |
|  7 | 2019-06-29 15:00:00 |                     37       |    37      |    3.00092  |       28.8889 |                  3.875   |
|  8 | 2019-06-29 16:00:00 |                     36.5     |    46      |    3.08666  |       28.3333 |                  3.75    |
|  9 | 2019-06-29 17:00:00 |                     36       |    64      |    4.11555  |       27.2222 |                  3.625   |
| 10 | 2019-06-29 18:00:00 |                     34       |    82      |    4.63     |       24.4444 |                  3.5     |
| 11 | 2019-06-29 19:00:00 |                     32       |    84      |    4.11555  |       22.2222 |                  3.375   |
| 12 | 2019-06-29 20:00:00 |                     29       |    86      |    3.85833  |       21.1111 |                  3.25    |
| 13 | 2019-06-29 21:00:00 |                     25       |    88      |    3.60111  |       20      |                  3.125   |
| 14 | 2019-06-29 22:00:00 |                     19       |    77      |    3.42963  |       18.8889 |                  3       |
| 15 | 2019-06-29 23:00:00 |                     12       |    66      |    3.25815  |       18.3333 |                  2       |
| 16 | 2019-06-30 00:00:00 |                      5       |    55      |    3.08666  |       17.7778 |                  1       |
| 17 | 2019-06-30 01:00:00 |                      4       |    49      |    2.05778  |       17.2222 |                  1.6     |
| 18 | 2019-06-30 02:00:00 |                      3       |    43      |    1.02889  |       16.6667 |                  1.68571 |
| 19 | 2019-06-30 03:00:00 |                      2       |    37      |    0.514444 |       16.1111 |                  1.77143 |
| 20 | 2019-06-30 04:00:00 |                      2.66667 |    31      |    0.771666 |       15      |                  1.85714 |
| 21 | 2019-06-30 05:00:00 |                      3.33333 |    26      |    1.02889  |       13.8889 |                  1.94286 |
| 22 | 2019-06-30 06:00:00 |                      4       |    20      |    1.54333  |       14.4444 |                  2.02857 |
| 23 | 2019-06-30 07:00:00 |                      4.66667 |    23      |    1.80055  |       15      |                  2.11429 |
| 24 | 2019-06-30 08:00:00 |                      5.33333 |    25      |    2.05778  |       16.6667 |                  2.2     |
| 25 | 2019-06-30 09:00:00 |                      6       |    28      |    2.13127  |       19.4444 |                  2.8     |
| 26 | 2019-06-30 10:00:00 |                     21       |    37      |    2.20476  |       21.1111 |                  3.4     |
| 27 | 2019-06-30 11:00:00 |                     36       |    46      |    2.27825  |       23.3333 |                  3.7     |
| 28 | 2019-06-30 12:00:00 |                     51       |    56      |    2.35174  |       25      |                  4       |
| 29 | 2019-06-30 13:00:00 |                     54.3333  |    56.5    |    2.42524  |       26.6667 |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                     57.6667  |    57      |    2.49873  |       27.7778 |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     61       |    75      |    2.57222  |       27.2222 |                  5       |
| 32 | 2019-06-30 16:00:00 |                     57       |    79.6667 |    3.60111  |       26.6667 |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                     53       |    84.3333 |    4.63     |       24.4444 |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                     49       |    89      |    2.57222  |       22.2222 |                  4       |
| 35 | 2019-06-30 19:00:00 |                     41.6667  |    88      |    2.05778  |       23.8889 |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     34.3333  |    86      |    1.54333  |       22.2222 |                  3       |
| 37 | 2019-06-30 21:00:00 |                     27       |    84      |    1.02889  |       20.5556 |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     19.3333  |    82      |    1.54333  |       18.8889 |                  2       |
| 39 | 2019-06-30 23:00:00 |                     11.6667  |    77      |    2.05778  |       17.7778 |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      4       |    71      |    1.88629  |       17.2222 |                  1       |
| 41 | 2019-07-01 01:00:00 |                      5.83333 |    69      |    1.71481  |       16.1111 |                  1.5     |
| 42 | 2019-07-01 02:00:00 |                      7.66667 |    67      |    1.54333  |       15.5556 |                  2       |
| 43 | 2019-07-01 03:00:00 |                     11.3333  |    65      |    1.67194  |       15      |                  2.25    |
| 44 | 2019-07-01 04:00:00 |                     12.5556  |    64.5    |    1.80055  |       14.7222 |                  2.5     |
| 45 | 2019-07-01 05:00:00 |                     13.7778  |    64      |    1.92917  |       14.4444 |                  2.75    |
| 46 | 2019-07-01 06:00:00 |                     15       |    60.5    |    2.05778  |       13.8889 |                  3       |
| 47 | 2019-07-01 07:00:00 |                     27.3333  |    57      |    1.88629  |       15      |                  3.16667 |
| 48 | 2019-07-01 08:00:00 |                     39.6667  |    50      |    1.71481  |       17.2222 |                  3.33333 |
| 49 | 2019-07-01 09:00:00 |                     52       |    43      |    1.54333  |       19.4444 |                  3.5     |
| 50 | 2019-07-01 10:00:00 |                     64.3333  |    52      |    2.05778  |       21.1111 |                  3.66667 |
| 51 | 2019-07-01 11:00:00 |                     76.6667  |    61      |    2.18639  |       22.2222 |                  3.83333 |
| 52 | 2019-07-01 12:00:00 |                     89       |    70      |    2.315    |       23.3333 |                  4       |
| 53 | 2019-07-01 13:00:00 |                     84.3333  |    72      |    2.44361  |       23.8889 |                  4       |
| 54 | 2019-07-01 14:00:00 |                     79.6667  |    75      |    2.57222  |       24.4444 |                  4       |
| 55 | 2019-07-01 15:00:00 |                     75       |    77      |    2.40074  |       25      |                  4       |
| 56 | 2019-07-01 16:00:00 |                     70.3333  |    81      |    2.22926  |       24.7222 |                  4       |
| 57 | 2019-07-01 17:00:00 |                     65.6667  |    84      |    2.05778  |       24.4444 |                  4       |
| 58 | 2019-07-01 18:00:00 |                     61       |    87      |    1.80055  |       23.8889 |                  4       |
| 59 | 2019-07-01 19:00:00 |                     61       |    88      |    1.54333  |       22.7778 |                  4       |
| 60 | 2019-07-01 20:00:00 |                     61       |    87      |    1.28611  |       21.1111 |                  4       |
| 61 | 2019-07-01 21:00:00 |                     61       |    86      |    1.02889  |       19.4444 |                  4       |
| 62 | 2019-07-01 22:00:00 |                     61       |    85      |    0.771666 |       17.7778 |                  4       |
| 63 | 2019-07-01 23:00:00 |                     61       |    82      |    0.514444 |       16.6667 |                  4       |

## La Plata

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      2       |      50    |    1.54333  |      14.4444  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      3.5     |      57    |    2.05778  |      16.3889  |                  1.33333 |
|  2 | 2019-06-29 10:00:00 |                      5       |      56    |    2.57222  |      18.3333  |                  1.5     |
|  3 | 2019-06-29 11:00:00 |                      7       |      54    |    3.60111  |      22.2222  |                  1.66667 |
|  4 | 2019-06-29 12:00:00 |                     10       |      53    |    4.11555  |      18.8889  |                  2       |
|  5 | 2019-06-29 13:00:00 |                     24       |      57    |    4.63     |      21.1111  |                  3       |
|  6 | 2019-06-29 14:00:00 |                     38       |      61    |    4.50138  |      23.3333  |                  4       |
|  7 | 2019-06-29 15:00:00 |                     52       |      65    |    4.37277  |      22.2222  |                  3.875   |
|  8 | 2019-06-29 16:00:00 |                     49       |      71    |    4.24416  |      21.1111  |                  3.75    |
|  9 | 2019-06-29 17:00:00 |                     47       |      76    |    4.11555  |      19.4444  |                  3.625   |
| 10 | 2019-06-29 18:00:00 |                     44       |      82    |    3.60111  |      18.0556  |                  3.5     |
| 11 | 2019-06-29 19:00:00 |                     39       |      78    |    3.34389  |      16.6667  |                  3.375   |
| 12 | 2019-06-29 20:00:00 |                     34       |      73    |    3.08666  |      13.3333  |                  3.25    |
| 13 | 2019-06-29 21:00:00 |                     29       |      69    |    2.57222  |      10.5556  |                  3.125   |
| 14 | 2019-06-29 22:00:00 |                     20       |      61    |    2.05778  |       8.88889 |                  3       |
| 15 | 2019-06-29 23:00:00 |                     12       |      52    |    1.54333  |       8.33333 |                  2       |
| 16 | 2019-06-30 00:00:00 |                      3       |      44    |    1.02889  |       8.11111 |                  1       |
| 17 | 2019-06-30 01:00:00 |                      2       |      34    |    1.54333  |       7.88889 |                  1.6     |
| 18 | 2019-06-30 02:00:00 |                      1.5     |      24    |    1.80055  |       7.66667 |                  1.68571 |
| 19 | 2019-06-30 03:00:00 |                      1       |      14    |    2.05778  |       7.44444 |                  1.77143 |
| 20 | 2019-06-30 04:00:00 |                      2       |      19    |    1.80055  |       7.22222 |                  1.85714 |
| 21 | 2019-06-30 05:00:00 |                      3       |      24    |    1.54333  |       6.66667 |                  1.94286 |
| 22 | 2019-06-30 06:00:00 |                      4       |      29    |    1.37185  |       7.22222 |                  2.02857 |
| 23 | 2019-06-30 07:00:00 |                      5.66667 |      33.25 |    1.20037  |      10       |                  2.11429 |
| 24 | 2019-06-30 08:00:00 |                      7.33333 |      37.5  |    1.02889  |      14.4444  |                  2.2     |
| 25 | 2019-06-30 09:00:00 |                      9       |      41.75 |    1.11463  |      17.7778  |                  2.8     |
| 26 | 2019-06-30 10:00:00 |                     26.3333  |      46    |    1.20037  |      20.5556  |                  3.4     |
| 27 | 2019-06-30 11:00:00 |                     43.6667  |      62    |    1.28611  |      21.6667  |                  3.7     |
| 28 | 2019-06-30 12:00:00 |                     61       |      78    |    1.37185  |      22.2222  |                  4       |
| 29 | 2019-06-30 13:00:00 |                     65.3333  |      81    |    1.45759  |      21.6667  |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                     69.6667  |      83    |    1.54333  |      21.1111  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     74       |      85    |    1.80055  |      19.4444  |                  5       |
| 32 | 2019-06-30 16:00:00 |                     69.6667  |      87    |    2.05778  |      17.2222  |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                     65.3333  |      89    |    1.54333  |      15       |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                     61       |      88    |    2.57222  |      12.7778  |                  4       |
| 35 | 2019-06-30 19:00:00 |                     52       |      87    |    1.54333  |      16.1111  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     43       |      86    |    1.02889  |      12.7778  |                  3       |
| 37 | 2019-06-30 21:00:00 |                     34       |      85    |    0.514444 |       8.88889 |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     24.6667  |      84    |    0.685925 |       7.77778 |                  2       |
| 39 | 2019-06-30 23:00:00 |                     15.3333  |      81    |    0.857407 |       7.5     |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      6       |      78    |    1.02889  |       7.22222 |                  1       |
| 41 | 2019-07-01 01:00:00 |                      8.66667 |      74    |    1.28611  |       6.66667 |                  1.5     |
| 42 | 2019-07-01 02:00:00 |                     11.3333  |      70    |    1.54333  |       6.11111 |                  2       |
| 43 | 2019-07-01 03:00:00 |                     16.6667  |      66    |    1.60049  |       5.83333 |                  2.25    |
| 44 | 2019-07-01 04:00:00 |                     18.4444  |      65.5  |    1.65765  |       5.55556 |                  2.5     |
| 45 | 2019-07-01 05:00:00 |                     20.2222  |      65    |    1.71481  |       5       |                  2.75    |
| 46 | 2019-07-01 06:00:00 |                     22       |      64.5  |    1.77197  |       6.11111 |                  3       |
| 47 | 2019-07-01 07:00:00 |                     32.6667  |      64    |    1.82913  |       7.22222 |                  3.16667 |
| 48 | 2019-07-01 08:00:00 |                     43.3333  |      61    |    1.88629  |      11.1111  |                  3.33333 |
| 49 | 2019-07-01 09:00:00 |                     54       |      59    |    1.94346  |      14.4444  |                  3.5     |
| 50 | 2019-07-01 10:00:00 |                     64.6667  |      60    |    2.00062  |      16.6667  |                  3.66667 |
| 51 | 2019-07-01 11:00:00 |                     75.3333  |      61    |    2.05778  |      18.3333  |                  3.83333 |
| 52 | 2019-07-01 12:00:00 |                     86       |      62    |    2.57222  |      18.8889  |                  4       |
| 53 | 2019-07-01 13:00:00 |                     80.3333  |      66    |    2.82944  |      19.4444  |                  4       |
| 54 | 2019-07-01 14:00:00 |                     74.6667  |      69    |    3.08666  |      19.2593  |                  4       |
| 55 | 2019-07-01 15:00:00 |                     69       |      72    |    2.91518  |      19.0741  |                  4       |
| 56 | 2019-07-01 16:00:00 |                     63.3333  |      74    |    2.7437   |      18.8889  |                  4       |
| 57 | 2019-07-01 17:00:00 |                     57.6667  |      76    |    2.57222  |      18.0556  |                  4       |
| 58 | 2019-07-01 18:00:00 |                     52       |      78    |    2.315    |      17.2222  |                  4       |
| 59 | 2019-07-01 19:00:00 |                     52       |      74    |    2.05778  |      15.5556  |                  4       |
| 60 | 2019-07-01 20:00:00 |                     52       |      69    |    1.54333  |      12.2222  |                  4       |
| 61 | 2019-07-01 21:00:00 |                     52       |      64    |    1.02889  |       8.33333 |                  4       |
| 62 | 2019-07-01 22:00:00 |                     52       |      61    |    1.09319  |       7.22222 |                  4       |
| 63 | 2019-07-01 23:00:00 |                     52       |      59    |    1.1575   |       6.94444 |                  4       |

## Nellie Creek

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      11      |    30      |     1.02889 |      15.5556  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      11      |    30      |     1.02889 |      15.5556  |                  1       |
|  2 | 2019-06-29 10:00:00 |                      14      |    32      |     1.54333 |      17.7778  |                  1.25    |
|  3 | 2019-06-29 11:00:00 |                      16      |    34      |     1.37185 |      19.4444  |                  1.5     |
|  4 | 2019-06-29 12:00:00 |                      18      |    52      |     1.20037 |      20.5556  |                  2       |
|  5 | 2019-06-29 13:00:00 |                      36      |    68      |     1.02889 |      19.4444  |                  4       |
|  6 | 2019-06-29 14:00:00 |                      53      |    85      |     4.11555 |      18.3333  |                  3.75    |
|  7 | 2019-06-29 15:00:00 |                      71      |   100      |     3.60111 |      18.1944  |                  3.5     |
|  8 | 2019-06-29 16:00:00 |                      64      |    96      |     3.34389 |      18.0556  |                  3.25    |
|  9 | 2019-06-29 17:00:00 |                      56      |    88      |     3.08666 |      17.9167  |                  3       |
| 10 | 2019-06-29 18:00:00 |                      49      |    81      |     2.05778 |      17.7778  |                  2.75    |
| 11 | 2019-06-29 19:00:00 |                      43      |    75      |     2.57222 |      16.6667  |                  2.5     |
| 12 | 2019-06-29 20:00:00 |                      38      |    70      |     2.82944 |      14.4444  |                  2.25    |
| 13 | 2019-06-29 21:00:00 |                      32      |    64      |     3.08666 |      13.3333  |                  2       |
| 14 | 2019-06-29 22:00:00 |                      26      |    58      |     3.21528 |      12.2222  |                  1.66667 |
| 15 | 2019-06-29 23:00:00 |                      21      |    53      |     3.34389 |      11.6667  |                  1.33333 |
| 16 | 2019-06-30 00:00:00 |                      15      |    47      |     3.4725  |      11.1111  |                  1       |
| 17 | 2019-06-30 01:00:00 |                      15.125  |    47.5    |     3.60111 |      10.5556  |                  1.33333 |
| 18 | 2019-06-30 02:00:00 |                      15.25   |    48      |     3.49822 |      10       |                  1.38095 |
| 19 | 2019-06-30 03:00:00 |                      15.375  |    48.5    |     3.39533 |       9.72222 |                  1.42857 |
| 20 | 2019-06-30 04:00:00 |                      15.5    |    49      |     3.29244 |       9.44444 |                  1.47619 |
| 21 | 2019-06-30 05:00:00 |                      15.625  |    49.5    |     3.18955 |       8.88889 |                  1.52381 |
| 22 | 2019-06-30 06:00:00 |                      15.75   |    50      |     3.08666 |       9.44444 |                  1.57143 |
| 23 | 2019-06-30 07:00:00 |                      15.875  |    53.75   |     2.57222 |      10.5556  |                  1.61905 |
| 24 | 2019-06-30 08:00:00 |                      16      |    57.5    |     1.54333 |      12.7778  |                  1.66667 |
| 25 | 2019-06-30 09:00:00 |                      24.5    |    61.25   |     1.02889 |      15.5556  |                  2       |
| 26 | 2019-06-30 10:00:00 |                      33      |    65      |     1.20037 |      17.2222  |                  3.5     |
| 27 | 2019-06-30 11:00:00 |                      51      |    83      |     1.37185 |      18.3333  |                  4.25    |
| 28 | 2019-06-30 12:00:00 |                      68      |   100      |     1.54333 |      18.0556  |                  5       |
| 29 | 2019-06-30 13:00:00 |                      74      |    98.6667 |     1.80055 |      17.7778  |                  4.83333 |
| 30 | 2019-06-30 14:00:00 |                      80      |    97.3333 |     2.05778 |      17.2222  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                      86      |    96      |     2.13127 |      16.6667  |                  4.5     |
| 32 | 2019-06-30 16:00:00 |                      78      |    94.6667 |     2.20476 |      16.4815  |                  4.33333 |
| 33 | 2019-06-30 17:00:00 |                      63      |    93.3333 |     2.27825 |      16.2963  |                  4.16667 |
| 34 | 2019-06-30 18:00:00 |                      55      |    92      |     2.35174 |      16.1111  |                  4       |
| 35 | 2019-06-30 19:00:00 |                      48.6667 |    90      |     2.42524 |      15.5556  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                      42.3333 |    87      |     2.49873 |      13.8889  |                  3       |
| 37 | 2019-06-30 21:00:00 |                      36      |    85      |     2.57222 |      12.2222  |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                      29.6667 |    85.5    |     2.7437  |      11.6667  |                  2       |
| 39 | 2019-06-30 23:00:00 |                      23.3333 |    86      |     2.91518 |      11.1111  |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      17      |    85.5    |     3.08666 |      10.8333  |                  1       |
| 41 | 2019-07-01 01:00:00 |                      17.25   |    85      |     2.91518 |      10.5556  |                  1.16667 |
| 42 | 2019-07-01 02:00:00 |                      17.5    |    82      |     2.7437  |      10       |                  1.33333 |
| 43 | 2019-07-01 03:00:00 |                      18      |    81      |     2.57222 |       9.44444 |                  1.41667 |
| 44 | 2019-07-01 04:00:00 |                      29      |    79      |     2.44361 |       8.88889 |                  1.5     |
| 45 | 2019-07-01 05:00:00 |                      40      |    74      |     2.315   |       8.33333 |                  1.58333 |
| 46 | 2019-07-01 06:00:00 |                      51      |    58      |     2.18639 |       8.88889 |                  1.66667 |
| 47 | 2019-07-01 07:00:00 |                      56.5    |    53      |     2.05778 |      10.5556  |                  1.77778 |
| 48 | 2019-07-01 08:00:00 |                      62      |    42      |     1.54333 |      12.7778  |                  1.88889 |
| 49 | 2019-07-01 09:00:00 |                      67.5    |    36      |     1.02889 |      15       |                  2       |
| 50 | 2019-07-01 10:00:00 |                      73      |    41      |     1.28611 |      16.6667  |                  3       |
| 51 | 2019-07-01 11:00:00 |                      78.5    |    50      |     1.54333 |      18.3333  |                  4       |
| 52 | 2019-07-01 12:00:00 |                      84      |    54      |     2.05778 |      18.8889  |                  5       |
| 53 | 2019-07-01 13:00:00 |                      75      |    59      |     2.09452 |      18.7037  |                  4.83333 |
| 54 | 2019-07-01 14:00:00 |                      66      |    68      |     2.13127 |      18.5185  |                  4.66667 |
| 55 | 2019-07-01 15:00:00 |                      57      |    72      |     2.16801 |      18.3333  |                  4.5     |
| 56 | 2019-07-01 16:00:00 |                      48      |    73      |     2.20476 |      18.0556  |                  4.33333 |
| 57 | 2019-07-01 17:00:00 |                      39      |    74      |     2.24151 |      17.7778  |                  4.16667 |
| 58 | 2019-07-01 18:00:00 |                      30      |    75      |     2.27825 |      17.2222  |                  4       |
| 59 | 2019-07-01 19:00:00 |                      30      |    72      |     2.315   |      16.1111  |                  3       |
| 60 | 2019-07-01 20:00:00 |                      30      |    65      |     2.35174 |      15       |                  2       |
| 61 | 2019-07-01 21:00:00 |                      30      |    62      |     2.38849 |      13.3333  |                  1       |
| 62 | 2019-07-01 22:00:00 |                      30      |    60      |     2.42524 |      12.2222  |                  1       |
| 63 | 2019-07-01 23:00:00 |                      30      |    56      |     2.46198 |      11.6667  |                  1       |

## South Colony Lakes

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      0       |    27      |     3.60111 |      15.5556  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      1.5     |    29      |     3.08666 |      16.6667  |                  1.33333 |
|  2 | 2019-06-29 10:00:00 |                      3       |    31      |     3.01317 |      18.8889  |                  1.5     |
|  3 | 2019-06-29 11:00:00 |                      7       |    36      |     2.93968 |      21.1111  |                  1.66667 |
|  4 | 2019-06-29 12:00:00 |                     10       |    40      |     2.86619 |      21.3889  |                  2       |
|  5 | 2019-06-29 13:00:00 |                     24       |    45      |     2.7927  |      21.6667  |                  3       |
|  6 | 2019-06-29 14:00:00 |                     38       |    50      |     2.7192  |      22.2222  |                  4       |
|  7 | 2019-06-29 15:00:00 |                     52       |    55      |     2.64571 |      21.6667  |                  3.85714 |
|  8 | 2019-06-29 16:00:00 |                     49       |    66      |     2.57222 |      21.1111  |                  3.71429 |
|  9 | 2019-06-29 17:00:00 |                     46       |    78      |     2.315   |      20       |                  3.57143 |
| 10 | 2019-06-29 18:00:00 |                     43       |    90      |     2.05778 |      18.3333  |                  3.42857 |
| 11 | 2019-06-29 19:00:00 |                     35       |    86      |     2.57222 |      16.6667  |                  3.28571 |
| 12 | 2019-06-29 20:00:00 |                     27       |    82      |     3.60111 |      15       |                  3.14286 |
| 13 | 2019-06-29 21:00:00 |                     19       |    78      |     4.11555 |      13.3333  |                  3       |
| 14 | 2019-06-29 22:00:00 |                     14       |    69      |     4.21844 |      12.7778  |                  2       |
| 15 | 2019-06-29 23:00:00 |                      9       |    60      |     4.32133 |      12.2222  |                  1       |
| 16 | 2019-06-30 00:00:00 |                      5       |    51      |     4.42422 |      11.9444  |                  1.5     |
| 17 | 2019-06-30 01:00:00 |                      4       |    44      |     4.52711 |      11.6667  |                  2       |
| 18 | 2019-06-30 02:00:00 |                      3       |    37      |     4.63    |      11.1111  |                  2.07143 |
| 19 | 2019-06-30 03:00:00 |                      2       |    31      |     4.45851 |      10       |                  2.14286 |
| 20 | 2019-06-30 04:00:00 |                      3       |    28      |     4.28703 |       9.44444 |                  2.21429 |
| 21 | 2019-06-30 05:00:00 |                      4       |    26      |     4.11555 |       8.88889 |                  2.28571 |
| 22 | 2019-06-30 06:00:00 |                      5       |    23      |     3.60111 |       9.44444 |                  2.35714 |
| 23 | 2019-06-30 07:00:00 |                      6.33333 |    22      |     3.49822 |      11.6667  |                  2.42857 |
| 24 | 2019-06-30 08:00:00 |                      7.66667 |    21      |     3.39533 |      14.4444  |                  2.5     |
| 25 | 2019-06-30 09:00:00 |                      9       |    19      |     3.29244 |      17.2222  |                  3       |
| 26 | 2019-06-30 10:00:00 |                     25.3333  |    36      |     3.18955 |      19.4444  |                  3.5     |
| 27 | 2019-06-30 11:00:00 |                     41.6667  |    53      |     3.08666 |      20.5556  |                  3.75    |
| 28 | 2019-06-30 12:00:00 |                     58       |    70      |     2.91518 |      21.6667  |                  4       |
| 29 | 2019-06-30 13:00:00 |                     63       |    66      |     2.7437  |      21.3889  |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                     68       |    62      |     2.57222 |      21.1111  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     73       |    75      |     3.08666 |      20       |                  5       |
| 32 | 2019-06-30 16:00:00 |                     70.3333  |    81.3333 |     3.60111 |      18.3333  |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                     67.6667  |    87.6667 |     5.14444 |      16.6667  |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                     65       |    94      |     4.11555 |      15       |                  4       |
| 35 | 2019-06-30 19:00:00 |                     55.6667  |    95      |     3.60111 |      17.2222  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     46.3333  |    95.5    |     3.94407 |      15       |                  3       |
| 37 | 2019-06-30 21:00:00 |                     37       |    96      |     4.28703 |      13.3333  |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     27.6667  |    87      |     4.63    |      11.6667  |                  2       |
| 39 | 2019-06-30 23:00:00 |                     18.3333  |    79      |     5.65888 |      11.1111  |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      9       |    70      |     6.68777 |      10.5556  |                  1       |
| 41 | 2019-07-01 01:00:00 |                     11.1667  |    69      |     6.43055 |       8.88889 |                  1.5     |
| 42 | 2019-07-01 02:00:00 |                     13.3333  |    67      |     6.17333 |       8.33333 |                  2       |
| 43 | 2019-07-01 03:00:00 |                     17.6667  |    66      |     5.91611 |       8.14815 |                  2.25    |
| 44 | 2019-07-01 04:00:00 |                     19.1111  |    66.3333 |     5.65888 |       7.96296 |                  2.5     |
| 45 | 2019-07-01 05:00:00 |                     20.5556  |    66.6667 |     4.63    |       7.77778 |                  2.75    |
| 46 | 2019-07-01 06:00:00 |                     22       |    67      |     4.11555 |       8.88889 |                  3       |
| 47 | 2019-07-01 07:00:00 |                     34.1667  |    60      |     4.01266 |      10       |                  3.16667 |
| 48 | 2019-07-01 08:00:00 |                     46.3333  |    52      |     3.90977 |      12.7778  |                  3.33333 |
| 49 | 2019-07-01 09:00:00 |                     58.5     |    45      |     3.80689 |      13.8889  |                  3.5     |
| 50 | 2019-07-01 10:00:00 |                     70.6667  |    56      |     3.704   |      15.5556  |                  3.66667 |
| 51 | 2019-07-01 11:00:00 |                     82.8333  |    67      |     3.60111 |      16.6667  |                  3.83333 |
| 52 | 2019-07-01 12:00:00 |                     95       |    78      |     3.08666 |      17.2222  |                  4       |
| 53 | 2019-07-01 13:00:00 |                     91.5     |    81      |     2.57222 |      16.6667  |                  4       |
| 54 | 2019-07-01 14:00:00 |                     88       |    84      |     2.315   |      17.2222  |                  4       |
| 55 | 2019-07-01 15:00:00 |                     84.5     |    86      |     2.05778 |      17.037   |                  4       |
| 56 | 2019-07-01 16:00:00 |                     81       |    87      |     2.18639 |      16.8519  |                  4       |
| 57 | 2019-07-01 17:00:00 |                     77.5     |    88      |     2.315   |      16.6667  |                  4       |
| 58 | 2019-07-01 18:00:00 |                     74       |    89      |     2.44361 |      16.1111  |                  4       |
| 59 | 2019-07-01 19:00:00 |                     74       |    88.5    |     2.57222 |      15.5556  |                  4       |
| 60 | 2019-07-01 20:00:00 |                     74       |    88      |     2.82944 |      13.8889  |                  4       |
| 61 | 2019-07-01 21:00:00 |                     74       |    84.5    |     3.08666 |      12.2222  |                  4       |
| 62 | 2019-07-01 22:00:00 |                     74       |    81      |     2.57222 |      11.1111  |                  4       |
| 63 | 2019-07-01 23:00:00 |                     74       |    73      |     2.05778 |      10.5556  |                  4       |

## Kite Lake

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      2       |    38      |     2.05778 |      11.1111  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      7.5     |    58      |     3.08666 |      12.2222  |                  1.33333 |
|  2 | 2019-06-29 10:00:00 |                     13       |    66      |     3.34389 |      13.3333  |                  1.5     |
|  3 | 2019-06-29 11:00:00 |                     18.5     |    70      |     3.60111 |      15       |                  1.66667 |
|  4 | 2019-06-29 12:00:00 |                     24       |    75      |     4.11555 |      15.5556  |                  2       |
|  5 | 2019-06-29 13:00:00 |                     33       |    83      |     4.63    |      16.1111  |                  4       |
|  6 | 2019-06-29 14:00:00 |                     41       |    84      |     2.05778 |      16.6667  |                  3.81818 |
|  7 | 2019-06-29 15:00:00 |                     43       |    89      |     2.57222 |      15.8333  |                  3.63636 |
|  8 | 2019-06-29 16:00:00 |                     44       |    94      |     2.82944 |      15       |                  3.45455 |
|  9 | 2019-06-29 17:00:00 |                     43       |    95      |     3.08666 |      13.3333  |                  3.27273 |
| 10 | 2019-06-29 18:00:00 |                     42       |    96      |     2.05778 |      11.1111  |                  3.09091 |
| 11 | 2019-06-29 19:00:00 |                     40.25    |    95.3333 |     1.02889 |       9.44444 |                  2.90909 |
| 12 | 2019-06-29 20:00:00 |                     38.5     |    94.6667 |     1.54333 |       7.22222 |                  2.72727 |
| 13 | 2019-06-29 21:00:00 |                     36.75    |    94      |     2.57222 |       5.55556 |                  2.54545 |
| 14 | 2019-06-29 22:00:00 |                     35       |    84      |     3.08666 |       5       |                  2.36364 |
| 15 | 2019-06-29 23:00:00 |                     28       |    82      |     3.25815 |       5.18519 |                  2.18182 |
| 16 | 2019-06-30 00:00:00 |                     21       |    71      |     3.42963 |       5.37037 |                  2       |
| 17 | 2019-06-30 01:00:00 |                     13       |    61      |     3.60111 |       5.55556 |                  1       |
| 18 | 2019-06-30 02:00:00 |                      6       |    60      |     3.4725  |       6.11111 |                  1.07143 |
| 19 | 2019-06-30 03:00:00 |                      5       |    52      |     3.34389 |       6.66667 |                  1.14286 |
| 20 | 2019-06-30 04:00:00 |                      5.8     |    54      |     3.21528 |       6.11111 |                  1.21429 |
| 21 | 2019-06-30 05:00:00 |                      6.6     |    52      |     3.08666 |       5.55556 |                  1.28571 |
| 22 | 2019-06-30 06:00:00 |                      7.4     |    50      |     5.14444 |       6.11111 |                  1.35714 |
| 23 | 2019-06-30 07:00:00 |                      8.2     |    45      |     4.63    |       7.22222 |                  1.42857 |
| 24 | 2019-06-30 08:00:00 |                      9       |    44      |     4.45851 |       8.88889 |                  1.5     |
| 25 | 2019-06-30 09:00:00 |                     12       |    39      |     4.28703 |      11.1111  |                  2       |
| 26 | 2019-06-30 10:00:00 |                     16       |    58      |     4.11555 |      12.7778  |                  3       |
| 27 | 2019-06-30 11:00:00 |                     20       |    64      |     4.63    |      14.4444  |                  3.5     |
| 28 | 2019-06-30 12:00:00 |                     33       |    85      |     6.17333 |      15       |                  4       |
| 29 | 2019-06-30 13:00:00 |                     47       |    87      |     6.68777 |      14.7222  |                  4.5     |
| 30 | 2019-06-30 14:00:00 |                     60       |    89      |     7.71666 |      14.4444  |                  5       |
| 31 | 2019-06-30 15:00:00 |                     73       |    94      |     8.74555 |      13.3333  |                  4.75    |
| 32 | 2019-06-30 16:00:00 |                     70.3333  |    95      |     8.2311  |      11.6667  |                  4.5     |
| 33 | 2019-06-30 17:00:00 |                     67.6667  |    90.5    |     7.71666 |      10.5556  |                  4.25    |
| 34 | 2019-06-30 18:00:00 |                     65       |    86      |     7.20222 |       8.88889 |                  4       |
| 35 | 2019-06-30 19:00:00 |                     55.5     |    87      |     7.0736  |       7.22222 |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     46       |    88      |     6.94499 |       6.11111 |                  3       |
| 37 | 2019-06-30 21:00:00 |                     36.5     |    89      |     6.81638 |       5.55556 |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     27       |    86      |     6.68777 |       5       |                  2       |
| 39 | 2019-06-30 23:00:00 |                     17.5     |    81      |     6.17333 |       5.27778 |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      8       |    78      |     5.65888 |       5.55556 |                  1       |
| 41 | 2019-07-01 01:00:00 |                      5       |    77      |     6.17333 |       6.11111 |                  1.25    |
| 42 | 2019-07-01 02:00:00 |                      2       |    74      |     6.68777 |       6.66667 |                  1.5     |
| 43 | 2019-07-01 03:00:00 |                      7       |    72      |     7.20222 |       6.38889 |                  1.625   |
| 44 | 2019-07-01 04:00:00 |                      8.66667 |    71      |     7.71666 |       6.11111 |                  1.75    |
| 45 | 2019-07-01 05:00:00 |                     10.3333  |    68      |     7.45944 |       6.38889 |                  1.875   |
| 46 | 2019-07-01 06:00:00 |                     12       |    69      |     7.20222 |       6.66667 |                  2       |
| 47 | 2019-07-01 07:00:00 |                     23.5     |    67      |     7.09933 |       7.22222 |                  2.5     |
| 48 | 2019-07-01 08:00:00 |                     35       |    64      |     6.99644 |       8.88889 |                  3       |
| 49 | 2019-07-01 09:00:00 |                     46.5     |    62      |     6.89355 |      10.5556  |                  3.5     |
| 50 | 2019-07-01 10:00:00 |                     58       |    61      |     6.79066 |      11.6667  |                  4       |
| 51 | 2019-07-01 11:00:00 |                     69.5     |    59      |     6.68777 |      13.3333  |                  4.5     |
| 52 | 2019-07-01 12:00:00 |                     81       |    58      |     6.94499 |      14.4444  |                  5       |
| 53 | 2019-07-01 13:00:00 |                     76       |    63      |     7.20222 |      14.0741  |                  4.83333 |
| 54 | 2019-07-01 14:00:00 |                     71       |    72      |     7.71666 |      13.7037  |                  4.66667 |
| 55 | 2019-07-01 15:00:00 |                     66       |    76      |     8.2311  |      13.3333  |                  4.5     |
| 56 | 2019-07-01 16:00:00 |                     61       |    74.75   |     8.05962 |      12.7778  |                  4.33333 |
| 57 | 2019-07-01 17:00:00 |                     56       |    73.5    |     7.88814 |      11.6667  |                  4.16667 |
| 58 | 2019-07-01 18:00:00 |                     51       |    72.25   |     7.71666 |      10.5556  |                  4       |
| 59 | 2019-07-01 19:00:00 |                     51       |    71      |     7.20222 |       8.88889 |                  4       |
| 60 | 2019-07-01 20:00:00 |                     51       |    62      |     6.17333 |       6.66667 |                  4       |
| 61 | 2019-07-01 21:00:00 |                     51       |    57      |     5.65888 |       5.55556 |                  4       |
| 62 | 2019-07-01 22:00:00 |                     51       |    56.5    |     5.74462 |       4.44444 |                  4       |
| 63 | 2019-07-01 23:00:00 |                     51       |    56      |     5.83037 |       3.88889 |                  4       |

## Grays Peak

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                       1      |      33    |     4.63    |      15       |                  1       |
|  1 | 2019-06-29 09:00:00 |                       6      |      46    |     6.17333 |      16.1111  |                  1.33333 |
|  2 | 2019-06-29 10:00:00 |                      11      |      61    |     5.91611 |      18.8889  |                  1.5     |
|  3 | 2019-06-29 11:00:00 |                      16      |      66    |     5.65888 |      19.4444  |                  1.66667 |
|  4 | 2019-06-29 12:00:00 |                      21      |      78    |     5.91611 |      20       |                  2       |
|  5 | 2019-06-29 13:00:00 |                      30      |      85    |     6.17333 |      20.5556  |                  4       |
|  6 | 2019-06-29 14:00:00 |                      39      |      88    |     3.08666 |      22.2222  |                  3.9     |
|  7 | 2019-06-29 15:00:00 |                      41      |      93    |     3.34389 |      21.6667  |                  3.8     |
|  8 | 2019-06-29 16:00:00 |                      44      |      95    |     3.60111 |      21.1111  |                  3.7     |
|  9 | 2019-06-29 17:00:00 |                      41      |      97    |     3.77259 |      19.4444  |                  3.6     |
| 10 | 2019-06-29 18:00:00 |                      37      |      96.25 |     3.94407 |      17.7778  |                  3.5     |
| 11 | 2019-06-29 19:00:00 |                      35.5    |      95.5  |     4.11555 |      15.5556  |                  3.4     |
| 12 | 2019-06-29 20:00:00 |                      34      |      94.75 |     3.60111 |      12.2222  |                  3.3     |
| 13 | 2019-06-29 21:00:00 |                      32.5    |      94    |     3.80689 |      10       |                  3.2     |
| 14 | 2019-06-29 22:00:00 |                      31      |      84    |     4.01266 |       7.77778 |                  3.1     |
| 15 | 2019-06-29 23:00:00 |                      24      |      81    |     4.21844 |       7.22222 |                  3       |
| 16 | 2019-06-30 00:00:00 |                      18      |      71    |     4.42422 |       7.5     |                  2       |
| 17 | 2019-06-30 01:00:00 |                      12      |      59    |     4.63    |       7.77778 |                  1       |
| 18 | 2019-06-30 02:00:00 |                       5      |      58    |     4.11555 |       8.88889 |                  1.07143 |
| 19 | 2019-06-30 03:00:00 |                       4      |      49    |     3.94407 |       9.44444 |                  1.14286 |
| 20 | 2019-06-30 04:00:00 |                       4.6    |      46    |     3.77259 |       9.16667 |                  1.21429 |
| 21 | 2019-06-30 05:00:00 |                       5.2    |      43.5  |     3.60111 |       8.88889 |                  1.28571 |
| 22 | 2019-06-30 06:00:00 |                       5.8    |      41    |     4.11555 |      10       |                  1.35714 |
| 23 | 2019-06-30 07:00:00 |                       6.4    |      39    |     3.85833 |      11.1111  |                  1.42857 |
| 24 | 2019-06-30 08:00:00 |                       7      |      38    |     3.60111 |      13.8889  |                  1.5     |
| 25 | 2019-06-30 09:00:00 |                      11      |      37    |     3.42963 |      16.6667  |                  2       |
| 26 | 2019-06-30 10:00:00 |                      15      |      59    |     3.25815 |      18.3333  |                  3       |
| 27 | 2019-06-30 11:00:00 |                      18      |      66    |     3.08666 |      19.4444  |                  3.5     |
| 28 | 2019-06-30 12:00:00 |                      31      |      88    |     5.14444 |      19.1667  |                  4       |
| 29 | 2019-06-30 13:00:00 |                      44      |      89.5  |     5.65888 |      18.8889  |                  4.5     |
| 30 | 2019-06-30 14:00:00 |                      57      |      91    |     5.14444 |      17.7778  |                  5       |
| 31 | 2019-06-30 15:00:00 |                      70      |      94    |     6.17333 |      16.6667  |                  4.75    |
| 32 | 2019-06-30 16:00:00 |                      69.3333 |      96    |     6.68777 |      15.5556  |                  4.5     |
| 33 | 2019-06-30 17:00:00 |                      68.6667 |      91    |     7.20222 |      14.4444  |                  4.25    |
| 34 | 2019-06-30 18:00:00 |                      68      |      86    |     6.17333 |      13.3333  |                  4       |
| 35 | 2019-06-30 19:00:00 |                      58.5    |      85.75 |     5.65888 |      11.6667  |                  3.66667 |
| 36 | 2019-06-30 20:00:00 |                      49      |      85.5  |     5.40166 |      10       |                  3.33333 |
| 37 | 2019-06-30 21:00:00 |                      39.5    |      85.25 |     5.14444 |       8.33333 |                  3       |
| 38 | 2019-06-30 22:00:00 |                      30      |      85    |     4.88722 |       7.22222 |                  2.66667 |
| 39 | 2019-06-30 23:00:00 |                      20.5    |      82    |     4.63    |       6.66667 |                  2.33333 |
| 40 | 2019-07-01 00:00:00 |                      11      |      80    |     4.71574 |       7.22222 |                  2       |
| 41 | 2019-07-01 01:00:00 |                       7      |      76    |     4.80148 |       7.77778 |                  1.5     |
| 42 | 2019-07-01 02:00:00 |                       3      |      69    |     4.88722 |       8.88889 |                  1       |
| 43 | 2019-07-01 03:00:00 |                       9      |      65    |     4.97296 |       9.44444 |                  1.5     |
| 44 | 2019-07-01 04:00:00 |                      11      |      65.5  |     5.0587  |       8.88889 |                  2       |
| 45 | 2019-07-01 05:00:00 |                      13      |      66    |     5.14444 |       8.33333 |                  2.5     |
| 46 | 2019-07-01 06:00:00 |                      15      |      68    |     4.63    |       8.88889 |                  3       |
| 47 | 2019-07-01 07:00:00 |                      26      |      67.5  |     5.14444 |      10.5556  |                  3.33333 |
| 48 | 2019-07-01 08:00:00 |                      37      |      67    |     5.65888 |      13.3333  |                  3.66667 |
| 49 | 2019-07-01 09:00:00 |                      48      |      66.5  |     6.17333 |      15.5556  |                  4       |
| 50 | 2019-07-01 10:00:00 |                      59      |      66    |     5.91611 |      17.2222  |                  4.33333 |
| 51 | 2019-07-01 11:00:00 |                      70      |      65    |     5.65888 |      18.3333  |                  4.66667 |
| 52 | 2019-07-01 12:00:00 |                      81      |      64    |     5.83037 |      18.1481  |                  5       |
| 53 | 2019-07-01 13:00:00 |                      76      |      66    |     6.00185 |      17.963   |                  4.83333 |
| 54 | 2019-07-01 14:00:00 |                      71      |      69    |     6.17333 |      17.7778  |                  4.66667 |
| 55 | 2019-07-01 15:00:00 |                      66      |      71    |     6.04472 |      16.6667  |                  4.5     |
| 56 | 2019-07-01 16:00:00 |                      61      |      72    |     5.91611 |      16.1111  |                  4.33333 |
| 57 | 2019-07-01 17:00:00 |                      56      |      75    |     5.78749 |      15.5556  |                  4.16667 |
| 58 | 2019-07-01 18:00:00 |                      51      |      76    |     5.65888 |      13.8889  |                  4       |
| 59 | 2019-07-01 19:00:00 |                      51      |      71    |     5.14444 |      12.2222  |                  4       |
| 60 | 2019-07-01 20:00:00 |                      51      |      61    |     4.11555 |      10       |                  4       |
| 61 | 2019-07-01 21:00:00 |                      51      |      56    |     3.60111 |       7.77778 |                  4       |
| 62 | 2019-07-01 22:00:00 |                      51      |      54.5  |     3.77259 |       6.11111 |                  4       |
| 63 | 2019-07-01 23:00:00 |                      51      |      53    |     3.94407 |       5.55556 |                  4       |

## Baldwin Gulch

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      1       |    39      |     3.08666 |      16.1111  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      2       |    41      |     2.57222 |      17.5     |                  1.5     |
|  2 | 2019-06-29 10:00:00 |                      3       |    40      |     3.08666 |      18.8889  |                  1.75    |
|  3 | 2019-06-29 11:00:00 |                      6       |    39.5    |     3.60111 |      21.1111  |                  2       |
|  4 | 2019-06-29 12:00:00 |                      8       |    39      |     3.85833 |      18.8889  |                  2.5     |
|  5 | 2019-06-29 13:00:00 |                     24       |    47      |     4.11555 |      21.1111  |                  3       |
|  6 | 2019-06-29 14:00:00 |                     39       |    55      |     3.60111 |      22.7778  |                  4       |
|  7 | 2019-06-29 15:00:00 |                     55       |    63      |     3.51537 |      22.2222  |                  5       |
|  8 | 2019-06-29 16:00:00 |                     50       |    70      |     3.42963 |      21.1111  |                  4       |
|  9 | 2019-06-29 17:00:00 |                     45       |    77      |     3.34389 |      19.4444  |                  3.83333 |
| 10 | 2019-06-29 18:00:00 |                     40       |    84      |     3.25815 |      17.7778  |                  3.66667 |
| 11 | 2019-06-29 19:00:00 |                     36       |    81      |     3.1724  |      16.1111  |                  3.5     |
| 12 | 2019-06-29 20:00:00 |                     31       |    79      |     3.08666 |      14.4444  |                  3.33333 |
| 13 | 2019-06-29 21:00:00 |                     27       |    76      |     2.82944 |      13.3333  |                  3.16667 |
| 14 | 2019-06-29 22:00:00 |                     20       |    62      |     2.57222 |      12.2222  |                  3       |
| 15 | 2019-06-29 23:00:00 |                     12       |    48      |     1.54333 |      11.1111  |                  2       |
| 16 | 2019-06-30 00:00:00 |                      5       |    34      |     1.80055 |      10.8333  |                  1       |
| 17 | 2019-06-30 01:00:00 |                      3       |    27      |     2.05778 |      10.5556  |                  1.6     |
| 18 | 2019-06-30 02:00:00 |                      2       |    21      |     2.57222 |      10       |                  1.68571 |
| 19 | 2019-06-30 03:00:00 |                      1       |    14      |     3.60111 |       9.44444 |                  1.77143 |
| 20 | 2019-06-30 04:00:00 |                      2       |    20      |     3.42963 |       8.88889 |                  1.85714 |
| 21 | 2019-06-30 05:00:00 |                      3       |    25      |     3.25815 |       9.44444 |                  1.94286 |
| 22 | 2019-06-30 06:00:00 |                      4       |    31      |     3.08666 |      10       |                  2.02857 |
| 23 | 2019-06-30 07:00:00 |                      5.66667 |    29      |     2.57222 |      12.7778  |                  2.11429 |
| 24 | 2019-06-30 08:00:00 |                      7.33333 |    27      |     2.05778 |      16.1111  |                  2.2     |
| 25 | 2019-06-30 09:00:00 |                      9       |    25      |     1.54333 |      19.4444  |                  2.8     |
| 26 | 2019-06-30 10:00:00 |                     26       |    37      |     1.67194 |      21.1111  |                  3.4     |
| 27 | 2019-06-30 11:00:00 |                     43       |    48      |     1.80055 |      22.2222  |                  3.7     |
| 28 | 2019-06-30 12:00:00 |                     60       |    60      |     1.92917 |      22.7778  |                  4       |
| 29 | 2019-06-30 13:00:00 |                     63.6667  |    69      |     2.05778 |      22.4074  |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                     67.3333  |    79      |     3.08666 |      22.037   |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     71       |    89      |     3.60111 |      21.6667  |                  5       |
| 32 | 2019-06-30 16:00:00 |                     68       |    90      |     4.11555 |      20       |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                     65       |    91      |     3.85833 |      17.7778  |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                     62       |    91.3333 |     3.60111 |      15.5556  |                  4       |
| 35 | 2019-06-30 19:00:00 |                     52.6667  |    91.6667 |     3.34389 |      16.6667  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     43.3333  |    92      |     3.08666 |      14.4444  |                  3       |
| 37 | 2019-06-30 21:00:00 |                     34       |    88.5    |     3.34389 |      12.2222  |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     24.6667  |    85      |     3.60111 |      11.6667  |                  2       |
| 39 | 2019-06-30 23:00:00 |                     15.3333  |    79      |     4.11555 |      11.1111  |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      6       |    72      |     4.63    |      10.5556  |                  1       |
| 41 | 2019-07-01 01:00:00 |                      7.66667 |    71.5    |     5.14444 |       9.44444 |                  1.5     |
| 42 | 2019-07-01 02:00:00 |                      9.33333 |    71      |     4.97296 |       7.77778 |                  2       |
| 43 | 2019-07-01 03:00:00 |                     12.6667  |    70      |     4.80148 |       7.22222 |                  2.25    |
| 44 | 2019-07-01 04:00:00 |                     13.7778  |    69      |     4.63    |       7.5     |                  2.5     |
| 45 | 2019-07-01 05:00:00 |                     14.8889  |    66      |     4.11555 |       7.77778 |                  2.75    |
| 46 | 2019-07-01 06:00:00 |                     16       |    64      |     3.60111 |       7.22222 |                  3       |
| 47 | 2019-07-01 07:00:00 |                     28       |    61      |     3.08666 |       8.33333 |                  3.16667 |
| 48 | 2019-07-01 08:00:00 |                     40       |    58      |     2.57222 |      11.1111  |                  3.33333 |
| 49 | 2019-07-01 09:00:00 |                     52       |    55      |     2.7437  |      13.8889  |                  3.5     |
| 50 | 2019-07-01 10:00:00 |                     64       |    60      |     2.91518 |      16.1111  |                  3.66667 |
| 51 | 2019-07-01 11:00:00 |                     76       |    64      |     3.08666 |      17.2222  |                  3.83333 |
| 52 | 2019-07-01 12:00:00 |                     88       |    68      |     3.34389 |      18.3333  |                  4       |
| 53 | 2019-07-01 13:00:00 |                     82.5     |    70      |     3.60111 |      17.7778  |                  4       |
| 54 | 2019-07-01 14:00:00 |                     77       |    71      |     3.4725  |      18.3333  |                  4       |
| 55 | 2019-07-01 15:00:00 |                     71.5     |    72      |     3.34389 |      18.8889  |                  4       |
| 56 | 2019-07-01 16:00:00 |                     66       |    75      |     3.21528 |      18.3333  |                  4       |
| 57 | 2019-07-01 17:00:00 |                     60.5     |    79      |     3.08666 |      16.6667  |                  4       |
| 58 | 2019-07-01 18:00:00 |                     55       |    82      |     2.57222 |      17.2222  |                  4       |
| 59 | 2019-07-01 19:00:00 |                     55       |    81      |     2.05778 |      16.1111  |                  4       |
| 60 | 2019-07-01 20:00:00 |                     55       |    79      |     1.54333 |      13.8889  |                  4       |
| 61 | 2019-07-01 21:00:00 |                     55       |    78      |     1.02889 |      11.6667  |                  4       |
| 62 | 2019-07-01 22:00:00 |                     55       |    72      |     1.54333 |      11.1111  |                  4       |
| 63 | 2019-07-01 23:00:00 |                     55       |    66      |     2.05778 |      10.5556  |                  4       |

## Castle Creek

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      6       |    53      |     2.05778 |      10       |                  1       |
|  1 | 2019-06-29 09:00:00 |                      6       |    53      |     2.05778 |      10       |                  1       |
|  2 | 2019-06-29 10:00:00 |                      7       |    60      |     1.02889 |      11.1111  |                  1.16667 |
|  3 | 2019-06-29 11:00:00 |                      9       |    55      |     1.54333 |      12.2222  |                  1.33333 |
|  4 | 2019-06-29 12:00:00 |                     11       |    44      |     2.05778 |      12.7778  |                  1.66667 |
|  5 | 2019-06-29 13:00:00 |                     22       |    54      |     1.54333 |      13.8889  |                  2       |
|  6 | 2019-06-29 14:00:00 |                     33       |    65      |     2.05778 |      13.3333  |                  3       |
|  7 | 2019-06-29 15:00:00 |                     43       |    75      |     2.57222 |      13.8889  |                  4       |
|  8 | 2019-06-29 16:00:00 |                     39       |    91      |     3.08666 |      14.4444  |                  3.6     |
|  9 | 2019-06-29 17:00:00 |                     34       |    73      |     4.11555 |      15.5556  |                  3.2     |
| 10 | 2019-06-29 18:00:00 |                     30       |    82      |     3.08666 |      13.3333  |                  2.8     |
| 11 | 2019-06-29 19:00:00 |                     27       |    73      |     3.18955 |      10.5556  |                  2.4     |
| 12 | 2019-06-29 20:00:00 |                     23       |    57      |     3.29244 |       9.44444 |                  2       |
| 13 | 2019-06-29 21:00:00 |                     20       |    60      |     3.39533 |       7.77778 |                  1.75    |
| 14 | 2019-06-29 22:00:00 |                     16       |    48      |     3.49822 |       6.66667 |                  1.5     |
| 15 | 2019-06-29 23:00:00 |                     13       |    45      |     3.60111 |       5.55556 |                  1.25    |
| 16 | 2019-06-30 00:00:00 |                      9       |    41      |     3.85833 |       5.74074 |                  1       |
| 17 | 2019-06-30 01:00:00 |                      8.75    |    40.75   |     4.11555 |       5.92593 |                  1.33333 |
| 18 | 2019-06-30 02:00:00 |                      8.5     |    40.5    |     4.01266 |       6.11111 |                  1.38095 |
| 19 | 2019-06-30 03:00:00 |                      8.25    |    40.25   |     3.90977 |       5.55556 |                  1.42857 |
| 20 | 2019-06-30 04:00:00 |                      8       |    40      |     3.80689 |       5       |                  1.47619 |
| 21 | 2019-06-30 05:00:00 |                      8.66667 |    40.6667 |     3.704   |       3.88889 |                  1.52381 |
| 22 | 2019-06-30 06:00:00 |                      9.33333 |    41.3333 |     3.60111 |       4.44444 |                  1.57143 |
| 23 | 2019-06-30 07:00:00 |                     10       |    42      |     3.08666 |       6.11111 |                  1.61905 |
| 24 | 2019-06-30 08:00:00 |                     13       |    45      |     2.05778 |       8.33333 |                  1.66667 |
| 25 | 2019-06-30 09:00:00 |                     15       |    47      |     2.22926 |      11.1111  |                  2       |
| 26 | 2019-06-30 10:00:00 |                     33       |    65      |     2.40074 |      12.7778  |                  3.5     |
| 27 | 2019-06-30 11:00:00 |                     51       |    83      |     2.57222 |      14.4444  |                  4.25    |
| 28 | 2019-06-30 12:00:00 |                     69       |   100      |     3.08666 |      15       |                  5       |
| 29 | 2019-06-30 13:00:00 |                     73       |    99.8    |     3.1724  |      15.5556  |                  4.83333 |
| 30 | 2019-06-30 14:00:00 |                     77       |    99.6    |     3.25815 |      15       |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     81       |    99.4    |     3.34389 |      14.4444  |                  4.5     |
| 32 | 2019-06-30 16:00:00 |                     76       |    99.2    |     3.42963 |      12.2222  |                  4.33333 |
| 33 | 2019-06-30 17:00:00 |                     67       |    99      |     3.51537 |      10.5556  |                  4.16667 |
| 34 | 2019-06-30 18:00:00 |                     62       |    94      |     3.60111 |       8.88889 |                  4       |
| 35 | 2019-06-30 19:00:00 |                     54.6667  |    92      |     3.85833 |       7.77778 |                  3.33333 |
| 36 | 2019-06-30 20:00:00 |                     47.3333  |    90      |     4.11555 |       6.66667 |                  2.66667 |
| 37 | 2019-06-30 21:00:00 |                     40       |    88      |     3.85833 |       6.11111 |                  2       |
| 38 | 2019-06-30 22:00:00 |                     32.3333  |    86      |     3.60111 |       5.55556 |                  1.66667 |
| 39 | 2019-06-30 23:00:00 |                     24.6667  |    82      |     3.08666 |       5       |                  1.33333 |
| 40 | 2019-07-01 00:00:00 |                     17       |    80      |     2.57222 |       5.18519 |                  1       |
| 41 | 2019-07-01 01:00:00 |                     24.875   |    78      |     2.05778 |       5.37037 |                  1.16667 |
| 42 | 2019-07-01 02:00:00 |                     32.75    |    73      |     2.315   |       5.55556 |                  1.33333 |
| 43 | 2019-07-01 03:00:00 |                     48.5     |    71      |     2.57222 |       5.27778 |                  1.41667 |
| 44 | 2019-07-01 04:00:00 |                     53.75    |    70.5    |     2.82944 |       5       |                  1.5     |
| 45 | 2019-07-01 05:00:00 |                     59       |    70      |     3.08666 |       4.44444 |                  1.58333 |
| 46 | 2019-07-01 06:00:00 |                     64.25    |    69      |     2.91518 |       5       |                  1.66667 |
| 47 | 2019-07-01 07:00:00 |                     66.875   |    65      |     2.7437  |       6.11111 |                  1.77778 |
| 48 | 2019-07-01 08:00:00 |                     69.5     |    58      |     2.57222 |       8.88889 |                  1.88889 |
| 49 | 2019-07-01 09:00:00 |                     72.125   |    54      |     2.67511 |      11.1111  |                  2       |
| 50 | 2019-07-01 10:00:00 |                     74.75    |    56      |     2.778   |      13.3333  |                  3       |
| 51 | 2019-07-01 11:00:00 |                     77.375   |    61      |     2.88089 |      14.4444  |                  4       |
| 52 | 2019-07-01 12:00:00 |                     80       |    63      |     2.98378 |      15.5556  |                  5       |
| 53 | 2019-07-01 13:00:00 |                     74.5     |    65      |     3.08666 |      16.1111  |                  4.83333 |
| 54 | 2019-07-01 14:00:00 |                     69       |    68      |     3.60111 |      15.8333  |                  4.66667 |
| 55 | 2019-07-01 15:00:00 |                     63.5     |    70      |     3.42963 |      15.5556  |                  4.5     |
| 56 | 2019-07-01 16:00:00 |                     58       |    69.25   |     3.25815 |      14.4444  |                  4.33333 |
| 57 | 2019-07-01 17:00:00 |                     52.5     |    68.5    |     3.08666 |      12.7778  |                  4.16667 |
| 58 | 2019-07-01 18:00:00 |                     47       |    67.75   |     2.57222 |      10.5556  |                  4       |
| 59 | 2019-07-01 19:00:00 |                     47       |    67      |     2.315   |       8.88889 |                  3       |
| 60 | 2019-07-01 20:00:00 |                     47       |    60      |     2.05778 |       6.66667 |                  2       |
| 61 | 2019-07-01 21:00:00 |                     47       |    57      |     2.11494 |       5.55556 |                  1       |
| 62 | 2019-07-01 22:00:00 |                     47       |    56      |     2.1721  |       4.44444 |                  1       |
| 63 | 2019-07-01 23:00:00 |                     47       |    53      |     2.22926 |       3.88889 |                  1       |

## Quandary

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      1       |    37      |     2.05778 |      12.2222  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      5.25    |    58      |     1.02889 |      12.7778  |                  1.5     |
|  2 | 2019-06-29 10:00:00 |                      9.5     |    65      |     1.67194 |      13.8889  |                  1.75    |
|  3 | 2019-06-29 11:00:00 |                     13.75    |    69      |     2.315   |      14.4444  |                  2       |
|  4 | 2019-06-29 12:00:00 |                     18       |    76      |     2.95805 |      15.5556  |                  2.5     |
|  5 | 2019-06-29 13:00:00 |                     26       |    83      |     3.60111 |      16.6667  |                  3       |
|  6 | 2019-06-29 14:00:00 |                     34       |    85      |     2.05778 |      17.2222  |                  4       |
|  7 | 2019-06-29 15:00:00 |                     37       |    89      |     2.57222 |      17.7778  |                  3.88889 |
|  8 | 2019-06-29 16:00:00 |                     39       |    93      |     3.08666 |      16.6667  |                  3.77778 |
|  9 | 2019-06-29 17:00:00 |                     37       |    94      |     3.34389 |      15       |                  3.66667 |
| 10 | 2019-06-29 18:00:00 |                     34       |    95      |     3.60111 |      13.3333  |                  3.55556 |
| 11 | 2019-06-29 19:00:00 |                     32.5     |    94.6667 |     3.08666 |      11.6667  |                  3.44444 |
| 12 | 2019-06-29 20:00:00 |                     31       |    94.3333 |     2.57222 |       9.44444 |                  3.33333 |
| 13 | 2019-06-29 21:00:00 |                     29.5     |    94      |     3.08666 |       7.77778 |                  3.22222 |
| 14 | 2019-06-29 22:00:00 |                     28       |    84      |     3.21528 |       6.66667 |                  3.11111 |
| 15 | 2019-06-29 23:00:00 |                     22       |    82      |     3.34389 |       7.03704 |                  3       |
| 16 | 2019-06-30 00:00:00 |                     16       |    70      |     3.4725  |       7.40741 |                  2       |
| 17 | 2019-06-30 01:00:00 |                     11       |    60      |     3.60111 |       7.77778 |                  1       |
| 18 | 2019-06-30 02:00:00 |                      5       |    56      |     3.4725  |       8.88889 |                  1.04762 |
| 19 | 2019-06-30 03:00:00 |                      3       |    52      |     3.34389 |       9.44444 |                  1.09524 |
| 20 | 2019-06-30 04:00:00 |                      3.6     |    50.3333 |     3.21528 |       9.16667 |                  1.14286 |
| 21 | 2019-06-30 05:00:00 |                      4.2     |    48.6667 |     3.08666 |       8.88889 |                  1.19048 |
| 22 | 2019-06-30 06:00:00 |                      4.8     |    47      |     4.63    |       9.16667 |                  1.2381  |
| 23 | 2019-06-30 07:00:00 |                      5.4     |    42      |     4.11555 |       9.44444 |                  1.28571 |
| 24 | 2019-06-30 08:00:00 |                      6       |    40      |     3.60111 |      10.5556  |                  1.33333 |
| 25 | 2019-06-30 09:00:00 |                      9       |    38      |     3.85833 |      12.2222  |                  1.66667 |
| 26 | 2019-06-30 10:00:00 |                     12       |    56      |     4.11555 |      14.4444  |                  2       |
| 27 | 2019-06-30 11:00:00 |                     15       |    62      |     3.60111 |      16.6667  |                  3       |
| 28 | 2019-06-30 12:00:00 |                     28       |    80      |     5.65888 |      18.3333  |                  4       |
| 29 | 2019-06-30 13:00:00 |                     40       |    84      |     6.17333 |      18.0556  |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                     53       |    87      |     6.68777 |      17.7778  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     66       |    93      |     7.71666 |      16.1111  |                  5       |
| 32 | 2019-06-30 16:00:00 |                     64.6667  |    95      |     7.20222 |      14.4444  |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                     63.3333  |    90      |     6.68777 |      12.2222  |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                     62       |    85      |     6.17333 |      10.5556  |                  4       |
| 35 | 2019-06-30 19:00:00 |                     52.8333  |    86      |     5.91611 |       9.44444 |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     43.6667  |    88      |     5.65888 |       8.33333 |                  3       |
| 37 | 2019-06-30 21:00:00 |                     34.5     |    89      |     5.40166 |       7.77778 |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     25.3333  |    87      |     5.14444 |       6.66667 |                  2       |
| 39 | 2019-06-30 23:00:00 |                     16.1667  |    82      |     4.63    |       7.03704 |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      7       |    79      |     4.80148 |       7.40741 |                  1       |
| 41 | 2019-07-01 01:00:00 |                      4.5     |    77      |     4.97296 |       7.77778 |                  1.25    |
| 42 | 2019-07-01 02:00:00 |                      2       |    74      |     5.14444 |       8.88889 |                  1.5     |
| 43 | 2019-07-01 03:00:00 |                      6       |    72      |     5.65888 |       9.44444 |                  1.625   |
| 44 | 2019-07-01 04:00:00 |                      7.33333 |    71      |     6.17333 |       9.16667 |                  1.75    |
| 45 | 2019-07-01 05:00:00 |                      8.66667 |    68      |     5.91611 |       8.88889 |                  1.875   |
| 46 | 2019-07-01 06:00:00 |                     10       |    69      |     5.65888 |       9.25926 |                  2       |
| 47 | 2019-07-01 07:00:00 |                     21.3333  |    68      |     5.72319 |       9.62963 |                  2.5     |
| 48 | 2019-07-01 08:00:00 |                     32.6667  |    65      |     5.78749 |      10       |                  3       |
| 49 | 2019-07-01 09:00:00 |                     44       |    63      |     5.8518  |      11.6667  |                  3.5     |
| 50 | 2019-07-01 10:00:00 |                     55.3333  |    61      |     5.91611 |      13.3333  |                  4       |
| 51 | 2019-07-01 11:00:00 |                     66.6667  |    58      |     5.98041 |      15.5556  |                  4.5     |
| 52 | 2019-07-01 12:00:00 |                     78       |    56      |     6.04472 |      17.2222  |                  5       |
| 53 | 2019-07-01 13:00:00 |                     72.3333  |    61      |     6.10902 |      17.7778  |                  4.83333 |
| 54 | 2019-07-01 14:00:00 |                     66.6667  |    70      |     6.17333 |      17.2222  |                  4.66667 |
| 55 | 2019-07-01 15:00:00 |                     61       |    74      |     6.04472 |      16.6667  |                  4.5     |
| 56 | 2019-07-01 16:00:00 |                     55.3333  |    75      |     5.91611 |      15       |                  4.33333 |
| 57 | 2019-07-01 17:00:00 |                     49.6667  |    76      |     5.78749 |      13.3333  |                  4.16667 |
| 58 | 2019-07-01 18:00:00 |                     44       |    73.5    |     5.65888 |      11.6667  |                  4       |
| 59 | 2019-07-01 19:00:00 |                     44       |    71      |     5.14444 |      10       |                  4       |
| 60 | 2019-07-01 20:00:00 |                     44       |    61      |     4.88722 |       8.33333 |                  4       |
| 61 | 2019-07-01 21:00:00 |                     44       |    56      |     4.63    |       7.22222 |                  4       |
| 62 | 2019-07-01 22:00:00 |                     44       |    55      |     4.73288 |       6.11111 |                  4       |
| 63 | 2019-07-01 23:00:00 |                     44       |    54      |     4.83577 |       5.55556 |                  4       |

## Guanella Pass

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                       1      |    32      |     2.05778 |      12.7778  |                  1       |
|  1 | 2019-06-29 09:00:00 |                       7.5    |    46      |     3.60111 |      14.4444  |                  1.66667 |
|  2 | 2019-06-29 10:00:00 |                      14      |    60      |     3.85833 |      16.6667  |                  2       |
|  3 | 2019-06-29 11:00:00 |                      20.5    |    66      |     4.11555 |      16.9444  |                  2.33333 |
|  4 | 2019-06-29 12:00:00 |                      27      |    79      |     4.37277 |      17.2222  |                  3       |
|  5 | 2019-06-29 13:00:00 |                      35      |    87      |     4.63    |      17.7778  |                  4       |
|  6 | 2019-06-29 14:00:00 |                      44      |    89      |     3.08666 |      17.4074  |                  3.81818 |
|  7 | 2019-06-29 15:00:00 |                      47      |    95      |     2.91518 |      17.037   |                  3.63636 |
|  8 | 2019-06-29 16:00:00 |                      49      |    97      |     2.7437  |      16.6667  |                  3.45455 |
|  9 | 2019-06-29 17:00:00 |                      46      |    98      |     2.57222 |      14.4444  |                  3.27273 |
| 10 | 2019-06-29 18:00:00 |                      40      |    97      |     3.08666 |      12.7778  |                  3.09091 |
| 11 | 2019-06-29 19:00:00 |                      38.5    |    96      |     3.60111 |      10.5556  |                  2.90909 |
| 12 | 2019-06-29 20:00:00 |                      37      |    95      |     3.08666 |       7.77778 |                  2.72727 |
| 13 | 2019-06-29 21:00:00 |                      35.5    |    94      |     3.39533 |       6.11111 |                  2.54545 |
| 14 | 2019-06-29 22:00:00 |                      34      |    82      |     3.704   |       5       |                  2.36364 |
| 15 | 2019-06-29 23:00:00 |                      27      |    79      |     4.01266 |       5.18519 |                  2.18182 |
| 16 | 2019-06-30 00:00:00 |                      20      |    66      |     4.32133 |       5.37037 |                  2       |
| 17 | 2019-06-30 01:00:00 |                      13      |    55      |     4.63    |       5.55556 |                  1       |
| 18 | 2019-06-30 02:00:00 |                       6      |    54      |     4.50138 |       6.11111 |                  1.07143 |
| 19 | 2019-06-30 03:00:00 |                       5      |    45      |     4.37277 |       5.83333 |                  1.14286 |
| 20 | 2019-06-30 04:00:00 |                       5.6    |    44      |     4.24416 |       5.55556 |                  1.21429 |
| 21 | 2019-06-30 05:00:00 |                       6.2    |    42      |     4.11555 |       5       |                  1.28571 |
| 22 | 2019-06-30 06:00:00 |                       6.8    |    40      |     4.63    |       6.11111 |                  1.35714 |
| 23 | 2019-06-30 07:00:00 |                       7.4    |    44.75   |     4.11555 |       7.22222 |                  1.42857 |
| 24 | 2019-06-30 08:00:00 |                       8      |    49.5    |     3.94407 |      10       |                  1.5     |
| 25 | 2019-06-30 09:00:00 |                      12      |    54.25   |     3.77259 |      12.7778  |                  2       |
| 26 | 2019-06-30 10:00:00 |                      16      |    59      |     3.60111 |      15       |                  3       |
| 27 | 2019-06-30 11:00:00 |                      20      |    67      |     2.57222 |      16.1111  |                  3.5     |
| 28 | 2019-06-30 12:00:00 |                      33      |    87      |     5.14444 |      16.6667  |                  4       |
| 29 | 2019-06-30 13:00:00 |                      46      |    88.5    |     5.40166 |      16.1111  |                  4.5     |
| 30 | 2019-06-30 14:00:00 |                      59      |    90      |     5.65888 |      15.5556  |                  5       |
| 31 | 2019-06-30 15:00:00 |                      72      |    94      |     6.68777 |      14.4444  |                  4.75    |
| 32 | 2019-06-30 16:00:00 |                      69.6667 |    95      |     7.20222 |      12.7778  |                  4.5     |
| 33 | 2019-06-30 17:00:00 |                      67.3333 |    96      |     6.68777 |      11.1111  |                  4.25    |
| 34 | 2019-06-30 18:00:00 |                      65      |    87      |     6.17333 |       9.44444 |                  4       |
| 35 | 2019-06-30 19:00:00 |                      55.8333 |    86.5    |     5.65888 |       7.77778 |                  3.66667 |
| 36 | 2019-06-30 20:00:00 |                      46.6667 |    86      |     5.40166 |       6.66667 |                  3.33333 |
| 37 | 2019-06-30 21:00:00 |                      37.5    |    85      |     5.14444 |       5.55556 |                  3       |
| 38 | 2019-06-30 22:00:00 |                      28.3333 |    84      |     4.63    |       5.69444 |                  2.66667 |
| 39 | 2019-06-30 23:00:00 |                      19.1667 |    81      |     4.37277 |       5.83333 |                  2.33333 |
| 40 | 2019-07-01 00:00:00 |                      10      |    79      |     4.11555 |       5.97222 |                  2       |
| 41 | 2019-07-01 01:00:00 |                       6.5    |    76      |     4.21844 |       6.11111 |                  1.5     |
| 42 | 2019-07-01 02:00:00 |                       3      |    69      |     4.32133 |       5.92593 |                  1       |
| 43 | 2019-07-01 03:00:00 |                      10      |    65      |     4.42422 |       5.74074 |                  1.5     |
| 44 | 2019-07-01 04:00:00 |                      12.3333 |    66      |     4.52711 |       5.55556 |                  2       |
| 45 | 2019-07-01 05:00:00 |                      14.6667 |    67      |     4.63    |       6.11111 |                  2.5     |
| 46 | 2019-07-01 06:00:00 |                      17      |    66.6667 |     4.88722 |       6.66667 |                  3       |
| 47 | 2019-07-01 07:00:00 |                      28      |    66.3333 |     5.14444 |       7.77778 |                  3.33333 |
| 48 | 2019-07-01 08:00:00 |                      39      |    66      |     5.65888 |      10       |                  3.66667 |
| 49 | 2019-07-01 09:00:00 |                      50      |    65.6667 |     6.17333 |      12.2222  |                  4       |
| 50 | 2019-07-01 10:00:00 |                      61      |    65.3333 |     5.91611 |      13.8889  |                  4.33333 |
| 51 | 2019-07-01 11:00:00 |                      72      |    65      |     5.65888 |      15       |                  4.66667 |
| 52 | 2019-07-01 12:00:00 |                      83      |    66.5    |     5.14444 |      15.5556  |                  5       |
| 53 | 2019-07-01 13:00:00 |                      78      |    68      |     5.65888 |      15       |                  4.83333 |
| 54 | 2019-07-01 14:00:00 |                      73      |    73      |     5.91611 |      14.4444  |                  4.66667 |
| 55 | 2019-07-01 15:00:00 |                      68      |    75      |     6.17333 |      13.3333  |                  4.5     |
| 56 | 2019-07-01 16:00:00 |                      63      |    77      |     6.00185 |      12.7778  |                  4.33333 |
| 57 | 2019-07-01 17:00:00 |                      58      |    80      |     5.83037 |      11.6667  |                  4.16667 |
| 58 | 2019-07-01 18:00:00 |                      53      |    81      |     5.65888 |      10       |                  4       |
| 59 | 2019-07-01 19:00:00 |                      53      |    75      |     4.63    |       8.33333 |                  4       |
| 60 | 2019-07-01 20:00:00 |                      53      |    63      |     3.60111 |       6.66667 |                  4       |
| 61 | 2019-07-01 21:00:00 |                      53      |    57      |     3.08666 |       5.55556 |                  4       |
| 62 | 2019-07-01 22:00:00 |                      53      |    57.5    |     3.25815 |       4.44444 |                  4       |
| 63 | 2019-07-01 23:00:00 |                      53      |    58      |     3.42963 |       3.88889 |                  4       |

## Longs Peak

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                       0      |       42   |     2.57222 |      17.2222  |                  1       |
|  1 | 2019-06-29 09:00:00 |                       3.75   |       56   |     3.60111 |      19.4444  |                  1.33333 |
|  2 | 2019-06-29 10:00:00 |                       7.5    |       66   |     4.11555 |      21.1111  |                  1.5     |
|  3 | 2019-06-29 11:00:00 |                      11.25   |       68   |     4.63    |      21.3889  |                  1.66667 |
|  4 | 2019-06-29 12:00:00 |                      15      |       71   |     4.11555 |      21.6667  |                  2       |
|  5 | 2019-06-29 13:00:00 |                      21      |       80   |     2.57222 |      21.1111  |                  3       |
|  6 | 2019-06-29 14:00:00 |                      27      |       82   |     2.82944 |      22.7778  |                  4       |
|  7 | 2019-06-29 15:00:00 |                      28      |       90   |     3.08666 |      23.3333  |                  3.75    |
|  8 | 2019-06-29 16:00:00 |                      27      |       92   |     3.34389 |      21.6667  |                  3.5     |
|  9 | 2019-06-29 17:00:00 |                      26      |       91.5 |     3.60111 |      20       |                  3.25    |
| 10 | 2019-06-29 18:00:00 |                      22      |       91   |     4.11555 |      18.3333  |                  3       |
| 11 | 2019-06-29 19:00:00 |                      21.25   |       91.5 |     4.63    |      16.1111  |                  2.66667 |
| 12 | 2019-06-29 20:00:00 |                      20.5    |       92   |     5.14444 |      13.8889  |                  2.33333 |
| 13 | 2019-06-29 21:00:00 |                      19.75   |       90   |     4.11555 |      11.6667  |                  2       |
| 14 | 2019-06-29 22:00:00 |                      19      |       85   |     3.60111 |      10.5556  |                  1.66667 |
| 15 | 2019-06-29 23:00:00 |                      15      |       83   |     3.08666 |      10       |                  1.33333 |
| 16 | 2019-06-30 00:00:00 |                      11      |       79   |     2.57222 |      10.5556  |                  1       |
| 17 | 2019-06-30 01:00:00 |                       8      |       70   |     3.60111 |      10.8333  |                  1.6     |
| 18 | 2019-06-30 02:00:00 |                       4      |       69   |     3.42963 |      11.1111  |                  1.68571 |
| 19 | 2019-06-30 03:00:00 |                       3      |       59   |     3.25815 |      10.8333  |                  1.77143 |
| 20 | 2019-06-30 04:00:00 |                       3.6    |       55   |     3.08666 |      10.5556  |                  1.85714 |
| 21 | 2019-06-30 05:00:00 |                       4.2    |       51   |     3.60111 |      10.8333  |                  1.94286 |
| 22 | 2019-06-30 06:00:00 |                       4.8    |       47   |     4.11555 |      11.1111  |                  2.02857 |
| 23 | 2019-06-30 07:00:00 |                       5.4    |       45   |     3.60111 |      12.7778  |                  2.11429 |
| 24 | 2019-06-30 08:00:00 |                       6      |       43.5 |     3.08666 |      15       |                  2.2     |
| 25 | 2019-06-30 09:00:00 |                       9      |       42   |     2.57222 |      17.2222  |                  2.8     |
| 26 | 2019-06-30 10:00:00 |                      12      |       61   |     2.05778 |      19.4444  |                  3.4     |
| 27 | 2019-06-30 11:00:00 |                      16      |       68   |     1.54333 |      20.5556  |                  3.7     |
| 28 | 2019-06-30 12:00:00 |                      27      |       87   |     4.11555 |      21.1111  |                  4       |
| 29 | 2019-06-30 13:00:00 |                      39      |       89   |     4.45851 |      20.8333  |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                      51      |       90   |     4.80148 |      20.5556  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                      62      |       95   |     5.14444 |      19.4444  |                  5       |
| 32 | 2019-06-30 16:00:00 |                      60.3333 |       92   |     5.40166 |      18.3333  |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                      58.6667 |       94   |     5.65888 |      16.6667  |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                      57      |       79   |     4.63    |      14.4444  |                  4       |
| 35 | 2019-06-30 19:00:00 |                      49.3333 |       80   |     4.50138 |      13.3333  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                      41.6667 |       82   |     4.37277 |      11.6667  |                  3       |
| 37 | 2019-06-30 21:00:00 |                      34      |       83   |     4.24416 |      11.1111  |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                      26.3333 |       82   |     4.11555 |      10.5556  |                  2       |
| 39 | 2019-06-30 23:00:00 |                      18.6667 |       80   |     3.60111 |      10.463   |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      11      |       79   |     3.08666 |      10.3704  |                  1       |
| 41 | 2019-07-01 01:00:00 |                       7      |       78.5 |     3.25815 |      10.2778  |                  1.5     |
| 42 | 2019-07-01 02:00:00 |                       3      |       78   |     3.42963 |      10.1852  |                  2       |
| 43 | 2019-07-01 03:00:00 |                       9      |       76   |     3.60111 |      10.0926  |                  2.25    |
| 44 | 2019-07-01 04:00:00 |                      11      |       74   |     3.85833 |      10       |                  2.5     |
| 45 | 2019-07-01 05:00:00 |                      13      |       67   |     4.11555 |      10.2778  |                  2.75    |
| 46 | 2019-07-01 06:00:00 |                      15      |       55   |     4.63    |      10.5556  |                  3       |
| 47 | 2019-07-01 07:00:00 |                      25.5    |       59   |     4.50138 |      12.2222  |                  3.33333 |
| 48 | 2019-07-01 08:00:00 |                      36      |       66   |     4.37277 |      14.4444  |                  3.66667 |
| 49 | 2019-07-01 09:00:00 |                      46.5    |       69   |     4.24416 |      16.6667  |                  4       |
| 50 | 2019-07-01 10:00:00 |                      57      |       68.5 |     4.11555 |      18.3333  |                  4.33333 |
| 51 | 2019-07-01 11:00:00 |                      67.5    |       68   |     3.85833 |      19.4444  |                  4.66667 |
| 52 | 2019-07-01 12:00:00 |                      78      |       67.5 |     3.60111 |      20       |                  5       |
| 53 | 2019-07-01 13:00:00 |                      72.5    |       67   |     3.85833 |      19.6296  |                  4.83333 |
| 54 | 2019-07-01 14:00:00 |                      67      |       66   |     4.11555 |      19.2593  |                  4.66667 |
| 55 | 2019-07-01 15:00:00 |                      61.5    |       65   |     3.94407 |      18.8889  |                  4.5     |
| 56 | 2019-07-01 16:00:00 |                      56      |       66   |     3.77259 |      18.3333  |                  4.33333 |
| 57 | 2019-07-01 17:00:00 |                      50.5    |       68   |     3.60111 |      16.6667  |                  4.16667 |
| 58 | 2019-07-01 18:00:00 |                      45      |       69   |     3.51537 |      15       |                  4       |
| 59 | 2019-07-01 19:00:00 |                      45      |       66   |     3.42963 |      13.3333  |                  4       |
| 60 | 2019-07-01 20:00:00 |                      45      |       59   |     3.34389 |      11.6667  |                  4       |
| 61 | 2019-07-01 21:00:00 |                      45      |       55   |     3.25815 |      10.5556  |                  4       |
| 62 | 2019-07-01 22:00:00 |                      45      |       54.5 |     3.1724  |       9.44444 |                  4       |
| 63 | 2019-07-01 23:00:00 |                      45      |       54   |     3.08666 |       8.88889 |                  4       |

## Rock of Ages

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                       5      |    19      |     1.02889 |      16.1111  |                  1       |
|  1 | 2019-06-29 09:00:00 |                       5      |    19      |     1.02889 |      16.1111  |                  1       |
|  2 | 2019-06-29 10:00:00 |                       6      |    12      |     1.20037 |      18.3333  |                  1.16667 |
|  3 | 2019-06-29 11:00:00 |                       8      |    10      |     1.37185 |      20       |                  1.33333 |
|  4 | 2019-06-29 12:00:00 |                       9      |    41      |     1.54333 |      21.1111  |                  1.66667 |
|  5 | 2019-06-29 13:00:00 |                      20      |    52      |     1.28611 |      21.6667  |                  2       |
|  6 | 2019-06-29 14:00:00 |                      31      |    63      |     1.02889 |      22.2222  |                  4       |
|  7 | 2019-06-29 15:00:00 |                      42      |    74      |     1.54333 |      22.0833  |                  3.66667 |
|  8 | 2019-06-29 16:00:00 |                      37      |    69      |     2.05778 |      21.9444  |                  3.33333 |
|  9 | 2019-06-29 17:00:00 |                      33      |    75      |     2.57222 |      21.8056  |                  3       |
| 10 | 2019-06-29 18:00:00 |                      28      |    68      |     1.54333 |      21.6667  |                  2.66667 |
| 11 | 2019-06-29 19:00:00 |                      26      |    58      |     1.67194 |      20       |                  2.33333 |
| 12 | 2019-06-29 20:00:00 |                      23      |    55      |     1.80055 |      18.3333  |                  2       |
| 13 | 2019-06-29 21:00:00 |                      21      |    53      |     1.92917 |      16.6667  |                  1.75    |
| 14 | 2019-06-29 22:00:00 |                      18      |    50      |     2.05778 |      15       |                  1.5     |
| 15 | 2019-06-29 23:00:00 |                      16      |    48      |     3.08666 |      13.8889  |                  1.25    |
| 16 | 2019-06-30 00:00:00 |                      13      |    45      |     3.60111 |      13.3333  |                  1       |
| 17 | 2019-06-30 01:00:00 |                      12.5    |    44.5    |     4.11555 |      12.7778  |                  1.33333 |
| 18 | 2019-06-30 02:00:00 |                      12      |    44      |     3.60111 |      12.2222  |                  1.38095 |
| 19 | 2019-06-30 03:00:00 |                      11.5    |    43.5    |     3.42963 |      11.6667  |                  1.42857 |
| 20 | 2019-06-30 04:00:00 |                      11      |    43      |     3.25815 |      10.5556  |                  1.47619 |
| 21 | 2019-06-30 05:00:00 |                      10.5    |    42.5    |     3.08666 |      10       |                  1.52381 |
| 22 | 2019-06-30 06:00:00 |                      10      |    42      |     2.57222 |      10.5556  |                  1.57143 |
| 23 | 2019-06-30 07:00:00 |                      10.5    |    42.5    |     2.05778 |      12.2222  |                  1.61905 |
| 24 | 2019-06-30 08:00:00 |                      11      |    43      |     1.54333 |      15       |                  1.66667 |
| 25 | 2019-06-30 09:00:00 |                      18      |    50      |     1.02889 |      17.7778  |                  2       |
| 26 | 2019-06-30 10:00:00 |                      25      |    57      |     1.28611 |      19.4444  |                  3       |
| 27 | 2019-06-30 11:00:00 |                      39      |    71      |     1.54333 |      20       |                  3.5     |
| 28 | 2019-06-30 12:00:00 |                      53      |    88      |     1.80055 |      19.4444  |                  4       |
| 29 | 2019-06-30 13:00:00 |                      57      |    89      |     2.05778 |      18.8889  |                  5       |
| 30 | 2019-06-30 14:00:00 |                      62      |    94      |     1.92917 |      17.7778  |                  4.75    |
| 31 | 2019-06-30 15:00:00 |                      66      |    99      |     1.80055 |      16.6667  |                  4.5     |
| 32 | 2019-06-30 16:00:00 |                      62      |    94      |     1.67194 |      17.2222  |                  4.25    |
| 33 | 2019-06-30 17:00:00 |                      53      |    88      |     1.54333 |      18.3333  |                  4       |
| 34 | 2019-06-30 18:00:00 |                      49      |    81      |     1.67194 |      17.7778  |                  3       |
| 35 | 2019-06-30 19:00:00 |                      44      |    80.3333 |     1.80055 |      17.2222  |                  2.66667 |
| 36 | 2019-06-30 20:00:00 |                      39      |    79.6667 |     1.92917 |      15.5556  |                  2.33333 |
| 37 | 2019-06-30 21:00:00 |                      34      |    79      |     2.05778 |      13.8889  |                  2       |
| 38 | 2019-06-30 22:00:00 |                      28.6667 |    80      |     2.22926 |      12.2222  |                  1.66667 |
| 39 | 2019-06-30 23:00:00 |                      23.3333 |    81      |     2.40074 |      11.1111  |                  1.33333 |
| 40 | 2019-07-01 00:00:00 |                      18      |    79.5    |     2.57222 |      10.5556  |                  1       |
| 41 | 2019-07-01 01:00:00 |                      17.25   |    78      |     2.49873 |      10       |                  1.16667 |
| 42 | 2019-07-01 02:00:00 |                      16.5    |    72      |     2.42524 |       9.72222 |                  1.33333 |
| 43 | 2019-07-01 03:00:00 |                      15      |    69      |     2.35174 |       9.44444 |                  1.41667 |
| 44 | 2019-07-01 04:00:00 |                      14      |    70      |     2.27825 |       8.88889 |                  1.5     |
| 45 | 2019-07-01 05:00:00 |                      13      |    71      |     2.20476 |       8.33333 |                  1.58333 |
| 46 | 2019-07-01 06:00:00 |                      12      |    58      |     2.13127 |       8.88889 |                  1.66667 |
| 47 | 2019-07-01 07:00:00 |                      19.8333 |    55      |     2.05778 |      11.1111  |                  1.77778 |
| 48 | 2019-07-01 08:00:00 |                      27.6667 |    50      |     1.02889 |      14.4444  |                  1.88889 |
| 49 | 2019-07-01 09:00:00 |                      35.5    |    47      |     1.28611 |      17.7778  |                  2       |
| 50 | 2019-07-01 10:00:00 |                      43.3333 |    49      |     1.54333 |      19.4444  |                  2.66667 |
| 51 | 2019-07-01 11:00:00 |                      51.1667 |    52      |     2.05778 |      20.5556  |                  3.33333 |
| 52 | 2019-07-01 12:00:00 |                      59      |    54      |     2.57222 |      20.4762  |                  4       |
| 53 | 2019-07-01 13:00:00 |                      52.3333 |    57      |     3.08666 |      20.3968  |                  3.66667 |
| 54 | 2019-07-01 14:00:00 |                      45.6667 |    62      |     2.95805 |      20.3175  |                  3.33333 |
| 55 | 2019-07-01 15:00:00 |                      39      |    65      |     2.82944 |      20.2381  |                  3       |
| 56 | 2019-07-01 16:00:00 |                      32.3333 |    64.5    |     2.70083 |      20.1587  |                  2.66667 |
| 57 | 2019-07-01 17:00:00 |                      25.6667 |    64      |     2.57222 |      20.0794  |                  2.33333 |
| 58 | 2019-07-01 18:00:00 |                      19      |    63      |     2.05778 |      20       |                  2       |
| 59 | 2019-07-01 19:00:00 |                      19      |    59      |     1.54333 |      18.3333  |                  1.66667 |
| 60 | 2019-07-01 20:00:00 |                      19      |    51      |     1.71481 |      16.1111  |                  1.33333 |
| 61 | 2019-07-01 21:00:00 |                      19      |    47      |     1.88629 |      14.4444  |                  1       |
| 62 | 2019-07-01 22:00:00 |                      19      |    46      |     2.05778 |      12.7778  |                  1       |
| 63 | 2019-07-01 23:00:00 |                      19      |    44      |     2.315   |      11.6667  |                  1       |

## Shavano Tabeguache

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      0       |       35   |     2.57222 |      16.1111  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      1       |       37   |     2.82944 |      17.2222  |                  1.5     |
|  2 | 2019-06-29 10:00:00 |                      2       |       34   |     3.08666 |      20       |                  1.75    |
|  3 | 2019-06-29 11:00:00 |                      5       |       30   |     4.11555 |      22.2222  |                  2       |
|  4 | 2019-06-29 12:00:00 |                      7       |       27   |     4.63    |      21.1111  |                  2.5     |
|  5 | 2019-06-29 13:00:00 |                     22       |       39   |     4.88722 |      22.7778  |                  3       |
|  6 | 2019-06-29 14:00:00 |                     36       |       51   |     5.14444 |      23.8889  |                  4       |
|  7 | 2019-06-29 15:00:00 |                     51       |       62   |     4.63    |      23.3333  |                  3.875   |
|  8 | 2019-06-29 16:00:00 |                     46       |       69   |     4.50138 |      22.7778  |                  3.75    |
|  9 | 2019-06-29 17:00:00 |                     40       |       76   |     4.37277 |      21.6667  |                  3.625   |
| 10 | 2019-06-29 18:00:00 |                     35       |       83   |     4.24416 |      18.8889  |                  3.5     |
| 11 | 2019-06-29 19:00:00 |                     32       |       81   |     4.11555 |      17.2222  |                  3.375   |
| 12 | 2019-06-29 20:00:00 |                     29       |       78   |     3.60111 |      15.5556  |                  3.25    |
| 13 | 2019-06-29 21:00:00 |                     27       |       76   |     3.08666 |      13.8889  |                  3.125   |
| 14 | 2019-06-29 22:00:00 |                     20       |       64   |     3.18955 |      12.7778  |                  3       |
| 15 | 2019-06-29 23:00:00 |                     13       |       51   |     3.29244 |      12.2222  |                  2       |
| 16 | 2019-06-30 00:00:00 |                      6       |       39   |     3.39533 |      11.6667  |                  1       |
| 17 | 2019-06-30 01:00:00 |                      4       |       31   |     3.49822 |      11.3889  |                  1.6     |
| 18 | 2019-06-30 02:00:00 |                      3       |       24   |     3.60111 |      11.1111  |                  1.68571 |
| 19 | 2019-06-30 03:00:00 |                      1       |       16   |     3.34389 |      10.8333  |                  1.77143 |
| 20 | 2019-06-30 04:00:00 |                      2       |       23   |     3.08666 |      10.5556  |                  1.85714 |
| 21 | 2019-06-30 05:00:00 |                      3       |       29   |     2.57222 |      10       |                  1.94286 |
| 22 | 2019-06-30 06:00:00 |                      4       |       36   |     2.05778 |      10.5556  |                  2.02857 |
| 23 | 2019-06-30 07:00:00 |                      5.66667 |       33   |     1.80055 |      12.2222  |                  2.11429 |
| 24 | 2019-06-30 08:00:00 |                      7.33333 |       30   |     1.54333 |      14.4444  |                  2.2     |
| 25 | 2019-06-30 09:00:00 |                      9       |       27   |     1.64622 |      17.2222  |                  2.8     |
| 26 | 2019-06-30 10:00:00 |                     24.6667  |       39   |     1.74911 |      19.4444  |                  3.4     |
| 27 | 2019-06-30 11:00:00 |                     40.3333  |       51   |     1.852   |      21.6667  |                  3.7     |
| 28 | 2019-06-30 12:00:00 |                     56       |       63   |     1.95489 |      22.7778  |                  4       |
| 29 | 2019-06-30 13:00:00 |                     60       |       72   |     2.05778 |      23.3333  |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                     64       |       81   |     2.315   |      22.7778  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     68       |       91   |     2.57222 |      22.2222  |                  5       |
| 32 | 2019-06-30 16:00:00 |                     65.6667  |       91.5 |     3.08666 |      20.5556  |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                     63.3333  |       92   |     4.11555 |      18.3333  |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                     61       |       88   |     5.14444 |      16.6667  |                  4       |
| 35 | 2019-06-30 19:00:00 |                     52       |       89   |     4.11555 |      18.8889  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     43       |       90   |     3.60111 |      17.2222  |                  3       |
| 37 | 2019-06-30 21:00:00 |                     34       |       91   |     3.08666 |      15.5556  |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     25       |       84   |     3.60111 |      13.8889  |                  2       |
| 39 | 2019-06-30 23:00:00 |                     16       |       76   |     4.11555 |      12.7778  |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      7       |       69   |     4.37277 |      12.2222  |                  1       |
| 41 | 2019-07-01 01:00:00 |                      8.33333 |       70   |     4.63    |      11.6667  |                  1.5     |
| 42 | 2019-07-01 02:00:00 |                      9.66667 |       72   |     4.28703 |      11.1111  |                  2       |
| 43 | 2019-07-01 03:00:00 |                     12.3333  |       73   |     3.94407 |      10.5556  |                  2.25    |
| 44 | 2019-07-01 04:00:00 |                     13.2222  |       69   |     3.60111 |      10       |                  2.5     |
| 45 | 2019-07-01 05:00:00 |                     14.1111  |       65   |     2.57222 |       9.44444 |                  2.75    |
| 46 | 2019-07-01 06:00:00 |                     15       |       61   |     2.05778 |      10       |                  3       |
| 47 | 2019-07-01 07:00:00 |                     27.3333  |       59   |     1.54333 |      10.5556  |                  3.16667 |
| 48 | 2019-07-01 08:00:00 |                     39.6667  |       56   |     1.67194 |      12.7778  |                  3.33333 |
| 49 | 2019-07-01 09:00:00 |                     52       |       53   |     1.80055 |      15.5556  |                  3.5     |
| 50 | 2019-07-01 10:00:00 |                     64.3333  |       58   |     1.92917 |      17.2222  |                  3.66667 |
| 51 | 2019-07-01 11:00:00 |                     76.6667  |       63   |     2.05778 |      18.3333  |                  3.83333 |
| 52 | 2019-07-01 12:00:00 |                     89       |       68   |     2.315   |      18.8889  |                  4       |
| 53 | 2019-07-01 13:00:00 |                     83       |       69   |     2.57222 |      19.1667  |                  4       |
| 54 | 2019-07-01 14:00:00 |                     77       |       70   |     3.08666 |      19.4444  |                  4       |
| 55 | 2019-07-01 15:00:00 |                     71       |       71   |     2.91518 |      20.5556  |                  4       |
| 56 | 2019-07-01 16:00:00 |                     65       |       77   |     2.7437  |      20       |                  4       |
| 57 | 2019-07-01 17:00:00 |                     59       |       82   |     2.57222 |      18.3333  |                  4       |
| 58 | 2019-07-01 18:00:00 |                     53       |       87   |     2.05778 |      18.8889  |                  4       |
| 59 | 2019-07-01 19:00:00 |                     53       |       85   |     1.54333 |      18.3333  |                  4       |
| 60 | 2019-07-01 20:00:00 |                     53       |       82   |     1.28611 |      16.6667  |                  4       |
| 61 | 2019-07-01 21:00:00 |                     53       |       80   |     1.02889 |      15       |                  4       |
| 62 | 2019-07-01 22:00:00 |                     53       |       74   |     1.28611 |      13.3333  |                  4       |
| 63 | 2019-07-01 23:00:00 |                     53       |       68   |     1.54333 |      12.7778  |                  4       |

## Missouri Gulch

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      1       |       47   |    2.05778  |      12.7778  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      2.5     |       53   |    1.54333  |      14.4444  |                  1.33333 |
|  2 | 2019-06-29 10:00:00 |                      4       |       54   |    2.57222  |      16.1111  |                  1.5     |
|  3 | 2019-06-29 11:00:00 |                      7       |       54.5 |    4.11555  |      17.7778  |                  1.66667 |
|  4 | 2019-06-29 12:00:00 |                     10       |       55   |    4.63     |      18.3333  |                  2       |
|  5 | 2019-06-29 13:00:00 |                     25       |       57   |    4.37277  |      18.8889  |                  4       |
|  6 | 2019-06-29 14:00:00 |                     39       |       60   |    4.11555  |      19.4444  |                  3.88889 |
|  7 | 2019-06-29 15:00:00 |                     54       |       62   |    3.60111  |      18.8889  |                  3.77778 |
|  8 | 2019-06-29 16:00:00 |                     48       |       70   |    2.57222  |      18.3333  |                  3.66667 |
|  9 | 2019-06-29 17:00:00 |                     42       |       77   |    1.54333  |      17.2222  |                  3.55556 |
| 10 | 2019-06-29 18:00:00 |                     35       |       85   |    1.71481  |      16.1111  |                  3.44444 |
| 11 | 2019-06-29 19:00:00 |                     33       |       80   |    1.88629  |      15       |                  3.33333 |
| 12 | 2019-06-29 20:00:00 |                     30       |       76   |    2.05778  |      13.3333  |                  3.22222 |
| 13 | 2019-06-29 21:00:00 |                     28       |       71   |    2.57222  |      11.1111  |                  3.11111 |
| 14 | 2019-06-29 22:00:00 |                     20       |       58   |    2.05778  |      10       |                  3       |
| 15 | 2019-06-29 23:00:00 |                     12       |       45   |    1.54333  |       9.72222 |                  2       |
| 16 | 2019-06-30 00:00:00 |                      4       |       33   |    1.02889  |       9.44444 |                  1       |
| 17 | 2019-06-30 01:00:00 |                      3       |       26   |    1.54333  |       9.16667 |                  1.6     |
| 18 | 2019-06-30 02:00:00 |                      2       |       20   |    2.05778  |       8.88889 |                  1.68571 |
| 19 | 2019-06-30 03:00:00 |                      1       |       14   |    3.08666  |       7.77778 |                  1.77143 |
| 20 | 2019-06-30 04:00:00 |                      2       |       21   |    2.82944  |       7.22222 |                  1.85714 |
| 21 | 2019-06-30 05:00:00 |                      3       |       27   |    2.57222  |       7.77778 |                  1.94286 |
| 22 | 2019-06-30 06:00:00 |                      4       |       34   |    2.315    |       8.33333 |                  2.02857 |
| 23 | 2019-06-30 07:00:00 |                      5.66667 |       33   |    2.05778  |      10       |                  2.11429 |
| 24 | 2019-06-30 08:00:00 |                      7.33333 |       31   |    1.80055  |      13.3333  |                  2.2     |
| 25 | 2019-06-30 09:00:00 |                      9       |       30   |    1.54333  |      16.1111  |                  2.8     |
| 26 | 2019-06-30 10:00:00 |                     26.6667  |       45   |    1.02889  |      17.7778  |                  3.4     |
| 27 | 2019-06-30 11:00:00 |                     44.3333  |       60   |    1.37185  |      18.8889  |                  3.7     |
| 28 | 2019-06-30 12:00:00 |                     62       |       74   |    1.71481  |      19.4444  |                  4       |
| 29 | 2019-06-30 13:00:00 |                     66.3333  |       78   |    2.05778  |      18.8889  |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                     70.6667  |       81   |    3.08666  |      18.3333  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     75       |       85   |    4.11555  |      17.2222  |                  5       |
| 32 | 2019-06-30 16:00:00 |                     69.3333  |       86   |    3.85833  |      16.1111  |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                     63.6667  |       88   |    3.60111  |      14.4444  |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                     58       |       89   |    2.57222  |      12.7778  |                  4       |
| 35 | 2019-06-30 19:00:00 |                     49.3333  |       88.5 |    1.54333  |      13.8889  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     40.6667  |       88   |    1.02889  |      11.1111  |                  3       |
| 37 | 2019-06-30 21:00:00 |                     32       |       86   |    0.514444 |       8.88889 |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     23.3333  |       84   |    1.02889  |       7.77778 |                  2       |
| 39 | 2019-06-30 23:00:00 |                     14.6667  |       80   |    1.54333  |       7.5     |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      6       |       76   |    2.05778  |       7.22222 |                  1       |
| 41 | 2019-07-01 01:00:00 |                      8.33333 |       72   |    2.18639  |       6.66667 |                  1.5     |
| 42 | 2019-07-01 02:00:00 |                     10.6667  |       68   |    2.315    |       6.11111 |                  2       |
| 43 | 2019-07-01 03:00:00 |                     15.3333  |       64   |    2.44361  |       5.55556 |                  2.25    |
| 44 | 2019-07-01 04:00:00 |                     16.8889  |       63.5 |    2.57222  |       5.37037 |                  2.5     |
| 45 | 2019-07-01 05:00:00 |                     18.4444  |       63   |    2.46933  |       5.18519 |                  2.75    |
| 46 | 2019-07-01 06:00:00 |                     20       |       62.5 |    2.36644  |       5       |                  3       |
| 47 | 2019-07-01 07:00:00 |                     31.1667  |       62   |    2.26355  |       6.11111 |                  3.16667 |
| 48 | 2019-07-01 08:00:00 |                     42.3333  |       60   |    2.16066  |       8.88889 |                  3.33333 |
| 49 | 2019-07-01 09:00:00 |                     53.5     |       58   |    2.05778  |      11.1111  |                  3.5     |
| 50 | 2019-07-01 10:00:00 |                     64.6667  |       60   |    2.315    |      12.2222  |                  3.66667 |
| 51 | 2019-07-01 11:00:00 |                     75.8333  |       61   |    2.57222  |      13.3333  |                  3.83333 |
| 52 | 2019-07-01 12:00:00 |                     87       |       63   |    2.7437   |      13.8889  |                  4       |
| 53 | 2019-07-01 13:00:00 |                     81       |       66   |    2.91518  |      14.1667  |                  4       |
| 54 | 2019-07-01 14:00:00 |                     75       |       69   |    3.08666  |      14.4444  |                  4       |
| 55 | 2019-07-01 15:00:00 |                     69       |       72   |    2.91518  |      14.1667  |                  4       |
| 56 | 2019-07-01 16:00:00 |                     63       |       75   |    2.7437   |      13.8889  |                  4       |
| 57 | 2019-07-01 17:00:00 |                     57       |       78   |    2.57222  |      13.3333  |                  4       |
| 58 | 2019-07-01 18:00:00 |                     51       |       80   |    2.05778  |      12.7778  |                  4       |
| 59 | 2019-07-01 19:00:00 |                     51       |       78   |    1.80055  |      12.2222  |                  4       |
| 60 | 2019-07-01 20:00:00 |                     51       |       75   |    1.54333  |      10       |                  4       |
| 61 | 2019-07-01 21:00:00 |                     51       |       72   |    1.02889  |       7.77778 |                  4       |
| 62 | 2019-07-01 22:00:00 |                     51       |       67   |    1.54333  |       7.22222 |                  4       |
| 63 | 2019-07-01 23:00:00 |                     51       |       63   |    1.80055  |       6.66667 |                  4       |

## Mt Princeton Road

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      1       |       32   |    1.54333  |      17.7778  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      2       |       33   |    1.37185  |      19.4444  |                  1.5     |
|  2 | 2019-06-29 10:00:00 |                      3       |       34   |    1.20037  |      21.1111  |                  1.75    |
|  3 | 2019-06-29 11:00:00 |                      4       |       34.5 |    1.02889  |      24.4444  |                  2       |
|  4 | 2019-06-29 12:00:00 |                      6       |       35   |    1.28611  |      22.2222  |                  2.5     |
|  5 | 2019-06-29 13:00:00 |                     21       |       43   |    1.54333  |      23.8889  |                  3       |
|  6 | 2019-06-29 14:00:00 |                     36       |       51   |    2.05778  |      25.5556  |                  4       |
|  7 | 2019-06-29 15:00:00 |                     51       |       59   |    2.57222  |      24.4444  |                  3.875   |
|  8 | 2019-06-29 16:00:00 |                     45       |       68   |    2.70083  |      23.8889  |                  3.75    |
|  9 | 2019-06-29 17:00:00 |                     38       |       77   |    2.82944  |      22.2222  |                  3.625   |
| 10 | 2019-06-29 18:00:00 |                     32       |       86   |    2.95805  |      20.5556  |                  3.5     |
| 11 | 2019-06-29 19:00:00 |                     30       |       84   |    3.08666  |      18.8889  |                  3.375   |
| 12 | 2019-06-29 20:00:00 |                     29       |       82   |    3.60111  |      17.2222  |                  3.25    |
| 13 | 2019-06-29 21:00:00 |                     27       |       80   |    3.34389  |      16.1111  |                  3.125   |
| 14 | 2019-06-29 22:00:00 |                     20       |       64   |    3.08666  |      15       |                  3       |
| 15 | 2019-06-29 23:00:00 |                     14       |       49   |    2.82944  |      13.8889  |                  2       |
| 16 | 2019-06-30 00:00:00 |                      7       |       33   |    2.57222  |      13.3333  |                  1       |
| 17 | 2019-06-30 01:00:00 |                      5       |       27   |    2.05778  |      12.7778  |                  1.6     |
| 18 | 2019-06-30 02:00:00 |                      3       |       20   |    1.97204  |      12.2222  |                  1.68571 |
| 19 | 2019-06-30 03:00:00 |                      1       |       14   |    1.88629  |      11.6667  |                  1.77143 |
| 20 | 2019-06-30 04:00:00 |                      2       |       19   |    1.80055  |      11.1111  |                  1.85714 |
| 21 | 2019-06-30 05:00:00 |                      3       |       25   |    1.71481  |      10.5556  |                  1.94286 |
| 22 | 2019-06-30 06:00:00 |                      4       |       30   |    1.62907  |      11.1111  |                  2.02857 |
| 23 | 2019-06-30 07:00:00 |                      5.33333 |       32   |    1.54333  |      13.3333  |                  2.11429 |
| 24 | 2019-06-30 08:00:00 |                      6.66667 |       34   |    1.02889  |      16.6667  |                  2.2     |
| 25 | 2019-06-30 09:00:00 |                      8       |       36   |    1.1575   |      19.4444  |                  2.8     |
| 26 | 2019-06-30 10:00:00 |                     23.3333  |       38   |    1.28611  |      22.2222  |                  3.4     |
| 27 | 2019-06-30 11:00:00 |                     38.6667  |       47   |    1.41472  |      23.8889  |                  3.7     |
| 28 | 2019-06-30 12:00:00 |                     54       |       56   |    1.54333  |      25       |                  4       |
| 29 | 2019-06-30 13:00:00 |                     57.6667  |       64   |    1.80055  |      24.7222  |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                     61.3333  |       73   |    2.05778  |      24.4444  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     65       |       81   |    2.315    |      23.3333  |                  5       |
| 32 | 2019-06-30 16:00:00 |                     62.3333  |       85   |    2.57222  |      21.6667  |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                     59.6667  |       88   |    3.08666  |      19.4444  |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                     57       |       94   |    3.60111  |      17.2222  |                  4       |
| 35 | 2019-06-30 19:00:00 |                     48.6667  |       93   |    3.34389  |      20.5556  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     40.3333  |       92   |    3.08666  |      17.7778  |                  3       |
| 37 | 2019-06-30 21:00:00 |                     32       |       91   |    3.21528  |      16.1111  |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     23.3333  |       85   |    3.34389  |      15       |                  2       |
| 39 | 2019-06-30 23:00:00 |                     14.6667  |       79   |    3.4725   |      12.7778  |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      6       |       73   |    3.60111  |      12.2222  |                  1       |
| 41 | 2019-07-01 01:00:00 |                      7.5     |       71   |    3.85833  |      11.1111  |                  1.5     |
| 42 | 2019-07-01 02:00:00 |                      9       |       69   |    4.11555  |      11.6667  |                  2       |
| 43 | 2019-07-01 03:00:00 |                     12       |       67   |    3.60111  |      10       |                  2.25    |
| 44 | 2019-07-01 04:00:00 |                     13       |       65   |    3.08666  |       9.72222 |                  2.5     |
| 45 | 2019-07-01 05:00:00 |                     14       |       63   |    2.57222  |       9.44444 |                  2.75    |
| 46 | 2019-07-01 06:00:00 |                     15       |       62   |    2.05778  |       8.88889 |                  3       |
| 47 | 2019-07-01 07:00:00 |                     27.1667  |       60   |    1.54333  |      10       |                  3.16667 |
| 48 | 2019-07-01 08:00:00 |                     39.3333  |       58   |    1.02889  |      12.7778  |                  3.33333 |
| 49 | 2019-07-01 09:00:00 |                     51.5     |       56   |    0.514444 |      16.1111  |                  3.5     |
| 50 | 2019-07-01 10:00:00 |                     63.6667  |       60   |    1.02889  |      18.8889  |                  3.66667 |
| 51 | 2019-07-01 11:00:00 |                     75.8333  |       65   |    1.28611  |      21.1111  |                  3.83333 |
| 52 | 2019-07-01 12:00:00 |                     88       |       69   |    1.54333  |      21.6667  |                  4       |
| 53 | 2019-07-01 13:00:00 |                     81.5     |       70   |    2.05778  |      21.1111  |                  4       |
| 54 | 2019-07-01 14:00:00 |                     75       |       71   |    1.95489  |      21.6667  |                  4       |
| 55 | 2019-07-01 15:00:00 |                     68.5     |       72   |    1.852    |      22.7778  |                  4       |
| 56 | 2019-07-01 16:00:00 |                     62       |       77   |    1.74911  |      22.2222  |                  4       |
| 57 | 2019-07-01 17:00:00 |                     55.5     |       82   |    1.64622  |      20.5556  |                  4       |
| 58 | 2019-07-01 18:00:00 |                     49       |       86   |    1.54333  |      21.1111  |                  4       |
| 59 | 2019-07-01 19:00:00 |                     49       |       84   |    1.62907  |      19.4444  |                  4       |
| 60 | 2019-07-01 20:00:00 |                     49       |       82   |    1.71481  |      17.2222  |                  4       |
| 61 | 2019-07-01 21:00:00 |                     49       |       80   |    1.80055  |      15.5556  |                  4       |
| 62 | 2019-07-01 22:00:00 |                     49       |       74   |    1.88629  |      14.4444  |                  4       |
| 63 | 2019-07-01 23:00:00 |                     49       |       67   |    1.97204  |      12.2222  |                  4       |

## Denny Creek

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      1       |       33   |     3.60111 |      11.6667  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      2.5     |       34   |     3.77259 |      12.2222  |                  1.33333 |
|  2 | 2019-06-29 10:00:00 |                      4       |       37   |     3.94407 |      14.4444  |                  1.5     |
|  3 | 2019-06-29 11:00:00 |                      7       |       39   |     4.11555 |      16.1111  |                  1.66667 |
|  4 | 2019-06-29 12:00:00 |                     10       |       42   |     4.37277 |      16.6667  |                  2       |
|  5 | 2019-06-29 13:00:00 |                     25       |       50   |     4.63    |      17.2222  |                  4       |
|  6 | 2019-06-29 14:00:00 |                     39       |       58   |     5.14444 |      17.7778  |                  3.88889 |
|  7 | 2019-06-29 15:00:00 |                     54       |       66   |     4.63    |      17.2222  |                  3.77778 |
|  8 | 2019-06-29 16:00:00 |                     51       |       71   |     4.11555 |      16.1111  |                  3.66667 |
|  9 | 2019-06-29 17:00:00 |                     47       |       77   |     3.08666 |      14.4444  |                  3.55556 |
| 10 | 2019-06-29 18:00:00 |                     44       |       83   |     2.57222 |      13.8889  |                  3.44444 |
| 11 | 2019-06-29 19:00:00 |                     39       |       80   |     3.08666 |      13.3333  |                  3.33333 |
| 12 | 2019-06-29 20:00:00 |                     34       |       76   |     3.34389 |      11.6667  |                  3.22222 |
| 13 | 2019-06-29 21:00:00 |                     28       |       73   |     3.60111 |      10       |                  3.11111 |
| 14 | 2019-06-29 22:00:00 |                     20       |       60   |     3.08666 |       8.88889 |                  3       |
| 15 | 2019-06-29 23:00:00 |                     12       |       48   |     2.57222 |       8.61111 |                  2       |
| 16 | 2019-06-30 00:00:00 |                      5       |       35   |     2.05778 |       8.33333 |                  1       |
| 17 | 2019-06-30 01:00:00 |                      3       |       28   |     2.315   |       7.77778 |                  1.6     |
| 18 | 2019-06-30 02:00:00 |                      2       |       20   |     2.57222 |       7.5     |                  1.68571 |
| 19 | 2019-06-30 03:00:00 |                      1       |       13   |     3.08666 |       7.22222 |                  1.77143 |
| 20 | 2019-06-30 04:00:00 |                      2       |       18   |     3.34389 |       6.66667 |                  1.85714 |
| 21 | 2019-06-30 05:00:00 |                      3       |       24   |     3.60111 |       6.11111 |                  1.94286 |
| 22 | 2019-06-30 06:00:00 |                      4       |       29   |     3.34389 |       6.66667 |                  2.02857 |
| 23 | 2019-06-30 07:00:00 |                      5.66667 |       33   |     3.08666 |       8.33333 |                  2.11429 |
| 24 | 2019-06-30 08:00:00 |                      7.33333 |       37   |     2.82944 |      10.5556  |                  2.2     |
| 25 | 2019-06-30 09:00:00 |                      9       |       41   |     2.57222 |      13.3333  |                  2.8     |
| 26 | 2019-06-30 10:00:00 |                     27.6667  |       45   |     2.05778 |      15       |                  3.4     |
| 27 | 2019-06-30 11:00:00 |                     46.3333  |       60   |     2.22926 |      16.1111  |                  3.7     |
| 28 | 2019-06-30 12:00:00 |                     65       |       76   |     2.40074 |      16.6667  |                  4       |
| 29 | 2019-06-30 13:00:00 |                     68.3333  |       82   |     2.57222 |      17.2222  |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                     71.6667  |       88   |     3.60111 |      16.6667  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     75       |       93   |     4.63    |      16.1111  |                  5       |
| 32 | 2019-06-30 16:00:00 |                     70.3333  |       92.5 |     4.37277 |      14.4444  |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                     65.6667  |       92   |     4.11555 |      12.2222  |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                     61       |       94   |     3.08666 |      10.5556  |                  4       |
| 35 | 2019-06-30 19:00:00 |                     52       |       92   |     3.60111 |      12.7778  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     43       |       91   |     3.77259 |      11.1111  |                  3       |
| 37 | 2019-06-30 21:00:00 |                     34       |       89   |     3.94407 |      10       |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     24.6667  |       84   |     4.11555 |       9.44444 |                  2       |
| 39 | 2019-06-30 23:00:00 |                     15.3333  |       79   |     4.63    |       8.33333 |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      6       |       73   |     5.14444 |       8.05556 |                  1       |
| 41 | 2019-07-01 01:00:00 |                      8.16667 |       72   |     5.40166 |       7.77778 |                  1.5     |
| 42 | 2019-07-01 02:00:00 |                     10.3333  |       70   |     5.65888 |       6.11111 |                  2       |
| 43 | 2019-07-01 03:00:00 |                     14.6667  |       69   |     5.40166 |       5.92593 |                  2.25    |
| 44 | 2019-07-01 04:00:00 |                     16.1111  |       67   |     5.14444 |       5.74074 |                  2.5     |
| 45 | 2019-07-01 05:00:00 |                     17.5556  |       66   |     4.63    |       5.55556 |                  2.75    |
| 46 | 2019-07-01 06:00:00 |                     19       |       65   |     4.37277 |       6.38889 |                  3       |
| 47 | 2019-07-01 07:00:00 |                     30.5     |       62   |     4.11555 |       7.22222 |                  3.16667 |
| 48 | 2019-07-01 08:00:00 |                     42       |       60   |     4.06411 |       9.44444 |                  3.33333 |
| 49 | 2019-07-01 09:00:00 |                     53.5     |       57   |     4.01266 |      11.1111  |                  3.5     |
| 50 | 2019-07-01 10:00:00 |                     65       |       61   |     3.96122 |      12.7778  |                  3.66667 |
| 51 | 2019-07-01 11:00:00 |                     76.5     |       65   |     3.90977 |      13.8889  |                  3.83333 |
| 52 | 2019-07-01 12:00:00 |                     88       |       69   |     3.85833 |      14.4444  |                  4       |
| 53 | 2019-07-01 13:00:00 |                     82.3333  |       70   |     3.80689 |      14.5833  |                  4       |
| 54 | 2019-07-01 14:00:00 |                     76.6667  |       71   |     3.75544 |      14.7222  |                  4       |
| 55 | 2019-07-01 15:00:00 |                     71       |       72   |     3.704   |      14.8611  |                  4       |
| 56 | 2019-07-01 16:00:00 |                     65.3333  |       75   |     3.65255 |      15       |                  4       |
| 57 | 2019-07-01 17:00:00 |                     59.6667  |       77   |     3.60111 |      13.8889  |                  4       |
| 58 | 2019-07-01 18:00:00 |                     54       |       80   |     3.08666 |      12.7778  |                  4       |
| 59 | 2019-07-01 19:00:00 |                     54       |       79   |     2.82944 |      12.2222  |                  4       |
| 60 | 2019-07-01 20:00:00 |                     54       |       77   |     2.57222 |      11.1111  |                  4       |
| 61 | 2019-07-01 21:00:00 |                     54       |       76   |     2.65796 |       9.44444 |                  4       |
| 62 | 2019-07-01 22:00:00 |                     54       |       70   |     2.7437  |       8.88889 |                  4       |
| 63 | 2019-07-01 23:00:00 |                     54       |       65   |     2.82944 |       7.77778 |                  4       |

## Willow Creek

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      0       |    19      |     2.05778 |       16.1111 |                  1       |
|  1 | 2019-06-29 09:00:00 |                      1.5     |    20      |     2.18639 |       18.3333 |                  1.5     |
|  2 | 2019-06-29 10:00:00 |                      3       |    21      |     2.315   |       21.6667 |                  1.75    |
|  3 | 2019-06-29 11:00:00 |                      6       |    23      |     2.44361 |       24.4444 |                  2       |
|  4 | 2019-06-29 12:00:00 |                      9       |    26      |     2.57222 |       23.8889 |                  2.5     |
|  5 | 2019-06-29 13:00:00 |                     21       |    29      |     2.70083 |       25.5556 |                  3       |
|  6 | 2019-06-29 14:00:00 |                     33       |    32      |     2.82944 |       26.6667 |                  4       |
|  7 | 2019-06-29 15:00:00 |                     45       |    45      |     2.95805 |       26.3889 |                  3.875   |
|  8 | 2019-06-29 16:00:00 |                     42       |    53      |     3.08666 |       26.1111 |                  3.75    |
|  9 | 2019-06-29 17:00:00 |                     40       |    70      |     4.63    |       25.5556 |                  3.625   |
| 10 | 2019-06-29 18:00:00 |                     37       |    88      |     5.14444 |       24.4444 |                  3.5     |
| 11 | 2019-06-29 19:00:00 |                     33       |    87      |     4.88722 |       22.7778 |                  3.375   |
| 12 | 2019-06-29 20:00:00 |                     29       |    86.5    |     4.63    |       20.5556 |                  3.25    |
| 13 | 2019-06-29 21:00:00 |                     25       |    86      |     3.60111 |       18.8889 |                  3.125   |
| 14 | 2019-06-29 22:00:00 |                     18       |    76      |     2.57222 |       17.2222 |                  3       |
| 15 | 2019-06-29 23:00:00 |                     11       |    65      |     2.05778 |       16.6667 |                  2       |
| 16 | 2019-06-30 00:00:00 |                      5       |    55      |     1.54333 |       16.1111 |                  1       |
| 17 | 2019-06-30 01:00:00 |                      4       |    46      |     1.02889 |       15.5556 |                  1.6     |
| 18 | 2019-06-30 02:00:00 |                      3       |    37      |     1.20037 |       15      |                  1.68571 |
| 19 | 2019-06-30 03:00:00 |                      2       |    29      |     1.37185 |       13.8889 |                  1.77143 |
| 20 | 2019-06-30 04:00:00 |                      2.66667 |    27      |     1.54333 |       12.7778 |                  1.85714 |
| 21 | 2019-06-30 05:00:00 |                      3.33333 |    26      |     1.80055 |       11.6667 |                  1.94286 |
| 22 | 2019-06-30 06:00:00 |                      4       |    24      |     2.05778 |       12.7778 |                  2.02857 |
| 23 | 2019-06-30 07:00:00 |                      4.66667 |    23      |     2.315   |       13.8889 |                  2.11429 |
| 24 | 2019-06-30 08:00:00 |                      5.33333 |    22      |     2.57222 |       16.6667 |                  2.2     |
| 25 | 2019-06-30 09:00:00 |                      6       |    20      |     2.40074 |       20      |                  2.8     |
| 26 | 2019-06-30 10:00:00 |                     21       |    34      |     2.22926 |       22.2222 |                  3.4     |
| 27 | 2019-06-30 11:00:00 |                     36       |    47      |     2.05778 |       24.4444 |                  3.7     |
| 28 | 2019-06-30 12:00:00 |                     51       |    60      |     2.18639 |       25.5556 |                  4       |
| 29 | 2019-06-30 13:00:00 |                     55.6667  |    58      |     2.315   |       26.6667 |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                     60.3333  |    55      |     2.44361 |       26.3889 |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     65       |    75      |     2.57222 |       26.1111 |                  5       |
| 32 | 2019-06-30 16:00:00 |                     62.6667  |    80.6667 |     2.82944 |       24.4444 |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                     60.3333  |    86.3333 |     3.08666 |       22.2222 |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                     58       |    92      |     2.57222 |       20.5556 |                  4       |
| 35 | 2019-06-30 19:00:00 |                     49.6667  |    91      |     2.05778 |       21.1111 |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     41.3333  |    90      |     1.54333 |       19.4444 |                  3       |
| 37 | 2019-06-30 21:00:00 |                     33       |    89      |     1.80055 |       17.7778 |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     24.3333  |    85      |     2.05778 |       15.5556 |                  2       |
| 39 | 2019-06-30 23:00:00 |                     15.6667  |    80      |     2.315   |       15      |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      7       |    76      |     2.57222 |       13.8889 |                  1       |
| 41 | 2019-07-01 01:00:00 |                      8.33333 |    72      |     2.82944 |       13.3333 |                  1.5     |
| 42 | 2019-07-01 02:00:00 |                      9.66667 |    69      |     3.08666 |       12.7778 |                  2       |
| 43 | 2019-07-01 03:00:00 |                     12.3333  |    66      |     2.82944 |       11.6667 |                  2.25    |
| 44 | 2019-07-01 04:00:00 |                     13.2222  |    65.5    |     2.57222 |       11.1111 |                  2.5     |
| 45 | 2019-07-01 05:00:00 |                     14.1111  |    65      |     2.40074 |       10.5556 |                  2.75    |
| 46 | 2019-07-01 06:00:00 |                     15       |    62      |     2.22926 |       10.8333 |                  3       |
| 47 | 2019-07-01 07:00:00 |                     28       |    59      |     2.05778 |       11.1111 |                  3.16667 |
| 48 | 2019-07-01 08:00:00 |                     41       |    52      |     1.92917 |       14.4444 |                  3.33333 |
| 49 | 2019-07-01 09:00:00 |                     54       |    45      |     1.80055 |       17.2222 |                  3.5     |
| 50 | 2019-07-01 10:00:00 |                     67       |    55      |     1.67194 |       18.3333 |                  3.66667 |
| 51 | 2019-07-01 11:00:00 |                     80       |    64      |     1.54333 |       20      |                  3.83333 |
| 52 | 2019-07-01 12:00:00 |                     93       |    74      |     1.67194 |       21.1111 |                  4       |
| 53 | 2019-07-01 13:00:00 |                     88       |    75      |     1.80055 |       21.6667 |                  4       |
| 54 | 2019-07-01 14:00:00 |                     83       |    76      |     1.92917 |       22.2222 |                  4       |
| 55 | 2019-07-01 15:00:00 |                     78       |    77      |     2.05778 |       22.7778 |                  4       |
| 56 | 2019-07-01 16:00:00 |                     73       |    81      |     1.54333 |       22.2222 |                  4       |
| 57 | 2019-07-01 17:00:00 |                     68       |    85      |     1.02889 |       22.037  |                  4       |
| 58 | 2019-07-01 18:00:00 |                     63       |    89      |     1.13178 |       21.8519 |                  4       |
| 59 | 2019-07-01 19:00:00 |                     63       |    88      |     1.23467 |       21.6667 |                  4       |
| 60 | 2019-07-01 20:00:00 |                     63       |    87      |     1.33755 |       19.4444 |                  4       |
| 61 | 2019-07-01 21:00:00 |                     63       |    86      |     1.44044 |       17.2222 |                  4       |
| 62 | 2019-07-01 22:00:00 |                     63       |    79      |     1.54333 |       15.5556 |                  4       |
| 63 | 2019-07-01 23:00:00 |                     63       |    72      |     1.80055 |       14.4444 |                  4       |

## Navajo Lake

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                       4      |    12      |    1.02889  |      13.3333  |                  1       |
|  1 | 2019-06-29 09:00:00 |                       4      |    12      |    1.02889  |      13.3333  |                  1       |
|  2 | 2019-06-29 10:00:00 |                       5      |    10      |    0.514444 |      16.6667  |                  1.16667 |
|  3 | 2019-06-29 11:00:00 |                       6      |    24.5    |    1.02889  |      18.3333  |                  1.33333 |
|  4 | 2019-06-29 12:00:00 |                       7      |    39      |    1.28611  |      17.5     |                  1.66667 |
|  5 | 2019-06-29 13:00:00 |                      18      |    56      |    1.54333  |      16.6667  |                  2       |
|  6 | 2019-06-29 14:00:00 |                      30      |    62      |    2.05778  |      17.7778  |                  4       |
|  7 | 2019-06-29 15:00:00 |                      40      |    72      |    2.57222  |      16.6667  |                  3.71429 |
|  8 | 2019-06-29 16:00:00 |                      37      |    75      |    3.08666  |      16.3889  |                  3.42857 |
|  9 | 2019-06-29 17:00:00 |                      35      |    82.5    |    3.60111  |      16.1111  |                  3.14286 |
| 10 | 2019-06-29 18:00:00 |                      32      |    90      |    4.11555  |      15.5556  |                  2.85714 |
| 11 | 2019-06-29 19:00:00 |                      29      |    61      |    3.08666  |      14.4444  |                  2.57143 |
| 12 | 2019-06-29 20:00:00 |                      25      |    57      |    2.82944  |      12.7778  |                  2.28571 |
| 13 | 2019-06-29 21:00:00 |                      22      |    54      |    2.57222  |      11.6667  |                  2       |
| 14 | 2019-06-29 22:00:00 |                      19      |    51      |    3.60111  |      10.5556  |                  1.66667 |
| 15 | 2019-06-29 23:00:00 |                      15      |    47      |    4.63     |       9.44444 |                  1.33333 |
| 16 | 2019-06-30 00:00:00 |                      12      |    44      |    5.14444  |       8.88889 |                  1       |
| 17 | 2019-06-30 01:00:00 |                      11      |    43      |    4.97296  |       8.61111 |                  1.33333 |
| 18 | 2019-06-30 02:00:00 |                      10.5    |    42.5    |    4.80148  |       8.33333 |                  1.38095 |
| 19 | 2019-06-30 03:00:00 |                      10      |    42      |    4.63     |       7.77778 |                  1.42857 |
| 20 | 2019-06-30 04:00:00 |                       9      |    41      |    4.11555  |       7.22222 |                  1.47619 |
| 21 | 2019-06-30 05:00:00 |                       8.5    |    40.5    |    3.60111  |       7.5     |                  1.52381 |
| 22 | 2019-06-30 06:00:00 |                       8      |    40      |    3.6746   |       7.77778 |                  1.57143 |
| 23 | 2019-06-30 07:00:00 |                      10      |    42      |    3.74809  |       9.44444 |                  1.61905 |
| 24 | 2019-06-30 08:00:00 |                      13      |    45      |    3.82158  |      11.6667  |                  1.66667 |
| 25 | 2019-06-30 09:00:00 |                      15      |    47      |    3.89508  |      13.8889  |                  2       |
| 26 | 2019-06-30 10:00:00 |                      31      |    63      |    3.96857  |      15       |                  3.5     |
| 27 | 2019-06-30 11:00:00 |                      46      |    78      |    4.04206  |      15.5556  |                  4.25    |
| 28 | 2019-06-30 12:00:00 |                      62      |    94      |    4.11555  |      15       |                  5       |
| 29 | 2019-06-30 13:00:00 |                      65      |    97      |    4.04206  |      14.4444  |                  4.83333 |
| 30 | 2019-06-30 14:00:00 |                      69      |   100      |    3.96857  |      13.3333  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                      72      |    99.5    |    3.89508  |      12.7778  |                  4.5     |
| 32 | 2019-06-30 16:00:00 |                      67      |    99      |    3.82158  |      13.3333  |                  4.33333 |
| 33 | 2019-06-30 17:00:00 |                      56      |    89      |    3.74809  |      13.6111  |                  4.16667 |
| 34 | 2019-06-30 18:00:00 |                      51      |    83      |    3.6746   |      13.8889  |                  4       |
| 35 | 2019-06-30 19:00:00 |                      45.6667 |    81.3333 |    3.60111  |      12.7778  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                      40.3333 |    79.6667 |    3.6746   |      11.1111  |                  3       |
| 37 | 2019-06-30 21:00:00 |                      35      |    78      |    3.74809  |      10       |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                      29.3333 |    79      |    3.82158  |       8.88889 |                  2       |
| 39 | 2019-06-30 23:00:00 |                      23.6667 |    80      |    3.89508  |       8.33333 |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      18      |    79      |    3.96857  |       8.05556 |                  1       |
| 41 | 2019-07-01 01:00:00 |                      17.5    |    78      |    4.04206  |       7.77778 |                  1.16667 |
| 42 | 2019-07-01 02:00:00 |                      17      |    73      |    4.11555  |       7.5     |                  1.33333 |
| 43 | 2019-07-01 03:00:00 |                      16      |    70      |    3.85833  |       7.22222 |                  1.41667 |
| 44 | 2019-07-01 04:00:00 |                      15      |    70.5    |    3.60111  |       6.66667 |                  1.5     |
| 45 | 2019-07-01 05:00:00 |                      14      |    71      |    3.08666  |       6.94444 |                  1.58333 |
| 46 | 2019-07-01 06:00:00 |                      13      |    59      |    2.57222  |       7.22222 |                  1.66667 |
| 47 | 2019-07-01 07:00:00 |                      20.8333 |    56      |    3.60111  |       8.88889 |                  1.77778 |
| 48 | 2019-07-01 08:00:00 |                      28.6667 |    49      |    3.85833  |      11.1111  |                  1.88889 |
| 49 | 2019-07-01 09:00:00 |                      36.5    |    45      |    4.11555  |      12.7778  |                  2       |
| 50 | 2019-07-01 10:00:00 |                      44.3333 |    47      |    4.37277  |      13.8889  |                  2.66667 |
| 51 | 2019-07-01 11:00:00 |                      52.1667 |    50      |    4.63     |      14.4444  |                  3.33333 |
| 52 | 2019-07-01 12:00:00 |                      60      |    51      |    4.88722  |      14.1667  |                  4       |
| 53 | 2019-07-01 13:00:00 |                      53.6667 |    54      |    5.14444  |      13.8889  |                  3.66667 |
| 54 | 2019-07-01 14:00:00 |                      47.3333 |    61      |    5.65888  |      13.3333  |                  3.33333 |
| 55 | 2019-07-01 15:00:00 |                      41      |    64      |    6.17333  |      13.6111  |                  3       |
| 56 | 2019-07-01 16:00:00 |                      34.6667 |    63.5    |    5.65888  |      13.8889  |                  2.66667 |
| 57 | 2019-07-01 17:00:00 |                      28.3333 |    63      |    5.14444  |      14.4444  |                  2.33333 |
| 58 | 2019-07-01 18:00:00 |                      22      |    62      |    4.11555  |      13.8889  |                  2       |
| 59 | 2019-07-01 19:00:00 |                      22      |    58      |    3.60111  |      12.7778  |                  1.66667 |
| 60 | 2019-07-01 20:00:00 |                      22      |    50      |    3.08666  |      11.1111  |                  1.33333 |
| 61 | 2019-07-01 21:00:00 |                      22      |    46      |    2.82944  |       9.44444 |                  1       |
| 62 | 2019-07-01 22:00:00 |                      22      |    45      |    2.57222  |       8.88889 |                  1       |
| 63 | 2019-07-01 23:00:00 |                      22      |    44      |    2.7437   |       8.33333 |                  1       |

## Maroon Lake

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      4       |    40      |     3.08666 |      12.2222  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      4       |    40      |     3.08666 |      12.2222  |                  1       |
|  2 | 2019-06-29 10:00:00 |                      5       |    54      |     2.05778 |      15       |                  1.16667 |
|  3 | 2019-06-29 11:00:00 |                      6       |    51      |     1.92917 |      17.2222  |                  1.33333 |
|  4 | 2019-06-29 12:00:00 |                      7       |    39      |     1.80055 |      18.8889  |                  1.66667 |
|  5 | 2019-06-29 13:00:00 |                     15       |    47      |     1.67194 |      20.5556  |                  2       |
|  6 | 2019-06-29 14:00:00 |                     24       |    56      |     1.54333 |      20       |                  3       |
|  7 | 2019-06-29 15:00:00 |                     33       |    66      |     2.05778 |      19.4444  |                  4       |
|  8 | 2019-06-29 16:00:00 |                     30       |    65      |     3.08666 |      18.8889  |                  3.33333 |
|  9 | 2019-06-29 17:00:00 |                     26       |    67      |     3.60111 |      18.3333  |                  2.66667 |
| 10 | 2019-06-29 18:00:00 |                     23       |    71      |     3.08666 |      17.2222  |                  2       |
| 11 | 2019-06-29 19:00:00 |                     20       |    67      |     3.18955 |      16.1111  |                  1.83333 |
| 12 | 2019-06-29 20:00:00 |                     18       |    51      |     3.29244 |      14.4444  |                  1.66667 |
| 13 | 2019-06-29 21:00:00 |                     15       |    64      |     3.39533 |      12.7778  |                  1.5     |
| 14 | 2019-06-29 22:00:00 |                     12       |    44      |     3.49822 |      12.2222  |                  1.33333 |
| 15 | 2019-06-29 23:00:00 |                     10       |    42      |     3.60111 |      11.6667  |                  1.16667 |
| 16 | 2019-06-30 00:00:00 |                      7       |    39      |     4.11555 |      11.1111  |                  1       |
| 17 | 2019-06-30 01:00:00 |                      7.28571 |    39.2857 |     4.63    |      10.5556  |                  1.33333 |
| 18 | 2019-06-30 02:00:00 |                      7.57143 |    39.5714 |     4.88722 |      10       |                  1.38095 |
| 19 | 2019-06-30 03:00:00 |                      7.85714 |    39.8571 |     5.14444 |       9.44444 |                  1.42857 |
| 20 | 2019-06-30 04:00:00 |                      8.14286 |    40.1429 |     4.63    |       8.88889 |                  1.47619 |
| 21 | 2019-06-30 05:00:00 |                      8.42857 |    40.4286 |     4.37277 |       9.25926 |                  1.52381 |
| 22 | 2019-06-30 06:00:00 |                      8.71429 |    40.7143 |     4.11555 |       9.62963 |                  1.57143 |
| 23 | 2019-06-30 07:00:00 |                      9       |    41      |     3.08666 |      10       |                  1.61905 |
| 24 | 2019-06-30 08:00:00 |                     10       |    42      |     2.57222 |      11.6667  |                  1.66667 |
| 25 | 2019-06-30 09:00:00 |                     12       |    44      |     2.05778 |      13.8889  |                  2       |
| 26 | 2019-06-30 10:00:00 |                     28       |    60      |     2.315   |      15.5556  |                  3       |
| 27 | 2019-06-30 11:00:00 |                     44       |    76      |     2.57222 |      17.2222  |                  3.5     |
| 28 | 2019-06-30 12:00:00 |                     60       |    92      |     3.08666 |      17.7778  |                  4       |
| 29 | 2019-06-30 13:00:00 |                     64       |    96      |     3.18955 |      17.5     |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                     69       |   100      |     3.29244 |      17.2222  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     73       |    97.3333 |     3.39533 |      16.1111  |                  5       |
| 32 | 2019-06-30 16:00:00 |                     69       |    94.6667 |     3.49822 |      15.5556  |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                     60       |    92      |     3.60111 |      15       |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                     56       |    90      |     4.11555 |      14.4444  |                  4       |
| 35 | 2019-06-30 19:00:00 |                     49.3333  |    89      |     3.98694 |      13.8889  |                  3.33333 |
| 36 | 2019-06-30 20:00:00 |                     42.6667  |    88      |     3.85833 |      12.7778  |                  2.66667 |
| 37 | 2019-06-30 21:00:00 |                     36       |    87      |     3.72972 |      12.2222  |                  2       |
| 38 | 2019-06-30 22:00:00 |                     29.3333  |    84      |     3.60111 |      11.6667  |                  1.66667 |
| 39 | 2019-06-30 23:00:00 |                     22.6667  |    79      |     3.08666 |      11.1111  |                  1.33333 |
| 40 | 2019-07-01 00:00:00 |                     16       |    76      |     3.02236 |      10.8333  |                  1       |
| 41 | 2019-07-01 01:00:00 |                     15.8333  |    74      |     2.95805 |      10.5556  |                  1.16667 |
| 42 | 2019-07-01 02:00:00 |                     15.6667  |    71      |     2.89375 |      10.2778  |                  1.33333 |
| 43 | 2019-07-01 03:00:00 |                     15.3333  |    69      |     2.82944 |      10       |                  1.41667 |
| 44 | 2019-07-01 04:00:00 |                     15.2222  |    68.5    |     2.76514 |       9.44444 |                  1.5     |
| 45 | 2019-07-01 05:00:00 |                     15.1111  |    68      |     2.70083 |       8.88889 |                  1.58333 |
| 46 | 2019-07-01 06:00:00 |                     15       |    71      |     2.63653 |       9.44444 |                  1.66667 |
| 47 | 2019-07-01 07:00:00 |                     24.1667  |    67      |     2.57222 |      10       |                  1.77778 |
| 48 | 2019-07-01 08:00:00 |                     33.3333  |    58      |     2.05778 |      11.6667  |                  1.88889 |
| 49 | 2019-07-01 09:00:00 |                     42.5     |    54      |     2.18639 |      13.3333  |                  2       |
| 50 | 2019-07-01 10:00:00 |                     51.6667  |    56      |     2.315   |      15       |                  3       |
| 51 | 2019-07-01 11:00:00 |                     60.8333  |    61      |     2.44361 |      16.1111  |                  4       |
| 52 | 2019-07-01 12:00:00 |                     70       |    63      |     2.57222 |      16.6667  |                  5       |
| 53 | 2019-07-01 13:00:00 |                     64.6667  |    64      |     3.08666 |      17.2222  |                  4.83333 |
| 54 | 2019-07-01 14:00:00 |                     59.3333  |    66      |     3.60111 |      17.037   |                  4.66667 |
| 55 | 2019-07-01 15:00:00 |                     54       |    67      |     3.42963 |      16.8519  |                  4.5     |
| 56 | 2019-07-01 16:00:00 |                     48.6667  |    68      |     3.25815 |      16.6667  |                  4.33333 |
| 57 | 2019-07-01 17:00:00 |                     43.3333  |    69      |     3.08666 |      16.1111  |                  4.16667 |
| 58 | 2019-07-01 18:00:00 |                     38       |    70      |     2.57222 |      15       |                  4       |
| 59 | 2019-07-01 19:00:00 |                     38       |    67      |     2.60248 |      13.8889  |                  3       |
| 60 | 2019-07-01 20:00:00 |                     38       |    62      |     2.63274 |      12.7778  |                  2       |
| 61 | 2019-07-01 21:00:00 |                     38       |    59      |     2.663   |      11.6667  |                  1       |
| 62 | 2019-07-01 22:00:00 |                     38       |    58      |     2.69327 |      11.1111  |                  1       |
| 63 | 2019-07-01 23:00:00 |                     38       |    55      |     2.72353 |      10.8333  |                  1       |

## Yankee Boy Basin

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                       8      |    26      |    1.02889  |      16.6667  |                  1       |
|  1 | 2019-06-29 09:00:00 |                       8      |    26      |    1.02889  |      16.6667  |                  1       |
|  2 | 2019-06-29 10:00:00 |                      11      |    26.5    |    0.514444 |      18.8889  |                  1.25    |
|  3 | 2019-06-29 11:00:00 |                      13      |    27      |    1.02889  |      20.5556  |                  1.5     |
|  4 | 2019-06-29 12:00:00 |                      16      |    57      |    1.54333  |      21.1111  |                  2       |
|  5 | 2019-06-29 13:00:00 |                      30      |    62      |    1.71481  |      20.9259  |                  4       |
|  6 | 2019-06-29 14:00:00 |                      44      |    76      |    1.88629  |      20.7407  |                  3.75    |
|  7 | 2019-06-29 15:00:00 |                      58      |    90      |    2.05778  |      20.5556  |                  3.5     |
|  8 | 2019-06-29 16:00:00 |                      53      |    85      |    3.08666  |      20       |                  3.25    |
|  9 | 2019-06-29 17:00:00 |                      47      |    79      |    3.60111  |      19.4444  |                  3       |
| 10 | 2019-06-29 18:00:00 |                      42      |    74      |    3.08666  |      18.3333  |                  2.75    |
| 11 | 2019-06-29 19:00:00 |                      38      |    70      |    3.25815  |      16.6667  |                  2.5     |
| 12 | 2019-06-29 20:00:00 |                      33      |    65      |    3.42963  |      14.4444  |                  2.25    |
| 13 | 2019-06-29 21:00:00 |                      29      |    61      |    3.60111  |      13.3333  |                  2       |
| 14 | 2019-06-29 22:00:00 |                      24      |    56      |    3.85833  |      12.2222  |                  1.66667 |
| 15 | 2019-06-29 23:00:00 |                      20      |    52      |    4.11555  |      11.6667  |                  1.33333 |
| 16 | 2019-06-30 00:00:00 |                      15      |    47      |    4.63     |      11.3889  |                  1       |
| 17 | 2019-06-30 01:00:00 |                      15.3333 |    47.3333 |    5.14444  |      11.1111  |                  1.33333 |
| 18 | 2019-06-30 02:00:00 |                      15.6667 |    47.6667 |    5.65888  |      10.8333  |                  1.38095 |
| 19 | 2019-06-30 03:00:00 |                      16      |    48      |    5.40166  |      10.5556  |                  1.42857 |
| 20 | 2019-06-30 04:00:00 |                      15.75   |    47.75   |    5.14444  |      10       |                  1.47619 |
| 21 | 2019-06-30 05:00:00 |                      15.5    |    47.5    |    4.63     |       9.44444 |                  1.52381 |
| 22 | 2019-06-30 06:00:00 |                      15.25   |    47.25   |    4.11555  |      10       |                  1.57143 |
| 23 | 2019-06-30 07:00:00 |                      15      |    47      |    3.60111  |      11.6667  |                  1.61905 |
| 24 | 2019-06-30 08:00:00 |                      14.5    |    46.5    |    2.57222  |      13.8889  |                  1.66667 |
| 25 | 2019-06-30 09:00:00 |                      14      |    46      |    2.05778  |      16.1111  |                  2       |
| 26 | 2019-06-30 10:00:00 |                      29      |    61      |    2.315    |      17.7778  |                  3.5     |
| 27 | 2019-06-30 11:00:00 |                      45      |    77      |    2.57222  |      18.3333  |                  4.25    |
| 28 | 2019-06-30 12:00:00 |                      60      |    98      |    3.08666  |      17.7778  |                  5       |
| 29 | 2019-06-30 13:00:00 |                      65      |    99      |    2.98378  |      17.2222  |                  4.83333 |
| 30 | 2019-06-30 14:00:00 |                      70      |   100      |    2.88089  |      16.6667  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                      75      |    99.3333 |    2.778    |      16.4444  |                  4.5     |
| 32 | 2019-06-30 16:00:00 |                      70      |    98.6667 |    2.67511  |      16.2222  |                  4.33333 |
| 33 | 2019-06-30 17:00:00 |                      61      |    98      |    2.57222  |      16       |                  4.16667 |
| 34 | 2019-06-30 18:00:00 |                      56      |    88      |    2.7437   |      15.7778  |                  4       |
| 35 | 2019-06-30 19:00:00 |                      50      |    86.3333 |    2.91518  |      15.5556  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                      44      |    84.6667 |    3.08666  |      13.8889  |                  3       |
| 37 | 2019-06-30 21:00:00 |                      38      |    83      |    3.60111  |      12.2222  |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                      32      |    82.5    |    3.6746   |      11.6667  |                  2       |
| 39 | 2019-06-30 23:00:00 |                      26      |    82      |    3.74809  |      11.1111  |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      20      |    81.5    |    3.82158  |      10.5556  |                  1       |
| 41 | 2019-07-01 01:00:00 |                      19.5    |    81      |    3.89508  |      10       |                  1.16667 |
| 42 | 2019-07-01 02:00:00 |                      19      |    77      |    3.96857  |       9.72222 |                  1.33333 |
| 43 | 2019-07-01 03:00:00 |                      18      |    75      |    4.04206  |       9.44444 |                  1.41667 |
| 44 | 2019-07-01 04:00:00 |                      17.3333 |    74      |    4.11555  |       8.88889 |                  1.5     |
| 45 | 2019-07-01 05:00:00 |                      16.6667 |    72      |    3.98694  |       8.33333 |                  1.58333 |
| 46 | 2019-07-01 06:00:00 |                      16      |    58      |    3.85833  |       8.88889 |                  1.66667 |
| 47 | 2019-07-01 07:00:00 |                      25.6667 |    55      |    3.72972  |      11.1111  |                  1.77778 |
| 48 | 2019-07-01 08:00:00 |                      35.3333 |    50      |    3.60111  |      13.3333  |                  1.88889 |
| 49 | 2019-07-01 09:00:00 |                      45      |    47      |    3.704    |      15.5556  |                  2       |
| 50 | 2019-07-01 10:00:00 |                      54.6667 |    50      |    3.80689  |      16.6667  |                  3       |
| 51 | 2019-07-01 11:00:00 |                      64.3333 |    55      |    3.90977  |      17.7778  |                  4       |
| 52 | 2019-07-01 12:00:00 |                      74      |    57      |    4.01266  |      17.8889  |                  5       |
| 53 | 2019-07-01 13:00:00 |                      65.6667 |    60      |    4.11555  |      18       |                  4.66667 |
| 54 | 2019-07-01 14:00:00 |                      57.3333 |    65      |    4.63     |      18.1111  |                  4.33333 |
| 55 | 2019-07-01 15:00:00 |                      49      |    67      |    4.45851  |      18.2222  |                  4       |
| 56 | 2019-07-01 16:00:00 |                      40.6667 |    66.25   |    4.28703  |      18.3333  |                  3.33333 |
| 57 | 2019-07-01 17:00:00 |                      32.3333 |    65.5    |    4.11555  |      18.0556  |                  2.66667 |
| 58 | 2019-07-01 18:00:00 |                      24      |    64.75   |    3.60111  |      17.7778  |                  2       |
| 59 | 2019-07-01 19:00:00 |                      24      |    64      |    3.08666  |      15.5556  |                  1.66667 |
| 60 | 2019-07-01 20:00:00 |                      24      |    57      |    3.18955  |      13.8889  |                  1.33333 |
| 61 | 2019-07-01 21:00:00 |                      24      |    54      |    3.29244  |      11.6667  |                  1       |
| 62 | 2019-07-01 22:00:00 |                      24      |    52      |    3.39533  |      10.5556  |                  1       |
| 63 | 2019-07-01 23:00:00 |                      24      |    49      |    3.49822  |      10       |                  1       |

## Capitol Creek

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      2       |    22      |    1.54333  |       16.6667 |                  1       |
|  1 | 2019-06-29 09:00:00 |                      2       |    22      |    1.54333  |       16.6667 |                  1       |
|  2 | 2019-06-29 10:00:00 |                      2.5     |    44      |    1.02889  |       19.4444 |                  1.125   |
|  3 | 2019-06-29 11:00:00 |                      3       |    46      |    0.514444 |       21.6667 |                  1.25    |
|  4 | 2019-06-29 12:00:00 |                      6.5     |    36      |    1.02889  |       24.4444 |                  1.5     |
|  5 | 2019-06-29 13:00:00 |                     10       |    42      |    1.54333  |       25.5556 |                  1.75    |
|  6 | 2019-06-29 14:00:00 |                     22       |    54      |    2.05778  |       26.1111 |                  2       |
|  7 | 2019-06-29 15:00:00 |                     25       |    57      |    2.57222  |       25.5556 |                  4       |
|  8 | 2019-06-29 16:00:00 |                     22       |    62      |    3.60111  |       25.2778 |                  2       |
|  9 | 2019-06-29 17:00:00 |                     20       |    87      |    4.63     |       25      |                  1.83333 |
| 10 | 2019-06-29 18:00:00 |                     17       |    82      |    2.57222  |       23.3333 |                  1.66667 |
| 11 | 2019-06-29 19:00:00 |                     15       |    54      |    2.52545  |       21.6667 |                  1.5     |
| 12 | 2019-06-29 20:00:00 |                     13       |    59      |    2.47868  |       20.5556 |                  1.33333 |
| 13 | 2019-06-29 21:00:00 |                     11       |    50      |    2.43192  |       18.3333 |                  1.16667 |
| 14 | 2019-06-29 22:00:00 |                      9       |    42      |    2.38515  |       16.1111 |                  1       |
| 15 | 2019-06-29 23:00:00 |                      7       |    39      |    2.33838  |       15      |                  1.16667 |
| 16 | 2019-06-30 00:00:00 |                      5       |    37      |    2.29161  |       14.4444 |                  1.33333 |
| 17 | 2019-06-30 01:00:00 |                      5.14286 |    37.1429 |    2.24485  |       13.3333 |                  1.5     |
| 18 | 2019-06-30 02:00:00 |                      5.28571 |    37.2857 |    2.19808  |       12.7778 |                  1.52381 |
| 19 | 2019-06-30 03:00:00 |                      5.42857 |    37.4286 |    2.15131  |       12.2222 |                  1.54762 |
| 20 | 2019-06-30 04:00:00 |                      5.57143 |    37.5714 |    2.10454  |       11.1111 |                  1.57143 |
| 21 | 2019-06-30 05:00:00 |                      5.71429 |    37.7143 |    2.05778  |       11.6667 |                  1.59524 |
| 22 | 2019-06-30 06:00:00 |                      5.85714 |    37.8571 |    1.54333  |       12.2222 |                  1.61905 |
| 23 | 2019-06-30 07:00:00 |                      6       |    38      |    1.28611  |       12.7778 |                  1.64286 |
| 24 | 2019-06-30 08:00:00 |                      7       |    39      |    1.02889  |       15.5556 |                  1.66667 |
| 25 | 2019-06-30 09:00:00 |                      8       |    40      |    1.28611  |       18.3333 |                  1.83333 |
| 26 | 2019-06-30 10:00:00 |                     20       |    52      |    1.54333  |       20.5556 |                  2       |
| 27 | 2019-06-30 11:00:00 |                     33       |    65      |    2.05778  |       22.7778 |                  3       |
| 28 | 2019-06-30 12:00:00 |                     45       |    81      |    2.57222  |       23.8889 |                  4       |
| 29 | 2019-06-30 13:00:00 |                     48       |    81.5    |    2.62938  |       24.4444 |                  3.71429 |
| 30 | 2019-06-30 14:00:00 |                     50       |    82      |    2.68654  |       23.8889 |                  3.42857 |
| 31 | 2019-06-30 15:00:00 |                     53       |    85      |    2.7437   |       22.7778 |                  3.14286 |
| 32 | 2019-06-30 16:00:00 |                     52       |    84      |    2.80086  |       22.2222 |                  2.85714 |
| 33 | 2019-06-30 17:00:00 |                     51       |    86      |    2.85802  |       21.1111 |                  2.57143 |
| 34 | 2019-06-30 18:00:00 |                     50       |    90      |    2.91518  |       20.5556 |                  2.28571 |
| 35 | 2019-06-30 19:00:00 |                     44.6667  |    89      |    2.97234  |       18.8889 |                  2.19048 |
| 36 | 2019-06-30 20:00:00 |                     39.3333  |    87      |    3.0295   |       17.7778 |                  2.09524 |
| 37 | 2019-06-30 21:00:00 |                     34       |    86      |    3.08666  |       16.1111 |                  2       |
| 38 | 2019-06-30 22:00:00 |                     28.3333  |    83      |    2.57222  |       14.4444 |                  1.66667 |
| 39 | 2019-06-30 23:00:00 |                     22.6667  |    76      |    2.40074  |       13.3333 |                  1.33333 |
| 40 | 2019-07-01 00:00:00 |                     17       |    72      |    2.22926  |       12.2222 |                  1       |
| 41 | 2019-07-01 01:00:00 |                     16.5     |    70      |    2.05778  |       11.6667 |                  1.16667 |
| 42 | 2019-07-01 02:00:00 |                     16       |    67      |    1.80055  |       11.1111 |                  1.33333 |
| 43 | 2019-07-01 03:00:00 |                     15       |    65      |    1.54333  |       10.5556 |                  1.41667 |
| 44 | 2019-07-01 04:00:00 |                     14.3333  |    67      |    1.41472  |       10      |                  1.5     |
| 45 | 2019-07-01 05:00:00 |                     13.6667  |    69      |    1.28611  |       10.7407 |                  1.58333 |
| 46 | 2019-07-01 06:00:00 |                     13       |    71      |    1.1575   |       11.4815 |                  1.66667 |
| 47 | 2019-07-01 07:00:00 |                     20.8333  |    66      |    1.02889  |       12.2222 |                  1.77778 |
| 48 | 2019-07-01 08:00:00 |                     28.6667  |    56      |    1.20037  |       14.4444 |                  1.88889 |
| 49 | 2019-07-01 09:00:00 |                     36.5     |    51      |    1.37185  |       17.7778 |                  2       |
| 50 | 2019-07-01 10:00:00 |                     44.3333  |    54      |    1.54333  |       20.5556 |                  2.66667 |
| 51 | 2019-07-01 11:00:00 |                     52.1667  |    59      |    2.05778  |       22.2222 |                  3.33333 |
| 52 | 2019-07-01 12:00:00 |                     60       |    62      |    2.57222  |       23.8889 |                  4       |
| 53 | 2019-07-01 13:00:00 |                     55       |    64      |    3.08666  |       24.4444 |                  4.33333 |
| 54 | 2019-07-01 14:00:00 |                     50       |    69      |    2.95805  |       24.1667 |                  4.66667 |
| 55 | 2019-07-01 15:00:00 |                     45       |    71      |    2.82944  |       23.8889 |                  5       |
| 56 | 2019-07-01 16:00:00 |                     40       |    70.5    |    2.70083  |       23.3333 |                  4.66667 |
| 57 | 2019-07-01 17:00:00 |                     35       |    70      |    2.57222  |       22.7778 |                  4.33333 |
| 58 | 2019-07-01 18:00:00 |                     30       |    69      |    2.50791  |       21.6667 |                  4       |
| 59 | 2019-07-01 19:00:00 |                     30       |    66      |    2.44361  |       20      |                  3       |
| 60 | 2019-07-01 20:00:00 |                     30       |    60      |    2.3793   |       17.7778 |                  2       |
| 61 | 2019-07-01 21:00:00 |                     30       |    57      |    2.315    |       16.1111 |                  1       |
| 62 | 2019-07-01 22:00:00 |                     30       |    55      |    2.25069  |       14.4444 |                  1       |
| 63 | 2019-07-01 23:00:00 |                     30       |    52      |    2.18639  |       13.3333 |                  1       |

## Crags Campground

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      0       |    15      |     2.57222 |       16.1111 |                  1       |
|  1 | 2019-06-29 09:00:00 |                      1       |    12      |     3.08666 |       17.7778 |                  1.75    |
|  2 | 2019-06-29 10:00:00 |                      2       |    25      |     3.60111 |       19.4444 |                  2.125   |
|  3 | 2019-06-29 11:00:00 |                      3       |    38      |     3.42963 |       22.2222 |                  2.5     |
|  4 | 2019-06-29 12:00:00 |                      5       |    51      |     3.25815 |       21.6667 |                  3.25    |
|  5 | 2019-06-29 13:00:00 |                     26       |    54      |     3.08666 |       22.7778 |                  4       |
|  6 | 2019-06-29 14:00:00 |                     46       |    57      |     2.05778 |       23.8889 |                  4.5     |
|  7 | 2019-06-29 15:00:00 |                     67       |    67      |     1.54333 |       23.3333 |                  5       |
|  8 | 2019-06-29 16:00:00 |                     57       |    70      |     2.57222 |       22.2222 |                  4.5     |
|  9 | 2019-06-29 17:00:00 |                     47       |    79      |     3.60111 |       20.5556 |                  4       |
| 10 | 2019-06-29 18:00:00 |                     38       |    88      |     4.11555 |       17.2222 |                  3.8     |
| 11 | 2019-06-29 19:00:00 |                     35       |    87      |     3.60111 |       16.1111 |                  3.6     |
| 12 | 2019-06-29 20:00:00 |                     32       |    86.5    |     3.08666 |       15.5556 |                  3.4     |
| 13 | 2019-06-29 21:00:00 |                     30       |    86      |     2.57222 |       15      |                  3.2     |
| 14 | 2019-06-29 22:00:00 |                     23       |    74      |     2.05778 |       14.8148 |                  3       |
| 15 | 2019-06-29 23:00:00 |                     15       |    62      |     2.18639 |       14.6296 |                  2       |
| 16 | 2019-06-30 00:00:00 |                      8       |    50      |     2.315   |       14.4444 |                  1       |
| 17 | 2019-06-30 01:00:00 |                      6       |    45      |     2.44361 |       13.8889 |                  1.6     |
| 18 | 2019-06-30 02:00:00 |                      3       |    40      |     2.57222 |       12.7778 |                  1.68571 |
| 19 | 2019-06-30 03:00:00 |                      1       |    35      |     2.82944 |       12.2222 |                  1.77143 |
| 20 | 2019-06-30 04:00:00 |                      2       |    32      |     3.08666 |       11.6667 |                  1.85714 |
| 21 | 2019-06-30 05:00:00 |                      3       |    28      |     2.57222 |       11.9444 |                  1.94286 |
| 22 | 2019-06-30 06:00:00 |                      4       |    24      |     2.46933 |       12.2222 |                  2.02857 |
| 23 | 2019-06-30 07:00:00 |                      5.33333 |    22      |     2.36644 |       13.8889 |                  2.11429 |
| 24 | 2019-06-30 08:00:00 |                      6.66667 |    21      |     2.26355 |       15.5556 |                  2.2     |
| 25 | 2019-06-30 09:00:00 |                      8       |    20      |     2.16066 |       17.7778 |                  2.8     |
| 26 | 2019-06-30 10:00:00 |                     24.6667  |    32      |     2.05778 |       20      |                  3.4     |
| 27 | 2019-06-30 11:00:00 |                     41.3333  |    44      |     1.54333 |       21.6667 |                  3.7     |
| 28 | 2019-06-30 12:00:00 |                     58       |    58      |     1.80055 |       22.2222 |                  4       |
| 29 | 2019-06-30 13:00:00 |                     63.3333  |    63.6667 |     2.05778 |       21.6667 |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                     68.6667  |    69.3333 |     3.08666 |       20.5556 |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     74       |    75      |     3.60111 |       18.8889 |                  5       |
| 32 | 2019-06-30 16:00:00 |                     69.3333  |    75.6667 |     4.63    |       17.2222 |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                     64.6667  |    76.3333 |     5.14444 |       16.1111 |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                     60       |    77      |     1.02889 |       15      |                  4       |
| 35 | 2019-06-30 19:00:00 |                     51.6667  |    81      |     2.05778 |       18.3333 |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     43.3333  |    84      |     3.08666 |       17.2222 |                  3       |
| 37 | 2019-06-30 21:00:00 |                     35       |    87      |     3.60111 |       14.4444 |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     26.3333  |    84      |     3.42963 |       13.3333 |                  2       |
| 39 | 2019-06-30 23:00:00 |                     17.6667  |    81      |     3.25815 |       12.7778 |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      9       |    78      |     3.08666 |       12.2222 |                  1       |
| 41 | 2019-07-01 01:00:00 |                     12       |    75      |     3.03522 |       11.9444 |                  1.75    |
| 42 | 2019-07-01 02:00:00 |                     15       |    73      |     2.98378 |       11.6667 |                  2.5     |
| 43 | 2019-07-01 03:00:00 |                     21       |    70      |     2.93233 |       10.5556 |                  2.875   |
| 44 | 2019-07-01 04:00:00 |                     23       |    65      |     2.88089 |       10.8333 |                  3.25    |
| 45 | 2019-07-01 05:00:00 |                     25       |    61      |     2.82944 |       11.1111 |                  3.625   |
| 46 | 2019-07-01 06:00:00 |                     27       |    56      |     2.778   |       10.5556 |                  4       |
| 47 | 2019-07-01 07:00:00 |                     38.3333  |    54      |     2.72655 |       11.6667 |                  4       |
| 48 | 2019-07-01 08:00:00 |                     49.6667  |    52      |     2.67511 |       12.7778 |                  4       |
| 49 | 2019-07-01 09:00:00 |                     61       |    50      |     2.62366 |       14.4444 |                  4       |
| 50 | 2019-07-01 10:00:00 |                     72.3333  |    53      |     2.57222 |       15.5556 |                  4       |
| 51 | 2019-07-01 11:00:00 |                     83.6667  |    56      |     2.05778 |       16.6667 |                  4       |
| 52 | 2019-07-01 12:00:00 |                     95       |    59      |     2.22926 |       17.7778 |                  4       |
| 53 | 2019-07-01 13:00:00 |                     90.5     |    63      |     2.40074 |       18.0556 |                  4       |
| 54 | 2019-07-01 14:00:00 |                     86       |    66      |     2.57222 |       18.3333 |                  4       |
| 55 | 2019-07-01 15:00:00 |                     81.5     |    70      |     2.40074 |       18.6111 |                  4       |
| 56 | 2019-07-01 16:00:00 |                     77       |    76      |     2.22926 |       18.8889 |                  4       |
| 57 | 2019-07-01 17:00:00 |                     72.5     |    82      |     2.05778 |       17.7778 |                  4       |
| 58 | 2019-07-01 18:00:00 |                     68       |    88      |     1.54333 |       16.6667 |                  4       |
| 59 | 2019-07-01 19:00:00 |                     68       |    88.5    |     2.05778 |       15.8333 |                  4       |
| 60 | 2019-07-01 20:00:00 |                     68       |    89      |     2.315   |       15      |                  4       |
| 61 | 2019-07-01 21:00:00 |                     68       |    87.5    |     2.57222 |       13.3333 |                  4       |
| 62 | 2019-07-01 22:00:00 |                     68       |    86      |     2.315   |       12.2222 |                  4       |
| 63 | 2019-07-01 23:00:00 |                     68       |    82      |     2.05778 |       11.9444 |                  4       |

## Snowmass Creek

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      2       |    36      |     1.54333 |       17.2222 |                  1       |
|  1 | 2019-06-29 09:00:00 |                      2       |    36      |     1.54333 |       17.2222 |                  1       |
|  2 | 2019-06-29 10:00:00 |                      3       |    52      |     1.02889 |       19.4444 |                  1.125   |
|  3 | 2019-06-29 11:00:00 |                      3.5     |    46      |     1.20037 |       22.2222 |                  1.25    |
|  4 | 2019-06-29 12:00:00 |                      4       |    39      |     1.37185 |       23.8889 |                  1.5     |
|  5 | 2019-06-29 13:00:00 |                     11       |    44      |     1.54333 |       25.5556 |                  1.75    |
|  6 | 2019-06-29 14:00:00 |                     21       |    53      |     1.02889 |       25.3333 |                  2       |
|  7 | 2019-06-29 15:00:00 |                     26       |    66      |     2.57222 |       25.1111 |                  4       |
|  8 | 2019-06-29 16:00:00 |                     23       |    72      |     3.60111 |       24.8889 |                  2       |
|  9 | 2019-06-29 17:00:00 |                     20       |    85      |     5.14444 |       24.6667 |                  1.83333 |
| 10 | 2019-06-29 18:00:00 |                     17       |    83      |     2.57222 |       24.4444 |                  1.66667 |
| 11 | 2019-06-29 19:00:00 |                     15       |    60      |     2.315   |       22.7778 |                  1.5     |
| 12 | 2019-06-29 20:00:00 |                     13       |    49      |     2.05778 |       21.1111 |                  1.33333 |
| 13 | 2019-06-29 21:00:00 |                     11       |    43      |     2.57222 |       18.8889 |                  1.16667 |
| 14 | 2019-06-29 22:00:00 |                      8       |    40.5    |     2.82944 |       16.6667 |                  1       |
| 15 | 2019-06-29 23:00:00 |                      6       |    38      |     3.08666 |       15.5556 |                  1.16667 |
| 16 | 2019-06-30 00:00:00 |                      4       |    30      |     2.95805 |       14.4444 |                  1.33333 |
| 17 | 2019-06-30 01:00:00 |                      4.5     |    33.5    |     2.82944 |       13.8889 |                  1.5     |
| 18 | 2019-06-30 02:00:00 |                      5       |    37      |     2.70083 |       13.3333 |                  1.52381 |
| 19 | 2019-06-30 03:00:00 |                      5.33333 |    37.3333 |     2.57222 |       12.2222 |                  1.54762 |
| 20 | 2019-06-30 04:00:00 |                      5.66667 |    37.6667 |     2.315   |       11.6667 |                  1.57143 |
| 21 | 2019-06-30 05:00:00 |                      6       |    38      |     2.05778 |       11.1111 |                  1.59524 |
| 22 | 2019-06-30 06:00:00 |                      6.5     |    38.5    |     1.80055 |       11.9444 |                  1.61905 |
| 23 | 2019-06-30 07:00:00 |                      7       |    39      |     1.54333 |       12.7778 |                  1.64286 |
| 24 | 2019-06-30 08:00:00 |                      7.5     |    39.5    |     1.28611 |       15.5556 |                  1.66667 |
| 25 | 2019-06-30 09:00:00 |                      8       |    40      |     1.02889 |       18.3333 |                  1.83333 |
| 26 | 2019-06-30 10:00:00 |                     21       |    53      |     1.54333 |       20.5556 |                  2       |
| 27 | 2019-06-30 11:00:00 |                     34       |    66      |     2.05778 |       22.7778 |                  3       |
| 28 | 2019-06-30 12:00:00 |                     47       |    81      |     2.57222 |       23.8889 |                  4       |
| 29 | 2019-06-30 13:00:00 |                     50       |    82      |     2.53265 |       23.3333 |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                     54       |    86      |     2.49307 |       22.7778 |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     57       |    89      |     2.4535  |       21.6667 |                  5       |
| 32 | 2019-06-30 16:00:00 |                     54       |    87      |     2.41393 |       21.1111 |                  4       |
| 33 | 2019-06-30 17:00:00 |                     47       |    88      |     2.37436 |       20.5556 |                  3.33333 |
| 34 | 2019-06-30 18:00:00 |                     43       |    89      |     2.33478 |       20      |                  2.66667 |
| 35 | 2019-06-30 19:00:00 |                     38.3333  |    88      |     2.29521 |       18.8889 |                  2.44444 |
| 36 | 2019-06-30 20:00:00 |                     33.6667  |    87      |     2.25564 |       17.2222 |                  2.22222 |
| 37 | 2019-06-30 21:00:00 |                     29       |    86      |     2.21607 |       16.1111 |                  2       |
| 38 | 2019-06-30 22:00:00 |                     24.3333  |    83      |     2.17649 |       15      |                  1.66667 |
| 39 | 2019-06-30 23:00:00 |                     19.6667  |    78      |     2.13692 |       13.8889 |                  1.33333 |
| 40 | 2019-07-01 00:00:00 |                     15       |    75      |     2.09735 |       13.3333 |                  1       |
| 41 | 2019-07-01 01:00:00 |                     14.75    |    73      |     2.05778 |       12.7778 |                  1.16667 |
| 42 | 2019-07-01 02:00:00 |                     14.5     |    68      |     1.80055 |       12.2222 |                  1.33333 |
| 43 | 2019-07-01 03:00:00 |                     14       |    65      |     1.54333 |       11.1111 |                  1.41667 |
| 44 | 2019-07-01 04:00:00 |                     13.6667  |    67      |     1.41472 |       10.5556 |                  1.5     |
| 45 | 2019-07-01 05:00:00 |                     13.3333  |    69      |     1.28611 |       10      |                  1.58333 |
| 46 | 2019-07-01 06:00:00 |                     13       |    71      |     1.1575  |       10.5556 |                  1.66667 |
| 47 | 2019-07-01 07:00:00 |                     20.5     |    67      |     1.02889 |       12.2222 |                  1.77778 |
| 48 | 2019-07-01 08:00:00 |                     28       |    58      |     1.20037 |       15      |                  1.88889 |
| 49 | 2019-07-01 09:00:00 |                     35.5     |    53      |     1.37185 |       18.3333 |                  2       |
| 50 | 2019-07-01 10:00:00 |                     43       |    56      |     1.54333 |       21.1111 |                  2.66667 |
| 51 | 2019-07-01 11:00:00 |                     50.5     |    61      |     2.05778 |       23.3333 |                  3.33333 |
| 52 | 2019-07-01 12:00:00 |                     58       |    63      |     2.57222 |       24.4444 |                  4       |
| 53 | 2019-07-01 13:00:00 |                     52.6667  |    65      |     3.08666 |       24.1667 |                  4.33333 |
| 54 | 2019-07-01 14:00:00 |                     47.3333  |    68      |     2.95805 |       23.8889 |                  4.66667 |
| 55 | 2019-07-01 15:00:00 |                     42       |    70      |     2.82944 |       23.3333 |                  5       |
| 56 | 2019-07-01 16:00:00 |                     36.6667  |    70.5    |     2.70083 |       22.963  |                  4.66667 |
| 57 | 2019-07-01 17:00:00 |                     31.3333  |    71      |     2.57222 |       22.5926 |                  4.33333 |
| 58 | 2019-07-01 18:00:00 |                     26       |    69.5    |     2.40074 |       22.2222 |                  4       |
| 59 | 2019-07-01 19:00:00 |                     26       |    68      |     2.22926 |       20.5556 |                  3       |
| 60 | 2019-07-01 20:00:00 |                     26       |    63      |     2.05778 |       18.3333 |                  2       |
| 61 | 2019-07-01 21:00:00 |                     26       |    60      |     2.00062 |       16.1111 |                  1       |
| 62 | 2019-07-01 22:00:00 |                     26       |    58      |     1.94346 |       15      |                  1       |
| 63 | 2019-07-01 23:00:00 |                     26       |    55      |     1.88629 |       13.8889 |                  1       |

## Needleton

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                       5      |    20      |     1.02889 |      10.5556  |                  1       |
|  1 | 2019-06-29 09:00:00 |                       5      |    20      |     1.02889 |      10.5556  |                  1       |
|  2 | 2019-06-29 10:00:00 |                       7      |    15      |     1.54333 |      12.2222  |                  1.16667 |
|  3 | 2019-06-29 11:00:00 |                       8      |    28      |     2.05778 |      12.7778  |                  1.33333 |
|  4 | 2019-06-29 12:00:00 |                       9      |    41      |     2.57222 |      14.4444  |                  1.66667 |
|  5 | 2019-06-29 13:00:00 |                      23      |    55      |     2.05778 |      14.7222  |                  2       |
|  6 | 2019-06-29 14:00:00 |                      38      |    70      |     3.60111 |      15       |                  4       |
|  7 | 2019-06-29 15:00:00 |                      51      |    83      |     4.11555 |      15.5556  |                  3.71429 |
|  8 | 2019-06-29 16:00:00 |                      50.5    |    82.5    |     4.63    |      15.8333  |                  3.42857 |
|  9 | 2019-06-29 17:00:00 |                      50      |    82      |     5.14444 |      16.1111  |                  3.14286 |
| 10 | 2019-06-29 18:00:00 |                      47.5    |    79.5    |     5.65888 |      15       |                  2.85714 |
| 11 | 2019-06-29 19:00:00 |                      45      |    77      |     5.4874  |      12.7778  |                  2.57143 |
| 12 | 2019-06-29 20:00:00 |                      39      |    71      |     5.31592 |      10.5556  |                  2.28571 |
| 13 | 2019-06-29 21:00:00 |                      34      |    66      |     5.14444 |       8.33333 |                  2       |
| 14 | 2019-06-29 22:00:00 |                      28      |    60      |     5.08728 |       7.22222 |                  1.66667 |
| 15 | 2019-06-29 23:00:00 |                      23      |    55      |     5.03012 |       6.66667 |                  1.33333 |
| 16 | 2019-06-30 00:00:00 |                      17      |    49      |     4.97296 |       6.94444 |                  1       |
| 17 | 2019-06-30 01:00:00 |                      16      |    48      |     4.9158  |       7.22222 |                  1.33333 |
| 18 | 2019-06-30 02:00:00 |                      14      |    46      |     4.85864 |       7.03704 |                  1.38095 |
| 19 | 2019-06-30 03:00:00 |                      13      |    45      |     4.80148 |       6.85185 |                  1.42857 |
| 20 | 2019-06-30 04:00:00 |                      11      |    43      |     4.74432 |       6.66667 |                  1.47619 |
| 21 | 2019-06-30 05:00:00 |                      10      |    42      |     4.68716 |       5.55556 |                  1.52381 |
| 22 | 2019-06-30 06:00:00 |                       8      |    43      |     4.63    |       6.11111 |                  1.57143 |
| 23 | 2019-06-30 07:00:00 |                      11      |    44      |     4.75861 |       7.77778 |                  1.61905 |
| 24 | 2019-06-30 08:00:00 |                      13      |    45      |     4.88722 |      10       |                  1.66667 |
| 25 | 2019-06-30 09:00:00 |                      16      |    48      |     5.01583 |      12.2222  |                  2       |
| 26 | 2019-06-30 10:00:00 |                      33      |    65      |     5.14444 |      13.3333  |                  3.5     |
| 27 | 2019-06-30 11:00:00 |                      49      |    81      |     5.40166 |      14.4444  |                  4.25    |
| 28 | 2019-06-30 12:00:00 |                      66      |    98      |     5.65888 |      14.1667  |                  5       |
| 29 | 2019-06-30 13:00:00 |                      69      |   100      |     6.17333 |      13.8889  |                  4.83333 |
| 30 | 2019-06-30 14:00:00 |                      72      |    99.25   |     6.43055 |      13.6111  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                      75      |    98.5    |     6.68777 |      13.3333  |                  4.5     |
| 32 | 2019-06-30 16:00:00 |                      71      |    97.75   |     6.17333 |      13.0556  |                  4.33333 |
| 33 | 2019-06-30 17:00:00 |                      62      |    97      |     5.65888 |      12.7778  |                  4.16667 |
| 34 | 2019-06-30 18:00:00 |                      57      |    89      |     5.14444 |      12.2222  |                  4       |
| 35 | 2019-06-30 19:00:00 |                      50.6667 |    85.3333 |     4.63    |      10.5556  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                      44.3333 |    81.6667 |     4.37277 |       8.88889 |                  3       |
| 37 | 2019-06-30 21:00:00 |                      38      |    78      |     4.11555 |       7.22222 |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                      31.6667 |    81      |     4.28703 |       6.11111 |                  2       |
| 39 | 2019-06-30 23:00:00 |                      25.3333 |    84      |     4.45851 |       5.55556 |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      19      |    87      |     4.63    |       5.83333 |                  1       |
| 41 | 2019-07-01 01:00:00 |                      18.75   |    84      |     4.88722 |       6.11111 |                  1.16667 |
| 42 | 2019-07-01 02:00:00 |                      18.5    |    79      |     5.14444 |       6.66667 |                  1.33333 |
| 43 | 2019-07-01 03:00:00 |                      18      |    76      |     5.40166 |       6.38889 |                  1.41667 |
| 44 | 2019-07-01 04:00:00 |                      17.3333 |    75      |     5.65888 |       6.11111 |                  1.5     |
| 45 | 2019-07-01 05:00:00 |                      16.6667 |    73      |     5.14444 |       5.55556 |                  1.58333 |
| 46 | 2019-07-01 06:00:00 |                      16      |    59      |     5.65888 |       6.38889 |                  1.66667 |
| 47 | 2019-07-01 07:00:00 |                      25.6667 |    55      |     6.17333 |       7.22222 |                  1.77778 |
| 48 | 2019-07-01 08:00:00 |                      35.3333 |    46      |     6.68777 |       9.44444 |                  1.88889 |
| 49 | 2019-07-01 09:00:00 |                      45      |    42      |     6.51629 |      11.6667  |                  2       |
| 50 | 2019-07-01 10:00:00 |                      54.6667 |    45      |     6.34481 |      12.7778  |                  3       |
| 51 | 2019-07-01 11:00:00 |                      64.3333 |    52      |     6.17333 |      13.3333  |                  4       |
| 52 | 2019-07-01 12:00:00 |                      74      |    55      |     6.43055 |      13.8889  |                  5       |
| 53 | 2019-07-01 13:00:00 |                      66.3333 |    58      |     6.68777 |      13.75    |                  4.66667 |
| 54 | 2019-07-01 14:00:00 |                      58.6667 |    65      |     7.71666 |      13.6111  |                  4.33333 |
| 55 | 2019-07-01 15:00:00 |                      51      |    68      |     8.2311  |      13.4722  |                  4       |
| 56 | 2019-07-01 16:00:00 |                      43.3333 |    69      |     7.71666 |      13.3333  |                  3.66667 |
| 57 | 2019-07-01 17:00:00 |                      35.6667 |    70      |     7.20222 |      12.7778  |                  3.33333 |
| 58 | 2019-07-01 18:00:00 |                      28      |    67.5    |     6.17333 |      12.2222  |                  3       |
| 59 | 2019-07-01 19:00:00 |                      28      |    65      |     5.65888 |      10.5556  |                  2.66667 |
| 60 | 2019-07-01 20:00:00 |                      28      |    56      |     5.40166 |       8.33333 |                  2.33333 |
| 61 | 2019-07-01 21:00:00 |                      28      |    51      |     5.14444 |       6.66667 |                  2       |
| 62 | 2019-07-01 22:00:00 |                      28      |    52      |     4.63    |       5.55556 |                  2       |
| 63 | 2019-07-01 23:00:00 |                      28      |    53      |     4.11555 |       5.74074 |                  2       |

## American Basin

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      12      |    31      |     2.05778 |       8.88889 |                  1       |
|  1 | 2019-06-29 09:00:00 |                      12      |    31      |     2.05778 |       8.88889 |                  1       |
|  2 | 2019-06-29 10:00:00 |                      16      |    32      |     1.02889 |      10       |                  1.25    |
|  3 | 2019-06-29 11:00:00 |                      19      |    33      |     1.54333 |      10.5556  |                  1.5     |
|  4 | 2019-06-29 12:00:00 |                      23      |    55      |     1.80055 |      11.6667  |                  2       |
|  5 | 2019-06-29 13:00:00 |                      40      |    72      |     2.05778 |      10.5556  |                  4       |
|  6 | 2019-06-29 14:00:00 |                      58      |    90      |     1.02889 |      10.4444  |                  3.75    |
|  7 | 2019-06-29 15:00:00 |                      74      |   100      |     2.05778 |      10.3333  |                  3.5     |
|  8 | 2019-06-29 16:00:00 |                      68      |    97      |     3.08666 |      10.2222  |                  3.25    |
|  9 | 2019-06-29 17:00:00 |                      62      |    94      |     4.11555 |      10.1111  |                  3       |
| 10 | 2019-06-29 18:00:00 |                      56      |    88      |     3.85833 |      10       |                  2.75    |
| 11 | 2019-06-29 19:00:00 |                      51      |    83      |     3.60111 |       8.88889 |                  2.5     |
| 12 | 2019-06-29 20:00:00 |                      45      |    77      |     3.72972 |       7.22222 |                  2.25    |
| 13 | 2019-06-29 21:00:00 |                      40      |    72      |     3.85833 |       6.66667 |                  2       |
| 14 | 2019-06-29 22:00:00 |                      35      |    67      |     3.98694 |       6.11111 |                  1.66667 |
| 15 | 2019-06-29 23:00:00 |                      29      |    61      |     4.11555 |       5.55556 |                  1.33333 |
| 16 | 2019-06-30 00:00:00 |                      24      |    56      |     4.63    |       5.27778 |                  1       |
| 17 | 2019-06-30 01:00:00 |                      23      |    55      |     5.14444 |       5       |                  1.33333 |
| 18 | 2019-06-30 02:00:00 |                      22      |    54      |     5.04155 |       4.44444 |                  1.38095 |
| 19 | 2019-06-30 03:00:00 |                      21      |    53      |     4.93866 |       3.88889 |                  1.42857 |
| 20 | 2019-06-30 04:00:00 |                      19      |    51      |     4.83577 |       3.61111 |                  1.47619 |
| 21 | 2019-06-30 05:00:00 |                      18      |    50      |     4.73288 |       3.33333 |                  1.52381 |
| 22 | 2019-06-30 06:00:00 |                      17      |    56      |     4.63    |       3.88889 |                  1.57143 |
| 23 | 2019-06-30 07:00:00 |                      19      |    60      |     4.37277 |       5.55556 |                  1.61905 |
| 24 | 2019-06-30 08:00:00 |                      20      |    64      |     4.11555 |       7.22222 |                  1.66667 |
| 25 | 2019-06-30 09:00:00 |                      22      |    68      |     3.94407 |       8.88889 |                  2       |
| 26 | 2019-06-30 10:00:00 |                      40      |    72      |     3.77259 |      10.5556  |                  3.5     |
| 27 | 2019-06-30 11:00:00 |                      57      |    89      |     3.60111 |      11.1111  |                  4.25    |
| 28 | 2019-06-30 12:00:00 |                      75      |   100      |     4.11555 |      10.8333  |                  5       |
| 29 | 2019-06-30 13:00:00 |                      79      |    99.1667 |     4.37277 |      10.5556  |                  4.83333 |
| 30 | 2019-06-30 14:00:00 |                      83      |    98.3333 |     4.63    |       9.44444 |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                      87      |    97.5    |     4.37277 |       8.88889 |                  4.5     |
| 32 | 2019-06-30 16:00:00 |                      81      |    96.6667 |     4.11555 |       8.75    |                  4.33333 |
| 33 | 2019-06-30 17:00:00 |                      69      |    95.8333 |     3.60111 |       8.61111 |                  4.16667 |
| 34 | 2019-06-30 18:00:00 |                      63      |    95      |     3.08666 |       8.47222 |                  4       |
| 35 | 2019-06-30 19:00:00 |                      56      |    91.3333 |     3.60111 |       8.33333 |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                      49      |    87.6667 |     3.85833 |       6.66667 |                  3       |
| 37 | 2019-06-30 21:00:00 |                      42      |    84      |     4.11555 |       5.55556 |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                      34.6667 |    85      |     4.37277 |       5       |                  2       |
| 39 | 2019-06-30 23:00:00 |                      27.3333 |    86      |     4.63    |       4.81481 |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      20      |    87      |     4.54426 |       4.62963 |                  1       |
| 41 | 2019-07-01 01:00:00 |                      19.75   |    86      |     4.45851 |       4.44444 |                  1.16667 |
| 42 | 2019-07-01 02:00:00 |                      19.5    |    83      |     4.37277 |       3.88889 |                  1.33333 |
| 43 | 2019-07-01 03:00:00 |                      19      |    81      |     4.28703 |       3.33333 |                  1.41667 |
| 44 | 2019-07-01 04:00:00 |                      18.6667 |    79      |     4.20129 |       2.77778 |                  1.5     |
| 45 | 2019-07-01 05:00:00 |                      18.3333 |    74      |     4.11555 |       3.05556 |                  1.58333 |
| 46 | 2019-07-01 06:00:00 |                      18      |    58      |     4.37277 |       3.33333 |                  1.66667 |
| 47 | 2019-07-01 07:00:00 |                      29.6667 |    53      |     4.63    |       4.44444 |                  1.77778 |
| 48 | 2019-07-01 08:00:00 |                      41.3333 |    42      |     4.71574 |       6.11111 |                  1.88889 |
| 49 | 2019-07-01 09:00:00 |                      53      |    36      |     4.80148 |       7.22222 |                  2       |
| 50 | 2019-07-01 10:00:00 |                      64.6667 |    42      |     4.88722 |       8.33333 |                  3       |
| 51 | 2019-07-01 11:00:00 |                      76.3333 |    55      |     4.97296 |       9.44444 |                  4       |
| 52 | 2019-07-01 12:00:00 |                      88      |    61      |     5.0587  |       9.25926 |                  5       |
| 53 | 2019-07-01 13:00:00 |                      79.8333 |    64      |     5.14444 |       9.07407 |                  4.83333 |
| 54 | 2019-07-01 14:00:00 |                      71.6667 |    71      |     5.65888 |       8.88889 |                  4.66667 |
| 55 | 2019-07-01 15:00:00 |                      63.5    |    74      |     5.4874  |       8.7037  |                  4.5     |
| 56 | 2019-07-01 16:00:00 |                      55.3333 |    73      |     5.31592 |       8.51852 |                  4.33333 |
| 57 | 2019-07-01 17:00:00 |                      47.1667 |    72      |     5.14444 |       8.33333 |                  4.16667 |
| 58 | 2019-07-01 18:00:00 |                      39      |    71      |     4.63    |       7.77778 |                  4       |
| 59 | 2019-07-01 19:00:00 |                      39      |    70      |     4.11555 |       7.22222 |                  3       |
| 60 | 2019-07-01 20:00:00 |                      39      |    62      |     3.60111 |       6.11111 |                  2       |
| 61 | 2019-07-01 21:00:00 |                      39      |    58      |     3.77259 |       5       |                  1       |
| 62 | 2019-07-01 22:00:00 |                      39      |    57      |     3.94407 |       4.44444 |                  1       |
| 63 | 2019-07-01 23:00:00 |                      39      |    55      |     4.11555 |       3.88889 |                  1       |

## Culebra (main)

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                       1      |    13      |    2.05778  |      13.8889  |                  1       |
|  1 | 2019-06-29 09:00:00 |                       3      |    11      |    2.22926  |      18.3333  |                  1.33333 |
|  2 | 2019-06-29 10:00:00 |                       5      |    16      |    2.40074  |      19.4444  |                  1.5     |
|  3 | 2019-06-29 11:00:00 |                       8      |    22      |    2.57222  |      20       |                  1.66667 |
|  4 | 2019-06-29 12:00:00 |                      12      |    27      |    2.315    |      21.1111  |                  2       |
|  5 | 2019-06-29 13:00:00 |                      26      |    34      |    2.05778  |      21.6667  |                  4       |
|  6 | 2019-06-29 14:00:00 |                      41      |    41      |    1.54333  |      22.2222  |                  4.5     |
|  7 | 2019-06-29 15:00:00 |                      55      |    55      |    1.02889  |      21.6667  |                  5       |
|  8 | 2019-06-29 16:00:00 |                      51      |    64      |    2.57222  |      21.1111  |                  4       |
|  9 | 2019-06-29 17:00:00 |                      47      |    79      |    4.11555  |      20       |                  3.83333 |
| 10 | 2019-06-29 18:00:00 |                      44      |    94      |    5.14444  |      18.8889  |                  3.66667 |
| 11 | 2019-06-29 19:00:00 |                      38      |    91      |    4.63     |      17.7778  |                  3.5     |
| 12 | 2019-06-29 20:00:00 |                      33      |    89      |    4.11555  |      16.6667  |                  3.33333 |
| 13 | 2019-06-29 21:00:00 |                      28      |    86      |    3.08666  |      15.5556  |                  3.16667 |
| 14 | 2019-06-29 22:00:00 |                      21      |    76      |    2.57222  |      15       |                  3       |
| 15 | 2019-06-29 23:00:00 |                      13      |    65      |    2.40074  |      14.4444  |                  2       |
| 16 | 2019-06-30 00:00:00 |                       6      |    55      |    2.22926  |      14.1667  |                  1       |
| 17 | 2019-06-30 01:00:00 |                       5      |    48      |    2.05778  |      13.8889  |                  1.6     |
| 18 | 2019-06-30 02:00:00 |                       4      |    42      |    1.80055  |      13.3333  |                  1.68571 |
| 19 | 2019-06-30 03:00:00 |                       3      |    36      |    1.54333  |      12.2222  |                  1.77143 |
| 20 | 2019-06-30 04:00:00 |                       4      |    31      |    1.80055  |      11.6667  |                  1.85714 |
| 21 | 2019-06-30 05:00:00 |                       5      |    26      |    2.05778  |      11.1111  |                  1.94286 |
| 22 | 2019-06-30 06:00:00 |                       6      |    21      |    2.00062  |      11.6667  |                  2.02857 |
| 23 | 2019-06-30 07:00:00 |                       7      |    22      |    1.94346  |      12.7778  |                  2.11429 |
| 24 | 2019-06-30 08:00:00 |                       8      |    23      |    1.88629  |      15       |                  2.2     |
| 25 | 2019-06-30 09:00:00 |                       9      |    24      |    1.82913  |      17.2222  |                  2.8     |
| 26 | 2019-06-30 10:00:00 |                      26      |    37      |    1.77197  |      20       |                  3.4     |
| 27 | 2019-06-30 11:00:00 |                      43      |    50      |    1.71481  |      21.6667  |                  3.7     |
| 28 | 2019-06-30 12:00:00 |                      60      |    62      |    1.65765  |      22.7778  |                  4       |
| 29 | 2019-06-30 13:00:00 |                      65      |    65      |    1.60049  |      23.3333  |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                      70      |    67      |    1.54333  |      22.7778  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                      75      |    75      |    1.80055  |      22.2222  |                  5       |
| 32 | 2019-06-30 16:00:00 |                      67      |    76      |    2.05778  |      20.5556  |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                      59      |    77      |    3.08666  |      19.4444  |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                      51      |    95      |    2.82944  |      17.7778  |                  4       |
| 35 | 2019-06-30 19:00:00 |                      44      |    94      |    2.57222  |      16.6667  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                      37      |    91.6667 |    2.05778  |      15.5556  |                  3       |
| 37 | 2019-06-30 21:00:00 |                      30      |    89.3333 |    2.22926  |      13.8889  |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                      22.6667 |    87      |    2.40074  |      12.7778  |                  2       |
| 39 | 2019-06-30 23:00:00 |                      15.3333 |    81      |    2.57222  |      12.2222  |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                       8      |    74      |    3.08666  |      11.6667  |                  1       |
| 41 | 2019-07-01 01:00:00 |                      10      |    71      |    2.57222  |      10.5556  |                  1.5     |
| 42 | 2019-07-01 02:00:00 |                      12      |    67      |    2.05778  |      10.3704  |                  2       |
| 43 | 2019-07-01 03:00:00 |                      16      |    64      |    1.80055  |      10.1852  |                  2.25    |
| 44 | 2019-07-01 04:00:00 |                      17.3333 |    62      |    1.54333  |      10       |                  2.5     |
| 45 | 2019-07-01 05:00:00 |                      18.6667 |    60      |    1.62907  |       9.72222 |                  2.75    |
| 46 | 2019-07-01 06:00:00 |                      20      |    58      |    1.71481  |       9.44444 |                  3       |
| 47 | 2019-07-01 07:00:00 |                      31.5    |    56      |    1.80055  |      11.1111  |                  3.16667 |
| 48 | 2019-07-01 08:00:00 |                      43      |    49      |    1.88629  |      13.3333  |                  3.33333 |
| 49 | 2019-07-01 09:00:00 |                      54.5    |    41      |    1.97204  |      15.5556  |                  3.5     |
| 50 | 2019-07-01 10:00:00 |                      66      |    54      |    2.05778  |      16.6667  |                  3.66667 |
| 51 | 2019-07-01 11:00:00 |                      77.5    |    66      |    2.315    |      17.7778  |                  3.83333 |
| 52 | 2019-07-01 12:00:00 |                      89      |    79      |    2.57222  |      17.963   |                  4       |
| 53 | 2019-07-01 13:00:00 |                      86.3333 |    78      |    2.05778  |      18.1481  |                  4       |
| 54 | 2019-07-01 14:00:00 |                      83.6667 |    77      |    1.54333  |      18.3333  |                  4       |
| 55 | 2019-07-01 15:00:00 |                      81      |    79      |    1.02889  |      19.4444  |                  4       |
| 56 | 2019-07-01 16:00:00 |                      78.3333 |    81      |    0.964583 |      18.8889  |                  4       |
| 57 | 2019-07-01 17:00:00 |                      75.6667 |    85      |    0.900277 |      18.3333  |                  4       |
| 58 | 2019-07-01 18:00:00 |                      73      |    90      |    0.835972 |      17.7778  |                  4       |
| 59 | 2019-07-01 19:00:00 |                      73      |    89      |    0.771666 |      17.2222  |                  4       |
| 60 | 2019-07-01 20:00:00 |                      73      |    88.5    |    0.707361 |      15       |                  4       |
| 61 | 2019-07-01 21:00:00 |                      73      |    88      |    0.643055 |      13.3333  |                  4       |
| 62 | 2019-07-01 22:00:00 |                      73      |    87      |    0.57875  |      12.7778  |                  4       |
| 63 | 2019-07-01 23:00:00 |                      73      |    86      |    0.514444 |      12.2222  |                  4       |

## Huerfano-Lily Lake

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      0       |    22      |     3.08666 |      14.4444  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      2       |    20      |     3.34389 |      18.3333  |                  1.33333 |
|  2 | 2019-06-29 10:00:00 |                      4       |    22      |     3.60111 |      19.4444  |                  1.5     |
|  3 | 2019-06-29 11:00:00 |                      8       |    23      |     4.11555 |      20       |                  1.66667 |
|  4 | 2019-06-29 12:00:00 |                     12       |    25      |     3.77259 |      22.7778  |                  2       |
|  5 | 2019-06-29 13:00:00 |                     24       |    32      |     3.42963 |      22.5     |                  3       |
|  6 | 2019-06-29 14:00:00 |                     36       |    39      |     3.08666 |      22.2222  |                  4       |
|  7 | 2019-06-29 15:00:00 |                     48       |    48      |     2.57222 |      21.9444  |                  3.85714 |
|  8 | 2019-06-29 16:00:00 |                     46       |    60      |     3.08666 |      21.6667  |                  3.71429 |
|  9 | 2019-06-29 17:00:00 |                     44       |    74      |     3.34389 |      20.5556  |                  3.57143 |
| 10 | 2019-06-29 18:00:00 |                     42       |    87      |     3.60111 |      18.8889  |                  3.42857 |
| 11 | 2019-06-29 19:00:00 |                     35       |    85      |     3.68685 |      17.2222  |                  3.28571 |
| 12 | 2019-06-29 20:00:00 |                     28       |    84      |     3.77259 |      15.5556  |                  3.14286 |
| 13 | 2019-06-29 21:00:00 |                     21       |    82      |     3.85833 |      14.4444  |                  3       |
| 14 | 2019-06-29 22:00:00 |                     16       |    72      |     3.94407 |      13.3333  |                  2.5     |
| 15 | 2019-06-29 23:00:00 |                     10       |    62      |     4.02981 |      12.7778  |                  2       |
| 16 | 2019-06-30 00:00:00 |                      5       |    52      |     4.11555 |      11.6667  |                  1       |
| 17 | 2019-06-30 01:00:00 |                      4       |    49      |     4.37277 |      11.1111  |                  1.6     |
| 18 | 2019-06-30 02:00:00 |                      3       |    46      |     4.63    |      10.5556  |                  1.68571 |
| 19 | 2019-06-30 03:00:00 |                      2       |    43      |     4.45851 |      10       |                  1.77143 |
| 20 | 2019-06-30 04:00:00 |                      3       |    36      |     4.28703 |       9.44444 |                  1.85714 |
| 21 | 2019-06-30 05:00:00 |                      4       |    30      |     4.11555 |       8.88889 |                  1.94286 |
| 22 | 2019-06-30 06:00:00 |                      5       |    23      |     3.60111 |       9.44444 |                  2.02857 |
| 23 | 2019-06-30 07:00:00 |                      6.33333 |    27      |     3.49822 |      11.1111  |                  2.11429 |
| 24 | 2019-06-30 08:00:00 |                      7.66667 |    31      |     3.39533 |      13.8889  |                  2.2     |
| 25 | 2019-06-30 09:00:00 |                      9       |    35      |     3.29244 |      16.1111  |                  2.8     |
| 26 | 2019-06-30 10:00:00 |                     25.6667  |    39      |     3.18955 |      18.3333  |                  3.4     |
| 27 | 2019-06-30 11:00:00 |                     42.3333  |    54      |     3.08666 |      20       |                  3.7     |
| 28 | 2019-06-30 12:00:00 |                     59       |    70      |     2.82944 |      21.1111  |                  4       |
| 29 | 2019-06-30 13:00:00 |                     64       |    68      |     2.57222 |      21.6667  |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                     69       |    67      |     2.05778 |      21.3889  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     74       |    75      |     2.57222 |      21.1111  |                  5       |
| 32 | 2019-06-30 16:00:00 |                     66.6667  |    81.3333 |     3.08666 |      19.4444  |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                     59.3333  |    87.6667 |     4.11555 |      17.7778  |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                     52       |    94      |     2.57222 |      16.1111  |                  4       |
| 35 | 2019-06-30 19:00:00 |                     44.3333  |    93      |     2.7437  |      15.5556  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     36.6667  |    91      |     2.91518 |      15       |                  3       |
| 37 | 2019-06-30 21:00:00 |                     29       |    89      |     3.08666 |      12.2222  |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     21.3333  |    87      |     3.60111 |      11.1111  |                  2       |
| 39 | 2019-06-30 23:00:00 |                     13.6667  |    80      |     4.63    |      10       |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      6       |    74      |     5.65888 |       9.44444 |                  1       |
| 41 | 2019-07-01 01:00:00 |                      8.16667 |    71      |     6.17333 |       7.77778 |                  1.5     |
| 42 | 2019-07-01 02:00:00 |                     10.3333  |    67      |     5.91611 |       7.63889 |                  2       |
| 43 | 2019-07-01 03:00:00 |                     14.6667  |    64      |     5.65888 |       7.5     |                  2.25    |
| 44 | 2019-07-01 04:00:00 |                     16.1111  |    65      |     5.14444 |       7.36111 |                  2.5     |
| 45 | 2019-07-01 05:00:00 |                     17.5556  |    65.5    |     4.63    |       7.22222 |                  2.75    |
| 46 | 2019-07-01 06:00:00 |                     19       |    66      |     4.11555 |       8.33333 |                  3       |
| 47 | 2019-07-01 07:00:00 |                     31       |    59      |     4.37277 |       9.44444 |                  3.16667 |
| 48 | 2019-07-01 08:00:00 |                     43       |    51      |     4.63    |      12.2222  |                  3.33333 |
| 49 | 2019-07-01 09:00:00 |                     55       |    44      |     4.45851 |      13.3333  |                  3.5     |
| 50 | 2019-07-01 10:00:00 |                     67       |    55      |     4.28703 |      15       |                  3.66667 |
| 51 | 2019-07-01 11:00:00 |                     79       |    66      |     4.11555 |      16.1111  |                  3.83333 |
| 52 | 2019-07-01 12:00:00 |                     91       |    77      |     3.60111 |      16.6667  |                  4       |
| 53 | 2019-07-01 13:00:00 |                     86.8333  |    77.5    |     3.08666 |      17.2222  |                  4       |
| 54 | 2019-07-01 14:00:00 |                     82.6667  |    78      |     2.57222 |      17.4074  |                  4       |
| 55 | 2019-07-01 15:00:00 |                     78.5     |    79      |     2.05778 |      17.5926  |                  4       |
| 56 | 2019-07-01 16:00:00 |                     74.3333  |    82      |     2.18639 |      17.7778  |                  4       |
| 57 | 2019-07-01 17:00:00 |                     70.1667  |    84      |     2.315   |      17.2222  |                  4       |
| 58 | 2019-07-01 18:00:00 |                     66       |    87      |     2.44361 |      16.1111  |                  4       |
| 59 | 2019-07-01 19:00:00 |                     66       |    88      |     2.57222 |      15.5556  |                  4       |
| 60 | 2019-07-01 20:00:00 |                     66       |    88.5    |     3.60111 |      13.8889  |                  4       |
| 61 | 2019-07-01 21:00:00 |                     66       |    89      |     3.08666 |      11.6667  |                  4       |
| 62 | 2019-07-01 22:00:00 |                     66       |    85      |     2.57222 |      10.5556  |                  4       |
| 63 | 2019-07-01 23:00:00 |                     66       |    81      |     1.54333 |       9.44444 |                  4       |

## Fourmile Creek

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      2       |    36      |    1.54333  |      10.5556  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      8.25    |    56      |    2.57222  |      11.1111  |                  1.33333 |
|  2 | 2019-06-29 10:00:00 |                     14.5     |    64      |    3.08666  |      12.2222  |                  1.5     |
|  3 | 2019-06-29 11:00:00 |                     20.75    |    70      |    3.60111  |      13.3333  |                  1.66667 |
|  4 | 2019-06-29 12:00:00 |                     27       |    75      |    3.85833  |      14.4444  |                  2       |
|  5 | 2019-06-29 13:00:00 |                     36       |    83      |    4.11555  |      15       |                  4       |
|  6 | 2019-06-29 14:00:00 |                     44       |    85.5    |    2.57222  |      15.5556  |                  3.81818 |
|  7 | 2019-06-29 15:00:00 |                     45       |    88      |    3.08666  |      15       |                  3.63636 |
|  8 | 2019-06-29 16:00:00 |                     44.6667  |    94      |    3.60111  |      14.4444  |                  3.45455 |
|  9 | 2019-06-29 17:00:00 |                     44.3333  |    95      |    4.11555  |      12.2222  |                  3.27273 |
| 10 | 2019-06-29 18:00:00 |                     44       |    96      |    4.63     |      10.5556  |                  3.09091 |
| 11 | 2019-06-29 19:00:00 |                     42       |    95.3333 |    2.57222  |       9.44444 |                  2.90909 |
| 12 | 2019-06-29 20:00:00 |                     40       |    94.6667 |    0.514444 |       7.77778 |                  2.72727 |
| 13 | 2019-06-29 21:00:00 |                     38       |    94      |    2.05778  |       6.66667 |                  2.54545 |
| 14 | 2019-06-29 22:00:00 |                     36       |    87      |    3.08666  |       6.11111 |                  2.36364 |
| 15 | 2019-06-29 23:00:00 |                     29       |    85      |    3.60111  |       5.92593 |                  2.18182 |
| 16 | 2019-06-30 00:00:00 |                     22       |    76      |    3.08666  |       5.74074 |                  2       |
| 17 | 2019-06-30 01:00:00 |                     14       |    65      |    3.60111  |       5.55556 |                  1       |
| 18 | 2019-06-30 02:00:00 |                      7       |    64      |    4.11555  |       5.27778 |                  1.14286 |
| 19 | 2019-06-30 03:00:00 |                      5       |    54      |    4.50138  |       5       |                  1.28571 |
| 20 | 2019-06-30 04:00:00 |                      6       |    56      |    4.88722  |       4.44444 |                  1.42857 |
| 21 | 2019-06-30 05:00:00 |                      7       |    53.5    |    5.27305  |       5       |                  1.57143 |
| 22 | 2019-06-30 06:00:00 |                      8       |    51      |    5.65888  |       5.55556 |                  1.71429 |
| 23 | 2019-06-30 07:00:00 |                      9       |    47      |    5.14444  |       6.11111 |                  1.85714 |
| 24 | 2019-06-30 08:00:00 |                     10       |    46      |    4.88722  |       7.77778 |                  2       |
| 25 | 2019-06-30 09:00:00 |                     14       |    42      |    4.63     |       9.44444 |                  2.66667 |
| 26 | 2019-06-30 10:00:00 |                     18       |    59      |    5.14444  |      11.1111  |                  3.33333 |
| 27 | 2019-06-30 11:00:00 |                     22       |    66      |    6.17333  |      11.6667  |                  3.66667 |
| 28 | 2019-06-30 12:00:00 |                     34       |    84      |    7.20222  |      12.2222  |                  4       |
| 29 | 2019-06-30 13:00:00 |                     46       |    86      |    7.71666  |      11.9444  |                  4.5     |
| 30 | 2019-06-30 14:00:00 |                     59       |    88      |    8.74555  |      11.6667  |                  5       |
| 31 | 2019-06-30 15:00:00 |                     71       |    94      |    9.77444  |      11.1111  |                  4.75    |
| 32 | 2019-06-30 16:00:00 |                     66.3333  |    95      |    9.25999  |      10       |                  4.5     |
| 33 | 2019-06-30 17:00:00 |                     61.6667  |    92      |    8.74555  |       8.88889 |                  4.25    |
| 34 | 2019-06-30 18:00:00 |                     57       |    89      |    7.71666  |       7.77778 |                  4       |
| 35 | 2019-06-30 19:00:00 |                     48.5     |    88.5    |    7.58805  |       6.66667 |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     40       |    88      |    7.45944  |       6.11111 |                  3       |
| 37 | 2019-06-30 21:00:00 |                     31.5     |    87      |    7.33083  |       5.55556 |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     23       |    86      |    7.20222  |       5.37037 |                  2       |
| 39 | 2019-06-30 23:00:00 |                     14.5     |    81      |    6.17333  |       5.18519 |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      6       |    79      |    5.65888  |       5       |                  1       |
| 41 | 2019-07-01 01:00:00 |                      4       |    77      |    5.91611  |       4.81481 |                  1.25    |
| 42 | 2019-07-01 02:00:00 |                      2       |    74      |    6.17333  |       4.62963 |                  1.5     |
| 43 | 2019-07-01 03:00:00 |                      7       |    72      |    6.68777  |       4.44444 |                  1.625   |
| 44 | 2019-07-01 04:00:00 |                      8.66667 |    71      |    7.20222  |       4.16667 |                  1.75    |
| 45 | 2019-07-01 05:00:00 |                     10.3333  |    68      |    7.45944  |       3.88889 |                  1.875   |
| 46 | 2019-07-01 06:00:00 |                     12       |    69      |    7.71666  |       4.44444 |                  2       |
| 47 | 2019-07-01 07:00:00 |                     23.5     |    67      |    8.2311   |       5.55556 |                  2.5     |
| 48 | 2019-07-01 08:00:00 |                     35       |    62      |    8.05962  |       6.66667 |                  3       |
| 49 | 2019-07-01 09:00:00 |                     46.5     |    59      |    7.88814  |       8.33333 |                  3.5     |
| 50 | 2019-07-01 10:00:00 |                     58       |    60.25   |    7.71666  |       9.44444 |                  4       |
| 51 | 2019-07-01 11:00:00 |                     69.5     |    61.5    |    7.45944  |      11.1111  |                  4.5     |
| 52 | 2019-07-01 12:00:00 |                     81       |    62.75   |    7.20222  |      11.6667  |                  5       |
| 53 | 2019-07-01 13:00:00 |                     76       |    64      |    7.45944  |      11.3889  |                  4.83333 |
| 54 | 2019-07-01 14:00:00 |                     71       |    75      |    7.71666  |      11.1111  |                  4.66667 |
| 55 | 2019-07-01 15:00:00 |                     66       |    80      |    8.2311   |      10.8333  |                  4.5     |
| 56 | 2019-07-01 16:00:00 |                     61       |    79.5    |    8.10249  |      10.5556  |                  4.33333 |
| 57 | 2019-07-01 17:00:00 |                     56       |    79      |    7.97388  |      10       |                  4.16667 |
| 58 | 2019-07-01 18:00:00 |                     51       |    78      |    7.84527  |       8.88889 |                  4       |
| 59 | 2019-07-01 19:00:00 |                     51       |    74      |    7.71666  |       7.77778 |                  4       |
| 60 | 2019-07-01 20:00:00 |                     51       |    65      |    6.68777  |       6.11111 |                  4       |
| 61 | 2019-07-01 21:00:00 |                     51       |    61      |    6.17333  |       5       |                  4       |
| 62 | 2019-07-01 22:00:00 |                     51       |    60      |    6.24682  |       4.44444 |                  4       |
| 63 | 2019-07-01 23:00:00 |                     51       |    58      |    6.32031  |       4.30556 |                  4       |

## Silver Creek-Grizzly Gulch

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      13      |       31   |     2.05778 |       8.33333 |                  1       |
|  1 | 2019-06-29 09:00:00 |                      13      |       31   |     2.05778 |       8.33333 |                  1       |
|  2 | 2019-06-29 10:00:00 |                      17      |       33   |     1.54333 |       8.88889 |                  1.25    |
|  3 | 2019-06-29 11:00:00 |                      20      |       34   |     1.74911 |      10       |                  1.5     |
|  4 | 2019-06-29 12:00:00 |                      23      |       55   |     1.95489 |      10.5556  |                  2       |
|  5 | 2019-06-29 13:00:00 |                      40      |       74   |     2.16066 |      10       |                  4       |
|  6 | 2019-06-29 14:00:00 |                      58      |       90   |     2.36644 |      10.2778  |                  3.75    |
|  7 | 2019-06-29 15:00:00 |                      75      |      100   |     2.57222 |      10.5556  |                  3.5     |
|  8 | 2019-06-29 16:00:00 |                      68      |       97   |     3.60111 |      11.1111  |                  3.25    |
|  9 | 2019-06-29 17:00:00 |                      62      |       94   |     4.63    |      10.5556  |                  3       |
| 10 | 2019-06-29 18:00:00 |                      55      |       87   |     4.37277 |      10       |                  2.75    |
| 11 | 2019-06-29 19:00:00 |                      50      |       82   |     4.11555 |       9.44444 |                  2.5     |
| 12 | 2019-06-29 20:00:00 |                      44      |       76   |     4.28703 |       7.77778 |                  2.25    |
| 13 | 2019-06-29 21:00:00 |                      39      |       71   |     4.45851 |       6.66667 |                  2       |
| 14 | 2019-06-29 22:00:00 |                      33      |       65   |     4.63    |       6.11111 |                  1.66667 |
| 15 | 2019-06-29 23:00:00 |                      28      |       60   |     4.88722 |       5.55556 |                  1.33333 |
| 16 | 2019-06-30 00:00:00 |                      22      |       54   |     5.14444 |       5       |                  1       |
| 17 | 2019-06-30 01:00:00 |                      21      |       53   |     5.65888 |       4.81481 |                  1.33333 |
| 18 | 2019-06-30 02:00:00 |                      20      |       52   |     6.17333 |       4.62963 |                  1.38095 |
| 19 | 2019-06-30 03:00:00 |                      19.5    |       51.5 |     6.68777 |       4.44444 |                  1.42857 |
| 20 | 2019-06-30 04:00:00 |                      19      |       51   |     6.43055 |       4.72222 |                  1.47619 |
| 21 | 2019-06-30 05:00:00 |                      18      |       50   |     6.17333 |       5       |                  1.52381 |
| 22 | 2019-06-30 06:00:00 |                      17      |       56   |     5.65888 |       5.27778 |                  1.57143 |
| 23 | 2019-06-30 07:00:00 |                      19      |       60   |     5.14444 |       5.55556 |                  1.61905 |
| 24 | 2019-06-30 08:00:00 |                      20      |       64   |     4.63    |       6.66667 |                  1.66667 |
| 25 | 2019-06-30 09:00:00 |                      22      |       68   |     4.37277 |       8.33333 |                  2       |
| 26 | 2019-06-30 10:00:00 |                      40      |       72   |     4.11555 |      10       |                  3.5     |
| 27 | 2019-06-30 11:00:00 |                      57      |       89   |     4.28703 |      11.1111  |                  4.25    |
| 28 | 2019-06-30 12:00:00 |                      75      |      100   |     4.45851 |      11.6667  |                  5       |
| 29 | 2019-06-30 13:00:00 |                      79      |       99   |     4.63    |      11.1111  |                  4.83333 |
| 30 | 2019-06-30 14:00:00 |                      84      |       98   |     4.88722 |      10       |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                      88      |       97   |     5.14444 |       9.44444 |                  4.5     |
| 32 | 2019-06-30 16:00:00 |                      82      |       96   |     4.63    |       9.72222 |                  4.33333 |
| 33 | 2019-06-30 17:00:00 |                      69      |       95   |     4.11555 |      10       |                  4.16667 |
| 34 | 2019-06-30 18:00:00 |                      62      |       94   |     3.60111 |       9.44444 |                  4       |
| 35 | 2019-06-30 19:00:00 |                      55      |       91   |     4.11555 |       8.88889 |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                      48      |       88   |     4.63    |       7.22222 |                  3       |
| 37 | 2019-06-30 21:00:00 |                      41      |       85   |     5.14444 |       6.11111 |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                      34      |       85.5 |     5.24733 |       5.83333 |                  2       |
| 39 | 2019-06-30 23:00:00 |                      27      |       86   |     5.35022 |       5.55556 |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      20      |       85.5 |     5.45311 |       5.37037 |                  1       |
| 41 | 2019-07-01 01:00:00 |                      19.75   |       85   |     5.556   |       5.18519 |                  1.16667 |
| 42 | 2019-07-01 02:00:00 |                      19.5    |       83   |     5.65888 |       5       |                  1.33333 |
| 43 | 2019-07-01 03:00:00 |                      19      |       82   |     5.40166 |       4.72222 |                  1.41667 |
| 44 | 2019-07-01 04:00:00 |                      18.6667 |       80   |     5.14444 |       4.44444 |                  1.5     |
| 45 | 2019-07-01 05:00:00 |                      18.3333 |       75   |     5.31592 |       4.72222 |                  1.58333 |
| 46 | 2019-07-01 06:00:00 |                      18      |       58   |     5.4874  |       5       |                  1.66667 |
| 47 | 2019-07-01 07:00:00 |                      29.8333 |       52   |     5.65888 |       5.55556 |                  1.77778 |
| 48 | 2019-07-01 08:00:00 |                      41.6667 |       41   |     5.53027 |       6.66667 |                  1.88889 |
| 49 | 2019-07-01 09:00:00 |                      53.5    |       35   |     5.40166 |       7.77778 |                  2       |
| 50 | 2019-07-01 10:00:00 |                      65.3333 |       41   |     5.27305 |       8.88889 |                  3       |
| 51 | 2019-07-01 11:00:00 |                      77.1667 |       53   |     5.14444 |      10       |                  4       |
| 52 | 2019-07-01 12:00:00 |                      89      |       59   |     5.40166 |      10.5556  |                  5       |
| 53 | 2019-07-01 13:00:00 |                      80.5    |       63   |     5.65888 |      10.3704  |                  4.83333 |
| 54 | 2019-07-01 14:00:00 |                      72      |       72   |     5.91611 |      10.1852  |                  4.66667 |
| 55 | 2019-07-01 15:00:00 |                      63.5    |       76   |     6.17333 |      10       |                  4.5     |
| 56 | 2019-07-01 16:00:00 |                      55      |       75   |     5.91611 |       9.81481 |                  4.33333 |
| 57 | 2019-07-01 17:00:00 |                      46.5    |       74   |     5.65888 |       9.62963 |                  4.16667 |
| 58 | 2019-07-01 18:00:00 |                      38      |       73   |     5.14444 |       9.44444 |                  4       |
| 59 | 2019-07-01 19:00:00 |                      38      |       72   |     4.88722 |       8.33333 |                  3       |
| 60 | 2019-07-01 20:00:00 |                      38      |       63   |     4.63    |       7.22222 |                  2       |
| 61 | 2019-07-01 21:00:00 |                      38      |       59   |     4.73288 |       6.11111 |                  1       |
| 62 | 2019-07-01 22:00:00 |                      38      |       58   |     4.83577 |       5.55556 |                  1       |
| 63 | 2019-07-01 23:00:00 |                      38      |       56   |     4.93866 |       5       |                  1       |

## Matterhorn Creek

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      12      |    31      |    0.514444 |      17.7778  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      12      |    31      |    0.514444 |      17.7778  |                  1       |
|  2 | 2019-06-29 10:00:00 |                      14      |    32      |    1.02889  |      20       |                  1.25    |
|  3 | 2019-06-29 11:00:00 |                      17      |    34      |    1.54333  |      21.1111  |                  1.5     |
|  4 | 2019-06-29 12:00:00 |                      20      |    52      |    1.71481  |      22.2222  |                  2       |
|  5 | 2019-06-29 13:00:00 |                      37      |    71      |    1.88629  |      20.5556  |                  4       |
|  6 | 2019-06-29 14:00:00 |                      55      |    87      |    2.05778  |      18.8889  |                  3.75    |
|  7 | 2019-06-29 15:00:00 |                      72      |   100      |    2.315    |      18.3333  |                  3.5     |
|  8 | 2019-06-29 16:00:00 |                      66      |    98      |    2.57222  |      17.7778  |                  3.25    |
|  9 | 2019-06-29 17:00:00 |                      61      |    93      |    2.65796  |      17.5     |                  3       |
| 10 | 2019-06-29 18:00:00 |                      55      |    87      |    2.7437   |      17.2222  |                  2.75    |
| 11 | 2019-06-29 19:00:00 |                      49      |    81      |    2.82944  |      15.5556  |                  2.5     |
| 12 | 2019-06-29 20:00:00 |                      42      |    74      |    2.91518  |      13.8889  |                  2.25    |
| 13 | 2019-06-29 21:00:00 |                      36      |    68      |    3.00092  |      12.2222  |                  2       |
| 14 | 2019-06-29 22:00:00 |                      30      |    62      |    3.08666  |      11.1111  |                  1.66667 |
| 15 | 2019-06-29 23:00:00 |                      23      |    55      |    3.25815  |      10.5556  |                  1.33333 |
| 16 | 2019-06-30 00:00:00 |                      17      |    56      |    3.42963  |      10       |                  1       |
| 17 | 2019-06-30 01:00:00 |                      17.125  |    49      |    3.60111  |       9.72222 |                  1.33333 |
| 18 | 2019-06-30 02:00:00 |                      17.25   |    50      |    4.11555  |       9.44444 |                  1.38095 |
| 19 | 2019-06-30 03:00:00 |                      17.375  |    51      |    3.94407  |       8.88889 |                  1.42857 |
| 20 | 2019-06-30 04:00:00 |                      17.5    |    52      |    3.77259  |       7.77778 |                  1.47619 |
| 21 | 2019-06-30 05:00:00 |                      17.625  |    53      |    3.60111  |       8.05556 |                  1.52381 |
| 22 | 2019-06-30 06:00:00 |                      17.75   |    54      |    3.34389  |       8.33333 |                  1.57143 |
| 23 | 2019-06-30 07:00:00 |                      17.875  |    57.25   |    3.08666  |      10       |                  1.61905 |
| 24 | 2019-06-30 08:00:00 |                      18      |    60.5    |    2.82944  |      12.7778  |                  1.66667 |
| 25 | 2019-06-30 09:00:00 |                      26.5    |    63.75   |    2.57222  |      15       |                  2       |
| 26 | 2019-06-30 10:00:00 |                      35      |    67      |    2.7437   |      16.6667  |                  3.5     |
| 27 | 2019-06-30 11:00:00 |                      52      |    84      |    2.91518  |      17.2222  |                  4.25    |
| 28 | 2019-06-30 12:00:00 |                      69      |   100      |    3.08666  |      16.9444  |                  5       |
| 29 | 2019-06-30 13:00:00 |                      75      |    98.6667 |    3.00092  |      16.6667  |                  4.83333 |
| 30 | 2019-06-30 14:00:00 |                      80      |    97.3333 |    2.91518  |      15.5556  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                      86      |    96      |    2.82944  |      15.4167  |                  4.5     |
| 32 | 2019-06-30 16:00:00 |                      80      |    94.6667 |    2.7437   |      15.2778  |                  4.33333 |
| 33 | 2019-06-30 17:00:00 |                      67      |    93.3333 |    2.65796  |      15.1389  |                  4.16667 |
| 34 | 2019-06-30 18:00:00 |                      60      |    92      |    2.57222  |      15       |                  4       |
| 35 | 2019-06-30 19:00:00 |                      53.3333 |    90      |    2.70083  |      13.8889  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                      46.6667 |    88      |    2.82944  |      11.6667  |                  3       |
| 37 | 2019-06-30 21:00:00 |                      40      |    86      |    2.95805  |      10       |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                      33      |    85.75   |    3.08666  |       8.88889 |                  2       |
| 39 | 2019-06-30 23:00:00 |                      26      |    85.5    |    3.60111  |       8.7037  |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      19      |    85.25   |    3.42963  |       8.51852 |                  1       |
| 41 | 2019-07-01 01:00:00 |                      18.8333 |    85      |    3.25815  |       8.33333 |                  1.16667 |
| 42 | 2019-07-01 02:00:00 |                      18.6667 |    82      |    3.08666  |       7.77778 |                  1.33333 |
| 43 | 2019-07-01 03:00:00 |                      18.3333 |    81      |    3.1724   |       7.5     |                  1.41667 |
| 44 | 2019-07-01 04:00:00 |                      18.2222 |    79      |    3.25815  |       7.22222 |                  1.5     |
| 45 | 2019-07-01 05:00:00 |                      18.1111 |    74      |    3.34389  |       6.66667 |                  1.58333 |
| 46 | 2019-07-01 06:00:00 |                      18      |    58      |    3.42963  |       7.77778 |                  1.66667 |
| 47 | 2019-07-01 07:00:00 |                      29.5    |    53      |    3.51537  |       9.44444 |                  1.77778 |
| 48 | 2019-07-01 08:00:00 |                      41      |    43      |    3.60111  |      12.2222  |                  1.88889 |
| 49 | 2019-07-01 09:00:00 |                      52.5    |    38      |    3.704    |      15       |                  2       |
| 50 | 2019-07-01 10:00:00 |                      64      |    42      |    3.80689  |      16.6667  |                  3       |
| 51 | 2019-07-01 11:00:00 |                      75.5    |    51      |    3.90977  |      17.2222  |                  4       |
| 52 | 2019-07-01 12:00:00 |                      87      |    55      |    4.01266  |      17.7778  |                  5       |
| 53 | 2019-07-01 13:00:00 |                      78      |    59      |    4.11555  |      17.2222  |                  4.83333 |
| 54 | 2019-07-01 14:00:00 |                      69      |    66      |    4.63     |      16.9444  |                  4.66667 |
| 55 | 2019-07-01 15:00:00 |                      60      |    70      |    4.45851  |      16.6667  |                  4.5     |
| 56 | 2019-07-01 16:00:00 |                      51      |    71      |    4.28703  |      16.4815  |                  4.33333 |
| 57 | 2019-07-01 17:00:00 |                      42      |    72      |    4.11555  |      16.2963  |                  4.16667 |
| 58 | 2019-07-01 18:00:00 |                      33      |    73      |    3.60111  |      16.1111  |                  4       |
| 59 | 2019-07-01 19:00:00 |                      33      |    70      |    3.34389  |      14.4444  |                  3       |
| 60 | 2019-07-01 20:00:00 |                      33      |    63      |    3.08666  |      12.2222  |                  2       |
| 61 | 2019-07-01 21:00:00 |                      33      |    60      |    2.91518  |      10       |                  1       |
| 62 | 2019-07-01 22:00:00 |                      33      |    59      |    2.7437   |       8.88889 |                  1       |
| 63 | 2019-07-01 23:00:00 |                      33      |    56      |    2.57222  |       8.33333 |                  1       |

## Stewart Creek

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      4       |       43   |     3.08666 |      13.3333  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      6       |       48   |     2.82944 |      17.2222  |                  1.5     |
|  2 | 2019-06-29 10:00:00 |                      8       |       50   |     2.57222 |      18.8889  |                  1.75    |
|  3 | 2019-06-29 11:00:00 |                     13       |       52   |     2.315   |      20       |                  2       |
|  4 | 2019-06-29 12:00:00 |                     17       |       54   |     2.05778 |      20.5556  |                  3       |
|  5 | 2019-06-29 13:00:00 |                     33       |       62   |     2.57222 |      20.2778  |                  4       |
|  6 | 2019-06-29 14:00:00 |                     50       |       71   |     3.60111 |      20       |                  4.5     |
|  7 | 2019-06-29 15:00:00 |                     66       |       80   |     3.34389 |      19.4444  |                  5       |
|  8 | 2019-06-29 16:00:00 |                     59       |       80.5 |     3.08666 |      18.8889  |                  4.5     |
|  9 | 2019-06-29 17:00:00 |                     53       |       81   |     2.05778 |      18.0556  |                  4       |
| 10 | 2019-06-29 18:00:00 |                     46       |       77.5 |     1.54333 |      17.2222  |                  3.8     |
| 11 | 2019-06-29 19:00:00 |                     39       |       74   |     2.05778 |      16.1111  |                  3.6     |
| 12 | 2019-06-29 20:00:00 |                     32       |       67   |     2.57222 |      14.4444  |                  3.4     |
| 13 | 2019-06-29 21:00:00 |                     25       |       60   |     3.08666 |      12.7778  |                  3.2     |
| 14 | 2019-06-29 22:00:00 |                     19       |       56   |     2.82944 |      11.6667  |                  3       |
| 15 | 2019-06-29 23:00:00 |                     13       |       52   |     2.57222 |      10.5556  |                  2       |
| 16 | 2019-06-30 00:00:00 |                      8       |       48   |     3.08666 |      10       |                  1       |
| 17 | 2019-06-30 01:00:00 |                      7       |       44   |     3.60111 |       9.72222 |                  1.33333 |
| 18 | 2019-06-30 02:00:00 |                      6       |       40   |     4.63    |       9.44444 |                  1.38095 |
| 19 | 2019-06-30 03:00:00 |                      5       |       36   |     5.65888 |       9.16667 |                  1.42857 |
| 20 | 2019-06-30 04:00:00 |                      6       |       36.5 |     5.14444 |       8.88889 |                  1.47619 |
| 21 | 2019-06-30 05:00:00 |                      7       |       37   |     4.11555 |       8.33333 |                  1.52381 |
| 22 | 2019-06-30 06:00:00 |                      8       |       37.5 |     2.57222 |       8.88889 |                  1.57143 |
| 23 | 2019-06-30 07:00:00 |                      9.66667 |       38   |     2.05778 |      10       |                  1.61905 |
| 24 | 2019-06-30 08:00:00 |                     11.3333  |       44   |     1.54333 |      12.7778  |                  1.66667 |
| 25 | 2019-06-30 09:00:00 |                     13       |       50   |     1.64622 |      15       |                  2       |
| 26 | 2019-06-30 10:00:00 |                     29.6667  |       56   |     1.74911 |      17.2222  |                  3.5     |
| 27 | 2019-06-30 11:00:00 |                     46.3333  |       74   |     1.852   |      18.3333  |                  4.25    |
| 28 | 2019-06-30 12:00:00 |                     63       |       93   |     1.95489 |      18.8889  |                  5       |
| 29 | 2019-06-30 13:00:00 |                     67       |       95   |     2.05778 |      18.3333  |                  4.83333 |
| 30 | 2019-06-30 14:00:00 |                     71       |       98   |     2.57222 |      16.6667  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     75       |      100   |     3.08666 |      15.5556  |                  4.5     |
| 32 | 2019-06-30 16:00:00 |                     70       |       97   |     2.82944 |      15       |                  4.33333 |
| 33 | 2019-06-30 17:00:00 |                     65       |       93   |     2.57222 |      14.4444  |                  4.16667 |
| 34 | 2019-06-30 18:00:00 |                     60       |       89   |     3.60111 |      15.2778  |                  4       |
| 35 | 2019-06-30 19:00:00 |                     52.6667  |       88   |     2.57222 |      16.1111  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     45.3333  |       87   |     1.54333 |      14.4444  |                  3       |
| 37 | 2019-06-30 21:00:00 |                     38       |       86   |     1.02889 |      11.6667  |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     30       |       83   |     1.54333 |      10.5556  |                  2       |
| 39 | 2019-06-30 23:00:00 |                     22       |       80   |     2.57222 |      10       |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                     14       |       77   |     3.60111 |       8.88889 |                  1       |
| 41 | 2019-07-01 01:00:00 |                     12.75    |       76.5 |     3.4725  |       8.75    |                  1.75    |
| 42 | 2019-07-01 02:00:00 |                     11.5     |       76   |     3.34389 |       8.61111 |                  2.5     |
| 43 | 2019-07-01 03:00:00 |                      9       |       75.5 |     3.21528 |       8.47222 |                  2.875   |
| 44 | 2019-07-01 04:00:00 |                     17.3333  |       75   |     3.08666 |       8.33333 |                  3.25    |
| 45 | 2019-07-01 05:00:00 |                     25.6667  |       73   |     2.57222 |       7.77778 |                  3.625   |
| 46 | 2019-07-01 06:00:00 |                     34       |       71   |     2.05778 |       7.22222 |                  4       |
| 47 | 2019-07-01 07:00:00 |                     43.8333  |       61   |     2.18639 |       9.44444 |                  4       |
| 48 | 2019-07-01 08:00:00 |                     53.6667  |       50   |     2.315   |      12.2222  |                  4       |
| 49 | 2019-07-01 09:00:00 |                     63.5     |       40   |     2.44361 |      13.8889  |                  4       |
| 50 | 2019-07-01 10:00:00 |                     73.3333  |       45   |     2.57222 |      16.1111  |                  4       |
| 51 | 2019-07-01 11:00:00 |                     83.1667  |       51   |     3.08666 |      17.2222  |                  4       |
| 52 | 2019-07-01 12:00:00 |                     93       |       57   |     3.60111 |      17.7778  |                  4       |
| 53 | 2019-07-01 13:00:00 |                     85.8333  |       62   |     3.45412 |      17.2222  |                  4       |
| 54 | 2019-07-01 14:00:00 |                     78.6667  |       67   |     3.30714 |      18.3333  |                  4       |
| 55 | 2019-07-01 15:00:00 |                     71.5     |       72   |     3.16016 |      18.0556  |                  4       |
| 56 | 2019-07-01 16:00:00 |                     64.3333  |       77   |     3.01317 |      17.7778  |                  4       |
| 57 | 2019-07-01 17:00:00 |                     57.1667  |       82   |     2.86619 |      17.5     |                  4       |
| 58 | 2019-07-01 18:00:00 |                     50       |       86   |     2.7192  |      17.2222  |                  4       |
| 59 | 2019-07-01 19:00:00 |                     50       |       80   |     2.57222 |      15.5556  |                  4       |
| 60 | 2019-07-01 20:00:00 |                     50       |       74   |     2.05778 |      13.8889  |                  4       |
| 61 | 2019-07-01 21:00:00 |                     50       |       68   |     1.54333 |      11.6667  |                  4       |
| 62 | 2019-07-01 22:00:00 |                     50       |       67   |     1.71481 |      10       |                  4       |
| 63 | 2019-07-01 23:00:00 |                     50       |       66   |     1.88629 |       9.44444 |                  4       |

## Half Moon

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                       4      |    35      |    2.05778  |      16.1111  |                  1       |
|  1 | 2019-06-29 09:00:00 |                       4      |    35      |    2.05778  |      16.1111  |                  1       |
|  2 | 2019-06-29 10:00:00 |                       6      |    53      |    2.57222  |      18.3333  |                  1.16667 |
|  3 | 2019-06-29 11:00:00 |                       8      |    46      |    1.54333  |      19.4444  |                  1.33333 |
|  4 | 2019-06-29 12:00:00 |                      11      |    49.5    |    2.05778  |      20       |                  1.66667 |
|  5 | 2019-06-29 13:00:00 |                      21      |    53      |    3.08666  |      21.1111  |                  2       |
|  6 | 2019-06-29 14:00:00 |                      32      |    64      |    1.54333  |      22.2222  |                  4       |
|  7 | 2019-06-29 15:00:00 |                      43      |    75      |    2.57222  |      21.9444  |                  3.6     |
|  8 | 2019-06-29 16:00:00 |                      37      |    82      |    3.08666  |      21.6667  |                  3.2     |
|  9 | 2019-06-29 17:00:00 |                      32      |    84      |    4.11555  |      21.3889  |                  2.8     |
| 10 | 2019-06-29 18:00:00 |                      26      |    93      |    1.54333  |      21.1111  |                  2.4     |
| 11 | 2019-06-29 19:00:00 |                      23      |    66      |    2.05778  |      18.8889  |                  2       |
| 12 | 2019-06-29 20:00:00 |                      20      |    75      |    2.22926  |      17.7778  |                  1.8     |
| 13 | 2019-06-29 21:00:00 |                      18      |    71      |    2.40074  |      15.5556  |                  1.6     |
| 14 | 2019-06-29 22:00:00 |                      15      |    61      |    2.57222  |      13.8889  |                  1.4     |
| 15 | 2019-06-29 23:00:00 |                      12      |    44      |    2.46933  |      12.7778  |                  1.2     |
| 16 | 2019-06-30 00:00:00 |                       9      |    41      |    2.36644  |      11.6667  |                  1       |
| 17 | 2019-06-30 01:00:00 |                       8.875  |    40.875  |    2.26355  |      11.1111  |                  1.25    |
| 18 | 2019-06-30 02:00:00 |                       8.75   |    40.75   |    2.16066  |      10.5556  |                  1.28571 |
| 19 | 2019-06-30 03:00:00 |                       8.625  |    40.625  |    2.05778  |      10       |                  1.32143 |
| 20 | 2019-06-30 04:00:00 |                       8.5    |    40.5    |    1.80055  |       9.44444 |                  1.35714 |
| 21 | 2019-06-30 05:00:00 |                       8.375  |    40.375  |    1.54333  |       8.88889 |                  1.39286 |
| 22 | 2019-06-30 06:00:00 |                       8.25   |    40.25   |    1.37185  |       9.44444 |                  1.42857 |
| 23 | 2019-06-30 07:00:00 |                       8.125  |    40.125  |    1.20037  |      10       |                  1.46429 |
| 24 | 2019-06-30 08:00:00 |                       8      |    40      |    1.02889  |      12.2222  |                  1.5     |
| 25 | 2019-06-30 09:00:00 |                      17      |    49      |    1.1575   |      15       |                  1.75    |
| 26 | 2019-06-30 10:00:00 |                      26      |    58      |    1.28611  |      17.7778  |                  2       |
| 27 | 2019-06-30 11:00:00 |                      43      |    75      |    1.41472  |      20       |                  3       |
| 28 | 2019-06-30 12:00:00 |                      61      |    95      |    1.54333  |      21.1111  |                  4       |
| 29 | 2019-06-30 13:00:00 |                      65      |    97      |    1.02889  |      21.6667  |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                      70      |   100      |    1.20037  |      20.5556  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                      74      |    98.3333 |    1.37185  |      19.4444  |                  5       |
| 32 | 2019-06-30 16:00:00 |                      68      |    96.6667 |    1.54333  |      18.8889  |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                      57      |    95      |    2.05778  |      17.7778  |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                      51      |    85      |    2.57222  |      16.6667  |                  4       |
| 35 | 2019-06-30 19:00:00 |                      45      |    87      |    2.05778  |      15.5556  |                  3.33333 |
| 36 | 2019-06-30 20:00:00 |                      39      |    90      |    1.88629  |      13.8889  |                  2.66667 |
| 37 | 2019-06-30 21:00:00 |                      33      |    91      |    1.71481  |      12.7778  |                  2       |
| 38 | 2019-06-30 22:00:00 |                      26.6667 |    88      |    1.54333  |      11.6667  |                  1.66667 |
| 39 | 2019-06-30 23:00:00 |                      20.3333 |    83      |    1.28611  |      11.1111  |                  1.33333 |
| 40 | 2019-07-01 00:00:00 |                      14      |    80      |    1.02889  |      10.8333  |                  1       |
| 41 | 2019-07-01 01:00:00 |                      14.25   |    78      |    0.955396 |      10.5556  |                  1.16667 |
| 42 | 2019-07-01 02:00:00 |                      14.5    |    73      |    0.881904 |      10       |                  1.33333 |
| 43 | 2019-07-01 03:00:00 |                      15      |    71      |    0.808412 |       9.44444 |                  1.41667 |
| 44 | 2019-07-01 04:00:00 |                      15.3333 |    69      |    0.73492  |       8.88889 |                  1.5     |
| 45 | 2019-07-01 05:00:00 |                      15.6667 |    66      |    0.661428 |       8.33333 |                  1.58333 |
| 46 | 2019-07-01 06:00:00 |                      16      |    71      |    0.587936 |       8.88889 |                  1.66667 |
| 47 | 2019-07-01 07:00:00 |                      26.3333 |    68      |    0.514444 |       9.44444 |                  1.77778 |
| 48 | 2019-07-01 08:00:00 |                      36.6667 |    63      |    0.643055 |      11.6667  |                  1.88889 |
| 49 | 2019-07-01 09:00:00 |                      47      |    60      |    0.771666 |      13.8889  |                  2       |
| 50 | 2019-07-01 10:00:00 |                      57.3333 |    59      |    0.900277 |      16.6667  |                  2.66667 |
| 51 | 2019-07-01 11:00:00 |                      67.6667 |    58      |    1.02889  |      18.8889  |                  3.33333 |
| 52 | 2019-07-01 12:00:00 |                      78      |    57      |    1.54333  |      20.5556  |                  4       |
| 53 | 2019-07-01 13:00:00 |                      71.1667 |    58      |    2.05778  |      21.1111  |                  4.33333 |
| 54 | 2019-07-01 14:00:00 |                      64.3333 |    59      |    2.57222  |      20.8333  |                  4.66667 |
| 55 | 2019-07-01 15:00:00 |                      57.5    |    60      |    2.40074  |      20.5556  |                  5       |
| 56 | 2019-07-01 16:00:00 |                      50.6667 |    61      |    2.22926  |      20       |                  4.66667 |
| 57 | 2019-07-01 17:00:00 |                      43.8333 |    66      |    2.05778  |      19.4444  |                  4.33333 |
| 58 | 2019-07-01 18:00:00 |                      37      |    68      |    1.54333  |      17.7778  |                  4       |
| 59 | 2019-07-01 19:00:00 |                      37      |    64      |    1.28611  |      16.6667  |                  3       |
| 60 | 2019-07-01 20:00:00 |                      37      |    55      |    1.02889  |      14.4444  |                  2       |
| 61 | 2019-07-01 21:00:00 |                      37      |    50      |    1.06318  |      12.7778  |                  1       |
| 62 | 2019-07-01 22:00:00 |                      37      |    51      |    1.09748  |      11.6667  |                  1       |
| 63 | 2019-07-01 23:00:00 |                      37      |    52      |    1.13178  |      10.5556  |                  1       |

## Clear Creek

|    | index               |   probabilityOfPrecipitation |   skyCover |   windSpeed |   temperature |   lightningActivityLevel |
|----|---------------------|------------------------------|------------|-------------|---------------|--------------------------|
|  0 | 2019-06-29 08:00:00 |                      2       |       44   |    1.54333  |      11.6667  |                  1       |
|  1 | 2019-06-29 09:00:00 |                      3.5     |       49   |    2.05778  |      13.3333  |                  1.33333 |
|  2 | 2019-06-29 10:00:00 |                      5       |       48.5 |    3.08666  |      15.5556  |                  1.5     |
|  3 | 2019-06-29 11:00:00 |                      8       |       48   |    4.63     |      17.2222  |                  1.66667 |
|  4 | 2019-06-29 12:00:00 |                     11       |       50.5 |    5.14444  |      17.7778  |                  2       |
|  5 | 2019-06-29 13:00:00 |                     24       |       53   |    4.88722  |      18.3333  |                  3       |
|  6 | 2019-06-29 14:00:00 |                     38       |       59   |    4.63     |      17.963   |                  4       |
|  7 | 2019-06-29 15:00:00 |                     51       |       65   |    4.11555  |      17.5926  |                  3.875   |
|  8 | 2019-06-29 16:00:00 |                     48       |       71   |    3.60111  |      17.2222  |                  3.75    |
|  9 | 2019-06-29 17:00:00 |                     46       |       76   |    3.08666  |      16.1111  |                  3.625   |
| 10 | 2019-06-29 18:00:00 |                     43       |       82   |    2.57222  |      16.6667  |                  3.5     |
| 11 | 2019-06-29 19:00:00 |                     38       |       78   |    2.46933  |      15       |                  3.375   |
| 12 | 2019-06-29 20:00:00 |                     33       |       73   |    2.36644  |      12.2222  |                  3.25    |
| 13 | 2019-06-29 21:00:00 |                     28       |       69   |    2.26355  |      10       |                  3.125   |
| 14 | 2019-06-29 22:00:00 |                     20       |       57   |    2.16066  |       8.88889 |                  3       |
| 15 | 2019-06-29 23:00:00 |                     12       |       45   |    2.05778  |       7.77778 |                  2       |
| 16 | 2019-06-30 00:00:00 |                      4       |       33   |    1.80055  |       7.59259 |                  1       |
| 17 | 2019-06-30 01:00:00 |                      3       |       26   |    1.54333  |       7.40741 |                  1.6     |
| 18 | 2019-06-30 02:00:00 |                      2       |       20   |    2.05778  |       7.22222 |                  1.68571 |
| 19 | 2019-06-30 03:00:00 |                      1       |       14   |    1.97204  |       6.66667 |                  1.77143 |
| 20 | 2019-06-30 04:00:00 |                      2       |       19   |    1.88629  |       6.11111 |                  1.85714 |
| 21 | 2019-06-30 05:00:00 |                      3       |       25   |    1.80055  |       5.55556 |                  1.94286 |
| 22 | 2019-06-30 06:00:00 |                      4       |       31   |    1.71481  |       6.11111 |                  2.02857 |
| 23 | 2019-06-30 07:00:00 |                      5.66667 |       30   |    1.62907  |       8.33333 |                  2.11429 |
| 24 | 2019-06-30 08:00:00 |                      7.33333 |       29.5 |    1.54333  |      12.2222  |                  2.2     |
| 25 | 2019-06-30 09:00:00 |                      9       |       29   |    1.28611  |      15.5556  |                  2.8     |
| 26 | 2019-06-30 10:00:00 |                     27       |       44   |    1.02889  |      17.2222  |                  3.4     |
| 27 | 2019-06-30 11:00:00 |                     45       |       58   |    1.37185  |      18.3333  |                  3.7     |
| 28 | 2019-06-30 12:00:00 |                     63       |       73   |    1.71481  |      18.8889  |                  4       |
| 29 | 2019-06-30 13:00:00 |                     67       |       77   |    2.05778  |      18.5185  |                  4.33333 |
| 30 | 2019-06-30 14:00:00 |                     71       |       81   |    3.08666  |      18.1481  |                  4.66667 |
| 31 | 2019-06-30 15:00:00 |                     75       |       85   |    3.60111  |      17.7778  |                  5       |
| 32 | 2019-06-30 16:00:00 |                     70.6667  |       87   |    3.34389  |      16.6667  |                  4.66667 |
| 33 | 2019-06-30 17:00:00 |                     66.3333  |       89   |    3.08666  |      14.4444  |                  4.33333 |
| 34 | 2019-06-30 18:00:00 |                     62       |       88.5 |    2.57222  |      12.2222  |                  4       |
| 35 | 2019-06-30 19:00:00 |                     52.6667  |       88   |    1.54333  |      11.1111  |                  3.5     |
| 36 | 2019-06-30 20:00:00 |                     43.3333  |       87.5 |    1.02889  |      10       |                  3       |
| 37 | 2019-06-30 21:00:00 |                     34       |       87   |    0.514444 |       6.66667 |                  2.5     |
| 38 | 2019-06-30 22:00:00 |                     24.6667  |       83   |    1.02889  |       5.55556 |                  2       |
| 39 | 2019-06-30 23:00:00 |                     15.3333  |       80   |    1.54333  |       5       |                  1.5     |
| 40 | 2019-07-01 00:00:00 |                      6       |       76   |    2.05778  |       4.62963 |                  1       |
| 41 | 2019-07-01 01:00:00 |                      8.66667 |       73   |    2.16066  |       4.25926 |                  1.5     |
| 42 | 2019-07-01 02:00:00 |                     11.3333  |       71   |    2.26355  |       3.88889 |                  2       |
| 43 | 2019-07-01 03:00:00 |                     16.6667  |       69   |    2.36644  |       3.33333 |                  2.25    |
| 44 | 2019-07-01 04:00:00 |                     18.4444  |       67   |    2.46933  |       3.05556 |                  2.5     |
| 45 | 2019-07-01 05:00:00 |                     20.2222  |       65   |    2.57222  |       2.77778 |                  2.75    |
| 46 | 2019-07-01 06:00:00 |                     22       |       63   |    2.64571  |       3.61111 |                  3       |
| 47 | 2019-07-01 07:00:00 |                     32.8333  |       61   |    2.7192   |       4.44444 |                  3.16667 |
| 48 | 2019-07-01 08:00:00 |                     43.6667  |       59   |    2.7927   |       7.22222 |                  3.33333 |
| 49 | 2019-07-01 09:00:00 |                     54.5     |       57   |    2.86619  |      10       |                  3.5     |
| 50 | 2019-07-01 10:00:00 |                     65.3333  |       60   |    2.93968  |      11.1111  |                  3.66667 |
| 51 | 2019-07-01 11:00:00 |                     76.1667  |       62   |    3.01317  |      12.2222  |                  3.83333 |
| 52 | 2019-07-01 12:00:00 |                     87       |       64   |    3.08666  |      13.3333  |                  4       |
| 53 | 2019-07-01 13:00:00 |                     81.5     |       66   |    3.60111  |      13.5185  |                  4       |
| 54 | 2019-07-01 14:00:00 |                     76       |       69   |    3.4725   |      13.7037  |                  4       |
| 55 | 2019-07-01 15:00:00 |                     70.5     |       72   |    3.34389  |      13.8889  |                  4       |
| 56 | 2019-07-01 16:00:00 |                     65       |       74   |    3.21528  |      13.3333  |                  4       |
| 57 | 2019-07-01 17:00:00 |                     59.5     |       77   |    3.08666  |      12.7778  |                  4       |
| 58 | 2019-07-01 18:00:00 |                     54       |       79   |    2.57222  |      11.1111  |                  4       |
| 59 | 2019-07-01 19:00:00 |                     54       |       75   |    2.05778  |      10.5556  |                  4       |
| 60 | 2019-07-01 20:00:00 |                     54       |       71   |    1.54333  |       8.33333 |                  4       |
| 61 | 2019-07-01 21:00:00 |                     54       |       68   |    1.02889  |       5.55556 |                  4       |
| 62 | 2019-07-01 22:00:00 |                     54       |       64   |    1.28611  |       4.44444 |                  4       |
| 63 | 2019-07-01 23:00:00 |                     54       |       61   |    1.54333  |       3.88889 |                  4       |
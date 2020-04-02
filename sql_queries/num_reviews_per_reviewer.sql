select sum(`RP`) as RP, sum(`JS`) as JS,sum(`WE`) as WE, sum(`WS`) as WS, SUM(`V`) as V from
(
select if(`RP`!= -1, 1,0) as RP, if(`JS`!= -1, 1,0) as JS, if(`WE`!= -1, 1,0) as WE, if(`WS`!= -1, 1,0) as WS, if(`V`!= -1, 1,0) as V from vin.winecom_filtered
)
 as T;
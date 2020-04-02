select (`RP`+`JS`+`WE`+`WS` +`V`) as num_reviews, count(*) from
(
select if(`RP`!= -1, 1,0) as RP, if(`JS`!= -1, 1,0) as JS, if(`WE`!= -1, 1,0) as WE, if(`WS`!= -1, 1,0) as WS, if(`V`!= -1, 1,0) as V from vin.winecom_filtered
)
 as T group by `num_reviews` order by count(*) desc;
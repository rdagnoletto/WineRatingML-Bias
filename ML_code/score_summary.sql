SELECT distinct `winecom_filtered`.`varietal`, 
	AVG (CASE WHEN `winecom_filtered`.`RP` > 0 THEN `winecom_filtered`.`RP` ELSE NULL END) as RP_avg, SUM(CASE WHEN `winecom_filtered`.`RP` > 0 THEN 1 ELSE 0 END) as RP_num,
    AVG (CASE WHEN `winecom_filtered`.`JS` > 0 THEN `winecom_filtered`.`JS` ELSE NULL END) as JS_avg, SUM(CASE WHEN `winecom_filtered`.`JS` > 0 THEN 1 ELSE 0 END) as JS_num,
    AVG (CASE WHEN `winecom_filtered`.`V` > 0 THEN `winecom_filtered`.`V` ELSE NULL END) as V_avg, SUM(CASE WHEN `winecom_filtered`.`V` > 0 THEN 1 ELSE 0 END) as V_num,
    AVG (CASE WHEN `winecom_filtered`.`WS` > 0 THEN `winecom_filtered`.`WS` ELSE NULL END) as WS_avg, SUM(CASE WHEN `winecom_filtered`.`WS` > 0 THEN 1 ELSE 0 END) as WS_num,
    AVG (CASE WHEN `winecom_filtered`.`WE` > 0 THEN `winecom_filtered`.`WE` ELSE NULL END) as WE_avg, SUM(CASE WHEN `winecom_filtered`.`WE` > 0 THEN 1 ELSE 0 END) as WE_num
    FROM vin.winecom_filtered group by `winecom_filtered`.`varietal` order by  RP_avg desc
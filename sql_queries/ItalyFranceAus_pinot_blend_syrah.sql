SELECT `winecom_filtered`.`id`,
    `winecom_filtered`.`name`,
    `winecom_filtered`.`vintage`,
    `winecom_filtered`.`price`,
    `winecom_filtered`.`RP`,
    `winecom_filtered`.`url`,
    `winecom_filtered`.`varietal`,
     `winecom_filtered`.`location`,
    if(`varietal` = 'Bordeaux Red Blends' or `varietal`='Tuscan Blends',1,0) as bordeauxBlends,
    if(`varietal` = 'Syrah/Shiraz',1,0) as syrah,
    if(`varietal` = 'Pinot Noir',1,0) as pinot,
    if(`location` like '%Italy%',1,0) as italy,
    if(`location` like '%France%',1,0) as france,
    if(`location` like '%Australia%',1,0) as australia
FROM `vin`.`winecom_filtered`
where (`varietal`='Bordeaux Red Blends' or `varietal` = 'Syrah/Shiraz' or `varietal` = 'Pinot Noir' or `varietal`='Tuscan Blends') 
and (`location` like '%Italy%' or `location` like '%France%' or `location` like '%Australia%') 
and `RP`!=-1;

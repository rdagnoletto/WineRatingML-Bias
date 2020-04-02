SELECT `winecom_filtered`.`id`,
    `winecom_filtered`.`name`,
    `winecom_filtered`.`vintage`,
    `winecom_filtered`.`price`,
    `winecom_filtered`.`JS`,
    `winecom_filtered`.`url`,
    `winecom_filtered`.`varietal`,
    if(`varietal` = 'Malbec',1,0) as malbec,
    if(`varietal` = 'Malbec',0,1) as brunello
FROM `vin`.`winecom_filtered`
where (`name` like '%Brunello%' or `varietal` = 'Malbec') and `JS`!=-1;

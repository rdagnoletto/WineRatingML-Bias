UPDATE `vin`.`winecom_filtered`
SET

`id` = SUBSTRING( `url` , LENGTH(`url`) -  LOCATE('/',REVERSE(`url`)) + 2  , LENGTH(`url`)  )


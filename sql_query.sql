SELECT forestilling.navn AS "forestilling", 
       forestilling.dato AS "dato", 
       COUNT(billett.billettID) AS "Antall solgte plasser"
FROM forestilling 
INNER JOIN billett ON forestilling.dato = billett.forestillingsdato 
                  AND forestilling.tid = billett.forestillingstid 
                  AND forestilling.teaterstykke = billett.stykkenavn 
GROUP BY forestilling.navn, forestilling.dato
ORDER BY "Antall solgte plasser" DESC;

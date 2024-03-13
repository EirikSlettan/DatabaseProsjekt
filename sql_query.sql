SELECT forestilling.teaterstykke AS forestilling, 
       forestilling.dato AS dato, 
       COUNT(billett.billettID) AS Antallsolgteplasser
FROM forestilling 
INNER JOIN billett ON forestilling.dato = billett.forestillingsdato 
                  AND forestilling.tid = billett.forestillingstid 
                  AND forestilling.teaterstykke = billett.stykkenavn 
GROUP BY forestilling.teaterstykke, forestilling.dato
ORDER BY Antallsolgteplasser DESC;



vi ønsker å lage et query i SQL som finner hvilke (navn på) skuespillere som 
opptrer i de forskjellige teaterstykkene. Skriv ut navn på teaterstykke, navn på 
skuespiller og rolle.

SELECT teaterstykke.navn AS teaterstykke, 
        ansatt.navn AS skuespiller, 
        rolle.rollenavn AS rolle

FROM teaterstykke
INNER JOIN akter ON teaterstykke.navn = akter.stykkenavn
INNER JOIN aktharrolle ON akter.aktnr = aktharrolle.aktnr
INNER JOIN rolle ON rolle.rolleID = aktharrolle.rolleID
INNER JOIN harrolle ON rolle.rolleID = harrolle.rolleID
INNER JOIN ansatt ON ansatt.ansattID = harrolle.ansattID


 SELECT dato, tid, count(billettID) AS solgt, stykkenavn FROM (forestilling INNER JOIN billett ON forestillingsdato = dato AND forestillingstid = tid AND stykkenavn = teaterstykke) GROUP by teaterstykke, dato, tid  ORDER BY solgt DESC;
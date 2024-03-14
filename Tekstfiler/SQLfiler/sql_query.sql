--Oppgave 5

SELECT DISTINCT teaterstykke.navn AS stykke, 
        ansatt.navn AS skuespiller, 
        rolle.rollenavn AS rolle

FROM teaterstykke
INNER JOIN akter ON teaterstykke.navn = akter.stykkenavn
INNER JOIN aktharrolle ON akter.aktnr = aktharrolle.aktnr
        AND akter.stykkenavn = aktharrolle.stykkenavn
INNER JOIN rolle ON rolle.rolleID = aktharrolle.rolleID
INNER JOIN harrolle ON rolle.rolleID = harrolle.rolleID
INNER JOIN ansatt ON ansatt.ansattID = harrolle.ansattID


oppgave 6

 SELECT teaterstykke, 
        dato, 
        tid,
        count(billettID) AS solgt 
 FROM (forestilling 
 FULL OUTER JOIN billett ON forestillingsdato = dato 
 AND forestillingstid = tid AND stykkenavn = teaterstykke) 
 GROUP by teaterstykke, dato, tid  
 ORDER BY solgt DESC;


 oppgave 7

Du skal lage et Pythonprogram (og SQL) som tar et skuespillernavn og finner 
hvilke skuespilllere de har spilt med i samme akt. Skriv ut navn på begge og 
hvilket skuespill det skjedde.


SELECT DISTINCT a1.navn AS skuespiller1, a2.navn AS skuespiller2, akter.stykkenavn AS skuespill
FROM ansatt AS a1
INNER JOIN harrolle AS hr1 ON a1.ansattID = hr1.ansattID
INNER JOIN rolle AS r1 ON hr1.rolleID = r1.rolleID
INNER JOIN aktharrolle AS ahr1 ON r1.rolleID = ahr1.rolleID
INNER JOIN akter ON ahr1.aktnr = akter.aktnr AND ahr1.stykkenavn = akter.stykkenavn
INNER JOIN aktharrolle AS ahr2 ON akter.aktnr = ahr2.aktnr AND akter.stykkenavn = ahr2.stykkenavn
INNER JOIN rolle AS r2 ON ahr2.rolleID = r2.rolleID
INNER JOIN harrolle AS hr2 ON r2.rolleID = hr2.rolleID
INNER JOIN ansatt AS a2 ON hr2.ansattID = a2.ansattID
WHERE a1.navn = 'skuespillernavn' AND a1.navn != a2.navn;
--Oppgave 3
SELECT dato, tid, teaterstykke 
FROM forestilling 
WHERE teaterstykke = ? 
ORDER BY dato, tid DESC;

select sete.rad, sete.omraade, sete.salnavn, count(billettID) as c 
from (billett INNER JOIN sete 
ON (billett.setenr = sete.setenr 
AND billett.rad = sete.rad 
AND sete.omraade = billett.omraade
 AND billett.salnavn = sete.salnavn)) 
INNER JOIN forestilling 
 ON billett.forestillingsdato = forestilling.dato
 AND billett.forestillingstid = forestilling.tid
 AND billett.stykkenavn = forestilling.teaterstykke
WHERE mobilnummer is NULL 
AND forestilling.dato = ?
AND forestilling.tid = ?
AND forestilling.teaterstykke = ?
 GROUP BY sete.rad, sete.omraade, sete.salnavn 
 HAVING c >=? ORDER BY sete.omraade, sete.rad ASC;

SELECT billettID from billett 
WHERE mobilnummer is NULL 
AND rad = ? 
AND omraade = ? 
AND salnavn = ? 
LIMIT ?;

UPDATE billett  SET 
kjopsdato = ?, 
kjopstid = ?, 
mobilnummer = ?, 
billettgruppe = ? 
WHERE billettID = ?;

SELECT pris FROM billettgruppe 
WHERE gruppe = (SELECT billettgruppe FROM billett WHERE billettID = ?) 
AND stykkenavn = ?;

SELECT mobilnummer FROM kundeprofil;

SELECT gruppe, pris 
FROM billettgruppe 
WHERE stykkenavn = ?;

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


--Oppgave 6
 SELECT teaterstykke, 
        dato, 
        tid,
        count(billettID) AS solgt 
 FROM (forestilling 
 FULL OUTER JOIN billett ON forestillingsdato = dato 
 AND forestillingstid = tid AND stykkenavn = teaterstykke) 
 GROUP by teaterstykke, dato, tid  
 ORDER BY solgt DESC;


 --Oppgave 7
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
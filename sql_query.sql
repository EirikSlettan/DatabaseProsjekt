--Oppgave 5

SELECT DISTINCT teaterstykke.navn AS yoyo, 
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

 SELECT dato, 
        tid, 
        count(billettID) AS solgt, 
        stykkenavn 
 
 FROM (forestilling 
 INNER JOIN billett ON forestillingsdato = dato 
 AND forestillingstid = tid AND stykkenavn = teaterstykke) 
 GROUP by teaterstykke, dato, tid  
 ORDER BY solgt DESC;


 oppgave 7

Du skal lage et Pythonprogram (og SQL) som tar et skuespillernavn og finner 
hvilke skuespilllere de har spilt med i samme akt. Skriv ut navn på begge og 
hvilket skuespill det skjedde.


SELECT DISTINCT a1.navn AS navn,
       
       akter.stykkenavn AS teaterstykke

FROM ansatt as a1
INNER JOIN harrolle as hr ON a1.ansattID = hr.ansattID
INNER JOIN rolle ON rolle.rolleID = hr.rolleID
INNER JOIN aktharrolle as ar ON ar.rolleID = rolle.rolleID
INNER JOIN akter ON akter.aktnr = ar.aktnr
        AND akter.stykkenavn = ar.stykkenavn




FROM skuespiller s1
JOIN akter a1 ON s1.skuespillerID = a1.skuespillerID
JOIN akter a2 ON a1.teaterstykkeID = a2.teaterstykkeID
JOIN skuespiller s2 ON a2.skuespillerID = s2.skuespillerID
JOIN teaterstykke t ON a1.teaterstykkeID = t.teaterstykkeID
WHERE s1.navn = 'Skuespiller A' AND s2.navn != 'Skuespiller A';
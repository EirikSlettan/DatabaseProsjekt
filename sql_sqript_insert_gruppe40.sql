--Kongsemnene
INSERT INTO teaterstykke VALUES ('Kongsemnene', 'Henrik Ibsen', 'V2024');

INSERT INTO forestilling VALUES ('2024-02-01', '19:00:00', 'Kongsemne');
INSERT INTO forestilling VALUES ('2024-02-02', '19:00:00', 'Kongsemne');
INSERT INTO forestilling VALUES ('2024-02-03', '19:00:00', 'Kongsemne');
INSERT INTO forestilling VALUES ('2024-02-05', '19:00:00', 'Kongsemne');
INSERT INTO forestilling VALUES ('2024-02-06', '19:00:00', 'Kongsemne');

INSERT INTO akter VALUES (1, 'Akt1', 'Kongsemnene');
INSERT INTO akter VALUES (2, 'Akt2', 'Kongsemnene');
INSERT INTO akter VALUES (3, 'Akt3', 'Kongsemnene');
INSERT INTO akter VALUES (4, 'Akt4', 'Kongsemnene');
INSERT INTO akter VALUES (5, 'Akt5', 'Kongsemnene');

INSERT INTO ansatt VALUES (1, 'Arturo Scotti', 'arturo.scotti@trondelagteater.no', 'fast ansatt', 1, 'skuespiller');
INSERT INTO ansatt VALUES (2, 'Ingunn Beate Strige Øyen', 'ingunn.beate.strige.øyen@trondelagteater.no',  'fast ansatt', 1, 'skuespiller');
INSERT INTO ansatt VALUES (3, 'Hans Petter Nilsen', 'hans.petter.nilsen@trondelagteater.no', 'fast ansatt', 1,'skuespiller');
INSERT INTO ansatt VALUES (4, 'Madeleine Brandtzæg Nilsen', 'madeleine.brandtzæg.nilsen@trondelagteater.no',  'fast ansatt',1, 'skuespiller');
INSERT INTO ansatt VALUES (5, 'Synnøve Fossum Eriksen', 'synnøve.fossum.eriksen@trondelagteater.no',  'fast ansatt',1, 'skuespiller');
INSERT INTO ansatt VALUES (6, 'Emma Caroline Deichmann', 'emma.caroline.deichmann@trondelagteater.no',  'fast ansatt',1, 'skuespiller');
INSERT INTO ansatt VALUES (7, 'Thomas Jensen Takyi', 'thomas.jensen.takyi@trondelagteater.no',  'fast ansatt',1, 'skuespiller');
INSERT INTO ansatt VALUES (8, 'Per Bogstad Gulliksen', 'per.bogstad.gulliksen@trondelagteater.no',  'fast ansatt', 1, 'skuespiller');
INSERT INTO ansatt VALUES (9, 'Isak Holmen Sørensen', 'isak.holmen.sørensen@trondelagteater.no',  'fast ansatt', 1,  'skuespiller');
INSERT INTO ansatt VALUES (10, 'Fabian Heidelberg Lunde', 'fabian.heidelberg.lunde@trondelagteater.no',  'fast ansatt', 1, 'skuespiller');
INSERT INTO ansatt VALUES (11, 'Emil Olafsson', 'emil.olafsson@trondelagteater.no',  'fast ansatt', 1, 'skuespiller');
INSERT INTO ansatt VALUES (12, 'Snorre Ryen Tøndel', 'snorre.ryen.tøndel@trondelagteater.no', 'fast ansatt', 1, 'skuespiller');
INSERT INTO ansatt VALUES (13, 'Yury Butusov', 'yury.butusov@trondelagteater.no', 'fast ansatt', 0, 'Regi og musikkutvelgelse');
INSERT INTO ansatt VALUES (14, 'Aleksandr Shishkin-Hokusai', 'aleksandr.shishkin-hokusai@trondelagteater.no', 'fast ansatt', 0, 'Scenografi og kostymer');
INSERT INTO ansatt VALUES (15, 'Eivind Myren', 'eivind.myren@trondelagteater.no',  'fast ansatt', 0, 'Lysdesign');
INSERT INTO ansatt VALUES (16, 'Mina Rype Stokke', 'mina.rype.stokke@trondelagteater.no', 'fast ansatt', 0, 'Dramaturg');

INSERT INTO jobbermed VALUES ('Kongsemnene', 1);
INSERT INTO jobbermed VALUES ('Kongsemnene', 2);
INSERT INTO jobbermed VALUES ('Kongsemnene', 3);
INSERT INTO jobbermed VALUES ('Kongsemnene', 4);
INSERT INTO jobbermed VALUES ('Kongsemnene', 5);
INSERT INTO jobbermed VALUES ('Kongsemnene', 6);
INSERT INTO jobbermed VALUES ('Kongsemnene', 7);
INSERT INTO jobbermed VALUES ('Kongsemnene', 8);
INSERT INTO jobbermed VALUES ('Kongsemnene', 9);
INSERT INTO jobbermed VALUES ('Kongsemnene', 10);
INSERT INTO jobbermed VALUES ('Kongsemnene', 11);
INSERT INTO jobbermed VALUES ('Kongsemnene', 12);
INSERT INTO jobbermed VALUES ('Kongsemnene', 13);
INSERT INTO jobbermed VALUES ('Kongsemnene', 14);
INSERT INTO jobbermed VALUES ('Kongsemnene', 15);
INSERT INTO jobbermed VALUES ('Kongsemnene', 16);

INSERT INTO rolle VALUES (1, 'Haakon Haakonson');
INSERT INTO rolle VALUES (2, 'Inga fra Vartejg (Haakons mor)');
INSERT INTO rolle VALUES (3, 'Skule jarl');
INSERT INTO rolle VALUES (4, 'Fru Ragnhild (Skules hustru)');
INSERT INTO rolle VALUES (5, 'Margrete (Skules datter)');
INSERT INTO rolle VALUES (6, 'Sigrid (Skules søster)');
INSERT INTO rolle VALUES (7, 'Ingebjørg');
INSERT INTO rolle VALUES (8, 'Biskop Nikolas');
INSERT INTO rolle VALUES (9, 'Gregorius Jonssønn');
INSERT INTO rolle VALUES (10, 'Paal Flida');
INSERT INTO rolle VALUES (11, 'Baard Bratte');
INSERT INTO rolle VALUES (12, 'Trønder');
INSERT INTO rolle VALUES (13, 'Jatgeir Skald');
INSERT INTO rolle VALUES (14, 'Dagdfinn Bonde');
INSERT INTO rolle VALUES (15, 'Peter (Prest og Ingebjørgs sønn)');

INSERT INTO harrolle VALUES (1, 1);
INSERT INTO harrolle VALUES (2, 2);
INSERT INTO harrolle VALUES (3, 3);
INSERT INTO harrolle VALUES (4, 4);
INSERT INTO harrolle VALUES (5, 5);
INSERT INTO harrolle VALUES (6, 6);
INSERT INTO harrolle VALUES (6, 7);
INSERT INTO harrolle VALUES (7, 8);
INSERT INTO harrolle VALUES (8, 9);
INSERT INTO harrolle VALUES (9, 10);
INSERT INTO harrolle VALUES (9, 12);
INSERT INTO harrolle VALUES (10, 11);
INSERT INTO harrolle VALUES (10, 12);
INSERT INTO harrolle VALUES (11, 13);
INSERT INTO harrolle VALUES (11, 14);
INSERT INTO harrolle VALUES (12, 15);

INSERT INTO aktharrolle VALUES (1, 1, 'Kongsemnene'); --RolleID, Aktnr, stykkenavn
INSERT INTO aktharrolle VALUES (1, 2, 'Kongsemnene'); 
INSERT INTO aktharrolle VALUES (1, 3, 'Kongsemnene');
INSERT INTO aktharrolle VALUES (1, 4, 'Kongsemnene');
INSERT INTO aktharrolle VALUES (1, 5, 'Kongsemnene');

INSERT INTO aktharrolle VALUES (11, 1, 'Kongsemnene'); 
INSERT INTO aktharrolle VALUES (11, 2, 'Kongsemnene'); 
INSERT INTO aktharrolle VALUES (11, 3, 'Kongsemnene');
INSERT INTO aktharrolle VALUES (11, 4, 'Kongsemnene');
INSERT INTO aktharrolle VALUES (11, 5, 'Kongsemnene');


INSERT INTO billettgruppe VALUES ('Ordinær', 450, 'Kongsemnene');
INSERT INTO billettgruppe VALUES ('Honnær', 380, 'Kongsemnene');
INSERT INTO billettgruppe VALUES ('Student', 280, 'Kongsemnene');
INSERT INTO billettgruppe VALUES ('Gruppe 10', 420, 'Kongsemnene');
INSERT INTO billettgruppe VALUES ('Gruppe honnør 10', 360, 'Kongsemnene');


--Storst av alt er kjaerligheten

INSERT INTO teaterstykke VALUES ('Storst av alt er kjaerligheten', 'Jonas Corell Petersen', 'V2024');

INSERT INTO forestilling VALUES ('2024-02-03', '18:30:00', 'Storst av alt er kjaerligheten');
INSERT INTO forestilling VALUES ('2024-02-06', '18:30:00', 'Storst av alt er kjaerligheten');
INSERT INTO forestilling VALUES ('2024-02-07', '18:30:00', 'Storst av alt er kjaerligheten');
INSERT INTO forestilling VALUES ('2024-02-12', '18:30:00', 'Storst av alt er kjaerligheten');
INSERT INTO forestilling VALUES ('2024-02-13', '18:30:00', 'Storst av alt er kjaerligheten');
INSERT INTO forestilling VALUES ('2024-02-14', '18:30:00', 'Storst av alt er kjaerligheten');

INSERT INTO akter VALUES (1, 'Hovedakt', 'Storst av alt er kjaerligheten');

INSERT INTO ansatt VALUES (17, 'Sunniva Du Mond Nordal', 'sunniva.du.mond.nordal@trondelagteater.no', 'fast ansatt', 1, 'skuespiller');
INSERT INTO ansatt VALUES (18, 'Jo Saberniak', 'jo.saberniak@trondelagteater.no', 'fast ansatt', 1, 'skuespiller');
INSERT INTO ansatt VALUES (19, 'Marte M. Steinholt', 'marte.m..steinholt@trondelagteater.no', 'fast ansatt', 1, 'skuespiller');
INSERT INTO ansatt VALUES (20, 'Tor Ivar Hagen', 'tor.ivar.hagen@trondelagteater.no', 'fast ansatt', 1, 'skuespiller');
INSERT INTO ansatt VALUES (21, 'Trond-Ove Skrødal', 'trond-ove.skrødal@trondelagteater.no', 'fast ansatt', 1, 'skuespiller');
INSERT INTO ansatt VALUES (22, 'Natalie Grøndahl', 'natalie.grøndahl@trondelagteater.no', 'fast ansatt', 1, 'skuespiller');
INSERT INTO ansatt VALUES (23, 'Tangen Åsmund Flaten', 'tangen.åsmund.flaten@trondelagteater.no', 'fast ansatt', 1, 'skuespiller');
INSERT INTO ansatt VALUES (24, 'Jonas Corell Petersen', 'jonas.corell.petersen@trondelagteater.no', 'fast ansatt', 0, 'Regi');
INSERT INTO ansatt VALUES (25, 'David Gehrt', 'david.gehrt@trondelagteater.no', 'fast ansatt', 0, 'Scenografi og kostymer');
INSERT INTO ansatt VALUES (26, 'Gaute Tønder', 'gaute.tønder@trondelagteater.no', 'fast ansatt', 0, 'Musikalsk ansvarlig');
INSERT INTO ansatt VALUES (27, 'Magnus Mikaelsen', 'magnus.mikaelsen@trondelagteater.no', 'fast ansatt', 0, 'Lysdesign');
INSERT INTO ansatt VALUES (28, 'Kristoffer Spender', 'kristoffer.spender@trondelagteater.no', 'fast ansatt', 0, 'Dramaturg');

INSERT INTO jobbermed VALUES ('Storst av alt er kjaerligheten', 17);
INSERT INTO jobbermed VALUES ('Storst av alt er kjaerligheten', 18);
INSERT INTO jobbermed VALUES ('Storst av alt er kjaerligheten', 19);
INSERT INTO jobbermed VALUES ('Storst av alt er kjaerligheten', 20);
INSERT INTO jobbermed VALUES ('Storst av alt er kjaerligheten', 21);
INSERT INTO jobbermed VALUES ('Storst av alt er kjaerligheten', 22);
INSERT INTO jobbermed VALUES ('Storst av alt er kjaerligheten', 23);
INSERT INTO jobbermed VALUES ('Storst av alt er kjaerligheten', 24);
INSERT INTO jobbermed VALUES ('Storst av alt er kjaerligheten', 25);
INSERT INTO jobbermed VALUES ('Storst av alt er kjaerligheten', 26);
INSERT INTO jobbermed VALUES ('Storst av alt er kjaerligheten', 27);
INSERT INTO jobbermed VALUES ('Storst av alt er kjaerligheten', 28);


INSERT INTO rolle VALUES (16, 'Sunniva Du Mond Nordal');
INSERT INTO rolle VALUES (17, 'Jo Saberniak');
INSERT INTO rolle VALUES (18, 'Marte M. Steinholt');
INSERT INTO rolle VALUES (19, 'Tor Ivar Hagen');
INSERT INTO rolle VALUES (20, 'Trond-Ove Skrødal');
INSERT INTO rolle VALUES (21, 'Natalie Grøndahl');
INSERT INTO rolle VALUES (22, 'Tangen Åsmund Flaten');

INSERT INTO harrolle VALUES (17, 16);
INSERT INTO harrolle VALUES (18, 17);
INSERT INTO harrolle VALUES (19, 18);
INSERT INTO harrolle VALUES (20, 19);
INSERT INTO harrolle VALUES (21, 20);
INSERT INTO harrolle VALUES (22, 21);
INSERT INTO harrolle VALUES (23, 22);

INSERT INTO billettgruppe VALUES ('Ordinær', 350, 'Storst av alt er kjaerligheten');
INSERT INTO billettgruppe VALUES ('Honnær', 300, 'Storst av alt er kjaerligheten');
INSERT INTO billettgruppe VALUES ('Student', 220, 'Storst av alt er kjaerligheten');
INSERT INTO billettgruppe VALUES ('Barn', 220, 'Storst av alt er kjaerligheten');
INSERT INTO billettgruppe VALUES ('Gruppe 10', 320, 'Storst av alt er kjaerligheten');
INSERT INTO billettgruppe VALUES ('Gruppe honnør 10', 270, 'Storst av alt er kjaerligheten');














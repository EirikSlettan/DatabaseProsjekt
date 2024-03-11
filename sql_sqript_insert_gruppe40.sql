create table kundeprofil(
    mobilnummer varchar(8) not null,
    navn varchar(30) not null,
    adresse varchar(50) not null,
    constraint kundeprofil_pk primary key (mobilnummer)
);

create table billettkjop(
    dato DATE not null, 
    tid TIME not null,
    mobilnummer varchar(8) not null, 
    constraint billettkjop_fk foreign key (mobilnummer) references kundeprofil(mobilnummer)
    on update cascade
	on delete cascade,

    constraint billettkjop_pk primary key (dato, tid, mobilnummer)
);

create table billett(
    billettID integer not null,
    kjopsdato date not null,
    kjopstid time not null,
    mobilnummer integer not null,
    billettgruppe varchar(30) not null,
    setenr integer not null,
    rad integer not null, 
    omraade varchar(50) null,
    salnavn varchar(40) not null,

    forestillingsdato date not null,
    forestillingstid time not null,
    stykkenavn varchar(30),

    constraint billett_fk1 foreign key (billettgruppe) references billettgruppe(gruppe)
    on update cascade
	on delete cascade,
    constraint billett_fk2 foreign key (kjopstid, kjopsdato, mobilnummer) references billettkjop(dato, tid, mobilnummer)
    on update cascade
	on delete cascade,
    constraint billett_fk3 foreign key (forestillingsdato, forestillingstid, stykkenavn) references forestilling(dato, tid, navn)
    on update cascade
	on delete cascade,
    constraint billett_fk4 foreign key (setenr, rad, omraade, salnavn) references sete(setenr, rad, omraade, salnavn)
    constraint billett_pk primary key (billettID)
);

create table sete(
    setenr integer not null,
    rad integer not null, 
    omraade varchar(50) null,
    salnavn varchar(40) not null,

    constraint sete_fk1 foreign key (salnavn) references sal(navn)
    on update cascade
	on delete cascade,


    constraint salnavn_pk primary key (setenr, rad, omraade, salnavn)
);

create table sal(
    navn varchar(30) not null,
    plasser integer not null,
    stykkenavn varchar(30) not null,
    constraint sal_fk foreign key (stykkenavn) references teaterstykke(navn),
    constraint sal_pk primary key (navn)
);

create table billettgruppe(
    gruppe varchar(30) not null,
    pris integer not null,
    constraint billettgruppe_pk primary key (gruppe)
);

create table harbillettgruppe(
    gruppe varchar(30) not null, 
    stykkenavn varchar(30) not null,

    constraint harbillettgruppe_fk1 foreign key (gruppe) references billettgruppe(gruppe)
    on update cascade
	on delete cascade,

    constraint harbillettgruppe_fk2 foreign key (stykkenavn) references teaterstykke(navn)
    on update cascade
	on delete cascade
);

create table forestilling(
    dato DATE not null, 
    tid TIME not null,
    teaterstykke varchar(30) not null,
    constraint forestilling_fk foreign key (teaterstykke) references teaterstykke(navn)
    on update cascade
	on delete cascade,

    constraint forestilling_pk primary key (dato, tid, teaterstykke)
);

create table teaterstykke(
	navn varchar(30) not null,
	forfatter varchar(30) not null,
    sesong varchar(30) not null,
	constraint teaterstykke_pk primary key (navn)
);


create table jobbermed(
    stykkenavn varchar(30) not null,
    ansattID integer not null, 

    constraint jobbermed_fk1 foreign key (stykkenavn) references teaterstykke(navn)
    on update cascade
	on delete cascade,

    constraint jobbermed_fk2 foreign key (ansattID) references ansatt(ansattID)
    on update cascade
	on delete cascade
);


create table akter(
    aktnr integer not null,
    navn varchar(30) not null,
    stykkenavn varchar(30) not null,

    constraint akter_fk foreign key (stykkenavn) references teaterstykke(navn)
    on update cascade
	on delete cascade,

    constraint akter_pk primary key (stykkenavn, aktnr)
);

create table aktharrolle(
    rolleID integer not null, 
    aktnr integer not null, 
    stykkenavn varchar(30) not null,

    constraint aktharrolle_fk1 foreign key (rolleID) references rolle(rolleID)
    on update cascade
	on delete cascade,
    constraint aktharrolle_fk2 foreign key (aktnr, stykkenavn) references akter(aktnr, stykkenavn)
    on update cascade
	on delete cascade
    constraint aktharrolle_pk primary key (rolleID, aktnr, stykkenavn)
);

create table rolle(
    rolleID integer not null,
    rollenavn varchar(30) not null,
    constraint rolle_pk primary key (rolleID)
);

create table harrolle( 
    ansattID integer not null,
    rolleID integer not null, 

    constraint harrolle_fk1 foreign key (rolleID) references rolle(rolleID)
    on update cascade
	on delete cascade,
    constraint harrolle_fk1 foreign key (ansattID) references ansatt(ansattID)
    constraint harrolle_pk primary key (ansattID, rolleID)
);


create table ansatt(
    ansattID integer not null, 
    navn varchar(30) not null, 
    epost varchar(30) not null,
    ansattstatus varchar(30) not null,
    skuespiller boolean not null, 
    arbeidsoppgave varchar(30) null,

    constraint ansatt_pk primary key (ansattID)
);

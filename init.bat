echo(----------Fjerner gammel database, lager ny-------------)
del teater_database.db
type nul >  teater_database.db
sqlite3 teater_database.db < sqlfiler/schema.sql
sqlite3 teater_database.db < sqlfiler/insert_known_values.sql
py pythonfiler/lese_fra_fil.py

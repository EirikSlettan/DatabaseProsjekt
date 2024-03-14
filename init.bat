echo(----------Fjerner gammel database, lager ny-------------)
del test1.db
type nul >  test1.db
sqlite3 test1.db < SQLfiler/sql_sqript_setup_gruppe40.sql
sqlite3 test1.db < SQLfiler/sql_sqript_insert_gruppe40.sql
py Pythonfiler/stoler.py

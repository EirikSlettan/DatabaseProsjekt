echo(----------Fjerner gammel database, lager ny-------------)
del test.db
touch test.db
sqlite3 test.db < sql_sqript_setup_gruppe40.sql

echo(----------Fjerner gammel database, lager ny-------------)
del test1.db
type nul >  test1.db
sqlite3 test1.db < sql_sqript_setup_gruppe40.sql
py stoler.py

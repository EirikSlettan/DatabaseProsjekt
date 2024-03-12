rm database.db
touch database.db
sqlite3 database.db < sql_sqript_setup_gruppe40.sql
sqlite3 database.db < sql_sqript_insert_gruppe40.sql
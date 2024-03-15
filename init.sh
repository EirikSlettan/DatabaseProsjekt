rm teater_database.db
touch teater_database.db
sqlite3 teater_database.db < sqlfiler/schema.sql
sqlite3 database.db < sqlfiler/insert_known_values.sql
python3 pythonfiler/lese_fra_fil.py
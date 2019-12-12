from sql_api import Database


rpg = Database.sqlite('../module1-introduction-to-sql/rpg_db.sqlite3', 'RPG')

login_info = ('rajje.db.elephantsql.com','xewuuake','fs0ufo508XkoVYj2dmrdZvyym8ijLeyr')

tita = Database.psycopg2(login_info[0], login_info[1], login_info[1], login_info[2])

tita.sqlite_to_ps2('charactercreator_character', rpg, indexes_to_keep=(1,3), name_position=1)
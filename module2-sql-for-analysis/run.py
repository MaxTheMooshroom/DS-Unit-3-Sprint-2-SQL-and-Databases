from sql_api import Database

rpg = Database('../module1-introduction-to-sql/rpg_db.sqlite3', 'RPG')

#print(rpg.table_info('charactercreator_character'))

url = 'rajje.db.elephantsql.com'
db_name = 'xewuuake'
user = db_name
passw = 'HaSsoiRh1Cl2U8JbGpDTNIU4civG_ug-'

db = Database(_lib='ps2', dir=url, _db_name=db_name, _username=user, _password=passw)

db.drop_table('charactercreator_character')

db.sqlite_to_ps2(rpg, 'charactercreator_character', name_position=1)

for row in db.get_all('charactercreator_character'):
    print(row)

#INSERT INTO charactercreator_character (name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES ('Aliquam n', 0, 0, 10, 1, 1, 1, 1);






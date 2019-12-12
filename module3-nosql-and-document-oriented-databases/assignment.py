import pymongo as pym
import sqlite3 as sql3
import pprint

rpg = sql3.connect('../module1-introduction-to-sql/rpg_db.sqlite3')

rpg_tables = ['']


username = 'MTM'
password = 'yWxlVd2WZ3mLGCCu'

url = f'mongodb+srv://{username}:{password}@cluster0-bq5e2.mongodb.net/test?retryWrites=true&w=majority'


client = pym.MongoClient(url)
db = client['rpg']

rpg_cursor = rpg.cursor()
table_data = rpg_cursor.execute(f'SELECT * FROM charactercreator_character;').fetchall()
rpg_cursor.close()
rpg.commit()

rpg_cursor = rpg.cursor()
table_column_data = rpg_cursor.execute(f'PRAGMA table_info(charactercreator_character);').fetchall()
rpg_cursor.close()

init_data = list(map(lambda x: x[1] + ' ' + x[2], table_column_data))
names = list(map(lambda x: x[1], table_column_data[1:]))
#print(names)

db_data = db['charactercreator_character']
for data in table_data:
    dict = {}
    data_transformed = data[1:]
    for j, name in enumerate(names):
        dict[name] = data_transformed[j]
    #print(dict)
    db_data.insert_one(dict)

for post in db_data.find():
    pprint.pprint(post)



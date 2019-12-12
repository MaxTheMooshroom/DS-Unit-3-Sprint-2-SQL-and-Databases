import pymongo as pym
import sqlite3 as sql3

rpg = sql3.connect('../module1-introduction-to-sql/rpg_db.sqlite3')

rpg_tables = ['']


username = 'MTM'
password = 'yWxlVd2WZ3mLGCCu'

url = f'mongodb+srv://{username}:{password}@cluster0-bq5e2.mongodb.net/test?retryWrites=true&w=majority'


client = pym.MongoClient(url)
db = client['test-db']
collection = db['test-coll']
post = {"author": "Max",
        "text": "My first mongodb post!",
        "tags": ["mongodb", "python", "pymongo"]}

posts = db.posts # test
post_id = posts.insert_one(post).inserted_id # test
print(post_id) # test


rpg_cursor = rpg.cursor()
table_data = rpg_cursor.execute(f'SELECT * FROM charactercreator_character;').fetchall()
rpg_cursor.close()
rpg.commit()

for result in table_data:
    print(result[1:])

rpg_cursor = rpg.cursor()
table_column_data = rpg_cursor.execute(f'PRAGMA table_info(charactercreator_character);').fetchall()
rpg_cursor.close()

init_data = list(map(lambda x: x[1] + ' ' + x[2], table_column_data))
names = list(map(lambda x: x[1], table_column_data[1:]))
print(names)

db_data = db['data']
for data in table_data:
    dict = {}
    data_transformed = data[1:]
    for j, name in enumerate(names):
        dict[name] = data_transformed[j]
    print(dict)
    db_data.insert_one(dict)

#db_data.get_many()?



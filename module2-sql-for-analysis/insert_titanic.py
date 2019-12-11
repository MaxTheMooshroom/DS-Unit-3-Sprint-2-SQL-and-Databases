import psycopg2 as ps2
import pandas as pd

url = 'rajje.db.elephantsql.com'
db_name = 'xewuuake'
user = db_name
passw = 'HaSsoiRh1Cl2U8JbGpDTNIU4civG_ug-'

conn = ps2.connect(dbname=db_name, user=user, password=passw, host=url)
titanic = pd.read_csv('titanic.csv')

make_table = """
CREATE TABLE Data (
    "index" SERIAL PRIMARY KEY,
    "Survived" INTEGER,
    "Pclass" INTEGER,
    "Name" TEXT,
    "Sex" TEXT,
    "Age" REAL,
    "Siblings_or_Spouses_Aboard" INTEGER,
    "Parents_or_Children_Aboard" INTEGER,
    "Fare" REAL
);
"""

insert_template = """INSERT INTO Data
                  ("Survived", "Pclass", "Name", "Sex", "Age", "Siblings_or_Spouses_Aboard", "Parents_or_Children_Aboard", "Fare")
                  VALUES"""

cursor = conn.cursor()
cursor.execute('DROP TABLE Data')
cursor.execute(make_table)

for i in range(0, titanic.shape[0]):
    flat = ''
    for arg in [str(titanic.iloc[i][j]).replace(' ', '_') + ', ' for j in range(0,8)]:
        flat += arg
    insert = insert_template + ' (' + flat[:-2].strip() + ');'

    print(insert)
    cursor.execute(insert)
conn.commit()

results = cursor.execute('SELECT * FROM Data;').fetchall()
cursor.close()
print(results)










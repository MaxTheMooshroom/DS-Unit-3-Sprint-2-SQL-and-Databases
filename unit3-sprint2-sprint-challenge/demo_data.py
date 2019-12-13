import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

cursor = conn.cursor()

try:
    cursor.execute('DROP TABLE demo')
except:
    print('Table doesn\'t exist. Creating now...\n')

cursor.execute("""CREATE TABLE demo (
s varchar(1),
x INTEGER,
y INTEGER
);
""")

cursor.execute('INSERT INTO demo VALUES ("g", 3, 9);')
cursor.execute('INSERT INTO demo VALUES ("v", 5, 7);')
cursor.execute('INSERT INTO demo VALUES ("f", 8, 7);')

for row in cursor.execute('SELECT * FROM demo;').fetchall():
    print(row)


print('\nCount how many rows you have - it should be 3: ' + str(cursor.execute('SELECT count(*) FROM demo;').fetchall()[0][0]))

threshold = cursor.execute('SELECT count(*) FROM demo AS t WHERE t.x > 5 AND t.y > 5;').fetchall()[0][0]
print('How many rows are there where both x and y are at least 5: ' + str(threshold))

y_unique = cursor.execute('SELECT count(DISTINCT y) FROM demo;').fetchall()[0][0]
print('How many unique values of y are there: ' + str(y_unique))

cursor.close()
conn.commit()

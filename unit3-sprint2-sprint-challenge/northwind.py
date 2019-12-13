import sqlite3
import pandas as pd

conn = sqlite3.connect('northwind_small.sqlite3')

cursor = conn.cursor()

#table_names = [name[0] for name in cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall()]

#for name in table_names:
#    print(name)

#print('\n' + str(cursor.execute('SELECT sql FROM sqlite_master WHERE name="Product";').fetchall()[0][0]))
prices = [item[0] for item in cursor.execute('SELECT ProductName FROM product ORDER BY UnitPrice DESC;').fetchall()[:10]]

print('\nWhat are the ten most expensive items (per unit price) in the database:\n\n' + str(prices))



dates = cursor.execute('SELECT HireDate, BirthDate FROM Employee;').fetchall()
hires = [pd.to_datetime(date[0]) for date in dates]
births = [pd.to_datetime(date[1]) for date in dates]

hiring_ages = []
for i in range(len(hires)):
    hiring_ages.append(int(str((hires[i] - births[i]) / 365)[:2]))


print('\n\nWhat is the average age of an employee at the time of their hiring: ' + str(sum(hiring_ages) / len(hiring_ages)))

#print('\n' + str(cursor.execute('SELECT sql FROM sqlite_master WHERE name="Supplier";').fetchall()[0][0]))

query = """SELECT Product.ProductName, Supplier.CompanyName
FROM Product INNER JOIN Supplier ON Product.SupplierID = Supplier.Id
;""" # ORDER BY Product.UnitPrice DESC
prods = cursor.execute(query).fetchall()[:10]

print('\nWhat are the ten most expensive items (per unit price) in the database and their suppliers:')
for prod in prods:
    print(f'{prod[0]}: {prod[1]}')
print('\n')

largestID = cursor.execute("""
SELECT  CategoryID,
COUNT(CategoryID) AS value_occurrence 
FROM Product
GROUP BY CategoryID
ORDER BY value_occurrence DESC
LIMIT 1;
""").fetchall()[0][0]

largest_cate = cursor.execute(f'SELECT CategoryName FROM Category WHERE Id = {largestID}').fetchall()[0][0]

print(f'What is the largest category: {largest_cate}')


cursor.close()
conn.commit()


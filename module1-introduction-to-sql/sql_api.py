""" Written by MaxTheMooshroom! http://github.com/MaxTheMooshroom
"""

import sqlite3
import pandas as pd

class Database:
    """ 
    container class to streamline interactions between python and sql.

    dir (string) - directory of the .db file
    """

    connection = None
    file = None
    table_params = {}

    def __init__(self, dir):
        self.file = dir
        self.open()
        
    def open(self):
        self.connection = sqlite3.connect(self.file)

    def read_csv(self, dir, table_name):
        df = pd.read_csv(dir)
        df.to_sql(table_name, self.connection)
        self.table_params[table_name] = df.columns
        return self

    def query(self, input, close_q=True):
        """ perform raw execution on stored connection.
        """
        cursor = self.connection.cursor()
        results = cursor.execute(input)

        if close_q is True:
            cursor.close()

        self.connection.commit()
        return results

    def fetchall(self, input):
        q = self.query(input, False)
        result = q.fetchall()
        q.close()
        return result

    def create_table(self, name, args):
        """ 
        helper function for creating a new table.
        
        name (string) - name of the table; eg: 'toy'
        args (string) - column names and types; eg: 'name VARCHAR(30), size int'
        """

        my_query = 'CREATE TABLE ' + name + ' (' + args + ');'
        self.table_params[name] = args
        return self.query(my_query)

    def insert_data(self, table_name, args, vals):
        """ 
        helper function for inserting a new row to a table.

        table_name (string) - name of the target table; eg: 'toy'
        args (string) - column names and types; eg: 'name, size'
        values (string) - values to be inserted for each specified column; eg: '"teddy bear", 10'
        """
        my_query = 'INSERT INTO ' + table_name + ' (' + args + ') VALUES (' + vals + ');'
        return self.query(my_query)

    def get_all(self, table_name):
        """ 
        helper function for returning all rows in a table.

        table_name (string) - name of table to fetch values from; eg: 'toy'
        """
        my_query = 'SELECT * FROM ' + table_name + ';'
        q = self.query(my_query, False)
        result = q.fetchall()
        q.close()
        return result

    def get_name(self):
        my_query = 'SELECT * FROM Sys.Databases'
        return self.query(my_query)

    def get_tables(self):
        """
        DOES NOT WORK
        helper function to return list of tables in database.
        """
        #my_query = f'SELECT * FROM {}.INFORMATION_SCHEMA.TABLES;'
        #return self.query(my_query)
        pass

    def close(self):
        """ helper function to close the connection.
        """
        return self.connection.close()
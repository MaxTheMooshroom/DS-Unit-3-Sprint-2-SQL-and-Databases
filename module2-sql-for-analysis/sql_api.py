""" Written by MaxTheMooshroom! http://github.com/MaxTheMooshroom
"""

import sqlite3
import pandas as pd
import psycopg2 as ps2
#import pickle

class WrongTypeException(Exception):
    """ If the database is the wrong type """
    def print_error():
        print('Wrong lib type!')

class Database:
    """ 
    container class to streamline interactions between python and sql.

    dir (string) - directory of the .db file
    """

    connection = None
    loc = None
    table_params = {}
    lib = None # default sqlite3

    def __init__(self, dir, _db_name, _lib='sqlite3', _username=None, _password=None):
        self.loc = dir
        self.lib = _lib
        self.db_name = _db_name
        self.username = _username
        self.password = _password
        try:
            #self.table_params = pickle.load(open(_db_name + '.sav', 'rb'))
            pass
        except:
            print('Failed to load ' + _db_name + '.sav')
        self.open()

    def open(self):
        """ open a connection using the file variable.
        """
        if self.lib.lower() == 'sqlite3':
            self.connection = sqlite3.connect(self.loc)
        elif self.lib.lower() == 'psycopgp2' or self.lib.lower() == 'ps2':
            self.connection = ps2.connect(dbname=self.db_name, user=self.username, password=self.password, host=self.loc)

    def read_csv(self, dir, table_name):
        """ read a csv file and save it as a table to this Database.
        dir (string) - directory of the csv you're reading.
        table_name (string) - the name of the table the csv will be saved as.
        """
        df = pd.read_csv(dir)
        df.to_sql(table_name, self.connection)
        self.table_params[table_name] = df.columns
        return self

    def update_table_params(self, table_name, params):
        self.table_params[table_name] = params
        #pickle.dump(self.table_params, open(self.db_name + '.sav', 'wb'))

    def query(self, input, close_c=True):
        """ perform raw execution on stored connection.
        input (string) - the query to execute.
        close_c (bool) - default: True. Whether to close the cursor or not
        """
        cursor = self.connection.cursor()
        results = cursor.execute(input)

        if close_c is True:
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
        self.update_table_params(name, args)
        return self.query(my_query)

    def insert_data(self, table_name, args, vals):
        """ 
        helper function for inserting a new row to a table.

        table_name (string) - name of the target table; eg: 'toy'
        args (string) - column names; eg: 'name, size'
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
        """ ONLY WORKS FOR PS2
        helper function to return the database's name
        """
        return self.db_name

    def table_info(self, table_name):
        return self.fetchall(f'PRAGMA table_info({table_name});')

    def sqlite_to_ps2(self, db, table_name, name_position=1, new_table_name=None):
        """ 
        helper function to load an sqlite table as a psycopg2 table
        db (Database) - another instance of this class that is sqlite that contains the table 
            you wish to transfer.
        table_name (string) - the name of the table you want to transfer
        indexes_to_keep (iterable) - iterable of row indexes to keep
        """
        try:
            if new_table_name is None:
                new_table_name = table_name

            if db.lib != 'sqlite3':
                raise WrongTypeException

            #-------------------------------------------
            # Table Creation

            types = ['SERIAL PRIMARY KEY, ']

            old_info = db.table_info(table_name)
            names = [str(col[name_position]) + ' ' for col in old_info]     # column names
            types += [str(col[2]) + ', ' for col in old_info[1:]]           # column types
            zipped = [z[0] + z[1] for z in zip(names, types)]               # ['colName type1, name2 type2, etc']
            args = ''
            for arg in zipped: # convert array of names and types to single string
                args += arg
            args = args[:-2] # remove trailing ', '

            self.create_table(new_table_name, args) # table's name, 'name VARCHAR(30), size int'

            #-------------------------------------------
            # Table Filling

            old_data = [data[1:] for data in db.get_all(table_name)] # remove internal indexing
            flat_names = ''
            for name in [str(col[name_position]) + ', ' for col in old_info[1:]]:
                flat_names += name
            flat_names = flat_names[:-2]

            for row in old_data:
                value = str(row)[1:-1]
                #my_query = "INSERT INTO " + table_name + " (" + flat_names + ") VALUES (" + value + ");"
                #print(my_query)
                self.insert_data(table_name, flat_names, value)



        except WrongTypeException:
            WrongTypeException.print_error()

    def get_tables(self):
        """
        DOES NOT WORK
        helper function to return list of tables in database.
        """
        #my_query = f'SELECT * FROM {}.INFORMATION_SCHEMA.TABLES;'
        #return self.query(my_query)
        pass

    def drop_table(self, table_name):
        self.query('DROP TABLE ' + table_name)

    def close(self):
        """ helper function to close the connection.
        """
        self.connection.commit()
        self.connection.close()

    def restart(self):
        self.close()
        self.open()






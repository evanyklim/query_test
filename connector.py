import pymysql
# import csv
import configparser
import pandas as pd
import numpy as np
config = configparser.ConfigParser()
config.read('config.ini')

# read config parameters into local constants
SQLHOST = config['mysql']['host']
SQLPORT = config['mysql']['port']
SQLUSER = config['mysql']['user']
SQLPASSWORD = config['mysql']['passwd']
SQLDATABASE = config['mysql']['db']

class Connector:
    '''MySQL connection class'''

    def __init__(self):
        '''initialize connection and cursor'''
        self.connection = pymysql.connect(
            host=SQLHOST,
            port=int(SQLPORT),
            user=SQLUSER,
            passwd=SQLPASSWORD,
            db=SQLDATABASE)

    def run_query(self, query_str, sqlargs={}):
        ''' run query, write results to csv and return the rows returned'''
        with self.connection.cursor() as cursor:
            numrows = cursor.execute(query_str, args=sqlargs)
            # with open('output_sql.csv', 'w') as csvfile:
            #     writer = csv.
            # print(cursor.fetchall())
            return 'number of rows returned: %s' % numrows

    def read_query(self, filename):
        '''open filename, read query string and store in self.next_query'''
        with open(filename) as f:
            return f.read()

    def execute_query(self, filename):
        query_string = self.read_query(filename)
        return self.run_query(query_string)

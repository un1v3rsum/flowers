import sqlite3
from get_data import newdata

#make a connection to database
connection = sqlite3.connect('db.sqlite3')
#import dataframe to database
newdata.to_sql(name='flowers_flower',con=connection, if_exists='replace', index=False)
connection.close()



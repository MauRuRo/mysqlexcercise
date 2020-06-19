import os
import datetime
import pymysql

# get username cloud9 workspace
# modify if runn on other envirentont

username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        list_of_names = ["Fred", "Fred"]
        # prepare a string with the same number of placeholders as in list of names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("delete from Friends where name in ({})".format(format_strings), list_of_names)
        connection.commit()
    # Note that the above will display a waring (not error) if the
    # table already exists.
finally:
    # Close the connection, regardless of whether the above was succesful
    connection.close()


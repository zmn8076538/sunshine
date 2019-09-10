import MySQLdb

connection = MySQLdb.connect(
                            host = '148.70.30.54',
                            user = 'root',
                            password = 'Zmn19880723@',
                            db = 'sunshine',
                            charset = 'utf8'
                            )

connection.autocommit(True)

cursor = connection.cursor()
import MySQLdb

connection = MySQLdb.connect(
                            host = '47.101.179.114',
                            user = 'root',
                            password = 'Zmn19880723@',
                            db = 'sunshine',
                            charset = 'utf8'
                            )

connection.autocommit(True)

cursor = connection.cursor()
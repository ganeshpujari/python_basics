import pymysql.cursors

def db_connection():
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='mysql',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    print("connect successful!!")

    connection.close()
db_connection()

class DBManager(object):

    def __init__(self, host, user, password,db ):
        self._host=host
        self._user=user
        self._password=password
        self._db=db
        self.connection = None

    def __enter__(self):
        self.connection = pymysql.connect(host=self._host,
                                     user=self._user,
                                     password=self._password,
                                     db=self._db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        if self.connection:
            print("connected .......!")
        else:
            print("Error in connection")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
            print(" connection closing done")
        else:
            print("Connection does not exist")

# obj=DBManager('127.0.0.1','root','root','mysql')

with DBManager('127.0.0.1','root','root','mysql') as d_b_manager:
    print("connection call")
import mysql
from mysql.connector import Error
#밑에 config 파일을 바꾸면 다른 DB에 접속가능
config = {
    #사용할 DB 정보 입력
    #"user": "",
    # "password": "",
    # "host": "",
    # "database": "",
    # "port": ''
}

#밑에 쿼리문들을 바꾸면 다른 데이터를 불러올 수 있음.
select_sql = "SELECT FROM "
select_sql_pw = "SELECT FROM "
select_sql_salt = "SELECT FROM "
select_join_sql = "SELECT  FROM "
select_sql_where = select_sql + "where "


class SAHDao():
    def select_item(self, ProductCode=None):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute(select_sql) if ProductCode is None else cursor.execute(select_sql_where, (ProductCode,))
            res = []
            [res.append(row) for row in self.__iter_row(cursor, 7)]
            return res

        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def select_item2(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute(select_sql)
            res = []
            [res.append(row) for row in self.__iter_row(cursor, 7)]
            return res

        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def select_item_salt(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute(select_sql_salt)
            res = []
            [res.append(row) for row in self.__iter_row(cursor, 7)]
            return res

        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def select_item_pw(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute(select_sql_pw)
            res = []
            [res.append(row) for row in self.__iter_row(cursor, 7)]
            return res

        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def select_item_join(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute(select_join_sql)
            res = []
            [res.append(row) for row in self.__iter_row(cursor, 7)]
            return res

        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def __iter_row(self, cursor, size=7):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row

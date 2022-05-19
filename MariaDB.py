import mariadb
import sys
class Mariadb():
    def __init__(self,db):
        try:
            self.conn = mariadb.connect(
            user="root",
            password="109ab0716",
            host="127.0.0.1",
            port=3306,
            database=db
            )
            self.conn.autocommit = False
            print(f"已進入資料庫 {self.conn.database}")
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
        self.cur = self.conn.cursor()

    def sql(self,sql):
        try:
            self.cur.execute(sql)
            print("以下為查詢結果:\n")
            if not sql[0:6]=="select":
                self.conn.commit()
        except mariadb.Error as e:
            print(f"Error: {e}")

    def getcur(self):
        return self.cur


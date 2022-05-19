from MariaDB import Mariadb

if __name__ == "__main__":
    maria = Mariadb("train")
    maria.sql("select * from name_info")
    for (id, id2) in maria.getcur():
        print(id,id2)




        
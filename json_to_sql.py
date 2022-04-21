# 21.04.2022
# Burak GÜN 
# burak.gun@hotmail.com



from asyncio.windows_events import NULL
from pickle import FALSE, TRUE
import sys
from urllib.request import AbstractDigestAuthHandler
import mysql.connector
from mysql.connector import Error
import json



# ilk önce server'a bağlanmayı dene, eğer hata olmazsa veritabanına bağlan.
# Bunu yapmaya gerek olmayabilir.Sadece tek try-except içinde de yapılabilir.
def connect_to_database(_host, _user, _password, _database):

    connection_status = False

    try:
        
        connection = mysql.connector.connect(
        host=_host,
        user=_user,
        password=_password)
        
        print(f'Connected to Server:{_user}@{_host} ')

        try:
            connection = mysql.connector.connect(
            host=_host,
            user=_user,
            password=_password,
            database=_database)
            
            print(f'Connected to Database:{_database}')

            cursor = connection.cursor(buffered=True)

            connection_status = True

        except Error as Err:
            print(f"Not Connected to Database:{_database}: '{Err}'")

           
    except Error as Err:
        print(f"Not Connected to Server:{_host}: '{Err}'")
        
    
    return connection_status




def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")  

    


    
    





if __name__ == "__main__": 

    config = {
        'host'     : 'localhost',
        'user'     : 'root',
        'password' : 'burak',
        'database' : 'school'

    }

    connection = mysql.connector.connect(**config)
    connection.autocommit = True

    cursor = connection.cursor(buffered=True)

    #  connection_status = connect_to_database(_host, _user, _password, _database)

    # eğer bağlantı uygunsa veri tabanında DDL DML işlemleri gerçekleştir.
    if connection :
        
        
        #-----------ÇOK ÖNEMLİ NOT---------#
        # string içerisinde '' veya "" yapmak için, dizinin tanıtıldığı karakterin dışındaki işareti yapmamız gerekiyor.
        # şöyleki " x = '5' " --> çift tırnak arasında olduğu için, değer tek tırnak içerisinde
        # veya ' x = "10" '  --> tek tırnak arasında olduğu için, çift tırnak arasına yazıldı.

        query = [
         'SHOW DATABASES', 
         'USE school', 
         'SHOW Tables', 
         "SELECT * FROM teacher WHERE language_1 = '{}' AND language_2 ='{}' ".format('ENG', 'IRI'),
         
         
        ]

        query_select_all = 'SELECT * FROM teacher'

        query_insert = (
            "INSERT INTO teacher(teacher_id, first_name, last_name ,language_1, language_2 , tax_id ,phone_no)"
            "VALUES( %s, %s, %s, %s, %s, %s, %s)"
         )
        
        insert_data = (44, 'nix', 'weat', 'ENG', 'TR', 789, '+41232')

        #-----------ÇOK ÖNEMLİ NOT---------#
        # INSERT, DELETE, and UPDATE ifadelerinden sonra commit kullanmak zorundasın (autocommit yapmadıysan)
        # connection = mysql.connector.connect(**config)
        # connection.autocommit = True

        cursor.execute(query_insert,insert_data)
        # connection.commit()

        # to retrieve data from Tuple Tuple[a:b]

        for result  in cursor:
            print(result)
            # print(x[0:3])
            # print( "id:{}  ".format(x) )
        
        # print( query[4] )
        
        # for x in  range ( len(query) ):
        #     cursor.execute(query[x], params=None, multi=False)

        #     for result in cursor:
        #         print(result)
     


            
        cursor.execute(query_select_all, params=None, multi=False)

        # # # to retrieve data from Tuple Tuple[a:b]
        for x  in cursor:
            print(x)
            # print(x[0:3])
            # print( "id:{}  ".format(x) )
   
        

    

  


        
        




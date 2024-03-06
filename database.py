import sqlite3

try:
     sqlite_connection = sqlite3.connect("booking.db")
     sqlite_create_table_query = '''  CREATE TABLE IF NOT EXISTS titles (
                                     title TEXT,
                                     subtitle TEXT,
                                     description TEXT); '''
     cursor = sqlite_connection.cursor()
     cursor.execute(sqlite_create_table_query)
     sqlite_connection.commit()
     print('Table titles Created')
     cursor.close()

except sqlite3.Error as error:
     print('Error: ', error)

finally:
     if sqlite_connection:
         sqlite_connection.commit()
         print('DB disconnected')




try:
     sqlite_connection = sqlite3.connect("booking.db")
     sqlite_create_table_query = '''  CREATE TABLE IF NOT EXISTS cities (
                                     city TEXT,
                                     city_link TEXT); '''
     cursor = sqlite_connection.cursor()
     cursor.execute(sqlite_create_table_query)
     sqlite_connection.commit()
     print('Table cities Created')
     cursor.close()

except sqlite3.Error as error:
     print('Error: ', error)

finally:
     if sqlite_connection:
         sqlite_connection.commit()
         print('DB disconnected')


try:
     sqlite_connection = sqlite3.connect("booking.db")
     sqlite_create_table_query = '''  CREATE TABLE IF NOT EXISTS tour_1 (
                                     title TEXT,
                                     description TEXT,
                                     departure TEXT,
                                     picture TEXT,
                                     price INT,
                                     stars TEXT,
                                     country TEXT,
                                     nights INT,
                                     date TEXT); '''
     cursor = sqlite_connection.cursor()
     cursor.execute(sqlite_create_table_query)
     sqlite_connection.commit()
     print('Table tour_1 Created')
     cursor.close()

except sqlite3.Error as error:
     print('Error: ', error)
finally:
     if sqlite_connection:
         sqlite_connection.commit()
         print('DB disconnected')

try:
     sqlite_connection = sqlite3.connect("booking.db")
     sqlite_create_table_query = '''  CREATE TABLE IF NOT EXISTS tour_2 (
                                     title TEXT,
                                     description TEXT,
                                     departure TEXT,
                                     picture TEXT,
                                     price INT,
                                     stars TEXT,
                                     country TEXT,
                                     nights INT,
                                     date TEXT); '''
     cursor = sqlite_connection.cursor()
     cursor.execute(sqlite_create_table_query)
     sqlite_connection.commit()
     print('Table tour_2 Created')
     cursor.close()

except sqlite3.Error as error:
     print('Error: ', error)

finally:
     if sqlite_connection:
         sqlite_connection.commit()
         print('DB disconnected')



try:
     sqlite_connection = sqlite3.connect("booking.db")
     sqlite_create_table_query = '''  CREATE TABLE IF NOT EXISTS tour_3 (
                                     title TEXT,
                                     description TEXT,
                                     departure TEXT,
                                     picture TEXT,
                                     price INT,
                                     stars TEXT,
                                     country TEXT,
                                     nights INT,
                                     date TEXT); '''
     cursor = sqlite_connection.cursor()
     cursor.execute(sqlite_create_table_query)
     sqlite_connection.commit()
     print('Table tour_3 Created')
     cursor.close()

except sqlite3.Error as error:
     print('Error: ', error)

finally:
     if sqlite_connection:
         sqlite_connection.commit()
         print('DB disconnected')




try:
     sqlite_connection = sqlite3.connect("booking.db")
     sqlite_create_table_query = '''  CREATE TABLE IF NOT EXISTS tour_4 (
                                     title TEXT,
                                     description TEXT,
                                     departure TEXT,
                                     picture TEXT,
                                     price INT,
                                     stars TEXT,
                                     country TEXT,
                                     nights INT,
                                     date TEXT); '''
     cursor = sqlite_connection.cursor()
     cursor.execute(sqlite_create_table_query)
     sqlite_connection.commit()
     print('Table tour_4 Created')
     cursor.close()

except sqlite3.Error as error:
     print('Error: ', error)

finally:
     if sqlite_connection:
         sqlite_connection.commit()
         print('DB disconnected')

try:
     sqlite_connection = sqlite3.connect("booking.db")
     sqlite_create_table_query = '''  CREATE TABLE IF NOT EXISTS tour_5 (
                                     title TEXT,
                                     description TEXT,
                                     departure TEXT,
                                     picture TEXT,
                                     price INT,
                                     stars TEXT,
                                     country TEXT,
                                     nights INT,
                                     date TEXT); '''
     cursor = sqlite_connection.cursor()
     cursor.execute(sqlite_create_table_query)
     sqlite_connection.commit()
     print('Table tour_5 Created')
     cursor.close()

except sqlite3.Error as error:
     print('Error: ', error)

finally:
     if sqlite_connection:
         sqlite_connection.commit()
         print('DB disconnected')






try:
     sqlite_connection = sqlite3.connect("booking.db")
     sqlite_create_table_query = '''  CREATE TABLE IF NOT EXISTS tour_6 (
                                     title TEXT,
                                     description TEXT,
                                     departure TEXT,
                                     picture TEXT,
                                     price INT,
                                     stars TEXT,
                                     country TEXT,
                                     nights INT,
                                     date TEXT); '''
     cursor = sqlite_connection.cursor()
     cursor.execute(sqlite_create_table_query)
     sqlite_connection.commit()
     print('Table tour_6 Created')
     cursor.close()

except sqlite3.Error as error:
     print('Error: ', error)

finally:
     if sqlite_connection:
         sqlite_connection.commit()
         print('DB disconnected')



try:
     sqlite_connection = sqlite3.connect("booking.db")
     sqlite_create_table_query = '''  CREATE TABLE IF NOT EXISTS tour_7 (
                                     title TEXT,
                                     description TEXT,
                                     departure TEXT,
                                     picture TEXT,
                                     price INT,
                                     stars TEXT,
                                     country TEXT,
                                     nights INT,
                                     date TEXT); '''
     cursor = sqlite_connection.cursor()
     cursor.execute(sqlite_create_table_query)
     sqlite_connection.commit()
     print('Table tour_7 Created')
     cursor.close()

except sqlite3.Error as error:
     print('Error: ', error)

finally:
     if sqlite_connection:
         sqlite_connection.commit()
         print('DB disconnected')




try:
     sqlite_connection = sqlite3.connect("booking.db")
     sqlite_create_table_query = '''  CREATE TABLE IF NOT EXISTS tour_8 (
                                     title TEXT,
                                     description TEXT,
                                     departure TEXT,
                                     picture TEXT,
                                     price INT,
                                     stars TEXT,
                                     country TEXT,
                                     nights INT,
                                     date TEXT); '''
     cursor = sqlite_connection.cursor()
     cursor.execute(sqlite_create_table_query)
     sqlite_connection.commit()
     print('Table tour_8 Created')
     cursor.close()

except sqlite3.Error as error:
     print('Error: ', error)

finally:
     if sqlite_connection:
         sqlite_connection.commit()
         print('DB disconnected')
#
#
#
#
#
#
#
# def insert_to_database(title, subtitle, description):
#     try:
#         sqlite_connection = sqlite3.connect("booking.db")
#         cursor = sqlite_connection.cursor()
#         sqlite_insert_param = ''' INSERT INTO titles
#                                     (title, subtitle, description)
#                                     VALUES
#                                     (?,?,?);'''
#         data_tuple = (title,subtitle,description)
#
#         cursor.execute(sqlite_insert_param, data_tuple)
#         print('INSERTED')
#         sqlite_connection.commit()
#         cursor.close()
#
#     except sqlite3.Error as error:
#         print('Error: ', error)
#
#     finally:
#         if sqlite_connection:
#             sqlite_connection.commit()
#             print('DB disconnected')
#
#
#
#
#
# def insert_to_database2(city, city_link):
#     try:
#         sqlite_connection = sqlite3.connect("booking.db")
#         cursor = sqlite_connection.cursor()
#         sqlite_insert_param = ''' INSERT INTO cities
#                                 (city,city_link)
#                                 VALUES
#                                 (?,?);'''
#         data_tuple = (city,city_link)
#
#         cursor.execute(sqlite_insert_param, data_tuple)
#         print('INSERTED2')
#         sqlite_connection.commit()
#         cursor.close()
#
#     except sqlite3.Error as error:
#         print('Error: ', error)
#
#     finally:
#         if sqlite_connection:
#             sqlite_connection.commit()
#             print('DB disconnected')
#
#
# def insert_to_database_tours(title, description, departure, picture, price, stars, country, nights, date):
#     try:
#         sqlite_connection = sqlite3.connect("booking.db")
#         cursor = sqlite_connection.cursor()
#         sqlite_insert_param = ''' INSERT INTO tour_8
#                                 (title, description, departure, picture, price, stars, country, nights, date)
#                                 VALUES
#                                 (?,?,?,?,?,?,?,?,?);'''
#         data_tuple = (title, description, departure, picture, price, stars, country, nights, date)
#
#         cursor.execute(sqlite_insert_param, data_tuple)
#         print('INSERTED!')
#         sqlite_connection.commit()
#         cursor.close()
#
#     except sqlite3.Error as error:
#         print('Error: ', error)
#
#     finally:
#         if sqlite_connection:
#             sqlite_connection.commit()
#             print('DB disconnected')
#
#
# insert_to_database_tours("Купель","термальні води","kuiv","https://turua.com.ua/upload/iblock/b6d/b6d7e9601f754931b633b8be6e10afd3.jpg",44000,"4","Велятино",7,"21 січня",)
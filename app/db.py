import pymysql


# def conectarMySQL():
#     return pymysql.connect(
#         host='localhost',
#         user='root',
#         password='',
#         db='productos',
#         charset='utf8mb4',
#         cursorclass=pymysql.cursors.DictCursor
#     )

# def conectarRestaurantes():
#     return pymysql.connect(
#         host='localhost',
#         user='root',
#         password='',
#         db='restaurant_db',
#         charset='utf8mb4',
#         cursorclass=pymysql.cursors.DictCursor
#     )

# def conectarContacto():
#     return pymysql.connect(
#         host='localhost',
#         user='root',
#         password='',
#         db='formulario',
#         charset='utf8mb4',
#         cursorclass=pymysql.cursors.DictCursor
#     )

def conectarMySQL():
    return pymysql.connect(
        host='zerogluten.mysql.pythonanywhere-services.com',
        user='zerogluten',
        password='admzero24',
        db='zerogluten$productos',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

def conectarRestaurantes():
    return pymysql.connect(
        host='zerogluten.mysql.pythonanywhere-services.com',
        user='zerogluten',
        password='admzero24',
        db='zerogluten$restaurant_db',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

def conectarContacto():
    return pymysql.connect(
        host='zerogluten.mysql.pythonanywhere-services.com',
        user='zerogluten',
        password='admzero24',
        db='zerogluten$formulario',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

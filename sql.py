import mysql.connector


from mysql.connector import Error


def DBconnector(hostname, uname, pwd, dbname):
    con = None
    try:
        con = mysql.connector.connect(
            host = hostname,
            user = uname,
            password = pwd,
            database = dbname
        )
        print("Connection successful")
    except Error as e:
        print("Coneection unsuccessful", e)
    return con


def execute_read_query(con, sql):
    mycursor = con.cursor(dictionary=True)
    rows = None
    try:
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        return rows
    except Error as e:
        print("Error is: ", e)


def execute_read_ID_query(con, sql, params):
    mycursor = con.cursor(dictionary=True)
    rows = None
    try:
        mycursor.execute(sql, params)
        rows = mycursor.fetchall()
        return rows
    except Error as e:
        print("Error is: ", e)


def execute_update_query(con, sql, params):
    mycursor = con.cursor()
    try:
        mycursor.execute(sql, params)
        con.commit()
        print("DB updated successfully")
    except Error as e:
        print("Error is: ", e)


def execute_post_query(con, sql):
    mycursor = con.cursor()
    try:
        mycursor.execute(sql)
        con.commit()
        print("DB updated successfully")
    except Error as e:
        print("Error is: ", e)
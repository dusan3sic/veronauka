import mariadb
import sys

def mariadbConnect():
    try:
        conn = mariadb.connect(
            user="admin",
            password="admin1234",
            host="127.0.0.1",
            port=3306,
            database="test"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    return conn

def kveri(cursor, query):
    cursor.execute(query)
    result = cursor.fetchall()

    return result

    cursor.close()
    conn.close()


conn = mariadbConnect()
cursor = conn.cursor()
ans = kveri(cursor, "SELECT * from books;")
for row in ans: print(row)
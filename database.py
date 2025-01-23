import pyodbc
import json

def connect_db(query,result=True):
    conn=pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};server=tcp:84.54.228.191,49172;database=Pushkarcki;UID=Pushkarcki;PWD=3kVJPI3h")

    cursor=conn.cursor()
    cursor.execute(query)
    if result:
        data=cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        # Преобразуем данные в список словарей
        result = [dict(zip(columns, row)) for row in data]
        # Преобразуем список словарей в JSON
        return json.dumps(result, ensure_ascii=False, indent=4)
    cursor.commit()
    return None


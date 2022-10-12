from mysql import connector
from mysql.connector.constants import ClientFlag
from dotenv import load_dotenv
from os import environ
from mysql.connector.errors import ProgrammingError

def connectDB():
    load_dotenv()
    
    try:
        connection = connector.connect(
            user=environ['MYSQL_USER'],
            password=environ['MYSQL_PASSWORD'],
            host=environ['MYSQL_HOST'],
            database=environ['MYSQL_DATABASE'],
            allow_local_infile=1
        )
        return connection
    except Exception as e:
        return e

def importData(connection: connector.connection_cext.CMySQLConnection, tableName: str, tableQuery: str, tableSchema: str):
    cursor = connection.cursor(buffered=True)

    # Check if DB exists
    try:
        cursor.execute(f"SELECT * FROM {tableName};")
        cursor.execute(f"DROP TABLE {tableName};")
        cursor.execute(tableQuery)
    except ProgrammingError:
        cursor.execute(tableQuery)
    finally:
        cursor.execute(f'''
        LOAD DATA LOCAL INFILE \"sources/{tableName}.txt\" REPLACE INTO TABLE {tableName}
        FIELDS TERMINATED BY '\t'
        LINES TERMINATED BY '\n'
        {tableSchema};
        ''')
        connection.commit()

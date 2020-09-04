# db insertion operations
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    # try:
    conn = sqlite3.connect(db_file)
    return conn
    # except Error as e:
    #     print(e)

    # return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
        
def insert_to_db(conn, data):
    """
    :param conn:
    :param data: DataFrame
    :return:
    """
    answer_sql = """INSERT OR IGNORE INTO answers(answer) VALUES(?)"""
    clue_sql = """INSERT INTO clues(clue, date, source) VALUES(?, ?, "NYT")"""
    mapping_sql = """INSERT INTO mapping(answer_id, clue_id) VALUES(?, ?)"""
    get_answer_id_sql = """SELECT answer_id FROM answers WHERE "answer" = ? """
    
    cur = conn.cursor()
    for i, row in data.iterrows():
        answer_input = (row['answer'],)
        clue_input = tuple(row[1:])
        print(answer_input, clue_input)
        cur.execute(answer_sql, answer_input)
        last_insert_answer = cur.execute(get_answer_id_sql, answer_input).fetchone()[0]
        
        cur.execute(clue_sql, clue_input)
        last_insert_clue = cur.lastrowid
        print(last_insert_clue, last_insert_answer)
        cur.execute(mapping_sql, (last_insert_answer, last_insert_clue))
    
    conn.commit()
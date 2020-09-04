# initialize DB file
import api.database.operations as dbop
import pandas as pd
import setting as s

sql_create_answers = """CREATE TABLE IF NOT EXISTS answers (
answer_id integer PRIMARY KEY,
answer text UNIQUE
);"""

sql_create_mapping_table = """CREATE TABLE IF NOT EXISTS mapping (
id integer PRIMARY KEY,
answer_id INTEGER,
clue_id INTEGER,
FOREIGN KEY (answer_id) REFERENCES answers(answer_id),
FOREIGN KEY (clue_id) REFERENCES clues(clue_id)
);"""

sql_create_clues_table = """CREATE TABLE IF NOT EXISTS clues (
clue_id integer PRIMARY KEY,
date text NOT NULL,
clue text NOT NULL,
source text NOT NULL
);"""


db_file = r"cw_data_test.db" #s.DB_PATH
data = r"C:\Users\gmao3\PycharmProjects\crossword_app\scraper_data\merged_cw_data.csv" #s.RAW_DATA_PATH
conn = dbop.create_connection(db_file)

dbop.create_table(conn, sql_create_answers)
dbop.create_table(conn, sql_create_mapping_table)
dbop.create_table(conn, sql_create_clues_table)

cw_data = pd.read_csv(data)
cw_data = cw_data.iloc[:200, 2:-1]
cw_data = cw_data[~cw_data['answer'].isna()]

dbop.insert_to_db(conn, cw_data)
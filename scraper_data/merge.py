# use if scraped via multiple parts
import pandas as pd
from datetime import datetime

df = pd.DataFrame()
for i in range(1, 8):
    cur = pd.read_csv(r"C:\Users\gmao3\PycharmProjects\crossword_app\scraper_data\page{}.csv".format(i))
    df = df.append(cur)
    print(len(df))
df.to_csv('merged_cw_data.csv')

# cur = pd.read_csv(r"C:\Users\gmao3\PycharmProjects\crossword_app\scraper_data\merged_cw_data.csv")
# # cur['day_of_week'] = cur["date"].apply(lambda x: datetime.strptime(str(x), "%m%d%Y").weekday())
# # cur.iloc[:,1:].to_csv(r"C:\Users\gmao3\PycharmProjects\crossword_app\scraper_data\merged_cw_data1.csv")
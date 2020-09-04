# scrapes crossword data
import time
import scraper.scraper as scrape
import pandas as pd
import requests
import setting as s
from bs4 import BeautifulSoup
from datetime import datetime

URL = [r"https://nytcrosswordanswers.org/nyt-crossword-puzzles/"]

proxy = {
    "https": s.PROXY,
    "http":  s.PROXY,
}

if __name__ == "__main__":
  compiled_answers = pd.DataFrame(columns=['answer', 'clue', 'date'])
  
  while len(URL) > 0:

    cur_url = URL.pop()
    print(cur_url)

    page = requests.get(cur_url, proxies=proxy)
    soup = BeautifulSoup(page.content, 'html.parser')

    next_url = scrape.get_next_page(soup)
    if next_url:
        URL.append(next_url)

    posts = scrape.get_posts(soup)
    for cur_soup in posts:
        try:
            dt = scrape.get_date_str(cur_soup)
            parsed_df = scrape.get_answer_clue(cur_soup,dt)
            compiled_answers = compiled_answers.append(parsed_df)
        except Exception as e:
            print("Encountered error", e, " for ", dt, " Saving and exiting....")
            compiled_answers["day_of_week"] = compiled_answers["date"].apply(lambda x: datetime.strptime(x, "%m%d%Y").weekday())
            compiled_answers.to_csv(r'scraper_data/page_data.csv')
            exit()

    time.sleep(15)

  compiled_answers["day_of_week"] = compiled_answers["date"].apply(lambda x: datetime.strptime(x, "%m%d%Y").weekday())
  compiled_answers.to_csv('scraper_data/page_data.csv')


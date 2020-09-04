# scraper helper functions
from datetime import datetime
import re
import pandas as pd

def get_date_str(soup):
    to_remove = "NYT Crossword Answers "
    title = soup.find("h2", class_="entry-title")
    if not title:
        raise ValueError
    header = title.string
    header = re.sub(to_remove, '', header)
    dt = datetime.strptime(header, "%m/%d/%y").strftime("%m%d%Y")
    return dt

def get_answer_clue(soup, dt):
    parsed = pd.DataFrame(columns=['answer','clue', 'date'])
    data = soup.find('div', class_="nywrap")

    try:
        answers = data.find_all('li')
    except AttributeError:
        print(f"{dt} did not have any data")
        return parsed

    for i in answers:
        answer = i.find('span').text if i.find('span') else i.text
        clue = i.find('a').text if i.find('a') else i.text
        parsed = parsed.append({'clue':clue,'answer':answer,'date':dt}, ignore_index=True)
    print('Added:', dt)
    return parsed

def get_posts(soup):
    _REGEX_POST = re.compile(".*post type-post status-publish format-standard hentry category-nyt-crossword-puzzles ast-col-sm-12 ast-article-post*.")
    return soup.find_all("article", class_=_REGEX_POST)

def get_next_page(soup):
    next_page = soup.find('a', class_="next page-numbers")
    if next_page and next_page['href']:
        return next_page['href']
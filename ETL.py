import requests
import pandas as pd
import sqlite3
import datetime
import numpy as np
from bs4 import BeautifulSoup
url = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
dic_csv = {
        'Country': [],
        'GDP_USD_millions': [],
    }
def log(message):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    message = f"{timestamp} - {message}"
    with open('log.txt', 'a') as log_file:
        log_file.write(message + '\n')
log("ETL process started")
def extract(url):
    log("Extracting data by using web scraping")
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    table = soup.find_all('tbody')
    rows = table[2].find_all('tr')

    for i , row in enumerate(rows):
        if i >= 3:
            dic_csv['Country'].append(row.contents[1].text.strip())
            dic_csv['GDP_USD_millions'].append(row.contents[5].text.strip())
    
def create_dataframe(dic_csv):
    log("Creating DataFrame")
    df = pd.DataFrame(dic_csv)
    return df     

def transform(df):
    log("Transforming data")
    df['GDP_USD_millions'] = df['GDP_USD_millions'].str.replace(',', '')
    df['GDP_USD_millions'] = df['GDP_USD_millions'].str.replace('—','0')
    df['GDP_USD_millions'] = df['GDP_USD_millions'].astype(float)
    df['GDP_USD_millions'] = df['GDP_USD_millions'].apply(lambda x: x / 1000)
    np.round(df['GDP_USD_millions'], 2)
    df.rename(columns={'GDP_USD_millions': 'GDP_USD_billions'}, inplace=True)
def load(df):
    log('loading data to csv')
    pd.DataFrame(df).to_csv('datasets/gdp.csv', index=False)
    log('loading data to json')
    pd.DataFrame(df).to_json('datasets/gdp.json', orient='records', lines=True)
    log('loading data to sqlite')
    conn = sqlite3.connect('datasets/gdp.db')
    pd.DataFrame(df).to_sql('gdp', conn, if_exists='replace', index=False)
    conn.close()
    log("ETL process completed")

def main():
    extract(url)
    df = create_dataframe(dic_csv)
    transform(df)
    load(df)
if __name__ == "__main__":
    main()
'''
This code is an ETL (Extract, Transform, Load) process that scrapes GDP data from a Wikipedia page, 
transforms it, and loads it into a CSV file and a SQLite database. 
The code uses the requests library to fetch the webpage, 
BeautifulSoup to parse the HTML, pandas for data manipulation, and 
sqlite3 for database operations. 
The log function records the progress of the ETL process in a log file.
'''    
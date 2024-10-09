import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Function to scrape Bloomberg headlines
def scrape_bloomberg():
    url = "https://www.bloomberg.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = []
    # Adjust based on actual observation of structure
    for item in soup.find_all('a', {'class': 'headline__link'}):  # Example class
        headline = item.get_text(strip=True)
        if headline:
            headlines.append({
                'source': 'Bloomberg',
                'headline': headline,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
    return headlines

# Function to scrape CNBC headlines
def scrape_cnbc():
    url = "https://www.cnbc.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = []
    # Adjust based on CNBC's structure
    for item in soup.find_all('a', {'class': 'LatestNews-headline'}):  # Example class
        headline = item.get_text(strip=True)
        if headline:
            headlines.append({
                'source': 'CNBC',
                'headline': headline,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
    return headlines

# Function to scrape WSJ headlines
def scrape_wsjs():
    url = "https://www.wsj.com/news/business"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = []
    # Adjust based on WSJ's structure
    for item in soup.find_all('a', {'class': 'WSJTheme--headline--7VCzo7v4'}):  # Example class
        headline = item.get_text(strip=True)
        if headline:
            headlines.append({
                'source': 'WSJ',
                'headline': headline,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
    return headlines

# Function to scrape Benzinga headlines
def scrape_benzinga():
    url = "https://www.benzinga.com/latest-news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = []
    # Adjust based on Benzinga's structure
    for item in soup.find_all('a', {'class': 'headline'}):  # Example class
        headline = item.get_text(strip=True)
        if headline:
            headlines.append({
                'source': 'Benzinga',
                'headline': headline,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
    return headlines

# Function to scrape Yahoo Finance headlines
def scrape_yahoo_finance():
    url = "https://finance.yahoo.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = []
    # Adjust based on Yahoo Finance's structure
    for item in soup.find_all('h3', {'class': 'Mb(5px)'}):  # Example class
        link = item.find('a')
        if link:
            headline = link.get_text(strip=True)
            if headline:
                headlines.append({
                    'source': 'Yahoo Finance',
                    'headline': headline,
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
    return headlines

# Combine results and save to CSV
def save_headlines_to_csv():
    bloomberg_headlines = scrape_bloomberg()
    cnbc_headlines = scrape_cnbc()
    wsj_headlines = scrape_wsjs()
    benzinga_headlines = scrape_benzinga()
    yahoo_finance_headlines = scrape_yahoo_finance()
    
    # Combine all lists
    all_headlines = bloomberg_headlines + cnbc_headlines + wsj_headlines + benzinga_headlines + yahoo_finance_headlines
    
    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(all_headlines)
    df.to_csv('headlines.csv', index=False)
    
    print("Headlines saved to CSV")

# Call the function
save_headlines_to_csv()

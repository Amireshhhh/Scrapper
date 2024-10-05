import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Function to scrape Bloomberg headlines
def scrape_bloomberg():
    url = "https://www.bloomberg.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Specific classes or tags for headlines in Bloomberg
    headlines = []
    # Adjust based on actual observation of structure
    for item in soup.find_all('a', {'class': 'headline__link'}):  # This is an example class, inspect actual site for correct class
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
    for item in soup.find_all('a', {'class': 'LatestNews-headline'}):  # Example: Adjust this to actual class used for news headlines
        headline = item.get_text(strip=True)
        if headline:
            headlines.append({
                'source': 'CNBC',
                'headline': headline,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
    return headlines

# Combine results and save to CSV
def save_headlines_to_csv():
    bloomberg_headlines = scrape_bloomberg()
    cnbc_headlines = scrape_cnbc()
    
    # Combine both lists
    all_headlines = bloomberg_headlines + cnbc_headlines
    
    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(all_headlines)
    df.to_csv('headlines.csv', index=False)
    
    print("Headlines saved to CSV")

# Call the function
save_headlines_to_csv()

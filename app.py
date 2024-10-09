from flask import Flask, render_template
import pandas as pd
from scraper import scrape_bloomberg, scrape_cnbc, scrape_wsjs, scrape_benzinga, scrape_yahoo_finance

app = Flask(__name__)

@app.route('/')
def home():
    # Scrape the headlines
    bloomberg_headlines = scrape_bloomberg()
    cnbc_headlines = scrape_cnbc()
    wsj_headlines = scrape_wsjs()
    benzinga_headlines = scrape_benzinga()
    yahoo_finance_headlines = scrape_yahoo_finance()
    
    # Combine all headlines
    all_headlines = bloomberg_headlines + cnbc_headlines + wsj_headlines + benzinga_headlines + yahoo_finance_headlines

    # Convert to DataFrame (optional)
    df = pd.DataFrame(all_headlines)

    # Pass the headlines to the HTML template
    return render_template('index.html', headlines=df.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

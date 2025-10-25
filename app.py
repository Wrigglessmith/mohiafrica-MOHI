from flask import Flask, jsonify
import subprocess
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>Welcome to MOHI Scraper</h2><p>Go to <a href='/scrape'>/scrape</a> to run the spider.</p>"

@app.route('/scrape')
def run_scraper():
    try:
        # Run Scrapy spider (replace 'myspider' with your actual spider name)
        subprocess.run(['scrapy', 'crawl', 'myspider', '-o', 'output.json'], check=True)
        
        # Load the scraped data
        with open('output.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to MOHI Africa</h1><p>This is your live website hosted on Render!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

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
        subprocess.run(['scrapy', 'crawl', 'example', '-o', 'output.json'], check=True)

        # Load the scraped data
        with open('output.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Render dynamically assigns a port — use it instead of hardcoding
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


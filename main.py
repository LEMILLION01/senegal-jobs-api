from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "API Sénégal Jobs fonctionne!"})

@app.route('/jobs')
def get_jobs():
    jobs = []
    try:
        url = "https://www.rekrute.com/offres-emploi-senegal.html"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "fr-FR,fr;q=0.9"
        }
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        return jsonify({
            "status": "OK",
            "html_sample": str(soup)[:3000]
        })
        
    except Exception as e:
        return jsonify({"error": str(e), "status": "FAILED"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

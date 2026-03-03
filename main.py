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
        url = "https://www.emploi.sn/offres-emploi"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Debug - retourne le HTML brut pour voir la structure
        return jsonify({
            "status": "OK",
            "html_sample": str(soup)[:2000]
        })
        
    except Exception as e:
        return jsonify({"error": str(e), "status": "FAILED"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

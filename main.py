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
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        offres = soup.find_all('div', class_='job-item')
        for offre in offres:
            titre = offre.find('h2')
            entreprise = offre.find('span', class_='company')
            lieu = offre.find('span', class_='location')
            lien = offre.find('a')
            
            if titre:
                jobs.append({
                    "job_title": titre.text.strip(),
                    "employer_name": entreprise.text.strip() if entreprise else "N/A",
                    "job_location": lieu.text.strip() if lieu else "Sénégal",
                    "job_apply_link": lien['href'] if lien else "#"
                })
    except Exception as e:
        return jsonify({"error": str(e)})
    
    return jsonify({"data": jobs, "status": "OK"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

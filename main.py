from flask import Flask, jsonify
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "API Sénégal Jobs fonctionne!"})

@app.route('/jobs')
def get_jobs():
    jobs = []
    try:
        url = "https://fr.indeed.com/rss?q=senegal&l=&sort=date"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=15)
        root = ET.fromstring(response.content)
        channel = root.find('channel')
        
        for item in channel.findall('item'):
            title = item.find('title')
            link = item.find('link')
            description = item.find('description')
            pubdate = item.find('pubDate')
            
            jobs.append({
                "job_title": title.text if title is not None else "N/A",
                "job_apply_link": link.text if link is not None else "#",
                "job_description": description.text if description is not None else "N/A",
                "job_posted_at": pubdate.text if pubdate is not None else "N/A",
                "job_location": "Sénégal",
                "employer_name": "N/A"
            })
            
    except Exception as e:
        return jsonify({"error": str(e), "status": "FAILED"})
    
    return jsonify({"data": jobs, "status": "OK"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

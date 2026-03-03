from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "API Sénégal Jobs fonctionne!"})

@app.route('/jobs')
def get_jobs():
    try:
        url = "https://remotive.com/api/remote-jobs?limit=20"
        response = requests.get(url, timeout=15)
        data = response.json()
        
        jobs = []
        for job in data.get('jobs', []):
            jobs.append({
                "job_title": job.get('title', 'N/A'),
                "employer_name": job.get('company_name', 'N/A'),
                "job_location": job.get('candidate_required_location', 'Remote'),
                "job_employment_type": job.get('job_type', 'N/A'),
                "job_apply_link": job.get('url', '#'),
                "job_posted_at": job.get('publication_date', 'N/A'),
                "employer_logo": job.get('company_logo', '')
            })
            
        return jsonify({"data": jobs, "status": "OK"})
        
    except Exception as e:
        return jsonify({"error": str(e), "status": "FAILED"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

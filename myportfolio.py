from flask import Flask, render_template

app = Flask(__name__)

class Portfolio:
    def __init__(self):
        self.data = {
            "name": "Steevansan M",
            "title": "Odoo ERP Specialist & AI/ML Enthusiast",
            "contact": {
                "location": "Pattukkottai, Tamil Nadu, India",
                "phone": "+91 8056950628",
                "email": "steevansan94@gmail.com",
                "languages": "English, Tamil"
            },
            "objective": "Remote-ready Project Coordinator and Odoo ERP Specialist with over 5 years of experience in ERP implementation, workflow automation, and client support. Currently studying AI/ML with Python to enhance automation capabilities.",
            "highlights": [
                {"icon": "⚙️", "text": "Odoo ERP Implementation (CRM, Sales, Inventory)"},
                {"icon": "🤖", "text": "Workflow Automation & Process Optimization"},
                {"icon": "🐍", "text": "Python, SQL, API Integration"},
                {"icon": "🧠", "text": "AI/ML Tools: Pandas, NumPy, Scikit-learn"},
                {"icon": "📊", "text": "Data Visualization: Power BI, Tableau"},
                {"icon": "🔄", "text": "Agile/Scrum Methodologies"}
            ],
            "experience": [
                {
                    "icon": "🌐",
                    "company": "Millennia Global Soft Pvt Ltd",
                    "role": "Project Coordinator (Odoo ERP & Android)",
                    "period": "Jan 2024 -- Nov 2024",
                    "details": [
                        "Acted as POC for project coordination",
                        "Integrated Odoo modules: CRM, Sales, Inventory",
                        "Automated reporting for performance tracking"
                    ]
                },
                {
                    "icon": "🛒",
                    "company": "FAST EXPO Pvt Ltd",
                    "role": "Delivery Manager",
                    "period": "2021 -- 2023",
                    "details": [
                        "Managed supermarket & restaurant POS systems",
                        "Automated tax handling and inventory control",
                        "Generated sales analytics reports"
                    ]
                }
            ],
            "projects": [
                {"icon": "🚢", "name": "L&T Shipbuilding", "desc": "API Integration for Work Order Tracking"},
                {"icon": "🛋️", "name": "Furniture Factory ERP", "desc": "Assembly Line & Delivery Control"},
                {"icon": "⛽", "name": "Oilfield Equipment ERP", "desc": "RFID Machine Tracking"},
                {"icon": "🍽️", "name": "Restaurant POS", "desc": "Real-time Billing & Table Management"}
            ],
            "education": {
                "icon": "🎓",
                "degree": "Bachelor of Engineering (Mechanical)",
                "institution": "SMR East Coast Engineering College, Anna University",
                "year": "2021",
                "score": "67.5%"
            },
            "certifications": [
                {"icon": "🤖", "name": "Introduction to Artificial Intelligence", "issuer": "Simplilearn", "year": "2025"},
                {"icon": "📈", "name": "Data Analytics using Google Bard with Excel and Python", "issuer": "Great Learning", "year": "2025"},
                {"icon": "🧠", "name": "Artificial Intelligence A-Z 2025", "issuer": "Udemy", "year": "2025"}
            ],
            "salary": {
                "current": "₹3,60,000 per annum",
                "expected": "₹5,00,000 per annum"
            },
            "availability": {
                "notice": "Immediately Available",
                "preference": "Remote / Work-from-home"
            }
        }

@app.route('/')
def home():
    portfolio = Portfolio()
    return render_template('index.html', data=portfolio.data)

if __name__ == '__main__':
    app.run(debug=True)
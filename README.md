# 🛡️ Sentinel AI

> **Enterprise AI Monitoring & Analytics Dashboard**

A professional AI observability platform built with **Python, Streamlit, SQLite, and Plotly** for monitoring AI model performance, latency, costs, errors, providers, and system health through an interactive dashboard.

---

## 📌 Overview

Sentinel AI is an enterprise-style monitoring dashboard designed to help developers and organizations monitor AI applications in real time.

The dashboard provides centralized visibility into:

- AI request monitoring
- Model performance
- Latency analytics
- Token usage
- Cost tracking
- Error monitoring
- System health
- Alerts
- Reports
- Configuration management

The project follows a modular architecture with reusable UI components, a SQLite backend, and interactive visualizations.

---

# ✨ Features

## 🏠 Executive Dashboard

- Live KPI Cards
- Request Statistics
- Success Rate Monitoring
- Latency Overview
- Token Consumption
- Cost Summary
- Error Summary
- Interactive Charts

---

## 📈 Request Monitoring

- Live Request History
- Request Metrics
- Request Timeline
- Latency Heatmap
- Demo Request Generator
- Traffic Simulator
- Request Insights
- Export Center

---

## ⏱️ Latency Analytics

- P50 / P95 / P99 Latency
- Provider Comparison
- Latency Trends
- Requests Processed
- Performance Visualization

---

## 💰 Cost Analytics

- Cost Breakdown
- Token Usage
- Provider Cost Comparison
- Daily Cost Trends
- Cost Recommendations

---

## ⚠️ Error Monitoring

- Error Dashboard
- Error Metrics
- Error Logs
- Severity Distribution
- Error Recommendations

---

## 🧊 Model Analytics

- Model Usage
- Provider Analytics
- Token Distribution
- Cost Distribution
- Performance Comparison

---

## 📊 System Health

- CPU Usage
- Memory Usage
- Database Health
- Provider Health
- Service Availability
- Health Recommendations

---

## 🔔 Alerts

- Active Alerts
- Alert Metrics
- Alert Rules
- Alert Recommendations

---

## 📄 Reports

- Dashboard Reports
- Export PDF
- Export CSV
- Export Excel
- Report History

---

## ⚙️ Settings

- Provider Settings
- Model Settings
- Notification Settings
- Database Settings
- Profile Settings

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Frontend | Streamlit |
| Database | SQLite |
| Charts | Plotly |
| Data Processing | Pandas |
| PDF Export | ReportLab |
| Excel Export | OpenPyXL |
| Auto Refresh | streamlit-autorefresh |

---

# 📁 Project Structure

```text
Sentinel-AI/
│
├── config/
├── database/
├── services/
│   ├── database/
│   ├── monitoring/
│   ├── reporting/
│
├── ui/
│   ├── alerts/
│   ├── charts/
│   ├── components/
│   ├── cost/
│   ├── dashboard/
│   ├── error_monitoring/
│   ├── latency/
│   ├── model/
│   ├── pages/
│   ├── reports/
│   ├── request_monitoring/
│   ├── settings/
│   ├── system_health/
│
├── run.py
├── requirements.txt
└── README.md
```

---

# 📊 Dashboard Modules

- Executive Dashboard
- Request Monitoring
- Latency Analytics
- Cost Analytics
- Error Monitoring
- Model Analytics
- System Health
- Alerts
- Reports
- Settings

---

# 🗄 Database

Sentinel AI uses SQLite for persistent storage.

Current tables include:

- requests
- providers
- alerts
- errors

The database initializes automatically on first launch.

---

# 📈 Data Flow

```text
Traffic Generator
        │
        ▼
Request Logger
        │
        ▼
SQLite Database
        │
        ▼
Database Services
        │
        ▼
Dashboard UI
        │
        ▼
Charts • Tables • KPIs
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Sentinel-AI.git
```

Move into the project

```bash
cd Sentinel-AI
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run run.py
```

---

# 📸 Screenshots

> Add screenshots here after deployment.

Example:

- Executive Dashboard
- Request Monitoring
- Latency Analytics
- Cost Analytics
- Reports
- Settings

---

# 📦 Exports

Supported export formats:

- PDF
- CSV
- Excel

---

# 🎯 Project Highlights

- Modular Architecture
- Reusable Components
- Enterprise Dashboard Design
- SQLite Integration
- Interactive Charts
- Auto Refresh
- Real-time Simulation
- Dynamic KPIs
- Dynamic Tables
- Export Support

---

# 🔮 Future Improvements

The current version (**v1.0**) is feature-complete. Potential future enhancements include:

- Real-time background traffic simulation
- FastAPI-based request ingestion API
- PostgreSQL support for production deployments
- User authentication and role-based access
- WebSocket-based live dashboard updates
- AI-powered root cause analysis
- Predictive alerting and anomaly detection
- Docker support
- Cloud deployment (AWS, Azure, GCP, Render, Railway)
- Email, Slack, and Microsoft Teams notifications
- Advanced PDF reports with embedded charts
- Audit logging
- CI/CD pipeline
- Unit and integration testing

---

# 📚 Learning Outcomes

This project demonstrates practical experience with:

- Dashboard Development
- Data Visualization
- SQLite Integration
- AI Monitoring Concepts
- Modular Software Architecture
- Enterprise UI Design
- Python Application Development

---

# 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit pull requests.

---


# 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

# 👨‍💻 Author

**Maitraiya Pravin Sonawane**

Artificial Intelligence & Data Science Student

Passionate about AI Engineering, Data Analytics, MLOps, and Building Production-Ready AI Applications.

---

⭐ If you found this project useful, consider giving it a star.
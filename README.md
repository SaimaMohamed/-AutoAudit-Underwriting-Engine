AutoAudit: Automated Policy Underwriting Engine

🚀 Project Overview
AutoAudit is an automated decision-support system designed to streamline the insurance underwriting process. It uses a rule-based Triage Engine to evaluate policy applications in real-time, categorizing them based on risk parameters to improve operational efficiency.

🛠️ Core Features
Automated Risk Triage: Implements logic to instantly approve low-risk applicants or flag high-risk cases for manual audit.

Dynamic Rule Configuration: Features a dashboard for adjusters to adjust thresholds without changing source code.

Observability Dashboard: Provides real-time feedback on application status and risk levels for system transparency.

Referential Integrity: Utilizes a MySQL backend to store both applicant data and the business rules.

🏗️ Tech Stack
Language: Python (Streamlit, Pandas).

Database: MySQL (Relational Database Management System).

Version Control: Git & GitHub.

📂 Repository Structure
audit_engine.py: The core underwriting logic and UI.

autoaudit.sql: The database schema for policies and rules.

💡 Alignment with Intact's Engineering Culture
This project demonstrates readiness for a Software Engineering role:

Defect Triage: Showcases the ability to build automated "Gatekeepers" that prevent high-risk data from moving further into the system.

Operational Excellence: Directly addresses the goal of reducing manual friction in the insurance lifecycle through software automation.

Reliability & Observability: Includes status indicators to ensure the system is "Healthy" and its decisions are traceable.

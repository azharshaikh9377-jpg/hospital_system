# hospital_system
🏥 Hospital Patient Management System
Python | MongoDB | Tkinter

📄 Project Overview
This application is designed to modernize hospital record-keeping. It allows medical staff to manage patient registration, track consulting doctors, and monitor patient status through a secure, high-performance NoSQL database.

🎯 Scenario: Healthcare Management
In a mid-sized hospital, keeping track of 100+ patients manually is prone to error. This system provides:

Digital Patient Cards: Stores ID, Age, Gender, and Blood Group.

Live Status Tracking: Monitor if a patient is "Stable," "Critical," or "Discharged."

Doctor Assignment: Track which consultant is handling which case.

🛠️ Tech Stack
Frontend: Python Tkinter (GUI)

Backend: MongoDB (NoSQL Database)

Connectivity: PyMongo

Reporting: CSV Module for data export

⚙️ Core Functionalities (CRUD)
Create: Add new patient records with validation to prevent duplicate IDs.

Read: Display 100+ records from MongoDB in a scrollable table.

Update: Select a patient from the list and update their status or doctor.

Delete: Remove records with a "Yes/No" confirmation popup.

Search: Instant search by patient name using regex (case-insensitive).

Export: Export the entire database to patient_records.csv for administrative use.

🚀 How to Run
Start MongoDB: Ensure your local MongoDB server is running on port 27017.

Setup Database:

Create database: hospital_db

Create collection: patients

Install Requirements:

Bash

pip install pymongo
Launch:

Bash

python app.py
🧪 Sample Data Format
The system is compatible with JSON imports. The standard document structure used is:

JSON

{
  "p_id": "P-1001",
  "name": "Arjun Sharma",
  "age": "28",
  "gender": "Male",
  "blood_group": "B+",
  "doctor": "Dr. Smith",
  "status": "Stable"
}

<img width="443" height="416" alt="image" src="https://github.com/user-attachments/assets/650df7c4-8957-42f5-890c-e5d211931fbf" />

<img width="1490" height="939" alt="image" src="https://github.com/user-attachments/assets/2ebadeb5-3701-47ce-a6b2-9289f411a28d" />


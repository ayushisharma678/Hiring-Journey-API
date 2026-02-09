# Candidate Journey Management API

This is a professional Backend API built with **FastAPI** to manage a candidate's journey from application to hiring. Designed as part of the recruitment task, it features a fixed sequential pipeline and Role-Based Access Control (RBAC).

## 🚀 Features
- **Candidate CRUD**: Create, Read, and Update candidate profiles.
- **Fixed Sequential Pipeline**: Managed stages: `APPLIED -> SCREENING -> INTERVIEW -> HIRED/REJECTED`.
- **RBAC (Role-Based Access Control)**:
  - `Recruiter`: Can view all candidates and move them across stages.
  - `Candidate`: Can view their own application status.

## 🛠 Tech Stack
- **Language**: Python 3.10+
- **Framework**: FastAPI
- **Environment Management**: Miniconda/Conda
- **Data Validation**: Pydantic

## 📂 Project Structure
- `main.py`: The core API logic and endpoints.
- `README.md`: Project documentation.
- `requirements.txt`: Dependencies list.

## ⚙️ How to Run
1. **Activate Environment**:
   ```bash
   conda activate hiring_api
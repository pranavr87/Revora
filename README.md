# 🚗 REVORA — Vehicle Fault Detection & Diagnosis System

REVORA is a full-stack vehicle fault diagnosis system that identifies potential vehicle faults based on vehicle details and symptoms. It provides the probable fault, root cause, recommended solution, severity, estimated cost, repair time, and a premium PDF report.

## 🛠️ Tech Stack

* **Frontend:** React.js, Vite, JavaScript, CSS, Axios
* **Backend:** Python, FastAPI, Pydantic, Uvicorn
* **Database:** SQLite
* **PDF:** ReportLab, Playwright, Jinja2

## 📁 Project Structure

```text
Vehicle_Fault_Detection/
├── Backend/
├── database/
├── Docs/
├── Frontend/
├── Screenshots/
├── requirements.txt
└── README.md
```

## ⚙️ Setup & Run

### 1. Backend

Open a terminal:

```bash
cd Backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required dependencies:

```powershell
pip install -r requirements.txt
```

If Playwright or Jinja2 is not installed, run:

```powershell
pip install playwright jinja2
python -m playwright install chromium
```

Start the backend:

```powershell
python -m uvicorn app.main:app --reload
```

Backend will run at:

```text
http://127.0.0.1:8000
```

Keep this terminal running.

---

### 2. Frontend

Open a **new terminal**:

```bash
cd Frontend
```

Install dependencies:

```bash
npm install
```

Start the frontend:

```bash
npm run dev
```

Vite will show a local URL such as:

```text
http://localhost:5173
```

Open that URL in your browser.

---

## 🚘 How to Use REVORA

1. Select **Vehicle Brand**
2. Select **Vehicle Model**
3. Select **Vehicle Component**
4. Select one or more **Symptoms**
5. Click **Diagnose**
6. View the detected fault and diagnostic details
7. Generate/download the **Premium PDF Report**

---

## 🔄 How It Works

```text
React Frontend
      ↓
    Axios
      ↓
FastAPI Backend
      ↓
 SQLite Database
      ↓
Symptom Matching
      ↓
Best Matching Fault
      ↓
Fault + Root Cause + Solution
+ Severity + Cost + Repair Time
      ↓
React Result Page
      ↓
Premium PDF Report
```

---

## 🗄️ Database

REVORA uses a SQLite vehicle-fault database containing **252,000+ records**.

The database provides the data for:

* Vehicle brands
* Vehicle models
* Components
* Symptoms
* Faults
* Root causes
* Solutions
* Severity
* Estimated cost
* Repair time

---

## 🔍 Diagnosis Logic

REVORA uses **database-driven symptom matching**.

The selected vehicle details and symptoms are sent to the FastAPI backend. The backend searches the fault database, compares the provided symptoms with stored records, and returns the most relevant matching fault and its associated diagnostic information.

---

## 📄 PDF Report

After diagnosis, REVORA generates a professionally designed PDF report using **ReportLab, Playwright, and Jinja2** containing the diagnosis and related vehicle information.

---

## ⚠️ Note

REVORA is a diagnostic assistance system. Actual vehicle faults should be confirmed by a qualified automotive professional.

**Note:** The `.venv` folder is not included in the project ZIP. Create a new virtual environment using the setup instructions above before running the backend.

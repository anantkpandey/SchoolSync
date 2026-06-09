# 🎓 SchoolSync

> A modern school management system built with Python, FastAPI, SQLite, and HTML.

SchoolSync is an open-source school management platform designed to streamline the day-to-day operations of educational institutions. It provides a centralized system for managing students, teachers, academics, attendance, examinations, and administrative workflows.

The project is being developed incrementally as a practical exploration of backend engineering, system design, databases, and software architecture.

---

## ✨ Current Features

### Student Management

* Add new students
* View all registered students
* Persistent storage using SQLite
* Server-side rendering with Jinja2 templates
* Automatic redirection after student registration

---

## 🏗️ Architecture

```text
Browser
   │
   ▼
HTML Forms
   │
   ▼
FastAPI Backend
   │
   ▼
SQLite Database
   │
   ▼
Jinja2 Templates
```

---

## 📂 Project Structure

```text
SchoolSync/
├── app/
│   ├── database/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── templates/
│
├── docs/
├── tests/
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/your-username/SchoolSync.git
cd SchoolSync
```

### Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python -m uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## 🛣️ Roadmap

### Version 0.1

* [x] Student Registration
* [x] Student Listing
* [x] SQLite Persistence

### Version 0.2

* [ ] Individual Student Profiles
* [ ] Edit Student Details
* [ ] Delete Student Records

### Version 0.3

* [ ] Teacher Management
* [ ] Subject Management
* [ ] Class Management

### Version 0.4

* [ ] Attendance Tracking
* [ ] Attendance Reports

### Version 0.5

* [ ] Examination System
* [ ] Marks & Grades

### Version 0.6

* [ ] Fee Management
* [ ] Payment Records

---

## 🧠 Learning Goals

SchoolSync is more than a software project. It is a hands-on journey through:

* Python Development
* Backend Engineering
* FastAPI
* SQL & Databases
* REST APIs
* Software Architecture
* System Design
* Testing & Deployment

---

## 📜 License

This project is licensed under the MIT License.

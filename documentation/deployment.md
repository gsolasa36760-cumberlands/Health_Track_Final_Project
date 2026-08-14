# HealthTrack Deployment Guide

## 1. Purpose

This document provides the steps required to install, configure, start, and verify the HealthTrack system.

The deployment includes the MySQL database, FastAPI backend, database migrations, and Dash dashboard.

---

## 2. System Requirements

The following software is required:

- Windows
- Python 3.x
- MySQL
- MySQL Workbench
- Git (optional)
- Web browser

---

## 3. Project Structure

The main HealthTrack project contains:

```text
HealthTrack_Final_Project/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── services/
│
├── dashboard/
│   └── dashboard.py
│
├── migrations/
│   └── versions/
│
├── tests/
│
├── documentation/
│
├── .env
├── alembic.ini
└── requirements.txt
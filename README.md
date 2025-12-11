# AI Rental DB

**Dockerized PostgreSQL + Analytics Environment for KPI Computation**
**Target Completion Date: 31 January 2026**

AI Rental DB is a self-contained, dockerized analytics environment built to support KPI computation for a synthetic DVD-Rental–style business dataset. It demonstrates strong skills in:

- SQL modeling
- Dockerized analytics workflows
- Python-based KPI calculations
- Database restoration automation
- Preparation for a future AI-powered data analysis stack

This project forms part of a larger portfolio showcasing end-to-end data intelligence engineering capabilities.

---

## Overview

The system consists of two coordinated services:

### **1. PostgreSQL (Dockerized)**

- Automatically restored from a full `.tar` database dump
- Runs inside an isolated Docker container
- Uses persistent Docker volumes
- Provides a clean, reproducible data environment for KPI analytics

### **2. Analytics Container (Python + SQLAlchemy)**

- Runs Jupyter Notebook inside Docker
- Designed for SQL and Pandas-based KPI analysis
- Connects to the internal Postgres service through a dedicated bridge network
- Contains the full analytics environment (requirements installed on build)

This separation provides production-style modularity:
**database layer ≠ analytics layer**.

---

## Key Features

### **Automated Database Initialization**

On first startup, Docker automatically restores the rental database using a scripted initialization process. This ensures reproducibility across machines.

### **Reproducible Python Analytics**

The analytics container includes:

- SQLAlchemy connection setup
- KPI notebooks
- Matplotlib, Pandas, NumPy
- Local configuration through `config_local_docker.py`

You can run KPI notebooks without needing a local Python environment.

### **Local Development Workflow**

The project supports both:

- **Option A — Running Jupyter inside Docker**, exposing port `8888`
- **Option B — Running analytics on your local machine**, connecting to Postgres in Docker

The repository is configured for strict reproducibility regardless of platform.

---

## Usage

### **Build and Start Everything**

```bash
docker compose up --build
```

### **Stop Everything**

```bash
docker compose down
```

### **Remove All Containers + Volumes (Fresh Reset)**

```bash
docker compose down --volumes
```

### **Launch Jupyter Notebook From Analytics Container**

```bash
docker exec -it drental-analytics bash
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

Then open:

```
http://localhost:8888
```

---

## Database Connection

### **From Local Machine**

```
postgresql://postgres:postgres@localhost:5450/ai_rental_db
```

### **From Inside the Analytics Container**

```bash
psql -h postgres -U postgres -d ai_rental_db
```

---

## KPIs Included (Ongoing)

The project includes a growing collection of notebooks demonstrating:

- Top 10 customers by spending
- Revenue-based film rankings
- Month-over-month rental activity
- Store-level comparisons
- Customer activity segmentation

Additional KPIs will be implemented prior to the project’s target completion date.

---

## Purpose

AI Rental DB showcases my ability to:

- Structure real analytics environments with Docker
- Restore and manage SQL databases in containerized environments
- Build KPI computation pipelines using SQL + Python
- Prepare data systems for future integration with AI-driven agents

This project is designed as a core component of my **Data Analyst / Data Intelligence Engineer** portfolio.

---

## Status

**Active development.**
Final version expected 31 January 2026.

---

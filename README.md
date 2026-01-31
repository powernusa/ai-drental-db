# 🎬 AI-DRental-DB

**End-to-End, Data-First Analytics Application**

**Target Completion Date:** **31 January 2026**

AI-DRental-DB is an end-to-end, data-first analytics application built on a synthetic DVD-rental–style dataset.  
The project emphasizes **correct metric definition before visualization**, production-style separation of concerns, and full reproducibility using Docker.

This repository represents the **engineering backbone** behind the interactive analytics showcased on my portfolio site.

---

## Core Design Philosophy

This project is built with a **data-first mindset**:

- Metrics are **defined, validated, and sanity-checked in notebooks**
- Business logic is **locked before any frontend visualization**
- APIs expose only **trusted, pre-validated data**
- The frontend visualizes **what the data supports — nothing more**

In particular, multiple revenue definitions are evaluated in notebooks (staff-centric vs customer-centric), and **staff-centric revenue** is intentionally selected once supported by the data. That definition then becomes the **single source of truth** exposed to the application.

## <a href="https://mydataaijournal.com/ai-rental-db/">Link to project</a>

## Architecture Overview

The system is composed of **clearly separated layers**, mirroring real production analytics systems.

### 1️⃣ Dockerized PostgreSQL (Data Layer)

- Restored automatically from a full `.tar` database dump
- Runs inside an isolated Docker container
- Uses persistent Docker volumes
- Guarantees a clean, reproducible data environment

### 2️⃣ Analytics Layer (Notebook Source of Truth)

- Python + SQLAlchemy + Pandas
- KPI computation and validation notebooks
- Metric definitions finalized here before being exposed elsewhere

### 3️⃣ API Layer (Django Backend)

- Django-based backend exposing validated metrics via REST-style APIs
- Acts as a strict contract between analytics and frontend
- Ensures:
  - Business logic and metric definitions live on the server
  - Frontend consumes only trusted, pre-computed data
  - Metrics are never redefined or recomputed in the UI layer

### 4️⃣ Frontend (Visualization Layer)

- **D3.js** for data-driven rendering
- **GSAP** for controlled, purposeful animation
- **Vite** for fast, clean bundling
- Visualizes only API-approved metrics

---

## What This Project Demonstrates

- Advanced SQL modeling and analytical reasoning
- KPI definition, validation, and metric governance
- **Django API backend design for analytics delivery**
- Production-style Docker workflows
- Clear separation between data, backend logic, and presentation
- Readiness for future AI-assisted analytics agents

---

## How to Run the Project

### 🔧 Build and Start All Services

```bash
docker compose up --build
```

This will:

- Restore the PostgreSQL database automatically
- Start the analytics and backend services
- Prepare the environment for KPI computation

---

### 🛑 Stop All Services

```bash
docker compose down
```

---

### ♻️ Full Reset (Remove Containers + Volumes)

```bash
docker compose down --volumes
```

Use this if you want a **fresh database restore**.

---

## Accessing the Analytics Environment

### 📓 Launch Jupyter Notebook (Inside Docker)

```bash
docker exec -it drental-analytics bash
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

Then open:

```
http://localhost:8888
```

No local Python setup is required.

---

## Database Connection Strings

### From Local Machine

```
postgresql://postgres:postgres@localhost:5450/ai_rental_db
```

### From Inside Docker Network

```bash
psql -h postgres -U postgres -d ai_rental_db
```

---

## KPIs Included (Ongoing)

- Top customers by spending
- Revenue-ranked films
- Store-level revenue comparisons
- Monthly trends and activity

---

## Purpose

This repository serves as a **core portfolio project** demonstrating my ability to:

- Design **end-to-end analytics applications**, from raw data modeling to interactive visualization
- Define, validate, and lock **business metrics** before exposing them downstream
- Build **reproducible, production-style data environments** using Docker and PostgreSQL
- Deliver analytics through a **Django API backend**, enforcing a clean contract between data and UI
- Integrate **notebook-driven analysis → backend APIs → frontend visualization** as a single system
- **Implement AI agents directly on top of validated APIs**, enabling natural-language querying

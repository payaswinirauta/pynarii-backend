<h1 align="center">🛍️ Pynarii Backend</h1>
<p align="center">
  <b>Fast, Lightweight, and Ready-to-Scale E-commerce API built with FastAPI</b><br>
  🔗 Seamlessly integrates with frontend | 💡 Ideal for smart shopping platforms | 🔐 Clean Code
</p>

---

## 🚀 Tech Stack

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-⚡-green?logo=fastapi)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-black?logo=uvicorn)
![Status](https://img.shields.io/badge/Build-Stable-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

---

## 📂 Project Structure

```text
pynarii-backend/
├── main.py # FastAPI main app & route setup
├── products.py # CRUD & logic layer
├── products.json # Sample product database (mock)
└── pycache/ # Python bytecode (ignored)


---

## 🧑‍💻 Local Development Setup

### ✅ Requirements:
- Python 3.11+
- pip

### 🛠️ Installation Steps:

```bash
# 1. Clone the repository
git clone https://github.com/payaswinirauta/pynarii-backend.git
cd pynarii-backend

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate       # Linux/Mac
.venv\Scripts\activate          # Windows

# 3. Install dependencies
pip install fastapi uvicorn

# 4. Run the server
uvicorn main:app --reload
✅ Visit: http://127.0.0.1:8000/products/
📘 Docs: http://127.0.0.1:8000/docs

🔗 API Endpoint
Method	Endpoint	Description
GET	/products/	Get all product data

💡 Features
🔌 RESTful API for product data

🌍 CORS Enabled (frontend-ready)

🧩 Clean separation of concerns (routes & logic)

⚙️ Easily upgradable to full stack system (cart, auth, admin)

📁 Flat & minimal project structure

🌐 Live Frontend Link
Pynarii is a full stack smart shopping app, and this backend powers the dynamic product logic.

👉 🌐 Visit Live Frontend Website(https://payaswinirauta.github.io/pynarii/) – Fully integrated with this API.

🛣️ Future Roadmap
 Add category-wise filtering

 Integrate search & sort

 Add cart APIs (session-based)

 Switch to SQL (SQLite/PostgreSQL)

 Authentication with JWT

 Admin product management (via FastAPI + Jinja2)

🧠 Ideal For
🎓 Students learning backend APIs

💼 Freelancers building MVPs

👩‍💻 AI-enabled e-commerce platforms

🛒 Small/medium online stores

👩‍💻 Developed By
Payaswini Rauta
🔗 GitHub | 💬 FastAPI • AI • Full Stack • Freelance

📜 License
Licensed under the MIT License

💬 Contributing
Pull requests and issues are welcome!
Let’s build a smarter e-commerce backend together 🛍️




# 🚌 Tourism Manager

A backend RESTful API built with **Flask** and **MySQL** to manage a tourism system.  
It provides endpoints for managers, drivers, guides, programs, tours, and tourists.  
Designed to serve as the backend for a mobile application.

## 🔧 Features
- Manager authentication (login/register)
- CRUD operations for:
  - Drivers
  - Guides
  - Programs
  - Tours
  - Tourists
- Tour history filtering by date
- JSON-based API responses
- MySQL database integration

## 🛠 Tech Stack
- **Backend:** Flask (Python)
- **Database:** MySQL
- **Libraries:** mysql-connector-python, Flask

## 🚀 Usage

### 1. Clone the repository
```bash
git clone https://github.com/YourUserName/flask-backend-api.git
cd flask-backend-api
```

### 2. Create a virtual environment & install dependencies
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

pip install -r requirements.txt
```

### 3. Configure database
```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DATABASE'] = 'tourism_db'
```

### 4. Run the server
```bash
python app.py
```
Server will start at: `http://127.0.0.1:5000`

## 📡 API Endpoints

### Manager
- POST /manager/login
- POST /manager/register

### Driver
- GET /drivers
- POST /driver
- PUT /driver/<id>
- DELETE /driver/<id>

### Guide
- GET /guides
- POST /guide
- PUT /guide/<id>
- DELETE /guide/<id>

### Program
- GET /programs
- POST /program
- PUT /program/<id>
- DELETE /program/<id>

### Tour
- GET /tours
- GET /tour/<id>
- POST /tour
- PUT /tour/<id>
- DELETE /tour/<id>
- POST /tour/history

### Tourist
- GET /tourists
- GET /tourist/<id>
- POST /tourist/register
- POST /tourist/login
- PUT /tourist/<id>
- DELETE /tourist/<id>


## 🌐 Connect with Me
- 💼 [LinkedIn](https://linkedin.com/in/mozeiter)
- 🌍 [Portfolio Website](https://mohammadalzeiter.com)
- 📧 Email: mohammadalzeiter@email.com

✨ A robust backend API built with **Flask & MySQL** to power mobile applications.


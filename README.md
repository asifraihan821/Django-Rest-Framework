# 🎬 Phimart API

Phimart is a **Django REST Framework (DRF)** based e-commerce backend that provides API endpoints for managing products, categories, carts, and orders.  
It includes **JWT authentication (Djoser)** for secure user management and **Swagger (drf_yasg)** for interactive API documentation.

---

## 🚀 Features

- ✅ JWT Authentication (using Djoser)  
- ✅ Product Management (CRUD APIs)  
- ✅ Categories Management  
- ✅ Shopping Cart APIs  
- ✅ Orders & Checkout APIs  
- ✅ Swagger & Redoc API Documentation  

---

## 📦 Tech Stack

- **Backend:** Django, Django REST Framework  
- **Authentication:** JWT (via Djoser)  
- **Documentation:** drf_yasg (Swagger / Redoc)  
- **Database:** SQLite / PostgreSQL (configurable)  

---

## ⚙️ Installation

Clone the repository:

```
bash
git clone https://github.com/your-username/phimart.git
cd phimart
```

```
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows 
```

```
pip install -r requirements.txt
```

```
python manage.py migrate
```

```
python manage.py createsuperuser
```

```
python manage.py runserver
```

```
POST /auth/jwt/create/
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```



---


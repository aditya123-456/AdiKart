# 🛒 AdiKart — Django E-Commerce Web Application

**AdiKart** is a Django-based e-commerce web application currently under development. The project is designed to provide a complete online shopping experience, including product browsing, category-based navigation, user authentication, session-based cart management, product customization, checkout, and order history.

The application is being developed incrementally, with additional e-commerce features planned for future updates.

> 🚧 **Project Status: In Development**
>
> The current version contains the core shopping workflow. More features, improvements, and production-ready functionality will be added in upcoming updates.

---

## 📌 Overview

AdiKart is built using **Python and Django** with a modular application structure.

The current shopping flow allows users to:

* Browse available products
* Search for products
* Browse products by category
* View individual product details
* Select product color and size
* Add products to a session-based shopping cart
* Increase or decrease product quantities
* Remove products from the cart
* View cart totals and tax
* Register an account
* Activate an account
* Login and logout
* Recover/reset passwords
* Proceed to checkout
* Enter delivery and billing information
* Select a payment method
* Place an order
* View previous orders from the user dashboard

The project also includes a Django admin interface for managing products, categories, users, and orders.

---

## ✨ Current Features

### 👤 User Authentication

* User registration
* Custom Django user model
* Email-based authentication
* Password hashing using Django authentication
* Account activation
* Login and logout
* Password reset workflow
* Protected dashboard and checkout pages

---

### 🛍️ Product Management

Products currently contain:

* Product name
* Slug
* Description
* Price
* Product image
* Availability status
* Category
* Created date
* Modified date

Products can be managed through the Django admin panel.

---

### 📂 Category Management

The application supports product categorization.

Each category contains:

* Category name
* Slug
* Description
* Category image

Users can browse products belonging to a specific category.

---

### 🔎 Product Search

The store currently supports searching by:

* Product name
* Product description
* Category name

Search results are displayed through the store page.

---

### 📄 Product Pagination

Products are paginated on the store page to avoid displaying all products on a single page.

---

### 🛒 Shopping Cart

The current cart system uses Django sessions.

Users can:

* Add products to cart
* Select product color
* Select product size
* Increase quantity
* Decrease quantity
* Remove products
* View item subtotal
* View cart subtotal
* View tax
* View grand total

The cart differentiates products based on their:

**Product + Color + Size**

This allows the same product to be added with different variations.

---

### 🎨 Product Variations

Before adding a product to the cart, the user is currently required to select:

* Color
* Size

This information is preserved throughout the cart and order process.

---

### 💳 Checkout

The checkout page currently collects:

* First name
* Last name
* Phone number
* Email
* Address
* City
* State
* Pincode

The checkout also displays:

* Cart items
* Subtotal
* Tax
* Shipping fee
* Grand total

Users can currently select a payment method such as:

* Cash on Delivery
* Online Payment

> **Note:** An actual online payment gateway has not yet been integrated. The payment method is currently stored with the order.

---

### 📦 Order Management

After checkout, an order is created with:

* Customer information
* Delivery information
* Order subtotal
* Tax
* Shipping fee
* Grand total
* Payment method
* Order status
* Order creation/update timestamps

Each order also contains its individual ordered products, including:

* Product
* Quantity
* Product price
* Color
* Size

Current order statuses include:

* New
* Accepted
* Completed
* Cancelled

---

### 📋 User Dashboard

Logged-in users can view their previous orders through the dashboard.

The dashboard currently displays:

* Order number
* Order date
* Delivery information
* Payment method
* Order total
* Ordered products
* Product quantity
* Current order status

Some dashboard actions such as tracking, returns/refunds, settings, and selling items are currently placeholders and are planned for future development.

---

### ⚙️ Django Admin

The Django admin panel currently provides management for:

* Users
* Categories
* Products
* Orders
* Order products

Administrators can manage product availability, product information, categories, and order status.

---

## 🧰 Tech Stack

### Backend

* **Python**
* **Django**

### Frontend

* **HTML5**
* **CSS3**
* **Bootstrap**
* **JavaScript**
* **Font Awesome**

### Database

* **SQLite3**

### Authentication

* Django Authentication System
* Custom `Account` user model
* Email-based login

### Other Django Components

* Django Sessions
* Django ORM
* Django Templates
* Django Admin
* Django Static Files
* Django Media Files
* Django Pagination

---

## 🏗️ Project Structure

```text
AdiKart/
│
├── AdiKart/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── category/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── migrations/
│
├── store/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── cart/
│   ├── views.py
│   ├── urls.py
│   ├── context_processors.py
│   └── migrations/
│
├── orders/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── templates/
│   ├── accounts/
│   ├── orders/
│   ├── store/
│   ├── base.html
│   └── home.html
│
├── static/
│
├── media/
│
├── manage.py
│
└── db.sqlite3
```

---

## 🔄 Current Application Flow

```text
Home Page
    ↓
Browse Products
    ↓
Search / Category Filter
    ↓
Product Details
    ↓
Select Color & Size
    ↓
Add to Cart
    ↓
Shopping Cart
    ↓
Update Quantity
    ↓
Checkout
    ↓
Enter Delivery Details
    ↓
Select Payment Method
    ↓
Place Order
    ↓
Order Created
    ↓
User Dashboard
    ↓
View Order History
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AdiKart.git
```

```bash
cd AdiKart
```

---

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv env
```

Activate it:

```bash
env\Scripts\activate
```

#### Git Bash

```bash
source env/Scripts/activate
```

---

### 3. Install Dependencies

```bash
pip install django pillow
```

If a `requirements.txt` file is added later, dependencies can be installed using:

```bash
pip install -r requirements.txt
```

---

### 4. Apply Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create the administrator account.

---

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

---

## 🔐 Authentication Flow

The current authentication workflow is:

```text
Register
   ↓
Account Created
   ↓
Account Activation
   ↓
Login
   ↓
Authenticated User
   ↓
Dashboard / Shopping / Checkout
```

The project uses a custom `Account` model instead of Django's default user model.

---

## 🗄️ Database Models

The current application contains the following major models:

### Account

Stores user information and authentication-related fields.

### Category

Stores product categories.

### Product

Stores product information and its category relationship.

### Order

Stores customer, delivery, payment, pricing, and order-status information.

### OrderProduct

Stores individual products belonging to an order, including quantity, price, color, and size.

---

## 📊 Current Project Status

| Module                             | Status        |
| ---------------------------------- | ------------- |
| Django Project Setup               | ✅ Implemented |
| Custom User Model                  | ✅ Implemented |
| Registration                       | ✅ Implemented |
| Account Activation                 | ✅ Implemented |
| Login / Logout                     | ✅ Implemented |
| Password Reset                     | ✅ Implemented |
| Categories                         | ✅ Implemented |
| Product Management                 | ✅ Implemented |
| Product Search                     | ✅ Implemented |
| Category Filtering                 | ✅ Implemented |
| Pagination                         | ✅ Implemented |
| Product Details                    | ✅ Implemented |
| Color Selection                    | ✅ Implemented |
| Size Selection                     | ✅ Implemented |
| Session Cart                       | ✅ Implemented |
| Quantity Management                | ✅ Implemented |
| Checkout                           | ✅ Implemented |
| Order Creation                     | ✅ Implemented |
| Order History                      | ✅ Implemented |
| Django Admin                       | ✅ Implemented |
| Online Payment Gateway             | 🚧 Planned    |
| Order Tracking                     | 🚧 Planned    |
| Returns & Refunds                  | 🚧 Planned    |
| Wishlist                           | 🚧 Planned    |
| Reviews & Ratings                  | 🚧 Planned    |
| Advanced Seller Features           | 🚧 Planned    |
| Production Deployment Improvements | 🚧 Planned    |

---

# 🛠️ Planned Features

AdiKart is an ongoing project. The following features are planned for future versions.

### 💳 Payment Integration

* Razorpay / Stripe integration
* Online payment processing
* Payment verification
* Payment success/failure handling
* Transaction records

### 📦 Advanced Order Management

* Order tracking
* Order details page
* Order cancellation
* Return requests
* Refund management
* Order status timeline

### ❤️ Wishlist

* Add/remove products from wishlist
* Wishlist page
* Move wishlist items to cart

### ⭐ Reviews & Ratings

* Product reviews
* Star ratings
* User-specific reviews
* Review moderation

### 👤 Improved User Dashboard

* Profile management
* Address management
* Saved addresses
* Transaction history
* Better order details
* Account settings

### 🛍️ Advanced Shopping Features

* Product filtering
* Price range filtering
* Sorting
* Multiple product images
* Better product variations
* Stock management
* Related products
* Recently viewed products

### 🔔 Notifications

* Order confirmation emails
* Order status emails
* Payment notifications
* Account-related notifications

### 📧 Production Email Configuration

The current development configuration uses Django's console email backend.

A production email service will be integrated in a future version for:

* Account activation
* Password reset
* Order confirmation
* Order status updates

### 🔐 Security & Production Improvements

Future versions will include additional production-level improvements such as:

* Environment variables for secrets
* Production email configuration
* Secure deployment configuration
* Better validation
* Improved error handling
* Production database configuration
* Security hardening

---

## 🎯 Future Vision

The long-term goal of AdiKart is to evolve from a basic e-commerce application into a more complete online shopping platform.

Planned architecture:

```text
                    ┌───────────────────┐
                    │      AdiKart      │
                    └─────────┬─────────┘
                              │
          ┌───────────────────┼───────────────────┐
          ↓                   ↓                   ↓
     Customers            Products             Orders
          │                   │                   │
          ↓                   ↓                   ↓
 Authentication        Categories          Order Tracking
          │                   │                   │
          ↓                   ↓                   ↓
       Cart              Wishlist           Payments
          │                   │                   │
          └───────────────────┼───────────────────┘
                              ↓
                       User Dashboard
```

---

## 📚 What This Project Demonstrates

AdiKart is also a practical Django project demonstrating concepts such as:

* Django project architecture
* Multiple Django applications
* Custom user authentication
* Django ORM
* Model relationships
* Foreign keys
* Django sessions
* Session-based cart implementation
* CRUD operations
* Django templates
* Template inheritance
* Context processors
* Pagination
* Search using Django `Q` objects
* File and image uploads
* Authentication decorators
* Django admin customization
* Order and cart workflows
* Database migrations
* Static and media file management

---

## 🚧 Development Note

This repository represents the **current development stage** of AdiKart and should not be considered the final version of the application.

Features are being added progressively. Some sections visible in the user interface, such as order tracking, returns/refunds, settings, and seller-related functionality, are currently placeholders and will be implemented in future updates.

The project structure and functionality will continue to evolve as new features are added.

---

## 👨‍💻 Developer

**Aditya Narayan**

Computer Science & Engineering

---

## ⭐ Future Updates

This README will be updated as new functionality is implemented.

Future releases may include:

```text
v1.0  → Core E-Commerce
v1.1  → Improved Product & Cart Features
v1.2  → Payment Integration
v1.3  → Wishlist & Reviews
v1.4  → Advanced Order Management
v2.0  → Expanded E-Commerce Platform
```

---

## 📌 Project Status

**AdiKart — 🚧 Actively Under Development**

> Built with Django, improved through continuous development, and gradually evolving into a complete e-commerce platform.

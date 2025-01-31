# Khuchra Workers

Khuchra Workers is a freelancing and micro-task platform designed to connect clients with freelancers and volunteers for various tasks. The platform supports job posting, bidding, messaging, payments, and reviews to ensure a smooth workflow between clients and service providers.

## Planned Features

### ✅ **Core Features**
- **User Authentication**: Secure authentication using Firebase Authentication.
- **Client Portal**:
  - Job posting and management
  - View and manage freelancer bids
  - Track job progress and deliverables
  - Leave reviews for freelancers
- **Freelancer Portal**:
  - Browse and bid on jobs
  - Manage ongoing projects
  - Submit deliverables
  - Receive reviews from clients
- **Administrator Dashboard**:
  - Manage users, jobs, and payments
  - Review and approve job postings
  - Resolve disputes
- **Real-time Messaging**: Secure chat between clients and freelancers.
- **Payments & Invoices**: Integrated payments via Stripe API with transaction tracking.
- **Review System**: Clients and freelancers can rate each other after job completion.
- **Landing Page**: Informative homepage with pricing, testimonials, blogs, and a call to action.

---

## Project Structure

```
khuchraworkers/
│── common/                 # Shared models, views, and templates
│── authentication/         # User authentication & management
│── administrator/          # Admin dashboard for managing users, jobs, payments
│── client/                 # Client-side features (job posting, hiring)
│── freelancer/             # Freelancer-side features (bidding, job execution)
│── landingpage/            # Public-facing pages (home, pricing, testimonials)
│── payments/               # Payment processing & invoices
│── messages/               # Messaging between clients & freelancers
│── reviews/                # Review & rating system
│── static/                 # Static assets (CSS, JavaScript, images)
│── templates/              # HTML templates for rendering views
│── manage.py               # Django management script
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation
```

---

## Getting Started

### 🔧 **Prerequisites**
- Python 3.10+
- Django 5+
- PostgreSQL

### 🚀 **Setup Instructions**

1️⃣ **Clone the repository**:
```bash
git clone https://github.com/yourusername/khuchraworkers.git
cd khuchraworkers
```

2️⃣ **Create a virtual environment**:
```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

3️⃣ **Install dependencies**:
```bash
pip install -r requirements.txt
```

4️⃣ **Configure environment variables**:
Create a `.env` file in the project root and add necessary configurations:
```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgresql://username:password@localhost:5432/khuchraworkers
```

5️⃣ **Run database migrations**:
```bash
python manage.py migrate
```

6️⃣ **Create a superuser**:
```bash
python manage.py createsuperuser
```

7️⃣ **Start the development server**:
```bash
python manage.py runserver
```

8️⃣ **Access the application**:
- Open `http://127.0.0.1:4090/` in your browser.

---

## 🚧 Future Plans
- **Job recommendation system** based on freelancer skills.
- **Mobile app support** for Android & iOS.
- **Enhanced dispute resolution** and arbitration features.
- **Integration with external freelancing APIs**.
- **Performance optimizations** for handling high traffic.

---

## 📜 License
This project is licensed under the MIT License.

---

## 🤝 Contributing
Pull requests and contributions are welcome! Please fork the repository and submit a PR with your changes.

---

## 📬 Contact
For any questions, feel free to reach out:
- **Email**: sadat.arefin.rafat@gmail.com
- **GitHub**: [SadatArefin](https://github.com/SadatArefin)
- **LinkedIn**: [Sadat Arefin Rafat](https://linkedin.com/in/sadat-arefin-rafat)

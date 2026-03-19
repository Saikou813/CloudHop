# ☁️ CloudHop | Full-Stack Flight Booking System

CloudHop is a premium flight booking platform built with **Django** and **PostgreSQL**. It allows users to search for specific flight routes, manage their travel itineraries, and maintain a personal travel profile.

## Features

- **Flight Search:** Custom "From/To" search logic using Django Q objects.

- **Booking Engine:** Real-time seat availability tracking and overbooking protection.

- **User Profiles:** Automated profile creation via Django Signals to store passport and frequent flyer data.

- **Customer Support:** Integrated contact system that records user requests in the database.# ☁️ CloudHop | Full-Stack Flight Booking System

### Ready for Takeoff? 🛫

![CloudHop Responsive Mockup](docs/images/screenshots/am_i_responsive.png)

CloudHop is a premium flight booking platform built with **Django** and **PostgreSQL**. It allows users to search for real-time flight routes, manage personal travel itineraries with full CRUD functionality, and maintain a secure travel profile.

**[Visit the Live Website](https://cloud-hop-5647c9f84dbd.herokuapp.com)**

---

## 🚀 Key Features

- **Smart Flight Search:** Filter by origin and destination using dynamic dropdowns and Django Q objects.

- **Full CRUD Itinerary:**

- **Create:** Book flights with real-time seat tracking.

- **Read:** View personalized trip cards with destination imagery.

- **Update:** Edit passenger names and seat preferences.

- **Delete/Rebook:** "Soft-delete" (cancel) or "Hard-delete" (wipe) bookings with confirmation screens.

- **User Profiles:** Automatic profile creation via **Django Signals** to store Passport and Frequent Flyer data.

- **Responsive UI:** A premium "Cloud-Grey" aesthetic built with **Bootstrap 5**.

---

## Tech Stack & Dependencies

- **Backend:** Django 4.2 (Python 3.12)

- **Database:** PostgreSQL (Heroku Postgres)

- **Image Hosting:** Cloudinary

- **Authentication:** Django Allauth

- **Deployment:** Heroku

- **HTML5 / CSS3 / JavaScript** (Frontend)

- **Bootstrap 5** (Styling)

### **Core Libraries**

- **Django-allauth:** Secure authentication and registration.

- **Django-crispy-forms:** Professional form rendering.

- **Cloudinary:** Cloud-based media management for destination images.

- **WhiteNoise:** Efficient static file serving on Heroku.

- **Gunicorn:** Python WSGI HTTP Server.

### **Full Dependency List**

``` text
asgiref==3.7.2
cloudinary==1.36.0
crispy-bootstrap5==0.7
dj-database-url==0.5.0
dj3-cloudinary-storage==0.0.6
Django==4.2.11
django-allauth==0.57.2
django-crispy-forms==2.1
gunicorn==20.1.0
psycopg2==2.9.9
sqlparse==0.4.4
whitenoise==5.3.0
```

---

## 📸 Deployment & Setup

1. **Environment Variables:** Ensure `SECRET_KEY`, `DATABASE_URL`, and `CLOUDINARY_URL` are set in your `env.py` or Heroku Config Vars.

2. **Migrations:** Run `python manage.py migrate` to sync the Flight and Booking models.

3. **Static Files:** Run `python manage.py collectstatic` for production CSS/JS.

---

## 🧪 Testing Summary

- **Manual CRUD:** Verified all Book/Edit/Cancel/Delete loops.

- **Validation:** Python code adheres to **PEP8** standards.

- **Defensive Design:** Confirmation pages implemented for all destructive (Delete) actions.

---

## ✍️ Credits

- **Images:** Unsplash & Cloudinary.

- **Icons:** FontAwesome (Passport/Flight icons).

- **Collaboration:** Built in an Authentic Adaptive Collaboration with an AI partner for logic refinement.

- **Responsive Design:** Mobile-first UI built with Bootstrap 5.

## Built with AI Collaboration

This project was developed in an **Authentic Adaptive Collaboration** with an AI assistant.

- **Pair Programming:** The AI acted as a senior developer, providing guidance on complex logic like Django Signals and Model Properties.

- **Logic Refinement:** Together, we iterated on the "Seat Counter" and "Search Filtering" to ensure the app behaves like a real-world airline system.

- **Deployment & Debugging:** The AI provided real-time troubleshooting for Heroku deployment errors and database migration issues.

## Requirements Met

- **Original Custom Models:**

- `Booking`: Custom status logic (Confirmed/Cancelled).

- `PassengerProfile`: Linked via Signals.

- `ContactMessage`: Recording user inputs to the DB.

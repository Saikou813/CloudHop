# ☁️ CloudHop | Full-Stack Flight Booking System

CloudHop is a premium flight booking platform built with **Django** and **PostgreSQL**. It allows users to search for specific flight routes, manage their travel itineraries, and maintain a personal travel profile.

## Features

- **Flight Search:** Custom "From/To" search logic using Django Q objects.
- **Booking Engine:** Real-time seat availability tracking and overbooking protection.
- **User Profiles:** Automated profile creation via Django Signals to store passport and frequent flyer data.
- **Customer Support:** Integrated contact system that records user requests in the database.
- **Responsive Design:** Mobile-first UI built with Bootstrap 5.

## Tech Stack

- **Backend:** Django 4.2 (Python 3.12)
- **Database:** PostgreSQL (Heroku Postgres)
- **Image Hosting:** Cloudinary
- **Authentication:** Django Allauth
- **Deployment:** Heroku

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

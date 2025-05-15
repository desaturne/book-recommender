# 📚 Book Recommender System

A simple and interactive web application that recommends books based on popularity and user preferences. Built with Flask, Bootstrap, and deployed on [Render](https://render.com/).

🌐 **Live Demo:**  
👉 [https://book-recommender-ppjn.onrender.com](https://book-recommender-ppjn.onrender.com)

---

## ✨ Features

- 🔥 Top 50 Popular Books (based on ratings and votes)
- 📖 Book Recommendation based on similar preferences
- 📷 Displays book cover images, ratings (rounded to 2 decimal places), and authors
- ⚡ Clean and responsive UI using Bootstrap 5
- ☁️ Hosted for free using Render

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, Bootstrap 5, Jinja2
- **Backend:** Flask (Python)
- **Deployment:** Render
- **Data Handling:** Pandas, Pickle (for preprocessed recommendation data)

---

## 🚀 Getting Started Locally

### Prerequisites

- Python 3.7 or above
- Git

### Clone the Repository

    ```bash
    git clone https://github.com/desaturne/book-recommender.git
    cd book-recommender

## 🛠️ Installation

It's recommended to use a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    

## 💻 Run the Application

    ```bash
    python app.py

## 🗂️ Project Structure

book-recommender/
│
├── static/              # Static assets (CSS, JS, Images)
├── templates/           # HTML templates
│   ├── index.html
│   └── recommend.html
├── popular.pkl          # Pickled data for popularity-based recommendation
├── similarity.pkl       # Cosine similarity matrix
├── final_df.pkl         # Dataframe used in recommendation
├── app.py               # Flask application
├── requirements.txt     # Python dependencies
└── README.md            # This file

## 🙏 Credits

This project was inspired by and adapted from the CampusX Book Recommendation tutorial. Special thanks to their amazing tutorials and content.
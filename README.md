# 🎬 Movie Recommendation System

A Content-Based Movie Recommendation System built using **Python, Flask, Pandas, Scikit-learn, and NLP**. This application recommends similar movies based on movie metadata such as genres, keywords, cast, crew, and overview.

---

## 📌 Features

- 🔍 Search any movie by name
- 🎯 Get Top 5 similar movie recommendations
- 🌐 Flask Web Application
- 📊 Content-Based Recommendation System
- 🧠 NLP-based feature engineering
- 🎨 Responsive and clean UI

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### Machine Learning
- Pandas
- NumPy
- Scikit-learn
- CountVectorizer
- Cosine Similarity

### Frontend
- HTML
- CSS
- Jinja2

---

## 📂 Project Structure

```
movie recomm/
│
├── app.py
├── model.ipynb
├── movies.pkl
├── similarity.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── css/
│       └── style.css
│
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
```

### Move to Project Folder

```bash
cd movie-recommendation-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask App

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

1. Load the movie dataset.
2. Merge movie and credits datasets.
3. Perform data preprocessing.
4. Create a **tags** feature using:
   - Overview
   - Genres
   - Keywords
   - Cast
   - Crew
5. Convert text into vectors using **CountVectorizer**.
6. Calculate similarity using **Cosine Similarity**.
7. Store processed data using **Pickle**.
8. Flask loads the model and recommends the Top 5 similar movies.

---

## 📚 Concepts Used

- Data Preprocessing
- Feature Engineering
- Natural Language Processing (NLP)
- Bag of Words
- CountVectorizer
- Cosine Similarity
- Content-Based Recommendation System
- Flask
- HTML & CSS
- Jinja2
- Pickle Serialization

---

## 📸 Screenshots

_Add screenshots of your application here._

Example:

- Home Page
- Search Result

---

## 🚀 Future Improvements

- Movie Posters
- TMDB API Integration
- Movie Ratings
- Autocomplete Search
- Responsive UI
- Dark Theme Improvements

---

## 👨‍💻 Author

**Rajeev Kumar**

GitHub: https://github.com/your-github-username

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.

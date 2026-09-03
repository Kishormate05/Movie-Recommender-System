# 🎬 Movie Recommendation System

> A Machine Learning based content recommendation system that suggests
> similar movies using movie metadata and cosine similarity.

## 📌 Overview

This project uses **Content-Based Filtering** to recommend the top 5
movies similar to a selected movie. It combines Machine Learning, data
preprocessing, cosine similarity, TMDB API integration, and Streamlit to
provide an interactive movie discovery experience.

## ✨ Features

-   🎥 Select a movie and get 5 similar recommendations
-   🤖 Content-Based Movie Recommendation
-   🧠 Cosine Similarity based recommendation engine
-   🖼️ Movie posters using TMDB API
-   ⚡ Fast recommendations using a precomputed similarity matrix
-   🎨 Professional Streamlit interface
-   🚀 Live Streamlit deployment

## 🛠️ Tech Stack

**Python • Pandas • NumPy • Scikit-learn • Streamlit • TMDB API • Git •
Git LFS**

## ⚙️ How It Works

``` text
Movie Dataset
     ↓
Data Preprocessing
     ↓
Feature Engineering
     ↓
Vectorization
     ↓
Cosine Similarity
     ↓
Top 5 Recommendations
     ↓
TMDB Posters
```

## 📂 Project Structure

``` text
Movie-Recommender-System/
├── app.py
├── Recommendation_System_ML_Logic.ipynb
├── movies.pkl
├── movies_dic.pkl
├── similarity.pkl
├── requirements.txt
├── .gitattributes
└── .gitignore
```

## 🚀 Run Locally

``` bash
git clone https://github.com/Kishormate05/Movie-Recommender-System.git
cd Movie-Recommender-System
pip install -r requirements.txt
streamlit run app.py
```

### 🔐 TMDB API Setup

Create `.streamlit/secrets.toml`:

``` toml
TMDB_API_KEY = "YOUR_TMDB_API_KEY"
```

## 🌐 Live Demo

👉 **[Launch Movie
Recommender](https://ai-movie-recommender-ml.streamlit.app/)**

## 👨‍💻 Author

**Kishormate05**

Machine Learning • Data Science • Generative AI • Agentic AI

⭐ If you find this project useful, consider giving it a star!

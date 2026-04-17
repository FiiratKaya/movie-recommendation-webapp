# Movie Recommendation Web App

## Overview
This project is a Streamlit-based movie recommendation web application that suggests similar movies based on genre and overview text.

## Project Goal
The goal of this project is to turn a recommendation algorithm into an interactive web application that users can directly interact with.

## Technologies Used
- Python
- Streamlit
- Pandas
- Scikit-learn

## Features
- Interactive movie selection
- Content-based recommendation system
- Clean and simple user interface

## Dataset
The project uses a small movie dataset containing:
- Title
- Genre
- Overview

## How It Works
- Combines genre and overview into one text feature
- Converts text into vectors using CountVectorizer
- Calculates similarity with cosine similarity
- Returns the top 5 most similar movies

## Project Structure
```bash
movie-recommendation-webapp/
├── data/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

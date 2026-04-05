import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Movie Recommendation App", page_icon="🎬")

st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get similar recommendations.")

@st.cache_data
def load_data():
    df = pd.read_csv("data/movies.csv")
    df["combined_features"] = df["genre"] + " " + df["overview"]
    return df

@st.cache_resource
def compute_similarity(df):
    vectorizer = CountVectorizer()
    feature_matrix = vectorizer.fit_transform(df["combined_features"])
    similarity = cosine_similarity(feature_matrix)
    return similarity

df = load_data()
similarity = compute_similarity(df)

movie_list = df["title"].tolist()
selected_movie = st.selectbox("Choose a movie:", movie_list)

def recommend(movie_title):
    index = df[df["title"] == movie_title].index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    for i in scores[1:6]:
        recommendations.append(df.iloc[i[0]]["title"])
    return recommendations

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write(f"- {movie}")
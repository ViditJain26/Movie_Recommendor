import streamlit as st
import pickle
import pandas as pd

# Page Configurations
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Recommender System")
st.markdown("Discover movies matching your favorite titles using content-based vector similarity filters.")

# Safeguarded Model Loading
@st.cache_resource
def load_model_data():
    try:
        movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
        movies_df = pd.DataFrame(movies_dict)
        similarity_matrix = pickle.load(open('similarity.pkl', 'rb'))
        return movies_df, similarity_matrix
    except FileNotFoundError:
        st.error("⚠️ Pickled tracking assets missing! Ensure 'movies_dict.pkl' and 'similarity.pkl' exist in the root folder.")
        return None, None

new_df, similarity = load_model_data()

if new_df is not None and similarity is not None:
    # Match drop-down options against exact dataset titles
    movie_list = new_df['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the catalog:",
        movie_list
    )

    # Core Content Recommendation Algorithm
    def recommend(movie):
        movie_index = new_df[new_df['title'] == movie].index[0]
        distances = similarity[movie_index]
        
        # Sort and track via indices matching your exact notebook logic
        recommended_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        
        recommendations = []
        for item in recommended_list:
            recommendations.append(new_df.iloc[item[0]].title)
        return recommendations

    # Display suggestions on execution trigger
    if st.button("Generate Recommendations", type="primary"):
        with st.spinner("Calculating vector mapping distances..."):
            results = recommend(selected_movie)
            
            st.subheader("🎉 Top 5 Recommended Movies:")
            for index, title in enumerate(results, 1):
                st.markdown(f"**{index}.** {title}")
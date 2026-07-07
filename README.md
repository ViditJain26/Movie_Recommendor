# 🎬 Movie Recommender System

An interactive, data-driven web application that suggests movies based on content similarity. This project utilizes a Content-Based Filtering approach to calculate vector distances between movie metadata features (genres, keywords, cast, crew, and overview) to provide accurate recommendations.

🖲️ **Live Application:** [Launch Live Web App](https://movierecommendor-aomqcvwwgywwjyunhngsqx.streamlit.app)

---

## 🚀 Features
* **Content-Based Filtering:** Recommends movies based on structural metadata tags and textual vector alignments.
* **Interactive UI:** Built using Streamlit to offer a clean drop-down movie selector and smooth user interactions.
* **Optimized Storage via Git LFS:** Utilizes Git Large File Storage to seamlessly track and host compressed pipeline files (.pkl matrices) on GitHub.

---

## 🛠️ Tech Stack & Libraries
* **Language:** Python 3.x
* **Web Framework:** Streamlit
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (CountVectorizer, cosine_similarity)
* **Version Control:** Git & Git LFS (Large File Storage)

---

## 🏗️ How It Works (Machine Learning Pipeline)
1. **Data Preprocessing:** Cleans and tokenizes features such as movie genres, keywords, cast, and crew from raw metadata.
2. **Vectorization:** Converts the combined textual "tags" into numeric token vectors using Scikit-Learn's CountVectorizer.
3. **Similarity Matrix:** Computes spatial angles between vectors using Cosine Similarity to construct a relative distance matrix.
4. **Recommendation Engine:** Fetches the top 5 closest mathematical neighbors for any selected movie title and displays them instantly.

---

## 💻 Local Setup & Installation

To run this project on your local machine, follow these steps:

1. **Clone the Repository:**
   \`\`\`bash
   git clone https://github.com/ViditJain26/Movie_Recommendor.git
   cd Movie_Recommendor
   \`\`\`

2. **Install System-Level Git LFS:**
   Ensure you have Git LFS installed on your local OS, then run:
   \`\`\`bash
   git lfs install
   git lfs pull
   \`\`\`

3. **Install Dependencies:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Launch the Local Server:**
   \`\`\`bash
   streamlit run app.py
   \`\`\`

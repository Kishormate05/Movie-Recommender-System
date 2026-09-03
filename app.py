import streamlit as st
import pickle
import requests
import os


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="CineMatch | Movie Recommender",
    page_icon="🎬",
    layout="wide"
)


# =========================================================
# PROFESSIONAL CSS
# =========================================================

st.html("""
<style>

.stApp {
    background:
        radial-gradient(circle at 15% 5%, rgba(99, 45, 180, 0.20), transparent 30%),
        radial-gradient(circle at 90% 10%, rgba(229, 9, 20, 0.13), transparent 30%),
        #08090d;
}

.main .block-container {
    max-width: 1250px;
    padding-top: 1rem;
    padding-bottom: 4rem;
}

/* Hide default Streamlit footer */
footer {
    visibility: hidden;
}

/* ================= NAVBAR ================= */

.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 18px 0;
    margin-bottom: 30px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
}

.logo {
    font-size: 26px;
    font-weight: 800;
    color: white;
}

.logo-red {
    color: #e50914;
}

.nav-label {
    color: #888b96;
    font-size: 13px;
}

/* ================= HERO ================= */

.hero {
    text-align: center;
    padding: 45px 10px 40px;
}

.badge {
    display: inline-block;
    padding: 8px 16px;
    border-radius: 50px;
    background: rgba(229,9,20,0.10);
    border: 1px solid rgba(229,9,20,0.30);
    color: #ff6972;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.6px;
    margin-bottom: 22px;
}

.hero-title {
    font-size: 60px;
    line-height: 1.05;
    font-weight: 850;
    letter-spacing: -3px;
    color: white;
    margin: 0;
}

.hero-red {
    color: #e50914;
}

.hero-description {
    max-width: 700px;
    margin: 22px auto 0;
    color: #9b9da7;
    font-size: 16px;
    line-height: 1.7;
}

/* ================= STATS ================= */

.stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin: 10px 0 50px;
}

.stat {
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 24px;
    text-align: center;
}

.stat-number {
    color: white;
    font-size: 28px;
    font-weight: 800;
}

.stat-label {
    color: #777a85;
    font-size: 12px;
    margin-top: 5px;
}

/* ================= SECTION ================= */

.section-heading {
    color: white;
    font-size: 25px;
    font-weight: 750;
    margin-bottom: 6px;
}

.section-description {
    color: #777a85;
    font-size: 13px;
    margin-bottom: 18px;
}

/* ================= MOVIE CARDS ================= */

.movie-rank {
    display: inline-block;
    background: rgba(229,9,20,0.12);
    border: 1px solid rgba(229,9,20,0.25);
    color: #ff6b73;
    border-radius: 6px;
    padding: 4px 8px;
    margin-top: 8px;
    font-size: 10px;
    font-weight: 700;
}

.movie-title {
    color: white;
    font-size: 14px;
    font-weight: 700;
    line-height: 1.4;
    margin-top: 8px;
    min-height: 40px;
}

.movie-match {
    color: #626570;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* ================= INFO ================= */

.info-card {
    background: linear-gradient(
        135deg,
        rgba(229,9,20,0.08),
        rgba(255,255,255,0.025)
    );
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 25px;
    margin-top: 35px;
}

.info-title {
    color: white;
    font-size: 17px;
    font-weight: 750;
    margin-bottom: 10px;
}

.info-text {
    color: #90929c;
    font-size: 13px;
    line-height: 1.7;
}

/* ================= FOOTER ================= */

.custom-footer {
    text-align: center;
    color: #626570;
    font-size: 12px;
    margin-top: 60px;
    padding-top: 25px;
    border-top: 1px solid rgba(255,255,255,0.07);
}

.footer-red {
    color: #e50914;
    font-weight: 700;
}

/* ================= RESPONSIVE ================= */

@media (max-width: 800px) {

    .hero-title {
        font-size: 40px;
    }

    .stats {
        grid-template-columns: 1fr;
    }

    .nav-label {
        display: none;
    }
}

</style>
""")


# =========================================================
# API KEY
# =========================================================

try:
    TMDB_API_KEY = st.secrets["TMDB_API_KEY"]
except Exception:
    TMDB_API_KEY = os.getenv("TMDB_API_KEY")

if not TMDB_API_KEY:
    st.error("TMDB API key is not configured.")
    st.stop()


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_data():

    with open("movies.pkl", "rb") as file:
        movies_data = pickle.load(file)

    with open("similarity.pkl", "rb") as file:
        similarity_data = pickle.load(file)

    return movies_data, similarity_data


movies, similarity = load_data()


# =========================================================
# NAVBAR
# =========================================================

st.html("""
<div class="navbar">
    <div class="logo">
        🎬 Cine<span class="logo-red">Match</span>
    </div>

    <div class="nav-label">
        ML-Powered Movie Discovery
    </div>
</div>
""")


# =========================================================
# HERO
# =========================================================

st.html("""
<div class="hero">

    <div class="badge">
        ✨ MACHINE LEARNING RECOMMENDER
    </div>

    <div class="hero-title">
        Discover your next<br>
        <span class="hero-red">favorite movie.</span>
    </div>

    <div class="hero-description">
        Explore movies similar to the ones you love.
        Our content-based recommendation engine analyzes
        movie characteristics and finds your next watch.
    </div>

</div>
""")


# =========================================================
# STATISTICS
# =========================================================

movie_count = len(movies)

st.html(f"""
<div class="stats">

    <div class="stat">
        <div class="stat-number">{movie_count:,}+</div>
        <div class="stat-label">Movies in Dataset</div>
    </div>

    <div class="stat">
        <div class="stat-number">5</div>
        <div class="stat-label">Recommendations</div>
    </div>

    <div class="stat">
        <div class="stat-number">ML</div>
        <div class="stat-label">Content-Based Filtering</div>
    </div>

</div>
""")


# =========================================================
# MOVIE SELECTION
# =========================================================

st.html("""
<div class="section-heading">
    🎥 Find movies similar to yours
</div>

<div class="section-description">
    Choose a movie and generate intelligent recommendations.
</div>
""")


movie_list = movies["title"].values

selected_movie = st.selectbox(
    "Select a movie",
    movie_list,
    label_visibility="collapsed"
)


# =========================================================
# POSTER FUNCTION
# =========================================================

@st.cache_data
def fetch_poster(movie_id):

    url = (
        f"https://api.themoviedb.org/3/movie/"
        f"{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    )

    try:

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:

            return (
                "https://image.tmdb.org/t/p/w500/"
                + poster_path
            )

    except requests.RequestException:
        pass

    return "https://via.placeholder.com/300x450?text=No+Image"


# =========================================================
# RECOMMENDATION ENGINE
# =========================================================

def recommend(movie):

    index = movies[movies["title"] == movie].index[0]

    distances = list(
        enumerate(similarity[index])
    )

    distances = sorted(
        distances,
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_names = []
    recommended_posters = []

    for i in distances:

        movie_id = movies.iloc[i[0]].id

        recommended_names.append(
            movies.iloc[i[0]].title
        )

        recommended_posters.append(
            fetch_poster(movie_id)
        )

    return recommended_names, recommended_posters


# =========================================================
# BUTTON
# =========================================================

if st.button(
    "🚀  Generate Recommendations",
    use_container_width=True
):

    with st.spinner("Analyzing movie similarity..."):

        names, posters = recommend(
            selected_movie
        )


    # =====================================================
    # RESULTS HEADER
    # =====================================================

    st.html(f"""
    <div class="section-heading">
        🎯 Recommended Movies
    </div>

    <div class="section-description">
        Movies similar to <strong>{selected_movie}</strong>
    </div>
    """)


    # =====================================================
    # MOVIE CARDS
    # =====================================================

    cols = st.columns(5)

    for i in range(5):

        with cols[i]:

            st.image(
                posters[i],
                use_container_width=True
            )

            st.html(f"""
            <div class="movie-rank">
                #{i + 1} MATCH
            </div>

            <div class="movie-title">
                {names[i]}
            </div>

            <div class="movie-match">
                Content Similarity
            </div>
            """)


# =========================================================
# HOW IT WORKS
# =========================================================

st.html("""
<div class="info-card">

    <div class="info-title">
        🧠 How the Recommendation Engine Works
    </div>

    <div class="info-text">
        CineMatch uses a Content-Based Filtering approach.
        Movie metadata is converted into numerical feature
        representations and similarity is calculated between
        movies. The system then identifies the closest matches
        and retrieves their posters using the TMDB API.
    </div>

</div>
""")


# =========================================================
# TECHNOLOGY STACK
# =========================================================

st.html("""
<div class="info-card">

    <div class="info-title">
        ⚙️ Technology Stack
    </div>

    <div class="info-text">
        Python &nbsp; • &nbsp;
        Pandas &nbsp; • &nbsp;
        NumPy &nbsp; • &nbsp;
        Scikit-learn &nbsp; • &nbsp;
        Streamlit &nbsp; • &nbsp;
        TMDB API
    </div>

</div>
""")


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="custom-footer">

    Built with ❤️ using
    <span class="footer-red">Machine Learning</span>
    & Streamlit

    <br>

    🎬 CineMatch — Intelligent Movie Discovery

</div>
""")
import streamlit as st

from ui import apply_theme, sidebar_brand, footer


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Contact | LoanGuard AI",
    page_icon="📬",
    layout="wide"
)


# ==========================================================
# COMMON UI
# ==========================================================

apply_theme()
sidebar_brand()


# ==========================================================
# HEADER
# ==========================================================

st.title("📬 Project & Contact")

st.write(
    "Welcome to the LoanGuard AI project information page."
)

st.divider()


# ==========================================================
# PROJECT INFORMATION
# ==========================================================

st.subheader("🏦 Project Information")

col1, col2 = st.columns(2)


with col1:

    with st.container(border=True):

        st.markdown("### 🤖 LoanGuard AI")

        st.write(
            "Loan Default Prediction using Machine Learning"
        )

        st.caption(
            "An academic Machine Learning project built "
            "using Python, Scikit-learn and Streamlit."
        )


with col2:

    with st.container(border=True):

        st.markdown("### 💡 Project Feedback")

        st.write(
            "Suggestions for improving this project can focus on:"
        )

        st.markdown(
            """
            - Model performance
            - User interface
            - Data analytics
            - Explainable AI
            """
        )


# ==========================================================
# TECHNOLOGY STACK
# ==========================================================

st.divider()

st.subheader("🛠️ Technology Stack")


col1, col2, col3 = st.columns(3)


with col1:

    with st.container(border=True):

        st.markdown("### 🐍 Python")

        st.write(
            "Used as the main programming language "
            "for the Machine Learning project."
        )


with col2:

    with st.container(border=True):

        st.markdown("### 🤖 Scikit-learn")

        st.write(
            "Used for Machine Learning model training, "
            "preprocessing and prediction."
        )


with col3:

    with st.container(border=True):

        st.markdown("### 🎨 Streamlit")

        st.write(
            "Used to build the interactive web application "
            "and frontend."
        )


# ==========================================================
# PROJECT DETAILS
# ==========================================================

st.divider()

st.subheader("📋 Project Details")


details = {
    "Project Name": "LoanGuard AI",
    "Project Type": "Machine Learning",
    "Problem": "Loan Default Prediction",
    "Algorithm": "Logistic Regression",
    "Frontend": "Streamlit",
    "Programming Language": "Python"
}


for key, value in details.items():

    col1, col2 = st.columns([1, 2])

    with col1:
        st.write(f"**{key}**")

    with col2:
        st.write(value)


# ==========================================================
# FUTURE ENHANCEMENTS
# ==========================================================

st.divider()

st.subheader("🚀 Future Enhancements")


future_features = [
    "📈 Model Performance Dashboard",
    "🧩 Explainable AI",
    "📊 Advanced Data Visualization",
    "🔐 Authentication System",
    "📝 Prediction History",
    "☁️ Online Deployment",
    "🔄 Multiple ML Model Comparison"
]


for feature in future_features:

    st.info(feature)


# ==========================================================
# CONTACT INFORMATION
# ==========================================================

st.divider()

st.subheader("📩 Contact")


st.write(
    """
    This section can be customized with your project team
    information, college details, GitHub repository and
    LinkedIn profile.
    """
)


col1, col2 = st.columns(2)


with col1:

    st.markdown("### 👨‍💻 Developer")

    st.write("Your Name")

    st.write("BCA / BSIT")


with col2:

    st.markdown("### 🎓 Academic Project")

    st.write("LoanGuard AI")

    st.write("Machine Learning Project")


# ==========================================================
# DISCLAIMER
# ==========================================================

st.divider()

st.warning(
    """
    ⚠️ This application is developed for academic and
    educational purposes. Predictions should not be used
    as the sole basis for real-world financial decisions.
    """
)


# ==========================================================
# FOOTER
# ==========================================================

footer()
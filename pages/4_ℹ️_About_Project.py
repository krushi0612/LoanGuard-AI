import streamlit as st

from ui import apply_theme, sidebar_brand, footer


st.set_page_config(
    page_title="About Project | LoanGuard AI",
    page_icon="ℹ️",
    layout="wide"
)

apply_theme()
sidebar_brand()


st.title("ℹ️ About LoanGuard AI")


st.markdown(
    """
    ## 🏦 What is LoanGuard AI?

    **LoanGuard AI** is a Machine Learning project developed to
    demonstrate how historical loan data can be used to predict
    the possibility of loan default.

    The project combines:

    - Data preprocessing
    - Feature engineering
    - Feature scaling
    - Machine Learning
    - Prediction
    - Data visualization
    - Streamlit frontend
    """
)


# =========================
# OBJECTIVE
# =========================

st.subheader("🎯 Project Objective")

st.write(
    """
    The main objective of this project is to develop a practical
    binary classification application that can analyze applicant
    information and estimate whether a loan applicant is likely
    to default.
    """
)


# =========================
# TECHNOLOGY
# =========================

st.subheader("🛠️ Technology Stack")


c1, c2, c3, c4 = st.columns(4)


with c1:

    st.markdown(
        """
        ### 🐍 Python

        Core programming language
        used for the ML project.
        """
    )


with c2:

    st.markdown(
        """
        ### 🐼 Pandas

        Used for dataset loading,
        preprocessing and analysis.
        """
    )


with c3:

    st.markdown(
        """
        ### 🤖 Scikit-learn

        Used for preprocessing
        and Logistic Regression.
        """
    )


with c4:

    st.markdown(
        """
        ### 🎨 Streamlit

        Used to create the
        interactive web application.
        """
    )


# =========================
# PROJECT COMPONENTS
# =========================

st.divider()

st.subheader("📁 Project Components")


components = [

    "Loan Default Dataset",
    "Machine Learning Training Notebook",
    "Trained Logistic Regression Model",
    "StandardScaler",
    "Feature Names",
    "Prediction Interface",
    "Dataset Analytics",
    "ML Workflow Explanation"
]


for component in components:

    st.markdown(
        f"""
        <div class="step">
            ✅ {component}
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================
# PROBLEM STATEMENT
# =========================

st.divider()

st.subheader("📌 Problem Statement")

st.write(
    """
    Financial institutions need to evaluate credit risk before
    approving loans. Manual evaluation can be time-consuming and
    may not always provide consistent results.

    Machine Learning can analyze historical borrower information
    and identify patterns associated with loan default.

    This project demonstrates that concept through a simple,
    interactive prediction system.
    """
)


# =========================
# FUTURE SCOPE
# =========================

st.subheader("🚀 Future Scope")

st.markdown(
    """
    - Compare multiple ML algorithms
    - Add model performance dashboard
    - Add confusion matrix
    - Add ROC-AUC visualization
    - Add feature importance
    - Add explainable AI
    - Add prediction history
    - Add user authentication
    - Deploy the application online
    """
)


st.warning(
    """
    ⚠️ This project is intended for academic and educational
    demonstration. Model predictions should not be used as the
    sole basis for real-world financial decisions.
    """
)


footer()
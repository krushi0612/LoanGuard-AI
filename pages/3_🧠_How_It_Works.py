import streamlit as st

from ui import apply_theme, sidebar_brand, footer


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="How It Works | LoanGuard AI",
    page_icon="🧠",
    layout="wide"
)

apply_theme()
sidebar_brand()


# ==========================================================
# HEADER
# ==========================================================

st.title("🧠 How LoanGuard AI Works")

st.write(
    """
    This page explains how the Machine Learning model processes
    applicant information and generates a loan default prediction.
    """
)

st.divider()


# ==========================================================
# MACHINE LEARNING PIPELINE
# ==========================================================

st.header("🔄 Machine Learning Pipeline")


steps = [
    (
        "01",
        "👤 User Input",
        "The user enters personal, employment, credit and loan information."
    ),
    (
        "02",
        "⚙️ Feature Encoding",
        "Categorical values are converted into numerical features."
    ),
    (
        "03",
        "📏 Feature Scaling",
        "The saved StandardScaler transforms the input features."
    ),
    (
        "04",
        "🤖 Logistic Regression",
        "The processed features are passed to the trained Logistic Regression model."
    ),
    (
        "05",
        "🎯 Prediction",
        "The model predicts whether the applicant is likely to default."
    ),
    (
        "06",
        "📊 Probability",
        "The application displays the estimated probability of loan default."
    )
]


for number, title, description in steps:

    col1, col2 = st.columns([1, 6])

    with col1:

        st.info(number)

    with col2:

        with st.container(border=True):

            st.subheader(title)

            st.write(description)


# ==========================================================
# INPUT CATEGORIES
# ==========================================================

st.divider()

st.header("📥 Main Model Inputs")


col1, col2, col3 = st.columns(3)


with col1:

    with st.container(border=True):

        st.subheader("👤 Personal Information")

        st.write("• Age")
        st.write("• Education")
        st.write("• Marital Status")
        st.write("• Dependents")
        st.write("• Mortgage")


with col2:

    with st.container(border=True):

        st.subheader("💳 Credit & Finance")

        st.write("• Annual Income")
        st.write("• Credit Score")
        st.write("• Credit Lines")
        st.write("• DTI Ratio")
        st.write("• Co-Signer")


with col3:

    with st.container(border=True):

        st.subheader("💰 Loan & Employment")

        st.write("• Loan Amount")
        st.write("• Interest Rate")
        st.write("• Loan Term")
        st.write("• Employment Type")
        st.write("• Months Employed")


# ==========================================================
# ALGORITHM
# ==========================================================

st.divider()

st.header("🤖 Machine Learning Algorithm")

st.subheader("Why Logistic Regression?")

st.write(
    """
    Logistic Regression is a supervised Machine Learning algorithm
    commonly used for binary classification problems.

    In this project, the model predicts one of two classes:
    """
)


col1, col2 = st.columns(2)


with col1:

    st.success(
        """
        ### 0️⃣ No Default

        The model predicts that the applicant is
        less likely to default.
        """
    )


with col2:

    st.error(
        """
        ### 1️⃣ Default

        The model predicts that the applicant is
        likely to default.
        """
    )


# ==========================================================
# PROCESSING FLOW
# ==========================================================

st.divider()

st.header("⚙️ What Happens During Prediction?")


with st.expander("Step 1 — Collect Input", expanded=True):

    st.write(
        """
        The application collects applicant information such as
        age, income, credit score, loan amount, employment type
        and other loan-related attributes.
        """
    )


with st.expander("Step 2 — Prepare Features"):

    st.write(
        """
        The categorical information is converted into numerical
        features so that it can be processed by the Machine
        Learning model.
        """
    )


with st.expander("Step 3 — Scale Features"):

    st.write(
        """
        The saved StandardScaler is used to transform the input
        features in the same way as during model training.
        """
    )


with st.expander("Step 4 — Model Prediction"):

    st.write(
        """
        The processed input is passed to the trained
        Logistic Regression model.
        """
    )


with st.expander("Step 5 — Display Result"):

    st.write(
        """
        The application displays the predicted class and the
        estimated probability of loan default.
        """
    )


# ==========================================================
# SIMPLE FLOW
# ==========================================================

st.divider()

st.header("🔁 Simple Flow")


st.info(
    """
    👤 Applicant Information

              ↓

    ⚙️ Feature Preparation

              ↓

    📏 Feature Scaling

              ↓

    🤖 Logistic Regression

              ↓

    🎯 Default / No Default

              ↓

    📊 Probability
    """
)


# ==========================================================
# IMPORTANT NOTE
# ==========================================================

st.divider()

st.warning(
    """
    ⚠️ This project is developed for academic and educational
    purposes. The prediction should not be treated as professional
    financial advice or as the sole basis for a real loan decision.
    """
)


# ==========================================================
# FOOTER
# ==========================================================

footer()
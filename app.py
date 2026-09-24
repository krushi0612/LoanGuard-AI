import streamlit as st

from ui import apply_theme, sidebar_brand, footer
from ml_utils import load_dataset


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="LoanGuard AI",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# COMMON UI
# ==========================================================

apply_theme()
sidebar_brand()


# ==========================================================
# HERO
# ==========================================================

st.title("🏦 LoanGuard AI")

st.subheader(
    "Smart Loan Default Prediction using Machine Learning"
)

st.write(
    """
    Analyze borrower information and estimate the probability
    of loan default using a trained Machine Learning model.
    """
)


st.divider()


# ==========================================================
# QUICK ACCESS
# ==========================================================

st.header("🚀 Explore LoanGuard AI")


col1, col2, col3 = st.columns(3)


with col1:

    with st.container(border=True):

        st.markdown("### 🔮 Loan Prediction")

        st.write(
            "Enter applicant information and predict "
            "the possibility of loan default."
        )

        st.page_link(
            "pages/1_🔮_Loan_Prediction.py",
            label="Open Prediction →"
        )


with col2:

    with st.container(border=True):

        st.markdown("### 📊 Dataset Analytics")

        st.write(
            "Explore the loan dataset using statistics "
            "and interactive visualizations."
        )

        st.page_link(
            "pages/2_📊_Analytics.py",
            label="Open Analytics →"
        )


with col3:

    with st.container(border=True):

        st.markdown("### 🧠 How It Works")

        st.write(
            "Understand the complete Machine Learning "
            "pipeline used in this project."
        )

        st.page_link(
            "pages/3_🧠_How_It_Works.py",
            label="Learn More →"
        )


# ==========================================================
# DATASET INFORMATION
# ==========================================================

st.divider()

st.header("📌 Project at a Glance")


try:

    df = load_dataset()

    total_records = len(df)

    default_rate = (
        df["Default"].mean() * 100
        if "Default" in df.columns
        else 0
    )

except Exception:

    total_records = 0
    default_rate = 0


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Dataset Records",
        f"{total_records:,}"
    )


with col2:

    st.metric(
        "Model",
        "Logistic Regression"
    )


with col3:

    st.metric(
        "Target",
        "Loan Default"
    )


with col4:

    st.metric(
        "Default Rate",
        f"{default_rate:.2f}%"
    )


# ==========================================================
# HOW TO USE
# ==========================================================

st.divider()

st.header("🛠️ How to Use")


steps = [
    (
        "1️⃣",
        "Enter Applicant Details",
        "Open the Loan Prediction page and enter the applicant's information."
    ),
    (
        "2️⃣",
        "Run Prediction",
        "Submit the form to process the information through the trained model."
    ),
    (
        "3️⃣",
        "Check Risk",
        "View the predicted class and estimated default probability."
    ),
    (
        "4️⃣",
        "Explore Analytics",
        "Use the Analytics page to understand the dataset."
    )
]


for icon, title, description in steps:

    with st.container(border=True):

        st.markdown(f"### {icon} {title}")

        st.write(description)


# ==========================================================
# MACHINE LEARNING
# ==========================================================

st.divider()

st.header("🤖 Machine Learning")


col1, col2 = st.columns(2)


with col1:

    st.markdown("### Algorithm")

    st.write(
        """
        **Logistic Regression**

        The model performs binary classification:

        - `0` → No Default
        - `1` → Default
        """
    )


with col2:

    st.markdown("### Processing")

    st.write(
        """
        Applicant information is processed and scaled before
        being passed to the trained Machine Learning model.
        """
    )


# ==========================================================
# NAVIGATION
# ==========================================================

st.divider()

st.header("📚 More About the Project")


col1, col2 = st.columns(2)


with col1:

    st.page_link(
        "pages/4_ℹ️_About_Project.py",
        label="ℹ️ About Project"
    )


with col2:

    st.page_link(
        "pages/5_📬_Contact.py",
        label="📬 Contact"
    )


# ==========================================================
# DISCLAIMER
# ==========================================================

st.divider()

st.warning(
    """
    ⚠️ This application is developed for academic and
    educational purposes. The prediction should not be used
    as the sole basis for real-world financial decisions.
    """
)


# ==========================================================
# FOOTER
# ==========================================================

footer()
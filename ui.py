import streamlit as st


# ==========================================================
# THEME
# ==========================================================

def apply_theme():

    st.markdown(
        """
        <style>

        .stApp {
            background-color: #f8fafc;
        }

        .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        h1 {
            color: #0f172a;
            font-weight: 800;
        }

        h2 {
            color: #0f172a;
            font-weight: 750;
        }

        h3 {
            color: #1e293b;
        }

        [data-testid="stSidebar"] {
            background-color: #0f172a;
        }

        [data-testid="stSidebar"] * {
            color: #e2e8f0;
        }

        div[data-testid="stMetric"] {
            background-color: white;
            border: 1px solid #e2e8f0;
            padding: 1rem;
            border-radius: 15px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# SIDEBAR
# ==========================================================

def sidebar_brand():

    with st.sidebar:

        st.markdown("## 🏦 LoanGuard AI")

        st.caption(
            "ML-powered Credit Risk"
        )

        st.divider()

        st.caption("NAVIGATION")

        st.write(
            "Use the pages above to explore "
            "the LoanGuard AI application."
        )

        st.divider()

        st.caption("🤖 Logistic Regression")

        st.caption("📊 Data Analytics")

        st.caption("🔮 Risk Prediction")


# ==========================================================
# FOOTER
# ==========================================================

def footer():

    st.divider()

    st.caption(
        "🏦 LoanGuard AI • Loan Default Prediction using Machine Learning"
    )

    st.caption(
        "Built with Python • Pandas • Scikit-learn • Streamlit"
    )
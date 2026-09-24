import pandas as pd
import streamlit as st

from ui import apply_theme, sidebar_brand, footer
from ml_utils import load_model_assets, prepare_input


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Loan Prediction | LoanGuard AI",
    page_icon="🔮",
    layout="wide"
)


# ==========================================================
# COMMON UI
# ==========================================================

apply_theme()
sidebar_brand()


# ==========================================================
# LOAD MODEL
# ==========================================================

model, scaler, feature_names = load_model_assets()


# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("🔮 Loan Default Prediction")

st.write(
    """
    Enter applicant information below and use the trained Machine Learning
    model to estimate the probability of loan default.
    """
)

st.divider()


# ==========================================================
# FORM
# ==========================================================

with st.form("prediction_form"):

    # ======================================================
    # PERSONAL INFORMATION
    # ======================================================

    st.subheader("👤 Personal Information")

    c1, c2, c3 = st.columns(3)

    with c1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=35
        )

    with c2:

        income = st.number_input(
            "Annual Income",
            min_value=0.0,
            value=50000.0,
            step=1000.0
        )

    with c3:

        education = st.selectbox(
            "Education",
            [
                "Bachelor's",
                "High School",
                "Master's",
                "PhD"
            ]
        )


    c1, c2, c3 = st.columns(3)

    with c1:

        marital_status = st.selectbox(
            "Marital Status",
            [
                "Divorced",
                "Married",
                "Single"
            ]
        )

    with c2:

        has_dependents = st.selectbox(
            "Has Dependents",
            [
                "No",
                "Yes"
            ]
        )

    with c3:

        has_mortgage = st.selectbox(
            "Has Mortgage",
            [
                "No",
                "Yes"
            ]
        )


    # ======================================================
    # EMPLOYMENT & CREDIT
    # ======================================================

    st.subheader("💼 Employment & Credit")

    c1, c2, c3 = st.columns(3)

    with c1:

        employment_type = st.selectbox(
            "Employment Type",
            [
                "Full-time",
                "Part-time",
                "Self-employed",
                "Unemployed"
            ]
        )

    with c2:

        months_employed = st.number_input(
            "Months Employed",
            min_value=0,
            max_value=600,
            value=60
        )

    with c3:

        credit_score = st.number_input(
            "Credit Score",
            min_value=300,
            max_value=850,
            value=700
        )


    c1, c2, c3 = st.columns(3)

    with c1:

        num_credit_lines = st.number_input(
            "Number of Credit Lines",
            min_value=0,
            max_value=50,
            value=3
        )

    with c2:

        dti_ratio = st.number_input(
            "Debt-to-Income Ratio",
            min_value=0.0,
            max_value=2.0,
            value=0.25,
            step=0.01
        )

    with c3:

        has_cosigner = st.selectbox(
            "Has Co-Signer",
            [
                "No",
                "Yes"
            ]
        )


    # ======================================================
    # LOAN INFORMATION
    # ======================================================

    st.subheader("💰 Loan Information")

    c1, c2, c3 = st.columns(3)

    with c1:

        loan_amount = st.number_input(
            "Loan Amount",
            min_value=0.0,
            value=100000.0,
            step=5000.0
        )

    with c2:

        interest_rate = st.number_input(
            "Interest Rate (%)",
            min_value=0.0,
            max_value=100.0,
            value=8.0,
            step=0.1
        )

    with c3:

        loan_term = st.number_input(
            "Loan Term (months)",
            min_value=1,
            max_value=360,
            value=36
        )


    loan_purpose = st.selectbox(
        "Loan Purpose",
        [
            "Business",
            "Education",
            "Home",
            "Other"
        ]
    )


    # Small spacing before button
    st.write("")


    submitted = st.form_submit_button(
        "🔮 Predict Default Risk",
        type="primary",
        use_container_width=True
    )


# ==========================================================
# PREDICTION
# ==========================================================

if submitted:

    # ======================================================
    # PREPARE INPUT
    # ======================================================

    values = locals()

    input_df = prepare_input(
        values,
        feature_names
    )


    # ======================================================
    # SCALE INPUT
    # ======================================================

    scaled_input = scaler.transform(
        input_df
    )


    # ======================================================
    # PREDICTION
    # ======================================================

    prediction = int(
        model.predict(
            scaled_input
        )[0]
    )


    # ======================================================
    # PROBABILITY
    # ======================================================

    probability = float(
        model.predict_proba(
            scaled_input
        )[0][1]
    )


    # ======================================================
    # RESULT
    # ======================================================

    st.divider()

    st.subheader("📋 Prediction Result")


    # ======================================================
    # RESULT MESSAGE
    # ======================================================

    if prediction == 1:

        st.error(
            "⚠️ High Risk of Loan Default"
        )

        st.write(
            """
            The trained model classifies this application
            as a likely default case.
            """
        )

    else:

        st.success(
            "✅ Low Risk of Loan Default"
        )

        st.write(
            """
            The trained model classifies this application
            as a likely non-default case.
            """
        )


    # ======================================================
    # PROBABILITY METRICS
    # ======================================================

    m1, m2, m3 = st.columns(3)


    with m1:

        st.metric(
            "Default Probability",
            f"{probability * 100:.2f}%"
        )


    with m2:

        st.metric(
            "No-Default Probability",
            f"{(1 - probability) * 100:.2f}%"
        )


    with m3:

        st.metric(
            "Predicted Class",
            "Default" if prediction else "No Default"
        )


    # ======================================================
    # RISK PROBABILITY CHART
    # ======================================================

    st.subheader("📊 Risk Probability")


    chart = pd.DataFrame(
        {
            "Probability": [
                probability,
                1 - probability
            ]
        },
        index=[
            "Default",
            "No Default"
        ]
    )


    st.bar_chart(
        chart
    )


    # ======================================================
    # INTERPRETATION
    # ======================================================

    st.subheader("💡 Interpretation")


    if probability >= 0.7:

        st.error(
            f"""
            The model estimates a relatively high default probability
            of **{probability * 100:.2f}%**.
            """
        )

    elif probability >= 0.4:

        st.warning(
            f"""
            The model estimates a moderate default probability
            of **{probability * 100:.2f}%**.
            """
        )

    else:

        st.success(
            f"""
            The model estimates a relatively low default probability
            of **{probability * 100:.2f}%**.
            """
        )


    # ======================================================
    # DISCLAIMER
    # ======================================================

    st.caption(
        "Educational demonstration only — this prediction should not "
        "be used as the sole basis for real financial decisions."
    )


# ==========================================================
# FOOTER
# ==========================================================

footer()

import pandas as pd
import streamlit as st

from ui import apply_theme, sidebar_brand, footer
from ml_utils import load_dataset


st.set_page_config(
    page_title="Analytics | LoanGuard AI",
    page_icon="📊",
    layout="wide"
)

apply_theme()
sidebar_brand()


df = load_dataset()


st.title("📊 Dataset Analytics")

st.write(
    """
    Explore the dataset used for the loan default prediction project.
    The charts below provide a quick understanding of borrower,
    credit and loan characteristics.
    """
)


# =========================
# METRICS
# =========================

m1, m2, m3, m4 = st.columns(4)

m1.metric(
    "Total Records",
    f"{len(df):,}"
)

m2.metric(
    "Average Income",
    f"{df['Income'].mean():,.0f}"
)

m3.metric(
    "Average Credit Score",
    f"{df['CreditScore'].mean():.0f}"
)

m4.metric(
    "Default Rate",
    f"{df['Default'].mean() * 100:.2f}%"
)


st.divider()


# =========================
# DEFAULT DISTRIBUTION
# =========================

st.subheader("🎯 Default Distribution")

default_counts = (
    df["Default"]
    .map({
        0: "No Default",
        1: "Default"
    })
    .value_counts()
    .rename_axis("Status")
    .to_frame("Applicants")
)

st.bar_chart(default_counts)


# =========================
# TWO COLUMN ANALYTICS
# =========================

c1, c2 = st.columns(2)


with c1:

    st.subheader("💰 Average Financial Values")

    summary = (
        df.groupby("Default")[
            [
                "Income",
                "LoanAmount",
                "CreditScore",
                "InterestRate",
                "DTIRatio"
            ]
        ]
        .mean()
        .round(2)
    )

    summary.index = summary.index.map(
        {
            0: "No Default",
            1: "Default"
        }
    )

    st.dataframe(
        summary,
        use_container_width=True
    )


with c2:

    st.subheader("💼 Employment Type")

    employment = (
        df["EmploymentType"]
        .value_counts()
        .to_frame("Applicants")
    )

    st.bar_chart(employment)


# =========================
# FEATURE EXPLORER
# =========================

st.divider()

st.subheader("🔍 Feature Explorer")

feature = st.selectbox(
    "Choose a numeric feature",
    [
        "Age",
        "Income",
        "LoanAmount",
        "CreditScore",
        "MonthsEmployed",
        "NumCreditLines",
        "InterestRate",
        "LoanTerm",
        "DTIRatio"
    ]
)


bins = pd.cut(
    df[feature],
    bins=12
)

hist = (
    df.groupby(
        bins,
        observed=False
    )
    .size()
    .rename("Applicants")
    .to_frame()
)

hist.index = hist.index.astype(str)

st.bar_chart(hist)


# =========================
# CATEGORICAL INSIGHTS
# =========================

st.divider()

st.subheader("📌 Borrower Characteristics")

c1, c2, c3 = st.columns(3)


with c1:

    st.write("**Education**")

    education = (
        df["Education"]
        .value_counts()
        .to_frame("Applicants")
    )

    st.bar_chart(education)


with c2:

    st.write("**Marital Status**")

    marital = (
        df["MaritalStatus"]
        .value_counts()
        .to_frame("Applicants")
    )

    st.bar_chart(marital)


with c3:

    st.write("**Loan Purpose**")

    purpose = (
        df["LoanPurpose"]
        .value_counts()
        .to_frame("Applicants")
    )

    st.bar_chart(purpose)


# =========================
# DATA PREVIEW
# =========================

st.divider()

with st.expander("📄 Preview Dataset"):

    st.dataframe(
        df.head(100),
        use_container_width=True
    )


footer()
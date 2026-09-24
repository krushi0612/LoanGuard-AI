from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent


@st.cache_resource
def load_model_assets():

    model = joblib.load(
        BASE_DIR / "loan_model.pkl"
    )

    scaler = joblib.load(
        BASE_DIR / "loan_scaler.pkl"
    )

    feature_names = joblib.load(
        BASE_DIR / "feature_names.pkl"
    )

    return model, scaler, feature_names


@st.cache_data
def load_dataset():

    return pd.read_csv(
        BASE_DIR / "Loan_default.csv"
    )


def prepare_input(values: dict, feature_names):

    input_df = pd.DataFrame(
        0,
        index=[0],
        columns=feature_names,
        dtype=float
    )

    numeric_map = {

        "Age":
            values["age"],

        "Income":
            values["income"],

        "LoanAmount":
            values["loan_amount"],

        "CreditScore":
            values["credit_score"],

        "MonthsEmployed":
            values["months_employed"],

        "NumCreditLines":
            values["num_credit_lines"],

        "InterestRate":
            values["interest_rate"],

        "LoanTerm":
            values["loan_term"],

        "DTIRatio":
            values["dti_ratio"],
    }


    for column, value in numeric_map.items():

        if column in input_df.columns:

            input_df.loc[0, column] = value


    categorical_columns = [

        f"Education_{values['education']}",

        f"EmploymentType_{values['employment_type']}",

        f"MaritalStatus_{values['marital_status']}",

        f"HasMortgage_{values['has_mortgage']}",

        f"HasDependents_{values['has_dependents']}",

        f"LoanPurpose_{values['loan_purpose']}",

        f"HasCoSigner_{values['has_cosigner']}",
    ]


    for column in categorical_columns:

        if column in input_df.columns:

            input_df.loc[0, column] = 1


    return input_df
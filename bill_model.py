import pandas as pd
import joblib

# Load artifacts
model = joblib.load("billing_model.pkl")
le_map = joblib.load("le_map.pkl")
label_encode_cols = joblib.load("label_encode_cols.pkl")
target_maps = joblib.load("target_maps.pkl")
target_encode_cols = joblib.load("target_encode_cols.pkl")
feature_columns = joblib.load("feature_columns.pkl")

def predict_bill(
    age, gender, blood_type, medical_condition,
    admission_type, insurance_provider,
    admission_date, discharge_date
):

    ad = pd.to_datetime(admission_date)
    dd = pd.to_datetime(discharge_date)

    patient = {
        "Age": age,
        "Length of Stay": (dd - ad).days,
        "Admission Month": ad.month,
        "Admission Day": ad.day,
        "Admission Weekday": ad.weekday(),
        "Discharge Month": dd.month,
        "Discharge Weekday": dd.weekday()
    }

    cat_values = {
        "Gender": gender,
        "Blood Type": blood_type,
        "Admission Type": admission_type,
        "Medical Condition": medical_condition,
        "Insurance Provider": insurance_provider
    }

    for col, value in cat_values.items():

        if col in label_encode_cols:
            if value in le_map[col].classes_:
                patient[col] = le_map[col].transform([value])[0]
            else:
                patient[col] = -1

        elif col in target_encode_cols:
            patient[col] = target_maps[col].get(
                value, target_maps[col].mean()
            )

        else:
            patient[col] = 0

    new_df = pd.DataFrame([patient])
    new_df = new_df.reindex(columns=feature_columns, fill_value=0)

    return model.predict(new_df)[0]

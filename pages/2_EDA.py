import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title("📊 Exploratory Data Analysis")

# --------------------------------------------------------
#  LOAD DATA
# --------------------------------------------------------
df = pd.read_csv("healthcare_dataset_cleaned.csv")
st.success(f"✅ Dataset loaded successfully: {df.shape}")

# Convert date columns to datetime (important for Length of Stay)
df["Date of Admission"] = pd.to_datetime(df["Date of Admission"], errors='coerce')
df["Discharge Date"] = pd.to_datetime(df["Discharge Date"], errors='coerce')

# --------------------------------------------------------
# 1. BASIC STATISTICS
# --------------------------------------------------------
st.subheader("📈 Basic Statistics")
st.dataframe(df.describe(include='all'), use_container_width=True)

# --------------------------------------------------------
# 2. AGE DISTRIBUTION
# --------------------------------------------------------
st.subheader("🩺 Distribution of Age")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df["Age"], kde=True, bins=20, color='skyblue', ax=ax)
ax.set_title("Age Distribution")
ax.set_xlabel("Age")
ax.set_ylabel("Count")
st.pyplot(fig)

# --------------------------------------------------------
# 3. MEDICAL CONDITION COUNT
# --------------------------------------------------------
st.subheader("💉 Medical Condition Count")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(
    y="Medical Condition",
    data=df,
    order=df["Medical Condition"].value_counts().index,
    palette="viridis",
    ax=ax
)
ax.set_title("Medical Condition Frequency")
ax.set_xlabel("Count")
ax.set_ylabel("Medical Condition")
st.pyplot(fig)

# --------------------------------------------------------
# 4. BLOOD TYPE DISTRIBUTION
# --------------------------------------------------------
st.subheader("🩸 Blood Type Distribution")
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(
    x="Blood Type",
    data=df,
    order=df["Blood Type"].value_counts().index,
    palette="plasma",
    ax=ax
)
ax.set_title("Blood Type Distribution")
ax.set_xlabel("Blood Type")
ax.set_ylabel("Count")
st.pyplot(fig)

# --------------------------------------------------------
# 5. ADMISSION TYPE DISTRIBUTION
# --------------------------------------------------------
st.subheader("📅 Admission Type Distribution")
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(
    x="Admission Type",
    data=df,
    order=df["Admission Type"].value_counts().index,
    palette="coolwarm",
    ax=ax
)
ax.set_title("Admission Type Distribution")
ax.set_xlabel("Admission Type")
ax.set_ylabel("Count")
st.pyplot(fig)

# --------------------------------------------------------
# 6. LENGTH OF STAY ANALYSIS
# --------------------------------------------------------
st.subheader("🕒 Length of Stay Analysis")

# Create Length of Stay column
df["Length of Stay"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days

# Display sample data
st.dataframe(df[["Date of Admission", "Discharge Date", "Length of Stay"]].head(), use_container_width=True)


# --------------------------------------------------------
# 7. CORRELATION HEATMAP
# --------------------------------------------------------
st.subheader("🔥 Correlation Heatmap (Numeric Features)")
numeric_df = df.select_dtypes(include=["float64", "int64"])

if not numeric_df.empty:
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm",
        linewidths=0.5,
        square=True,
        ax=ax
    )
    ax.set_title("Correlation Heatmap (Numeric Features)")
    st.pyplot(fig)
else:
    st.warning("⚠️ No numeric columns available for correlation heatmap.")

# --------------------------------------------------------
# 8. COMPLETION
# --------------------------------------------------------
st.success("✅ EDA Completed Successfully!")

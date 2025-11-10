# Healthcare Analytics Dashboard

A comprehensive Streamlit-based application for healthcare data analysis and billing prediction. This dashboard provides tools for data cleaning, exploratory data analysis (EDA), and estimating patient bills using machine learning models.

## Features

### 🧹 Data Cleaning
- Load and preview the raw healthcare dataset
- Check for missing values and data quality
- View dataset statistics and structure

### 📊 Exploratory Data Analysis (EDA)
- Visualize patient demographics (age distribution)
- Analyze medical conditions and their frequencies
- Examine blood type and admission type distributions
- Calculate and analyze length of stay
- Correlation heatmap for numeric features

### 💰 Billing Estimation
- Predict patient bills based on multiple factors:
  - Age, gender, blood type
  - Medical condition, admission type
  - Insurance provider, admission/discharge dates
- Interactive input form for bill estimation
- Cost breakdown and insurance coverage analysis

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd DataScience_SEE_Project-main
   ```

2. Install the required dependencies:
   ```bash
   pip install streamlit pandas matplotlib seaborn scikit-learn
   ```

3. Ensure you have the necessary data files:
   - `healthcare_dataset.csv` (raw dataset)
   - `healthcare_dataset_cleaned.csv` (cleaned dataset)
   - Model files (`.pkl` files for ML models and encoders)

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to the provided local URL (usually `http://localhost:8501`)

3. Use the sidebar to navigate between different pages:
   - **Home**: Overview and quick statistics
   - **Data Cleaning**: Review the cleaned dataset
   - **EDA**: Explore data visualizations and insights
   - **Billing**: Estimate patient bills

## File Structure

```
DataScience_SEE_Project-main/
├── app.py                          # Main Streamlit application
├── pages/
│   ├── 1_Data_Cleaning.py          # Data cleaning page
│   ├── 2_EDA.py                    # Exploratory data analysis page
│   └── Billing.py                  # Billing prediction page
├── bill_model.py                   # Billing prediction model functions
├── healthcare_dataset.csv          # Raw healthcare dataset
├── healthcare_dataset_cleaned.csv  # Cleaned healthcare dataset
├── *.pkl                           # Pickled ML models and encoders
├── *.ipynb                         # Jupyter notebooks for analysis
└── README.md                       # This file
```

## Dataset

The analysis is based on a healthcare dataset containing:
- Patient demographics (age, gender, blood type)
- Medical conditions and admission details
- Insurance information
- Billing and length of stay data

## Models

The application uses pre-trained machine learning models for billing prediction:
- Random Forest, XGBoost, and Linear Regression models
- Label and target encoders for categorical variables
- Feature selection and preprocessing pipelines

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## Support

For questions or issues, please open an issue in the repository or contact the maintainers.


Team Members:
1]Dattadeep Shetgaonkar 25P0630002
2]Sanil Virnodkar 25P0630014
3]Kaushik Tirodkar 25P0630006
4]Shreyash Devali 25P0630016

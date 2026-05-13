# Used Car Price Analysis and Regression

This project focuses on the exploratory data analysis (EDA) and preprocessing of a used car dataset (`autos.csv`) to prepare it for regression modeling.

## Project Overview

The main objective of this notebook is to clean the dataset and understand the distribution of various features such as the year of registration, price, and engine power to facilitate accurate price predictions.

## Features and Steps

1.  **Data Loading**: Importing the dataset using Pandas with specific encoding handling (`latin-1`).
2.  **Data Cleaning**:
    * Converting key columns like `yearOfRegistration`, `price`, and `powerPS` to numeric types.
    * Handling missing values in critical columns.
    * Filtering records to include only realistic registration years (1900 - 2024).
3.  **Exploratory Data Analysis (EDA)**:
    * Visualizing the distribution of vehicles based on their registration year using `Seaborn` histograms.
4.  **Regression Modeling**: (Future/Ongoing) Preparing the data for regression algorithms to predict car values.

## Dependencies

To run this notebook, you will need the following Python libraries installed:

* `numpy`
* `pandas`
* `seaborn`
* `matplotlib`

## How to Run

1.  Ensure you have `autos.csv` in the same directory as the notebook.
2.  Install the required dependencies:
    ```bash
    pip install numpy pandas seaborn matplotlib
    ```
3.  Open `Regressao.ipynb` in Jupyter Notebook or Google Colab.
4.  Execute the cells sequentially to see the cleaning process and generated plots.

## Dataset Information

The dataset contains over 660,000 records of car advertisements, including attributes such as brand, model, mileage, gearbox type, and more.

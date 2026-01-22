import pandas as pd
import numpy as np
import os

# 1. Path check karein
input_path = 'data/survey.csv'
output_path = 'data/cleaned_survey.csv'

if not os.path.exists(input_path):
    print("Error: survey.csv file 'data' folder mein nahi mili!")
else:
    df = pd.read_csv(input_path)
    print("Original Data Shape:", df.shape)

    # 2. Unnecessary columns drop karna (Timestamp aur Comments ki zaroorat nahi)
    df.drop(['Timestamp', 'state', 'comments'], axis=1, inplace=True)

    # 3. Age Cleaning (Sirf 15 se 100 saal tak ka data rakhein)
    df = df[(df['Age'] >= 15) & (df['Age'] <= 100)]

    # 4. Gender Cleaning (Most Important)
    df['Gender'] = df['Gender'].str.lower().str.strip()

    male_list = ['male', 'm', 'male-ish', 'maile', 'mal', 'male (cis)', 'make', 'guy (-ish)', 'cis male', 'cis man', 'msle', 'mail', 'malr', 'maile']
    female_list = ['female', 'f', 'woman', 'femake', 'female (cis)', 'cis female', 'femail', 'cis-female/femme', 'female (trans)', 'woman']

    def simplify_gender(g):
        if g in male_list: return 'male'
        elif g in female_list: return 'female'
        else: return 'other'

    df['Gender'] = df['Gender'].apply(simplify_gender)

    # 5. Missing Values Handle karna
    # self_employed mein NaN ko 'No' kar dein
    df['self_employed'] = df['self_employed'].fillna('No')
    # work_interfere mein NaN ko 'Unknown' kar dein
    df['work_interfere'] = df['work_interfere'].fillna('Unknown')

    # 6. Cleaned file save karein
    df.to_csv(output_path, index=False)
    print("Success: Cleaned data saved at", output_path)
    print("Cleaned Data Preview:")
    print(df.head())
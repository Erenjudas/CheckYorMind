import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# 1. Path Setup
data_folder = 'data'
input_file = os.path.join(data_folder, 'survey.csv')
output_file = os.path.join(data_folder, 'cleaned_survey.csv')

# Data Load karein
df = pd.read_csv(input_file)

# 2. PROPER CLEANING
# Timestamp aur unnecessary columns drop karein
df.drop(['Timestamp', 'state', 'comments'], axis=1, inplace=True, errors='ignore')

# Age filter (Sirf 18-70 years tak ka data rakhein jo valid hai)
df = df[(df['Age'] >= 18) & (df['Age'] <= 70)]

# Gender Standardization
df['Gender'] = df['Gender'].str.lower().str.strip()
male_list = ['male', 'm', 'male-ish', 'maile', 'mal', 'male (cis)', 'make', 'guy (-ish)', 'cis male', 'cis man', 'msle', 'mail', 'malr', 'maile']
female_list = ['female', 'f', 'woman', 'femake', 'female (cis)', 'cis female', 'femail', 'cis-female/femme', 'female (trans)', 'woman']

def clean_gender(g):
    if g in male_list: return 'male'
    elif g in female_list: return 'female'
    else: return 'other'

df['Gender'] = df['Gender'].apply(clean_gender)

# Missing values handle karein
df['work_interfere'] = df['work_interfere'].fillna('Unknown')
df['self_employed'] = df['self_employed'].fillna('No')

# Cleaned data save karein
df.to_csv(output_file, index=False)
print(f"Data clean ho kar {output_file} mein save ho gaya hai.")

# 3. GRAPHS SAVING LOGIC
sns.set_theme(style="whitegrid")

# Graph 1: Gender vs Treatment
plt.figure(figsize=(10, 6))
sns.countplot(x='Gender', hue='treatment', data=df, palette='magma')
plt.title('Mental Health Treatment by Gender')
plt.savefig(os.path.join(data_folder, 'gender_analysis.png')) # Save image in data folder
plt.close()

# Graph 2: Family History Impact
plt.figure(figsize=(10, 6))
sns.countplot(x='family_history', hue='treatment', data=df, palette='coolwarm')
plt.title('Impact of Family History on Treatment')
plt.savefig(os.path.join(data_folder, 'family_history_analysis.png')) # Save image in data folder
plt.close()

print("Graphs save ho gaye hain: data/gender_analysis.png aur data/family_history_analysis.png")
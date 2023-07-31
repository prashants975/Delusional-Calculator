import streamlit as st
import pandas as pd
import numpy as np
from utils import height_percentage_calc, working_ratio
st.title("Delusion Calculator (India)")

sel_gender = st.radio("Calculate for which gender:", ("Male", "Female"))

# Income slider
min_income = 0
max_income = 500_000_000  # 500 crores
default_income = 5_00_000  # Default income value on slider

df_income = pd.read_csv("data/income.csv")

any_income_flag = st.checkbox("Any Income")

if not any_income_flag:
    income_range = df_income["Income Up Boundary"]
    sel_income = st.select_slider("Select the desired income (in INR):", options = income_range, value=(500000, 1000000) )
    income_percent = df_income[(df_income["Income Up Boundary"] > sel_income[0]) & (df_income["Income Up Boundary"] <= sel_income[1])]["Percenatge in Income Range"].sum()
    income_number = df_income[(df_income["Income Up Boundary"] > sel_income[0]) & (df_income["Income Up Boundary"] <= sel_income[1])]["No. of Returns"].sum()
else:
    income_percent = 100.0
    income_number = "NA"

st.write(income_percent)
st.write(income_number)



#Religion 
df_religion = pd.read_csv("data/religion.csv")

any_religion_flag = st.checkbox("Any Religion")
religion_list = df_religion["Religion"]

if not any_religion_flag:
    sel_religion = st.multiselect("Select preferred Religions:",religion_list )
else:
    sel_religion = religion_list

religion_percent = df_religion[df_religion["Religion"].isin(sel_religion)]['%'].sum()
st.write(religion_percent)

#Caste

if not any_religion_flag:
    df_caste_religion = pd.read_csv("data/caste_religion.csv")

    any_caste_flag = st.checkbox("Any Caste")

    if not any_caste_flag:
        caste_list = ["SCs","STs","OBCs","General"]
        sel_caste = st.multiselect("Select preferred Castes:",caste_list)
    else:
        sel_caste = ["All Castes"]

    st.write(df_caste_religion[df_caste_religion["Religion"].isin(sel_religion)][sel_caste])
    caste_percent = df_caste_religion[df_caste_religion["Religion"].isin(sel_religion)][sel_caste].sum(axis = 1).values
    caste_by_rel_percent = df_caste_religion[df_caste_religion["Religion"].isin(sel_religion)]["%"].values

    st.write(caste_percent)
    st.write(caste_by_rel_percent)

    caste_percent_final = np.sum(caste_by_rel_percent * caste_percent) / np.sum(caste_by_rel_percent)
    st.write( caste_percent_final )
else:
    caste_percent_final = 100
# Height
sel_height = st.select_slider("Select the desired height (in cm):", options = np.arange(130, 210, 2), value=(140, 200) )
height_percent = height_percentage_calc(sel_gender, sel_height[0], sel_height[1])
st.write(height_percent)


#working ratio based on gender 
working_percent =  working_ratio[sel_gender]

# Final Score
total_percent = 100.0 * income_percent / 100 * religion_percent / 100 * working_percent / 1.00 * caste_percent_final / 100 * height_percent / 100
st.metric(label=f"Percentage of Possible {sel_gender}", value=str(round(total_percent, 6))+"%")


if income_number != "NA":
    total_count = income_number * total_percent
    st.metric(label=f"Number of Possible {sel_gender}", value= total_count)

# df_religion_caste_merged = df1.merge(df2, on='common_column', how='inner')


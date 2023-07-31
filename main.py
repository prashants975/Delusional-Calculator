import streamlit as st
import pandas as pd
import numpy as np
from utils import height_percentage_calc, working_ratio, conv_dict, conv_dict_rev


st.set_page_config(
    page_title="Dating Delusion Calculator (India)",
    page_icon="🎭",
    menu_items={
        'About': "This App is an approximation and just for fun."
    }
)
st.title("Dating Delusion Calculator (India)")

with st.sidebar:
    st.markdown("""#### Assumptions ❓❓""")
    st.write("* The Final Percentage shown at the end is based on people who filed ITR (~6crore) and not the total Indian Population.")
    st.write("* Age Distribution isn't applied, i.e. the final number or percentage is total for all the ages.")
    st.write("* Assumed that around 20% of workforce is women and 80% is men.")
    st.write("* Not considering income/wealth distribution over religion, caste or gender.")




sel_gender = st.radio("**Select the gender you want to date:**", ("Male", "Female"))
st.markdown("""---""")

# Income slider
df_income = pd.read_csv("data/income.csv")

any_income_flag = st.checkbox("Any Income")

if not any_income_flag:
    income_range = df_income["Income Up Boundary"].values
    # st.write(type(income_range))

    income_range = [conv_dict[inc] for inc in income_range]

    sel_income = st.select_slider("**Select the desired income (in INR):**", options = income_range, value=("5.00 Lak", "10.00 Lak") )
    sel_income = [conv_dict_rev[inc] for inc in sel_income]

    # st.write(sel_income)

    income_percent = df_income[(df_income["Income Up Boundary"] > sel_income[0]) & (df_income["Income Up Boundary"] <= sel_income[1])]["Percenatge in Income Range"].sum()
    income_number = df_income[(df_income["Income Up Boundary"] > sel_income[0]) & (df_income["Income Up Boundary"] <= sel_income[1])]["No. of Returns"].sum()
else:
    income_percent = 100.0
    income_number = "NA"

st.success(f"##### Around **{round(income_percent, 6)}%** of people are in the selected income range.")
st.success(f"##### **{round(income_number/100000, 3)}** Lakhs of people lie in the selected income range.")
st.markdown("""---""")


#Religion 
df_religion = pd.read_csv("data/religion.csv")
any_religion_flag = st.checkbox("Any Religion")
religion_list = df_religion["Religion"]

if not any_religion_flag:
    sel_religion = st.multiselect("**Select preferred Religions:**",religion_list )
else:
    sel_religion = religion_list

religion_percent = df_religion[df_religion["Religion"].isin(sel_religion)]['%'].sum()
st.success(f"##### **{religion_percent}**% of Indians lie in the selected religion choices.")
st.markdown("""---""")

#Caste

if not any_religion_flag:
    df_caste_religion = pd.read_csv("data/caste_religion.csv")

    any_caste_flag = st.checkbox("Any Caste")

    if not any_caste_flag:
        caste_list = ["SCs","STs","OBCs","General"]
        sel_caste = st.multiselect("**Select preferred Castes:**",caste_list)
    else:
        sel_caste = ["All Castes"]

    # st.write(df_caste_religion[df_caste_religion["Religion"].isin(sel_religion)][sel_caste])
    caste_percent = df_caste_religion[df_caste_religion["Religion"].isin(sel_religion)][sel_caste].sum(axis = 1).values
    caste_by_rel_percent = df_caste_religion[df_caste_religion["Religion"].isin(sel_religion)]["%"].values

    # st.write(caste_percent)
    # st.write(caste_by_rel_percent)

    caste_percent_final = np.sum(caste_by_rel_percent * caste_percent) / np.sum(caste_by_rel_percent)
    caste_percent_final = min(100,caste_percent_final )
    st.success(f"##### **{caste_percent_final}**% of population lies in the selected castes.")
    st.markdown("""---""")

    # st.write( caste_percent_final )
else:
    caste_percent_final = 100.0
# st.success(f"##### **{caste_percent_final}**% of population lies in the selected castes.")

st.markdown("""---""")
# Height
sel_height = st.select_slider("**Select the desired height (in cm):**", options = np.arange(130, 210, 2), value=(140, 200) )
height_percent = height_percentage_calc(sel_gender, sel_height[0], sel_height[1])
st.success(f"##### **{height_percent}**% of Indian {sel_gender}s lie in the selected height range.")


#working ratio based on gender 
working_percent =  working_ratio[sel_gender]

st.markdown("""---""")
# Final Score
col1, col2 = st.columns(2)
total_percent = 100.0 * income_percent / 100 * religion_percent / 100 * working_percent / 1.00 * caste_percent_final / 100 * height_percent / 100
col1.metric(label=f"**Percentage of Possible {sel_gender}**", value=str(round(total_percent, 6))+"%")


if income_number != "NA":
    total_count = income_number * total_percent
    col2.metric(label=f"**Number of Possible {sel_gender}**", value= total_count)

# df_religion_caste_merged = df1.merge(df2, on='common_column', how='inner')


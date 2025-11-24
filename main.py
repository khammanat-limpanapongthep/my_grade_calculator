import streamlit as st
import pandas as pd

weight = 0 
grade = 0
grade_dict = {
    "A" : 4.0,
    "B+" : 3.5,
    "B" : 3.0,
    "C+" : 2.5,
    "C" : 2.0, 
    "D+" : 1.5,
    "D" : 1.0,
    "F" : 0,
    "S" : 0,
    "U" : 0
}
col1, col2 = st.columns(2)

with st.sidebar:
    datasci = st.selectbox(
    "DATA SCI",
    ("A","B+","B","C+","C","D+","D","F"))
    adv_math = st.selectbox(
    "ADV MATH METH",
    ("A","B+","B","C+","C","D+","D","F"))
    cir_lab = st.selectbox(
    "CIR DIG ELEC LAB",
    ("A","B+","B","C+","C","D+","D","F"))
    fund_alg = st.selectbox(
    "FUND DS ALG",
    ("A","B+","B","C+","C","D+","D","F"))
    disrete = st.selectbox(
    "DISCRETE STRUC",
    ("A","B+","B","C+","C","D+","D","F"))
    elec = st.selectbox(
    "ELEC CIR ICE",
    ("A","B+","B","C+","C","D+","D","F"))
    lol = [datasci,adv_math,cir_lab,fund_alg,disrete,"S",elec]


with col1:
    st.subheader("Year 1 Sem 1")
    confusion_matrix = pd.DataFrame(
    {
        "COURSE": ["WINE EDUCATION","EXPL ENG WORLD","COMP PROG","CALCULUS I","PHYSICS ENGS","PHYSICS LAB ENGS","COMM ENG I"],
        "CREDITS": [3,3,3,3,3,1,3],
        "GRADES": ["S","A","A","A","B+","B","C+"],
    }
    )
    st.table(confusion_matrix)
    weight += 16
    grade += 57
with col2:
    st.subheader("Year 1 Sem 2")
    confusion_matrix = pd.DataFrame(
    {
        "COURSE": ["INTRO ICE","PROB STAT DATA","ADV COMP PROG","CALCULUS II","PHYSICS ELEC ENGS","PHYS ELEC LAB ELEC","COMM ENG II"],
        "CREDITS": [3,3,3,3,3,1,3],
        "GRADES": ["B+","C+","A","A","B+","A","A"],
    }
    )
    st.table(confusion_matrix)
    weight +=19
    grade += 68.5

col1, col2 = st.columns(2)

with col1:
    st.subheader("Year 2 Sem 1")
    confusion_matrix = pd.DataFrame(
    {
        "COURSE": ["DATA SCI","ADV MATH METH","CIR DIG ELEC LAB","FUND DS ALG","DISCRETE STRUC","AUTO STUDIES","ELEC CIR ICE"],
        "CREDITS": [3,3,1,4,3,3,3],
        "GRADES": lol,
    }
    )
    st.table(confusion_matrix)
    for i in range(len(lol)) :
        lol[i] = grade_dict[lol[i]]
    this_sem_grade = 0
    this_sem_weight = 17
    for i in range(7):
        this_sem_grade += ([3,3,1,4,3,3,3][i]) * (lol[i])

            
    weight += this_sem_weight
    grade += this_sem_grade

st.header("Summmary")
st.text("This Sem GPA: " + str(round(this_sem_grade / this_sem_weight , 2)))
st.text("Total Sem GPA: " + str(round(grade / weight , 2)))
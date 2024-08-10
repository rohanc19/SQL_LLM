from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def get_gemini_respomse(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt = [
    """
    You are a expert in converting english questions to SQL query! 
    The name of the SQL database is STUDENT and contains the following columns -
    NAME, CLASS, SECTION\n\n
    For example,\n
    Example 1 - How many entries of records are present?,
    SQL command - SELECT COUNT(*) FROM STUDENT;\n
    Example 2 - Tell me all students studying in Data Science class,
    SQL command - SELECT * FROM STUDENT where CLASS = "Data Science";
    also, the SQL code should not have ``` in the beginning nor end and should not have sql word in the output



    """
]    

st.set_page_config(page_title="Retrieval from SQL Query")
st.header("Gemini SQL Data Retrival")
question = st.text_input("Input :",key = "input")
submit = st.button("Ask question")

if submit:
    response = get_gemini_respomse(question, prompt)
    print(response)
    data = read_sql_query(response, "student.db")
    st.subheader("The Response is ")
    for row in data:
        print(row)
        st.header(row)
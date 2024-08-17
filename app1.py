import os
import sqlite3
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit page config
st.set_page_config(page_title="SQL Query Generator", layout="wide")

# Function to get Gemini response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to execute SQL query
def execute_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows
    except sqlite3.Error as e:
        st.error(f"Database error: {e}")
        return None

# Prompt for Gemini
prompt = [
    """
    You are an expert in converting English questions to SQL queries! 
    The SQL database is named STUDENT and contains the following columns:
    NAME, CLASS, SECTION, MARKS

    For example:
    Example 1 - How many entries of records are present?
    SQL command: SELECT COUNT(*) FROM STUDENT;

    Example 2 - Tell me all students studying in Data Science class
    SQL command: SELECT * FROM STUDENT WHERE CLASS = 'Data Science';

    Please provide only the SQL query without any additional text, backticks, or 'sql' prefix.
    """
]

# Streamlit UI
st.title("SQL Query Generator and Executor")

# Sidebar for database info
with st.sidebar:
    st.header("Database Information")
    st.info("Current database: student.db")
    st.info("Tables: STUDENT")
    st.info("Columns: NAME, CLASS, SECTION, MARKS")

# Main content
col1, col2 = st.columns([3, 2])

with col1:
    st.header("Ask a Question")
    question = st.text_input("Enter your question about the student database:", key="input")
    submit = st.button("Generate and Execute Query")

    if submit and question:
        with st.spinner("Generating SQL query..."):
            sql_query = get_gemini_response(question, prompt)
        
        st.subheader("Generated SQL Query")
        st.code(sql_query, language="sql")
        
        with st.spinner("Executing query..."):
            result = execute_sql_query(sql_query, "student.db")
        
        if result is not None:
            st.subheader("Query Result")
            st.table(result)

with col2:
    st.header("SQL Query Playground")
    user_query = st.text_area("Enter your own SQL query:", height=100)
    run_query = st.button("Run Query")

    if run_query and user_query:
        with st.spinner("Executing query..."):
            result = execute_sql_query(user_query, "student.db")
        
        if result is not None:
            st.subheader("Query Result")
            st.table(result)

# Footer
st.markdown("---")
st.markdown("Built with Streamlit and Google Generative AI")
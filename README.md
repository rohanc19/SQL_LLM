# Q-AChatBot_SQLdatabases
# SQL Query Generator and Executor

This project combines the power of Google's Generative AI (Gemini) with a SQLite database to create a natural language interface for querying student data. Users can ask questions in plain English, which are then converted to SQL queries and executed against the database.

## Features

- Natural language to SQL query conversion using Google's Gemini AI
- Execution of generated SQL queries against a SQLite database
- Direct SQL query execution for advanced users
- Interactive Streamlit web interface

## Prerequisites

- Python 3.7+
- Google API key for Gemini AI

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/sql-query-generator.git
   cd sql-query-generator
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the project root and add your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Usage

1. Set up the database:
   ```
   python sql.py
   ```
   This will create a `student.db` file in the `data` directory with sample data.

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

3. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

4. Use the interface to ask questions about the student data or execute custom SQL queries.

## Project Structure

```
sql-query-generator/
│
├── app.py              # Main Streamlit application
├── sql.py              # Database setup script
├── data/               
│   └── student.db      # SQLite database (created by sql.py)
├── .env                # Environment variables (API keys)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Contributing

Contributions to improve the project are welcome. Please feel free to submit a Pull Request.

## Acknowledgments

- Google for the Generative AI (Gemini) model
- Streamlit for the web application framework
- SQLite for the database engine

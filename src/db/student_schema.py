import sqlite3
from pathlib import Path
import pandas as pd
def check_sql_file(arg_1, arg_2, arg_3):
    the_sql_file = Path(__file__).parent.parent.joinpath(arg_1, arg_2, arg_3)
    return the_sql_file
def check_db_file(arg_1):
    the_db_file = Path(__file__).parent.joinpath(arg_1)
    return the_db_file
def check_csv_file(arg_1, arg_2, arg_3):
    the_csv_file = Path(__file__).parent.parent.joinpath(arg_1, arg_2, arg_3)
    return the_csv_file
def create_db(sql_script_path, db_path):
    """Create an SQLite database using a SQL schema script."""
    try:
        # Connect to the database (creates it if it doesn't exist)
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Read the SQL script from file
        with open(sql_script_path, 'r') as file:
            sql_script = file.read()

        # Execute the SQL script
        cursor.executescript(sql_script)

        # Commit and close
        connection.commit()
        print(f"Database created successfully at '{db_path}'.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def insert_data_from_csv(db_path, csv_path):
    """Insert teacher, student, and course data from a CSV file."""
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        # Read the CSV data
        df = pd.read_csv(csv_path)

        # Insert teachers
        teacher_df = df[['teacher_name', 'teacher_email']].drop_duplicates()
        cursor.executemany(
            "INSERT OR IGNORE INTO teacher (teacher_name, teacher_email) VALUES (?, ?);",
            teacher_df.values.tolist()
        )

        # Insert students
        student_df = df[['student_name', 'student_email']].drop_duplicates()
        cursor.executemany(
            "INSERT OR IGNORE INTO student (student_name, student_email) VALUES (?, ?);",
            student_df.values.tolist()
        )

        # Insert courses
        course_df = df[['course_name', 'course_code', 'course_schedule', 'course_location']].drop_duplicates()
        cursor.executemany(
            """INSERT OR IGNORE INTO course (course_name, course_code, course_schedule, course_location)
               VALUES (?, ?, ?, ?);""",
            course_df.values.tolist()
        )

        connection.commit()
        print("Data inserted into teacher, student, and course tables.")
    except Exception as e:
        print(f"Error inserting data: {e}")
    finally:
        connection.close()
if __name__ == "__main__":
    sql_script_path = check_sql_file("activities","starter","student_schema.sql")
    db_path = check_db_file("student_records.db")
    csv_path = check_csv_file("activities","data","student_data.csv")
    create_db(sql_script_path, db_path)
    insert_data_from_csv(db_path, csv_path)
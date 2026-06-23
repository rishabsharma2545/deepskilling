import psycopg2 as psql
import time

def get_db_connection():
    return psql.connect(
        dbname="college_db", user="postgres", password="310623104120", host="localhost", port = 5433
    )

# 56. Simulate the N+1 problem in Python: fetch all enrollments with SELECT * FROM enrollments, then loop through each row and issue a separate SELECT to fetch the student's name. Count the total queries executed.
def simulate_np1():
    conn = get_db_connection()
    cursor = conn.cursor()
    query_count = 0
    start_time = time.time()

    # 1 Query execution
    cursor.execute("SELECT student_id, course_id FROM enrollments;")
    enrollments = cursor.fetchall()
    query_count += 1

    # N Queries execution
    for row in enrollments:
        student_id = row[0]
        cursor.execute(f"SELECT first_name, last_name FROM students WHERE student_id = {student_id};")
        student_name = cursor.fetchone()
        query_count += 1

    end_time = time.time()
    cursor.close()
    conn.close()
    
    print(f"N+1 Approach")
    print(f"Total Queries Executed: {query_count}")
    print(f"Execution Latency Time: {end_time - start_time:.4f} seconds\n")


# 57. Rewrite the script using a single JOIN query that retrieves all enrollment records with student names in one query.
def run_optimized_join():
    conn = get_db_connection()
    cursor = conn.cursor()
    query_count = 0
    start_time = time.time()

    optimized_query = """
        SELECT e.course_id, s.first_name, s.last_name 
        FROM enrollments e
        INNER JOIN students s ON e.student_id = s.student_id;
    """
    cursor.execute(optimized_query)
    results = cursor.fetchall()
    query_count += 1

    end_time = time.time()
    cursor.close()
    conn.close()

    print(f"Optimized Approach")
    print(f"Total Queries Executed: {query_count}")
    print(f"Execution Latency Time: {end_time - start_time:.4f} seconds\n")

# 58. Compare the number of database round-trips between the two approaches and log the difference using Python's time module.
try:
    simulate_np1()
    run_optimized_join()
except Exception as err:
    print(f"Connection/execution error checked: {err}")

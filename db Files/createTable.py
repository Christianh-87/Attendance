import sqlite3
import sys
 
# Define valid SQLite data types for basic validation
SQLITE_TYPES = ['INTEGER', 'TEXT', 'REAL', 'BLOB', 'NULL']
 
def construct_sql_query(table_name: str, column_data: list) -> str:
    """Builds the final CREATE TABLE SQL string."""
    # 1. Start with the required Primary Key
    definitions = ["id INTEGER PRIMARY KEY"]
    # 2. Add the user-defined columns
    for name, data_type, not_null in column_data:
        constraint = " NOT NULL" if not_null else ""
        definitions.append(f"{name} {data_type}{constraint}")
    # 3. Format the definitions into the final query
    column_string = ",\n    ".join(definitions)
    return f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        {column_string}
    );
    """
 
def run_db_creation(db_name: str):
    """Handles user input, SQL generation, and database execution."""
 
    print(f"--- Welcome to the {db_name} Table Wizard ---")
    # --- Collect Table Name ---
    table_name = input("Enter the name for your new table: ").strip()
    if not table_name:
        print("Table name is required. Exiting.")
        sys.exit()
 
    # --- Collect Column Definitions ---
    columns_to_add = []
    print("\nAvailable Data Types: INTEGER, TEXT, REAL, BLOB (NULL is also an option)")
    print("Column 'id INTEGER PRIMARY KEY' is included automatically.")
 
    while True:
        col_name = input("\nColumn Name (or type 'done'): ").strip()
        if col_name.lower() == 'done':
            if len(columns_to_add) < 1:
                print("Please define at least one column besides 'id'.")
                continue
            break
        # Get and validate the data type
        col_type = input(f"Data Type for '{col_name}': ").strip().upper()
        if col_type not in SQLITE_TYPES:
            print(f"Invalid type '{col_type}'. Must be one of: {', '.join(SQLITE_TYPES)}. Try again.")
            continue
        # Get NOT NULL constraint
        is_not_null = input("Allow NULL values? (y/N - default is No): ").strip().lower() in ('n', '')
        # Store as a tuple (name, type, not_null_boolean)
        columns_to_add.append((col_name, col_type, is_not_null))
 
    # --- Generate and Execute SQL ---
    sql_command = construct_sql_query(table_name, columns_to_add)
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        print("\n--- Generated SQL Command ---")
        print(sql_command)
        cursor.execute(sql_command)
        conn.commit()
        print(f"\n✅ SUCCESS! Table **'{table_name}'** has been created in **'{db_name}'**.")
    except sqlite3.Error as e:
        print(f"\n❌ DATABASE ERROR: Could not create table. Details: {e}")
    finally:
        if conn:
            conn.close()
 
# ----------------------------------------------------------------------
 
if __name__ == "__main__":
    # The dedicated database file name
    DATABASE_FILE = "dragon.db"
    run_db_creation(DATABASE_FILE)
import sqlite3
import os
import hashlib

# 1. HARDCODED SECRET / CREDENTIAL (Security Risk)
# CodeQL Rule: py/hardcoded-credentials
DB_PASSWORD = "SuperSecretAdminPassword123!"

def get_user_data(username):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    # 2. SQL INJECTION (CWE-89)
    # Concatenating raw user input directly into an SQL string
    # CodeQL Rule: py/sql-injection
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    
    return cursor.fetchall()

def run_system_ping(host):
    # 3. COMMAND / SHELL INJECTION (CWE-78)
    # Passing unsanitized user input straight into a OS command shell
    # CodeQL Rule: py/command-line-injection
    os.system(f"ping -c 1 {host}")

def hash_password(password):
    # 4. WEAK CRYPTOGRAPHY (CWE-327)
    # MD5 is broken and easily cracked; secure apps must use SHA-256 or bcrypt
    # CodeQL Rule: py/weak-cryptographic-algorithm
    return hashlib.md5(password.encode()).hexdigest()

if __name__ == "__main__":
    # Test execution
    user_input = "admin' OR '1'='1"
    print("Fetching user:", get_user_data(user_input))
    
    user_host = "127.0.0.1; ls -la"
    run_system_ping(user_host)
    
    print("Hashed pass:", hash_password("12345"))
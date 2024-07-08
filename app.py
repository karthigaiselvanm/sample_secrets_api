# app.py
import os

def get_database_url():
    return "postgresql://user:password@localhost/mydatabase"

def get_api_key():
    return "SG.s3cr3tK3y.1U5"

def main():
    db_url = get_database_url()
    api_key = get_api_key()
    print(f"Connecting to database at {db_url} with API key {api_key}")

if __name__ == "__main__":
    main()

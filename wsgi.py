from app import app, init_db

# Initialize the database tables
init_db()

if __name__ == "__main__":
    app.run()

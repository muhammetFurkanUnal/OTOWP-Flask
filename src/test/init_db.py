
def initTest(app, db):
    with app.app_context():
        db.create_all()  # This creates all tables defined in your models
        print("Database tables created successfully.")
        
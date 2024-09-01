from app import create_app, db
from test import initTest, updateTest, clearTest

app = create_app()

# initTest(app, db)
# clearTest(app)
updateTest(app)

print("test works!")
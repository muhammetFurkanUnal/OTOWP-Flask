from app import create_app, db
from test import initTest, updateTest, clearTest, deleteTest

app = create_app()

# initTest(app, db)
# clearTest(app)
# updateTest(app)
# deleteTest(app)

print("test works!")
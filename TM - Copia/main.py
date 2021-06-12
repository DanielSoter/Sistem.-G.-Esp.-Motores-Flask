from app import create_app
from flask_admin import Admin

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

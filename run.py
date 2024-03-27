# run.py-1-A+
from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    app.run(host=os.getenv('FLASK_RUN_HOST', '127.0.0.1'),
            port=int(os.getenv('FLASK_RUN_PORT', 5000)),
            debug=True)  # Set debug=False for production

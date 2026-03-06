from flask import Flask
from dotenv import load_dotenv

from data.database import init_db

load_dotenv()

app = Flask(__name__)
init_db(app = app)

@app.route('/')
def home():
    return 'Hello World !'
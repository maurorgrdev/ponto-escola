# app/config/database.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Base = db.Model
from app import app
import os


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Ingreso871@localhost/Irso"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


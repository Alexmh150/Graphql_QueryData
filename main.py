from flask import Flask
from flask_graphql import GraphQLView
from models import db, Alumno
from schemas import schema
import json

PATH_DATA_JSON = 'data/partidos2.json'

app = Flask(__name__)
app.config.from_pyfile("settings.py")
db.init_app(app)

@app.before_first_request
def crea_bases():
    db.create_all()
    with open(PATH_DATA_JSON) as f:
        alumnos = json.load(f)
    for alumno in alumnos:
        db.session.add(Alumno(**alumno))
    db.session.commit()

app.add_url_rule(
        '/graphql'
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
    )
)

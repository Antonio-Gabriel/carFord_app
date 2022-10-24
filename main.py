from flask import Flask
from src.infra.http.routes.persons_route import persons_route
from src.infra.http.routes.vehicles_route import vehicles_route

app = Flask(__name__)
app.register_blueprint(persons_route)
app.register_blueprint(vehicles_route)


@app.get("/")
def main():
    """default route to greet"""
    return {"msg": "CarFord API"}

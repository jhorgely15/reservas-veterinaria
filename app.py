from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1> Bienvenido al Sistema de Reservas Veterinarias</h1>"

@app.route("/reservas")
def reservas():
    return "<h2>Listado de reservas</h2>"

@app.route("/reservas/nueva")
def nueva_reserva():
    return "<h2>Crear nueva reserva</h2>"

@app.route("/reservas/<int:id>/editar")
def editar_reserva(id):
    return f"<h2>Editando reserva {id}</h2>"

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

# Lista de poemas
poemas = [
    "En el jardín de la vida, floreces con alegría, tu risa es la melodía, que ilumina el día. \n"
    "Hoy el sol brilla más por ti, cada rayo es un abrazo, cada brisa un canto, \n"
    "te celebro en este momento, en el que el tiempo se detiene, \n"
    "y la felicidad danza en el aire.\n",

    "Hoy es tu cumpleaños, celebra con pasión, cada año es un regalo, una nueva canción. \n"
    "Deja que la luz de este día penetre en tu ser, \n"
    "cada susurro de la brisa te hable de sueños, \n"
    "y cada estrella en el cielo sea testigo de tu viaje.\n",

    "En este día especial, deseo para ti, amor, paz y felicidad, todo lo que hay en mí. \n"
    "Las olas del mar traen los ecos de un futuro brillante, \n"
    "donde tus risas resuenan como un canto ancestral, \n"
    "y la vida, en su infinita belleza, te abraza con suavidad.\n"
]


@app.route("/", methods=["GET", "POST"])
def index():
    nombre = ""
    poema_seleccionado = ""

    if request.method == "POST":
        nombre = request.form.get("nombre")
        poema_index = request.form.get("poema")

        # Verificamos que se ha seleccionado un poema
        if poema_index is not None:
            poema_seleccionado = poemas[int(poema_index)]

    return render_template("index.html", nombre=nombre, poema=poema_seleccionado, poemas=poemas)


if __name__ == "__main__":
    app.run(debug=True)

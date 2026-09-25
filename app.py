from flask import Flask, render_template, request

from modelos import Estudiante, Docente
from excepciones import CorreoInvalidoError

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', mensaje=None)

@app.route('/registrar', methods=['POST'])
def registrar():
    try:
        nombre = request.form.get('nombre', '').strip()
        correo = request.form.get('correo', '').strip()
        tipo = request.form.get('tipo', '').strip()  

        if not nombre or not correo:
            raise ValueError("El nombre y el correo son obligatorios.")

        if '@' not in correo: 
            raise CorreoInvalidoError("El correo debe contener '@'.")

        if tipo == 'estudiante':
            carnet = request.form.get('carnet', '').strip()
            persona = Estudiante(nombre, correo, carnet)

        elif tipo == 'docente':
            lector_biometrico = request.form.get('lector_biometrico', '').strip()
            persona = Docente(nombre, correo, lector_biometrico)

        else:
            raise ValueError("Debe indicar si es estudiante o docente.")

    except CorreoInvalidoError as e:
        mensaje = f"Error de correo: {e}"
    except ValueError as e:
        mensaje = str(e)
    else:
        mensaje = "Persona registrada con éxito."
    finally:
        print("Intento de registro procesado.")

    return render_template('index.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
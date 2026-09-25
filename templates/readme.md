# App Escuela CR

Aplicación web hecha en Flask para registrar personas usuarias (estudiantes y docentes) de una escuela, con validación de datos, manejo de excepciones y persistencia en formato JSON.

# ¿Qué hace la aplicación?

- Permite registrar personas mediante un formulario web, indicando si son **estudiante** (con carné) o **docente** (con lector biométrico).
- Valida que el nombre y el correo no vengan vacíos, y que el correo tenga un formato válido (usa una excepción personalizada `CorreoInvalidoError`).
- Guarda cada persona registrada en el archivo `usuarios.json`.
- Muestra en la misma página la lista de personas ya registradas.


## Requisitos
- Python 3.10 o superior
- Flask

## Cómo ejecutarla
1. Clona o descarga este repositorio.
2. Instala las dependencias:
```bash
   pip install -r requirements.txt
```
3. Ejecuta la aplicación:
```bash
   python app.py
```
4. Abre tu navegador en:
http://127.0.0.1:5000

5. Llena el formulario indicando el tipo de persona (estudiante o docente) y regístrala. Los datos quedan guardados en `usuarios.json`.

## Manejo de excepciones
El registro usa `try/except/else/finally`:
- Lanza `ValueError` si el nombre o el correo vienen vacíos.
- Lanza `CorreoInvalidoError` (excepción propia) si el correo no contiene `@`.
- Muestra un mensaje de éxito en el bloque `else` si todo salió bien.

Gracias por su tiempo!! (hice lo mejor que pude)
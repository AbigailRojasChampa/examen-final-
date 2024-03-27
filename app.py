from flask import Flask

app = Flask (__name__)

@app.route("/")
def portada():
      return '''
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>MI PRESENTACION</title>
        </head>
        <body>
            <h1>MI PRESENTACION</h1>
            <img src="https://cdn.icon-icons.com/icons2/2859/PNG/512/avatar_face_man_boy_profile_smiley_happy_people_icon_181659.png" alt="Descripción de la imagen">
            <p>Nombre: Nombre del usuario</p>
        </body>
        </html>
      '''
if __name__ == "__main__":
       app,run(debug=True)

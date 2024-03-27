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
    <title>Tipos de Maquillaje</title>
</head>
<body>
    <header>
        <h1>Tipos de Maquillaje</h1>
    </header>
    <main>
        <section>
            <h2>Maquillaje</h2>
            <img src="https://elcomercio.pe/resizer/baG32pMFY-rnpgNfZwezvZ0TRSo=/980x0/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/SVSVLNI6KBAZDJTYROSRRHWTTY.png" alt="Descripción de la imagen">
            <p>Nombre: maquillaje</p>
        </section>
    </main>
</body>
</html>

      '''
if __name__ == "__main__":
       app,run(debug=True)

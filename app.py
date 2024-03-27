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
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #ffcccc;
            padding: 20px;
            text-align: center;
        }
        h1 {
            margin: 0;
            color: #333;
        }
        main {
            padding: 20px;
        }
        section {
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-bottom: 20px;
        }
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 0 auto 20px;
            border-radius: 5px;
        }
        p {
            margin: 0;
            color: #666;
        }
    </style>
</head>
<body>
    <header>
        <h1>Tipos de Maquillaje</h1>
    </header>
    <main>
        <section>
            <h2>Maquillaje</h2>
            <img src="https://elcomercio.pe/resizer/baG32pMFY-rnpgNfZwezvZ0TRSo=/980x0/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/SVSVLNI6KBAZDJTYROSRRHWTTY.png" alt="Maquillaje">
            <p>El maquillaje es una forma de arte que nos permite resaltar la belleza natural del rostro.</p>
        </section>
    </main>
</body>
</html>

      '''
if __name__ == "__main__":
       app,run(debug=True)

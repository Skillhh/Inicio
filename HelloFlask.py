import json

from flask import Flask
from flask import render_template, url_for,redirect, request

#from flask import request

app = Flask( __name__ )


@app.route("/")
@app.route("/<nombre>")
def hola_mundo(nombre="Invitado"):
#    nombre = request.args.get('nombre',nombre)    
#    return "Hola %s" % nombre
#    return render_template("index.html", nombre=nombre)
    try:
        data = json.loads(request.cookies.get('data'))
    except TypeError:
        data = {}
    else:
        nombre = data.get('nombre')

    contexto = {'nombre': nombre} 
    return render_template("index.html", **contexto)

@app.route("/suma/<int:a>/<int:b>")
@app.route("/suma/<float:a>/<float:b>")
def sumar( a = 0, b = 0):
#    a = request.args.get('a',a)
#    b = request.args.get('b',b)
#    c = int(a) + int(b)
    # return """ 
    #         <html lang="en">
    #     <head>
    #         <meta charset="UTF-8">
    #         <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #         <meta http-equiv="X-UA-Compatible" content="ie=edge">
    #         <title>Sumar</title>
    #     </head>
    #     <body>
    #         <h2>{} + {} = {}</h2>
    #     </body>
    #     </html>
    # """.format( a,b, a + b  )
    # return "{} + {} = {}".format( a,b, a + b  )
    sumar = { 'a':a, 'b':b}
    return render_template("sumar.html", **sumar)

#resta
@app.route("/resta/<int:r1>/<int:r2>")
def restar( r1=0, r2=0):
    resta = { 'r1':r1, 'r2':r2 }
    return render_template("resta.html", **resta)

#Multiplicar
@app.route("/multiplica/<int:mul>/<int:multr>")
def multiplicacion( mul = 0, multr = 0 ):
    multiplica = { 'mul':mul, 'multr':multr }
    return render_template("multiplicacion.html", **multiplica )

#division
@app.route("/division/<int:d1>/<int:d2>")
def division( d1=0, d2=0 ):
    dividir = { 'd1':d1, 'd2':d2 }
    return render_template("division.html", **dividir)

#formulario
@app.route("/contacto")
def contacto ():
    return render_template("contacto.html")    

#Enviar formulario
@app.route("/enviado", methods=['POST'])
def enviado():
    response = redirect(url_for('hola_mundo'))
    response.set_cookie('data',json.dumps(dict(request.form.items())))
    response.set_cookie('Sesion', 'Informacion')
    
    # return render_template("enviado.html")
    return response

if __name__ == "__main__":
    app.run(debug=True)
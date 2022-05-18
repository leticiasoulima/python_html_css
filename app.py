from flask import Flask, render_template ##primeiro flask minusculo e o segundo flask com letra maiuscula

app = Flask("Rugby")  #criamos um novo serviço

@app.route("/rugby")  ##recurso que uma URL chama uma determinada função.
def rugby(): #função
    return render_template("hello.html")

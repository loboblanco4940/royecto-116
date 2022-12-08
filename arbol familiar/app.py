# importar modulos de la biblioteca Flask.
from flask import Flask , render_template

# crear objetos de la clase Flask, dando __name__ como argumento.
app = Flask(__name__)

# escribir las rutas usando las funciones "decorator".
# ruta o 'URL' predefinida.
@app.route("/")
def home():

    name = "Emmanuel" # escribe tu nombre
    age = "18" # escribe tu edad

    return render_template('index.html' , name = name , age = age)

# define la ruta a la página web de tu padre.
def father():

    name = "Edgar" 
    age = "44" 

    return render_template('father.html' , name = name , age = age)

# define la ruta a la página web de tu madre.
def mother():

    name = "Lupita" 
    age = "47" 

    return render_template('mother.html' , name = name , age = age)

# define la ruta a la página web de tus amigos.
def friend():

    name = "Julian" 
    age = "16" 

    return render_template('index.html' , name = name , age = age)

# agrega otras rutas, si tú quieres.




# ejecuta el archivo
if __name__  ==  '__main__':
    app.run(debug=True)

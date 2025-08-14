from flask import Flask

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return '''
    <h1>¡Bienvenido a mi aplicación Flask!</h1>
    <p>La aplicación está funcionando correctamente.</p>
    <p><a href="/usuario/Santiago">Prueba la ruta personalizada</a></p>
    '''

# Ruta con parámetro para mensaje personalizado
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'''
    <h1>¡Bienvenido, {nombre}!</h1>
    <p>Esta es tu página personalizada.</p>
    <p><a href="/">Volver al inicio</a></p>
    '''

# Ruta adicional para demostrar más funcionalidades
@app.route('/about')
def about():
    return '''
    <h1>Acerca de</h1>
    <p>Esta es una aplicación Flask básica creada como proyecto de aprendizaje.</p>
    <p><a href="/">Volver al inicio</a></p>
    '''

if __name__ == '__main__':
    # Ejecutar la aplicación en modo debug
    app.run(debug=True)
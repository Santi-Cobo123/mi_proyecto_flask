from flask import Flask
import os

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return '''
    <h1>¡Bienvenido a mi aplicación Flask!</h1>
    <p>La aplicación está funcionando correctamente en Render.</p>
    <p><a href="/usuario/Santiago">Prueba la ruta personalizada</a></p>
    '''

# Ruta con parámetro para mensaje personalizado
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'''
    <h1>¡Bienvenido, {nombre}!</h1>
    <p>Esta es tu página personalizada desplegada en Render.</p>
    <p><a href="/">Volver al inicio</a></p>
    '''

# Ruta adicional para demostrar más funcionalidades
@app.route('/about')
def about():
    return '''
    <h1>Acerca de</h1>
    <p>Esta es una aplicación Flask básica desplegada en Render.</p>
    <p><a href="/">Volver al inicio</a></p>
    '''

if __name__ == '__main__':
    # Para desarrollo local
    if os.environ.get('PORT'):
        # Para producción en Render
        port = int(os.environ.get('PORT'))
        app.run(debug=False, host='0.0.0.0', port=port)
    else:
        # Para desarrollo local
        app.run(debug=True)
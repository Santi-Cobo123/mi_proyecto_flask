from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Página de inicio"""
    user_name = "Usuario"  # Puedes cambiar esto por datos dinámicos
    projects = [
        {"name": "Proyecto Web", "description": "Una aplicación web con Flask"},
        {"name": "API REST", "description": "API para gestión de datos"},
        {"name": "Dashboard", "description": "Panel de control interactivo"}
    ]
    return render_template('index.html', 
                         user_name=user_name, 
                         projects=projects,
                         page_title="Inicio")

@app.route('/about')
def about():
    """Página Acerca de"""
    team_members = [
        {"name": "Santiago Cobo", "role": "Desarrollador Senior"},
        {"name": "Carlos López", "role": "Diseñador UX/UI"},
        {"name": "María Rodríguez", "role": "Product Manager"}
    ]
    return render_template('about.html', 
                         team_members=team_members,
                         page_title="Acerca de")

@app.route('/contact')
def contact():
    """Página de contacto (opcional)"""
    return render_template('contact.html', page_title="Contacto")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
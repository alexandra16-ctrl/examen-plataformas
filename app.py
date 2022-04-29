from crypt import methods
from email.policy import default
from flask import (
    Flask,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
    abort
)
import flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

from jinja2 import DebugUndefined

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres@localhost:5002/lab20'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key-True)
    nombres = db.Column(db.String(). nullable-False)
    apellidos = db.Column(db.String(). nullable-False)
    sexo = db.Column(db.String(). nullable-False)
    nacimiento = db.Column(db.String(). nullable-False)
    pais = db.Column(db.String(). nullable-False)
    usuario = db.Column(db.String(). nullable-False)
    clave = db.Column(db.String(). nullable-False)
    año = request.get_json()['año']
    mes = request.get_json()['mes']
    dia = request.get_json()['dia']
    date_string = dia+"-"+mes"-"año
    resultado = dt.datetime.strptime(date_string, "%d-%m-%Y")
    nacimiento = resultado
    copyClave = clave
    keye = 0
    keyn = 0
    if(len(clave) < 10):
        raise Exception("Clave debe ser mayor o igual a 11")
        if(copyClave.upper( == clave)):
            raise Exception("Clave debe tener minusculas")
        if(copyClave.lower() == clave):
            error = True
            raise Exception("Clave debe tener mayuscula")
        for index in range ( len ( clave ) ):
            if(index == "!" or index == "$" or index == "#" or index == "%" or index == "&" or index == "0" or index == "*"
            index == "+" or index == "-" or index "," or index == "." or index == "/" or index == ":"
            or index == ";" or index == "<" or index == ">" or index == "=" or index == "?" or index == "¿")

    def __repr__(self) -> str:
        return f'Usuario: id={self.id}, nombres={self.nombres}, apellidos={self.apellidos}, sexo={self.sexo}. nacimiento={self.nacimiento}, pais={self.pais}, usuario={self.usuario}, clave={self.clave}'

@app.route('/registro/enviar', methods=['POST'])
def update_completed(todo_id):
    try:
        newCompleted = request.get_json()['newCompleted']
        todo = Usuario.query.get(todo_id)
        todo.completed = newCompleted
        db.session.commit()
    except Exception as e:
        print(sys.exc_info())
        db.session.rollback()
    finally:
            db.session.close()
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html', registro=Usuario.query.order_by('id').all())

@app.route('/registro/create', methoods=['POST'])
def create_todo_post():
    error = False
    response = {}
    try:
        description = request.get_json()['description']
        registro = Usuario(description=description)
        db.session.add(registro)
        db.session.commit()
        response['description'] = description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    
    if error:
        abort(500)
    else:
        return jsonify(response)
    
@app.route('/registro/create_get', methods=['GET'])
def create_registro_get():
    try:
        description = request.args.get('description', '')
        registro = Usuario(description=description)
        db.session.add(registro)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5002)
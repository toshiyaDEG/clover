import pymongo
myclient = pymongo.MongoClient("mongodb+srv://toshiya:Kaoru_191219@seele.ouyyh.mongodb.net/Bedu?retryWrites=true&w=majority")
mydb = myclient["bedu"]


from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'bedu'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/bedu'

# configuraciones
app.secret_key = 'mysecretkey'


# Template de registro de alumnos
@app.route('/registro', methods=['GET','PUT'])
def RegistroAlumnos():
    return render_template('formt.html')

# GET para traer datos de alumnos y visualizar lista
@app.route('/get', methods=['GET'])
def listaAlumnos():
    mycol = mydb["alumnos"]
    output = []
    for x in mycol.find():
        output.append({'_id': x['_id'], 'nombre1' : x['nombre1'], 'nombre2' : x['nombre2'], 'apellido1' : x['apellido1'], 'apellido2' : x['apellido2'], 'tutor' : x['tutor'], 'telefono' : x['telefono'], 'correo' : x['correo']})
    grupo = output
    return render_template('lista.html', alumnos = grupo)

# POST para enviar alumnos a la BD
@app.route('/add_contact', methods=['POST'])
def add_contact():
    mycol = mydb["alumnos"]
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        apellido1 = request.form['apellido1']
        apellido2 = request.form['apellido2']
        tutor = request.form['tutor']
        telefono = request.form ['telefono']
        correo = request.form['correo']
        _id = mycol.insert_one({'nombre1': nombre1, 'nombre2': nombre2, 'apellido1': apellido1, 'apellido2': apellido2, 'tutor': tutor, 'telefono': telefono, 'correo': correo})
        # new_a = mycol.find_one({'_id': _id})
        flash('Alumno registrado satisfactoriamente')
    return redirect(url_for('RegistroAlumnos'))

@app.route('/home', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/uptareas', methods=['GET'])
def uptareas():
    return render_template('up_tarea.html')

@app.route('/sendtarea', methods=['GET'])
def sendtarea():
    return render_template('mi_tarea.html')

@app.route('/amaterias', methods=['GET'])
def amaterias():
    return render_template('alumno_materias.html')

@app.route('/tutorial', methods=['GET'])
def tutorial():
    return render_template('tutorial.html')

#PUT UPDATE
@app.route('/alumnos', methods=['PUT'])
def editPeople():
    mycol = mydb["alumnos"]
    myquery = { "tutor": "Sofia" }
    newvalues = { "$set": { "tutor": "Arturo" } }
    mycol.update_one(myquery, newvalues)
    return jsonify({"message": "People Updated"})


#DELETE
@app.route('/alumnos', methods=['DELETE'])
def deletePeople():
    mycol = mydb["alumnos"]
    myquery = { "nombre1": "nombre" }
    mycol.delete_one(myquery)
    return jsonify({"message": "People Delete"})

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/edit/<string:id>')
# def get_alumno(id):
#     mycol = mydb["alumnos"]
#     output = ()
#     for x in mycol.find({'_id':id}):
#         output.append({'_id' : x['_id'], 'nombre1' : x['nombre1'], 'nombre2' : x['nombre2'], 'apellido1' : x['apellido1'], 'apellido2' : x['apellido2'], 'tutor' : x['tutor'], 'telefono' : x['telefono'], 'correo' : x['correo']})
#     return jsonify({'result' : output})
#     # return render_template('getalumno.html', alumnos = grupo)

# @app.route('/update/<id>')
# def update_contact(id):
#     mycol = mydb["alumnos"]
#     output = []
#     for x in mycol.find():
#         output.append({'_id': x['_id'], 'nombre1' : x['nombre1'], 'nombre2' : x['nombre2'], 'apellido1' : x['apellido1'], 'apellido2' : x['apellido2'], 'tutor' : x['tutor'], 'telefono' : x['telefono'], 'correo' : x['correo']})
#     grupo = output
#     myquery = { "address": "Farm 5" }
#     newvalues = { "$set": { "address": "Granja 00" } }
#     mycol.update_one(myquery, newvalues)
#     return render_template('update.html', alumnos = grupo)


# @app.route('/delete/<string:id>')
# def delete_alumno(id):
#     mycol = mydb["alumnos"]
#     myquery = { '_id': id }
#     mycol.delete_one(myquery)
#     flash('Alumno borrado satisfactoriamente')
    # return ("Usuario borrado")

# @app.route('/test/<string:id>', methods=['GET', 'DELETE'])
# def test(id):
#     mycol = mydb["alumnos"]
#     output = []
#     myquery = { '_id': id }
#     x = mycol.find_one(myquery)
#     output.append({'nombre1' : x['nombre1'], 'nombre2' : x['nombre2'], 'apellido1' : x['apellido1'], 'apellido2' : x['apellido2'], 'tutor' : x['tutor'], 'telefono' : x['telefono'], 'correo' : x['correo']})
#     grupo = output
#     return render_template('test.html', alumnos = grupo[0])


# POST
# @app.route('/alumnos', methods=['POST'])
# def addPeople():
#     mycol = mydb["alumnos"]
#     name = request.json['name']
#     address = request.json['address']
#     cel = request.json['cel']
#     email = request.json['email']
#     _id = mycol.insert({'name': name, 'address': address, 'cel': cel, 'email': email})
#     new_p = mycol.find_one({'_id': _id })
#     output = {'name' : new_p['name'], 'address' : new_p['address'], 'cel' : new_p['cel'], 'email' : new_p['email']}
#     return jsonify({'result' : output})


#GET
# @app.route('/alumnos', methods=['GET'])
# def getAllPeople():
#     mycol = mydb["alumnos"]
#     output = []
#     for x in mycol.find():
#         output.append({'name' : x['name'], 'address' : x['address']})
#     return jsonify({'result' : output})
        # print(x)

# mycol = mydb["alumnos"]
# get para el primer documento
# x = mycol.find_one()
# get para todos los documentos
# for x in mycol.find():
# get con campos específicos
# for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
# get omitiendo un campo ->>0
# for x in mycol.find({}, {"address":0}):
#    print(x)

#PUT UPDATE
# @app.route('/alumnos', methods=['PUT'])
# def editPeople():
#     mycol = mydb["alumnos"]
#     myquery = { "address": "Farm 5" }
#     newvalues = { "$set": { "address": "Granja 00" } }
#     mycol.update_one(myquery, newvalues)
#     return jsonify({"message": "People Updated"})


#DELETE
# @app.route('/alumnos', methods=['DELETE'])
# def deletePeople():
#     mycol = mydb["alumnos"]
#     myquery = { "address": "Sakura 90" }
#     mycol.delete_one(myquery)
#     return jsonify({"message": "People Delete"})




# @app.route('/alumnos', methods=['POST'])
# def addAlumno():
#     mycol = mydb["alumnos"]
#     nombre1 = request.json['nombre1']
#     nombre2 = request.json['nombre2']
#     apellido1 = request.json['apellido1']
#     apellido2 = request.json['apellido2']
#     tutor = request.json['tutor']
#     telefono = request.json ['telefono']
#     correo = request.json['correo']
#     _id = mycol.insert({'nombre1': nombre1, 'nombre2': nombre2, 'apellido1': apellido1, 'apellido2': apellido2, 'tutor': tutor, 'telefono': telefono, 'correo': correo})
#     new_a = mycol.find_one({'_id': _id})
#     output = {'nombre1': new_a['nombre1'], 'nombre2': new_a['nombre2'], 'apellido1': new_a['apellido1'], 'apellido2': new_a['apellido2'], 'tutor': new_a['tutor'], 'telefono': new_a['telefono'], 'correo': new_a['correo'], }
#     return jsonify({'result' : output})



# http://localhost:5000/alumnos


    # mycol = mydb["alumnos"]
    # alumnos = mycol.alumnos.find({})
    # x = alumnos
    # print(x)
    # return render_template('formt.html')
    #     output.append({'nombre1' : x['nombre1'], 'nombre2' : x['nombre2'], 'apellido1' : x['apellido1'], 'apellido2' : x['apellido2'], 'tutor' : x['tutor'], 'telefono' : x['telefono'], 'correo' : x['correo']})
    # print(output)
    # return jsonify({'result' : output}


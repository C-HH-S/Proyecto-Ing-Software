from flask_mysqldb import MySQL
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
#import mysql.connector

app = Flask(__name__, static_folder='static', template_folder='template')


# Configura la conexión a la base de datos MySQL
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "bd_gimnasio"
mysql = MySQL(app)

# Inicializar sesion
app.secret_key = 'mysecretkey'


# Base de datos ficticia para usuarios
users_db = [{'nombre': 'maria', 'apellido': 'lopez', 'edad': '23', 'correo': 'maria@lopez', 'telefono': '2345678765', 'contraseña': '000'},
            {'nombre': 'jose', 'apellido': 'torres', 'edad': '22',
                'correo': 'jose@torres', 'telefono': '89765756876', 'contraseña': '001'},
            {'nombre': 'ana', 'apellido': 'cruz', 'edad': '45', 'correo': 'ana@cruz', 'telefono': '5678908767', 'contraseña': '002'}]


# Ruta para la página de inicio de sesión
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']
        usuario = authenticate_user(nombre, contraseña)
        if usuario:
            if usuario['nombre'] == 'maria' and usuario['contraseña'] == '000':
                return redirect('/administrador')
            if usuario['nombre'] == 'jose' and usuario['contraseña'] == '001':
                return redirect('/entrenador')
            if usuario['nombre'] == 'ana' and usuario['contraseña'] == '002':
                return redirect('/miembro')
        else:
            return 'Error: Usuario o contraseña incorrectos'
    return render_template('login.html')

# Función para autenticar al usuario
def authenticate_user(nombre, contraseña):
    for user in users_db:
        if user['nombre'] == nombre and user['contraseña'] == contraseña:
            return user
    return None


# Ruta para el panel del administrador (administrador)
@app.route('/administrador')
def administrador():
    for user in users_db:
        print(user)
    return render_template('administrador.html')

@app.route('/gestion_usuarios')
def gestion_usuarios():
     return render_template('gestion_usuarios.html')

@app.route('/gestion_maquinas')
def gestion_maquinas():
     return render_template('gestion_maquinas.html')



# Ruta para el panel del miembro (miembro)
@app.route('/miembro')
def miembro():
    return render_template('miembro.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/info_personal_user')
def info_personal_user():
    return render_template('info_personal_user.html')

@app.route('/cambio_contrasena_user')
def cambio_contrasena_user():
    return render_template('cambio_contrasena_user.html')

@app.route('/membresia_user')
def membresia_user():
    return render_template('membresia_user.html')

# Ruta para el panel del entrenador (entrenador)
@app.route('/entrenador')
def entrenador():
    return render_template('entrenador.html')

# Ruta para el panel de añadir maquina
@app.route('/agregar_maquina')
def añadir_maquina():
    return render_template('agregar_maquina.html')

# Ruta para el panel de ver historial de maquinaria
@app.route('/vista_historial_maquinaria')
def ver_historial():
    return render_template('vista_historial_maquinaria.html')


# Vista para el listado de ususarios
@app.route('/listado_usuarios', methods=['GET', 'POST'])
def listado_usuarios():
    return render_template('listado_usuarios.html')

#membresia administrador
@app.route('/membresia')
def membresia():
        #cur = mysql.connection.cursor()
        #cur.execute("SELECT * FROM clientes")  
        #rows = cur.fetchall()
        #cur.close()
        #return render_template('membresia.html', data=rows)
    return render_template('membresia.html')
       
# Vista para eliminar usuario
@app.route('/eliminar_usuario', methods=['GET', 'POST'])
def eliminar_usuario():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM miembros')
    data = cur.fetchall()
    mysql.connection.commit()
    return render_template('listado_usuarios.html', miembros=data)

# Vista para cambiar el estado de un usuario
@app.route('/estado_usuario', methods=['GET', 'POST'])
def estado_usuario():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM miembros')
    data = cur.fetchall()
    mysql.connection.commit()
    return render_template('estado_usuario.html', miembros=data)


#accion de cambiar el estado de un miembro
@app.route('/cambiar_estado_miembro', methods=['POST'])
def cambiar_estado_miembro():
    if request.method == 'POST':
        miembro_id=None
        estado_actual=None
        miembro_id = request.form.get('miembro_id')
        # Realiza una consulta para obtener el estado actual del miembro
        cur = mysql.connection.cursor()
        cur.execute("SELECT estado FROM miembros WHERE id = %s", (miembro_id,))
        estado_actual = cur.fetchone()
        print(estado_actual)
        # Cambia el estado (por ejemplo, de True a False o viceversa)
        nuevo_estado = not estado_actual[0]
        # Realiza la actualización en la base de datos
        cur.execute("UPDATE miembros SET estado = %s WHERE id = %s", (nuevo_estado, miembro_id))
        mysql.connection.commit()
        cur.close()
        flash('Estado actualizado correctamente')
    return redirect(url_for('estado_usuario') ) # Renderiza la plantilla con los datos actualizados


# Vista para editar usuario
@app.route('/editar_miembro', methods=['GET', 'POST'])
def editar_miembro():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM miembros')
    data = cur.fetchall()
    mysql.connection.commit()

    return render_template('editar_miembro.html', miembros=data)

# accion de buscar usuario
@app.route("/edit/<string:id>")
def buscarid(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM miembros WHERE id = %s', (id,))
    data = cur.fetchall()
   # mysql.connection.commit()
   # flash ('miembro editado correctamente')
    return render_template('vista_editar.html', miembro=data[0])


# accion de editar usuario
@app.route("/update/<id>", methods=['POST'])
def getid(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        correo = request.form['correo']
        telefono = request.form['telefono']
        contraseña = request.form['contraseña']

    cur = mysql.connection.cursor()
    cur.execute('UPDATE miembros SET nombre = %s, apellido = %s, edad = %s, correo = %s, telefono = %s, contraseña = %s WHERE id = %s',
                (nombre, apellido, edad, correo, telefono, contraseña, id))
    mysql.connection.commit()
    flash('miembro editado correctamente')
    return redirect(url_for('editar_miembro'))


# Vista para agregar usuario
@app.route('/admin/agregar_usuario', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        correo = request.form['correo']
        telefono = request.form['telefono']
        contraseña = request.form['contraseña']

        # Agregar el usuario a la base de datos
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO miembros (nombre, apellido, edad, correo, telefono, contraseña) VALUES (%s, %s, %s, %s, %s, %s)',
                    (nombre, apellido, edad, correo, telefono, contraseña))
        mysql.connection.commit()
        flash('Usuario agregado correctamente')

        # Redirigir a la página de administración o mostrar un mensaje de éxito
        # return redirect(url_for('administrador'))

    return render_template('agregar_usuario.html')


# Vista buscar miembro
@app.route('/buscar_miembro', methods=['GET', 'POST'])
def buscar_miembro():
    data = None
    if request.method == 'POST':
        # Obtén el término de búsqueda del formulario
        nombre = request.form.get('nombre')
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM miembros WHERE LOWER(nombre) = %s", (nombre,))
        data = cur.fetchall()
        cur.close()
        if data:
            flash('Miembro encontrado.')
            return render_template('buscar_miembro.html', resultados=data)
        else:
            flash('No se encontraron miembros con ese nombre.')
    return render_template('buscar_miembro.html')


# Vista para agregar máquina
@app.route('/agregar_maquina', methods=['GET', 'POST'])
def agregar_maquina():
    if request.method == 'POST':
        # Obtener los datos del formulario
        registro = request.form['registro']
        nombre = request.form['nombre']
        estado = request.form['estado']
        proveedor = request.form['proveedor']
        precio = request.form['precio']
        fechaCompra = request.form['fechaCompra']
        disponibilidad = request.form['disponibilidad']

        # Agregar el usuario a la base de datos
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO historial_maquinaria (IdRegistro, Fecha_Compra, Precio, Proveedor) VALUES (%s, %s, %s,%s)',
                    (registro, fechaCompra, precio, proveedor))
        cur.execute('INSERT INTO maquinas (IdRegistro, nombre, estado, disponibilidad) VALUES (%s, %s, %s,%s)',
                    (registro, nombre, estado, disponibilidad))
        mysql.connection.commit()
        flash('Máquina agregada correctamente')

    return render_template('agregar_maquina.html')


# Vista mirar el listado de maquinas
@app.route('/lista_maquinas', methods=['GET', 'POST'])
def lista_maquinas():
    data = None
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM maquinas')
    data = cur.fetchall()
    mysql.connection.commit()
    return render_template('lista_maquinas.html', miembros=data)

# Vista del estado de máquinas
@app.route('/estado_maquinas', methods=['GET', 'POST'])
def estado_maquinas():
    data = None
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM maquinas')
    data = cur.fetchall()
    mysql.connection.commit()
    return render_template('estado_maquinas.html', maquinas=data)

# accion de editar estado de máquina
@app.route('/cambiar_estado_maquina', methods=['POST'])
def cambiar_estado():
    if request.method == 'POST':
        maquina_id = None
        maquina_id = request.form.get('maquina_id')
        print("maquina_id:", maquina_id)
        # Realiza una consulta para obtener el estado actual del atributo booleano
        cur = mysql.connection.cursor()
        cur.execute("SELECT estado FROM maquinas WHERE IdMaquina = %s", (maquina_id,))
        estado_actual = cur.fetchone()
        print(estado_actual)
        # Cambia el estado (por ejemplo, de True a False o viceversa)
        nuevo_estado = not estado_actual[0]

        # Realiza la actualización en la base de datos
        cur.execute("UPDATE maquinas SET estado = %s, disponibilidad = %s WHERE IdMaquina = %s", (nuevo_estado, nuevo_estado, maquina_id))
        mysql.connection.commit()

        cur.close()
        flash('Estado actualizado correctamente')
        return redirect(url_for('estado_maquinas'))  # Renderiza la plantilla con los datos actualizados

# Traer el historial de la máquina
@app.route("/historial/<id>")
def gethistorial(id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM historial_maquinaria WHERE IdRegistro =%s", (id,))
        data = cur.fetchall()
        cur.close()
        flash('Historial de máquina encontrado correctamente')
        return render_template('vista_historial_maquina.html', resultados=data) # Renderiza la plantilla con los datos actualizados


#vista de buscar maquina
@app.route('/buscar_maquina', methods=['GET', 'POST'])
def buscar_maquina():
    data = None
    if request.method == 'POST':
        # Obtén el término de búsqueda del formulario
        nombre = request.form.get('nombre')
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM maquinas WHERE LOWER(nombre) = %s", (nombre,))
        data = cur.fetchall()
        cur.close()
        if data:
            flash('Máquina encontrado.')
            return render_template('buscar_maquina.html', resultados=data)
        else:
            flash('No se encontraron máquinas con ese nombre.')
    return render_template('buscar_maquina.html')


# Vista mantenimiento de maquinas
@app.route('/mantenimiento_maquinas', methods=['GET', 'POST'])
def mantenimiento_maquinas():
    data = None
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM maquinas WHERE estado = 0')
    data = cur.fetchall()
    mysql.connection.commit()
    return render_template('mantenimiento_maquinas.html', miembros=data)

# Traer el historial de la máquina
@app.route("/mantenimiento/<maquina_id>")
def getmantenimiento(maquina_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM maquinas WHERE IdMaquina = %s", (maquina_id,))
    maquina = cur.fetchone()
    cur.close()

    if request.method == 'POST':
        # Aquí puedes capturar los datos de fecha y hora seleccionados por el usuario
        fecha = request.form.get('fecha')
        hora = request.form.get('hora')
        # Luego, puedes guardar esta información en tu base de datos o realizar otras acciones necesarias.

        flash(f'Cita agendada para {fecha} a las {hora}')
    return render_template('vista_mantenimiento.html', maquina=maquina) # Renderiza la plantilla con los datos actualizados



if __name__ == '__main__':
    app.run(debug=True)

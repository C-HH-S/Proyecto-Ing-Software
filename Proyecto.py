from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from datetime import datetime
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash, send_file
import mysql.connector


app = Flask(__name__, static_folder='static', template_folder='template')
bcrypt = Bcrypt(app)


# Configura la conexión a la base de datos MySQL
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "gim_candelaria"
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

@app.route('/gestion_membresias')
def gestion_membresias():
     return render_template('gestion_membresias.html')
 
@app.route('/gestion_instructores')
def gestion_instructores():
     return render_template('gestion_instructores.html')
 
@app.route('/perfil_instructor')
def perfil_instructor():
     return render_template('perfil_instructor.html')
 
@app.route('/editar_info_personal_ins', methods=['GET', 'POST'])
def editar_info_personal_ins():
    return render_template('editar_info_personal_ins.html')



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




#estado membresia administrador
@app.route('/estado_membresia')
def estado_membresia():
        #cur = mysql.connection.cursor()
        #cur.execute("SELECT * FROM clientes")  
        #rows = cur.fetchall()
        #cur.close()
        #return render_template('membresia.html', data=rows)
    return render_template('estado_membresia.html')

#listado membresia administrador
@app.route('/listado_membresia')
def listado_membresia():
        #cur = mysql.connection.cursor()
        #cur.execute("SELECT * FROM clientes")  
        #rows = cur.fetchall()
        #cur.close()
        #return render_template('membresia.html', data=rows)
    return render_template('listado_membresia.html')

#editar membresia administrador
@app.route('/editar_membresia')
def editar_membresia():
        #cur = mysql.connection.cursor()
        #cur.execute("SELECT * FROM clientes")  
        #rows = cur.fetchall()
        #cur.close()
        #return render_template('membresia.html', data=rows)
    return render_template('editar_membresia.html')

#vista editar membresia
@app.route('/vista_editar_membresia')
def vista_editar_membresia():
        #cur = mysql.connection.cursor()
        #cur.execute("SELECT * FROM clientes")  
        #rows = cur.fetchall()
        #cur.close()
        #return render_template('membresia.html', data=rows)
    return render_template('vista_editar_membresia.html')

#vista principal de asignar membresia
@app.route('/asignar_membresia')
def asignar_membresia():
        #cur = mysql.connection.cursor()
        #cur.execute("SELECT * FROM clientes")  
        #rows = cur.fetchall()
        #cur.close()
        #return render_template('membresia.html', data=rows)
    return render_template('asignar_membresia.html')

#vista secundaria de asignar membresia
@app.route('/vista_asignar_membresia')
def vista_asignar_membresia():
        #cur = mysql.connection.cursor()
        #cur.execute("SELECT * FROM clientes")  
        #rows = cur.fetchall()
        #cur.close()
        #return render_template('membresia.html', data=rows)
    return render_template('vista_asignar_membresia.html')

#vista estdo de membresia desde miembro
@app.route('/miembro_estado_membresia')
def miembro_estado_membresia():
        #cur = mysql.connection.cursor()
        #cur.execute("SELECT * FROM clientes")  
        #rows = cur.fetchall()
        #cur.close()
        #return render_template('membresia.html', data=rows)
    return render_template('miembro_estado_membresia.html')

#vista de reservas desde miembro
@app.route('/reservas_miembro')
def reservas_miembro():
        #cur = mysql.connection.cursor()
        #cur.execute("SELECT * FROM clientes")  
        #rows = cur.fetchall()
        #cur.close()
        #return render_template('membresia.html', data=rows)
    return render_template('reservas_miembro.html')

#reservar clase desde miembro
@app.route('/reservar_clase')
def reservar_clase():
        #cur = mysql.connection.cursor()
        #cur.execute("SELECT * FROM clientes")  
        #rows = cur.fetchall()
        #cur.close()
        #return render_template('membresia.html', data=rows)
    return render_template('reservar_clase.html')

#reservar maquina desde miembro
@app.route('/reservar_maquina')
def reservar_maquina():
        #cur = mysql.connection.cursor()
        #cur.execute("SELECT * FROM clientes")  
        #rows = cur.fetchall()
        #cur.close()
        #return render_template('membresia.html', data=rows)
    return render_template('reservar_maquina.html')

#plan de trabajo de miembro
@app.route('/plan_de_trabajo_miembro')
def plan_de_trabajo_miembro():
        #cur = mysql.connection.cursor()
        #cur.execute("SELECT * FROM clientes")  
        #rows = cur.fetchall()
        #cur.close()
        #return render_template('membresia.html', data=rows)
    return render_template('plan_de_trabajo_miembro.html')
       
# Vista para eliminar usuario
@app.route('/listado_usuarios', methods=['GET', 'POST'])
def listado_usuarios():
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
        estado = request.form['estado']

        # Agregar el usuario a la base de datos
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO miembros (nombre, apellido, edad, correo, telefono, contraseña, estado) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                    (nombre, apellido, edad, correo, telefono, contraseña, estado))
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
        cur.execute('INSERT INTO maquina (IdRegistro, nombre, estado, disponibilidad) VALUES (%s, %s, %s,%s)',
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

# Vista listado instructores administrador
@app.route('/listado_instructores', methods=['GET', 'POST'])
def listado_instructores():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM empleado WHERE ID_SALARIO_EMPLE = '2'")
    data = cur.fetchall()
    mysql.connection.commit()
    
    return render_template('listado_instructores.html', empleado=data)

# Agregar instructor
@app.route('/agregar_instructor', methods=['GET', 'POST'])
def agregar_instructor():
    if request.method == 'POST':
        print(request.form)
        # Obtener los datos del formulario
        id_salario_emple = 2
        estado = 1
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        genero = request.form['genero']
        edad = request.form['edad']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        horario = request.form.get('horario')

        # Obtener las especialidades y unirlas como una cadena
        especialidad = ', '.join(request.form.getlist('especialidad'))
        
        #Hashear contraseña
        contrasena_hash = bcrypt.generate_password_hash('contrasena').decode('utf8')
        
        # Validar contraseña
        # is_valid = bcrypt.check_password_hash(contraseña_hash, contrasena)

        # Agregar el usuario a la base de datos utilizando parámetros
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO empleado (IDENTIFICACION_EMPLEADO, NOMBRE, APELLIDO, CONTRASENA, EDAD, CORREO, GENERO, ID_SALARIO_EMPLE, ESPECIALIDAD, HORARIO, ESTADO) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (cedula, nombre, apellido, contrasena_hash, edad, correo, genero, id_salario_emple, especialidad, horario, estado))
        
        mysql.connection.commit()
        flash('Instructor agregado correctamente')

    return render_template('agregar_instructor.html')

# Vista editar instructor
@app.route('/editar_instructor', methods=['GET', 'POST'])
def editar_instructor():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM empleado WHERE ID_SALARIO_EMPLE = "2"')
    data = cur.fetchall()
    mysql.connection.commit()

    return render_template('editar_instructor.html', empleado=data)

# Accion editar instructor
@app.route('/vista_editar_instructor/<cedula>', methods=['GET', 'POST'])
def vista_editar_instructor(cedula):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM empleado WHERE IDENTIFICACION_EMPLEADO = %s', (cedula,))
    instructor = cur.fetchone()
    mysql.connection.commit()

    if instructor:
        if request.method == 'POST':
            # Lógica para actualizar los detalles del instructor en la base de datos
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            edad = request.form['edad']
            correo = request.form['correo']
            horario = request.form.get('horario')
            especialidad = ', '.join(request.form.getlist('especialidad'))

            # Lista de tuplas
            campos_actualizar = []

            # Verificar y agregar campos al actualizar
            if nombre:
                campos_actualizar.append(('nombre', nombre))
            if apellido:
                campos_actualizar.append(('apellido', apellido))
            if edad:
                campos_actualizar.append(('edad', edad))
            if correo:
                campos_actualizar.append(('correo', correo))
            if horario:
                campos_actualizar.append(('horario', horario))
            if especialidad:
                campos_actualizar.append(('especialidad', especialidad))

            # Verifica si hay campos para actualizar
            if campos_actualizar:

                consulta = 'UPDATE empleado SET ' + ', '.join([f'{campo} = %s' for campo, valor in campos_actualizar]) + f' WHERE IDENTIFICACION_EMPLEADO = %s' 
                
                # Valores que se actualizarán
                valores_actualizar = [valor for campo, valor in campos_actualizar] + [cedula]

                cur.execute(consulta, valores_actualizar)
                mysql.connection.commit()

                flash('Instructor editado correctamente')
                return redirect(url_for('editar_instructor'))
            else:
                flash('Edición sin cambios')

        return render_template('vista_editar_instructor.html')

# Buscar instructor
@app.route('/buscar_instructor', methods=['GET', 'POST'])
def buscar_instructor():
    data = None
    if request.method == 'POST':
        # Obtén el término de búsqueda del formulario
        cedula = request.form.get('cedula')
        id_salario_emple = 2
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM empleado WHERE IDENTIFICACION_EMPLEADO = %s AND ID_SALARIO_EMPLE = %s", (cedula,id_salario_emple))
        data = cur.fetchall()
        cur.close()
        if data:
            flash('Instructor encontrado.')
            return render_template('buscar_instructor.html', resultados=data)
        else:
            flash('No se encontraron instructores con esa identificación.')
    return render_template('buscar_instructor.html')

# Vista estado instructor
@app.route('/estado_instructor', methods=['GET', 'POST'])
def estado_instructor():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM empleado WHERE ID_SALARIO_EMPLE = 2')
    data = cur.fetchall()
    mysql.connection.commit()
    return render_template('estado_instructor.html', empleado=data)


# Acción cambiar estado instructor
@app.route('/cambiar_estado_instructor', methods=['POST'])
def cambiar_estado_instructor():
    if request.method == 'POST':
        cedula = request.form.get('cedula')
        
        # Realiza una consulta para obtener el estado actual del instructor
        cur = mysql.connection.cursor()
        cur.execute("SELECT estado FROM empleado WHERE IDENTIFICACION_EMPLEADO = %s", (cedula,))
        estado_actual = cur.fetchone() 
        # Cambia el estado (por ejemplo, de True a False o viceversa)
        nuevo_estado = not estado_actual[0]
        # Realiza la actualización en la base de datos
        cur.execute("UPDATE empleado SET estado = %s WHERE IDENTIFICACION_EMPLEADO = %s", (nuevo_estado, cedula))
        mysql.connection.commit()
        cur.close()
        flash('Estado actualizado correctamente')
    return redirect(url_for('estado_instructor') )

# Nomina Instructores
@app.route('/gestion_nomina', methods=['GET', 'POST'])
def gestion_nomina():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM empleado WHERE ID_SALARIO_EMPLE = "2"')
    data = cur.fetchall()
    mysql.connection.commit()

    return render_template('gestion_nomina.html', empleado=data)

def generar_pdf(cedula, nombre, apellido):
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    id_salario_emple = 2
    
    cur = mysql.connection.cursor()
    cur.execute('SELECT SALARIO FROM salario_empleado WHERE ID_SALARIO_EMPLE = %s', (id_salario_emple,))
    data = cur.fetchone()

    salario_base = data[0]
    mysql.connection.commit()
    aporte_salud = 4 * salario_base / 100
    aporte_pension = 4 * salario_base / 100
    aux_transporte = 140606
    total_devengos = aux_transporte + salario_base
    total_deducciones = aporte_salud + aporte_pension
    total_liquido = total_devengos - total_deducciones
   
    
    # Crear el nombre del archivo con la fecha actual
    nombre_archivo = f"recibo_nomina_{fecha_actual}.pdf"
    
    # Crear un documento PDF con un título específico
    doc = SimpleDocTemplate(nombre_archivo, pagesize=letter, title="Recibo de Nómina")

    # Crear datos para la tabla basados en la estructura proporcionada
    datos = [
        ["EMPRESA", "", ""],
        ["Nombre de la Empresa:", "Gimnasio La Candelaria", ""],
        ["Dirección:", "Cl. 68 Sur # 47 - 10, Cdad. Bolívar, Bogotá", ""],
        ["", "", ""],
        ["TRABAJADOR/A", "", ""],
        ["Nombre del Instructor:", f"{nombre} {apellido}", ""],
        ["Identificación:", cedula, ""],
        ["", "", ""], 
        ["Devengos", "Cantidad", "Precio ($)", "Total ($)"],
        ["Salario base", "30 días", 48910, int(salario_base)],
        ["Auxilio de transporte", "", int(aux_transporte), int(aux_transporte)],
        ["", "", "Total", int(total_devengos)],
        ["Deducciones", "Cantidad", "Precio ($)", "Total ($)"],
        ["Aporte a la salud", "", "4%", int(aporte_salud)],
        ["Aporte a la pensión", "", "4%", int(aporte_pension)],
        ["", "", "Total", int(total_deducciones)],
        ["", "", ""],
        ["Liquido a percibir", int(total_liquido), ""],
        ["Fecha generación de nomina", fecha_actual, "", ""],
    ]

    # Crear la tabla y darle estilo con bordes
    tabla = Table(datos, colWidths=(200, 100, 100, 100))
    estilo_tabla = TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (3, 0), colors.Color(0.8, 0.8, 0.8)),
        ('BACKGROUND', (0, 4), (3, 4), colors.Color(0.8, 0.8, 0.8)),
        ('BACKGROUND', (0, 8), (3, 8), colors.Color(1.0, 1.0, 0.6)),
        ('BACKGROUND', (0, 12), (3, 12), colors.Color(1.0, 1.0, 0.6)),
        ('BACKGROUND', (1, 17), (3, 17), colors.Color(0.8, 0.8, 1.0))
    ])
    
    # Ajustar la combinación de filas
    estilo_tabla.add('SPAN', (0, 0), (3, 0))  # Combinar la primera fila
    # Ajustar la alineación de la primera fila
    estilo_tabla.add('ALIGN', (0, 0), (3, 0), 'CENTER')
    estilo_tabla.add('SPAN', (0, 4), (3, 4))
    estilo_tabla.add('ALIGN', (0, 4), (3, 4), 'CENTER')
    estilo_tabla.add('SPAN', (1, 1), (3, 1))
    estilo_tabla.add('SPAN', (1, 2), (3, 2))
    estilo_tabla.add('SPAN', (1, 5), (3, 5))
    estilo_tabla.add('SPAN', (1, 6), (3, 6))
    estilo_tabla.add('SPAN', (0, 3), (3, 3))
    estilo_tabla.add('SPAN', (0, 7), (3, 7))
    estilo_tabla.add('SPAN', (0, 11), (1, 11))
    estilo_tabla.add('SPAN', (0, 15), (1, 15))
    estilo_tabla.add('SPAN', (1, 17), (3, 17))
    estilo_tabla.add('SPAN', (1, 18), (3, 18))

    # Aplicar el estilo a la tabla
    tabla.setStyle(estilo_tabla)

    # Construir la tabla y agregarla al documento
    elementos = []
    elementos.append(tabla)

    # Construir el PDF
    doc.build(elementos)

    return nombre_archivo

@app.route('/descargar_pdf/<cedula>/<nombre>/<apellido>')
def descargar_pdf(cedula, nombre, apellido):
    nombre_archivo = generar_pdf(cedula, nombre, apellido)

    # Configurar las cabeceras HTTP para indicar el nombre del archivo al navegador
    return send_file(nombre_archivo, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=4000)

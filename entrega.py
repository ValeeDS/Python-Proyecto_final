import json

#guardar en base de datos
def guardar_usuario(nombre_archivo = "my_db"):
    with open(nombre_archivo + ".json", 'w') as file:
        json.dump(usuarios, file, indent=4)
    return

#cargar base de datos
def leer_base(nombre_archivo = "my_db"):
    try:
        with open(nombre_archivo + ".json", "r") as file:
            try:
                usuarios = json.load(file)
            except json.decoder.JSONDecodeError:
                usuarios = {}
    except FileNotFoundError:
        usuarios = {}   
    finally:
        return usuarios
    
#mostrar usuarios registrados
def mostrar_usuarios():
    users = []
    for user in usuarios.keys():
        print(user)
        users.append(user)
    return users

#registro
def registro_imprimir(func):
    def wrapper(*args):
        print(f"Se registró: {args[0]}")
    return wrapper

def registrar(usuario, contraseña):
    if not existe_usuario(usuario):
        if validar(usuario) and validar(contraseña):
            usuarios[usuario] = contraseña
            guardar_usuario()
            return {usuario: contraseña}
    return

#inicio de sesión
def bienvenido(func):
    def wrapper(*args):
        print(f"Bienvenido/a {args[0]}")
    return wrapper
        
def iniciar_sesion(usuario, contraseña):
    if existe_usuario(usuario) and usuarios[usuario] == contraseña:
        usuario_log = usuario
        return usuario_log
    return

#busqueda de usuario
def existe_usuario(usuario):
    if usuario in usuarios.keys():
        return True
    else: return False

#validación de longitud
def validar(parte):
    return len(parte) >= 4


#Variables globales

usuarios = leer_base("my_db")

#EJECUCIÓN
registrado = registrar(input("Ingrese nombre de usuario para registrar: "), input("Ingrese contraseña: "))
usuario_log = iniciar_sesion(input("Ingrese nombre de usuario para iniciar sesión: "), input("Ingrese contraseña: "))

mostrar_usuarios()


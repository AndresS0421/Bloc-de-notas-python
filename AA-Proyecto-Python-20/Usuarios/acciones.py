import Usuarios.usuario as modelo
import Notas.acciones as acciones_notas

class Acciones:


    def registro(self):
        print("\nOK, vamos a registrarte en el sistema...")
        nombre = input("¿Cuál es tu nombre? ")
        apellidos = input("¿Cuáles son tus apellidos? ")
        email = input("¿Cuál es tu email? ")
        password = input("Introduce tu constraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print("\nPerfecto {}, te has registrado con el email: {}".format(registro[1].nombre, registro[1].email))

        else:
            print("\nNo te has registrado correctamente.")

    def login(self):
        print("\nVale, identificate en el sistema...")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print("\nBienvenido {}, te has identificado en el sistema el: {}".format(login[1], login[5]))
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto. Inténtalo más tarde.")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)
        accion = input("¿Qué quieres hacer? ")

        hazEl = acciones_notas.Acciones()
        
        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "salir":
            print(f"\nOk {usuario[1]}, ¡hasta pronto!")
            exit()
        
        return accion

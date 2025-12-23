#Proyecto 4: Biblioteca

#Importo los módulos que voy a usar
import os
import colorama
from colorama import *
from tabulate import tabulate
import shutil

#Inicializo el colorama
colorama.init(autoreset=True)

os.system("cls")

#Defino las funciones de alinear pantalla
def centrar_texto_ascii(texto):
    '''Aqui ajusto el texto del menú en el centro'''
    ancho_terminal = shutil.get_terminal_size().columns
    lineas = texto.split("\n")
    return "\n".join(line.center(ancho_terminal, " ") for line in lineas)

def centrar_tabla(tabla, headers):
    '''Aqui ajusto la tabla del menu principal'''
    ancho_terminal = shutil.get_terminal_size().columns
    tabla_str = tabulate(tabla, headers=headers, tablefmt="fancy_grid")
    lineas = tabla_str.split("\n")
    return "\n".join(line.center(ancho_terminal) for line in lineas)


#Diccionario para almacenar libros
libros_registrados = {}


#Libros predeterminados 

libros_registrados = {
    "1": {
        "titulo": "Cien años de soledad",
        "autor": "gabriel garcía márquez",
        "editorial": "Anaya",
        "genero": "realismo mágico",
        "num_pag": 432
    },
    "2": {
        "titulo": "el principito",
        "autor": "antoine de saint-exupéry",
        "editorial": "salamandra",
        "genero": "literatura infantil",
        "num_pag": 96
    },
    "3": {
        "titulo": "1984",
        "autor": "george orwell",
        "editorial": "debolsillo",
        "genero": "ciencia ficción",
        "num_pag": 326
    }
}

usuarios_registrados = {
    "1": {
        "nombre de usuario": "Ana García",
        "ciudad": "Madrid"
    },
    "2": {
        "nombre de usuario": "Carlos Martínez",
        "ciudad": "Barcelona"
    },
    "3": {
        "nombre de usuario": "Laura Fernández",
        "ciudad": "Valencia"
    }
}

#CLASES ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Establezco una clase con los menus que voy a utilizar.

#MENUS -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Menus:
    def submenu_libros_general(self):
        ascii_libros = (Fore.LIGHTCYAN_EX + ''' 
                                    
                                            ▓█████████ 
                            ▓████████████████░░░░░░░█ 
                    ███████ ▓█░░░░░░██░░░░░░█░░░░░░░█ 
                    ▓█░░░░░████████████░░░░░░█████████ 
                    ██████░░░███░░░░░░██░░░░░░█████████ 
                    ██░░░░░██████░░░░░░██░░░░░░█░░░░░░░█ 
                ██░░░░░░░██ ██░░░░░░██░░░░░░█░░░░░░░█ 
                ██░░░░░░░██  ▓█░░░░░░██░░░░░░█░░░░░░░█ 
                ██░░░░░░░██   ▓█░░░░░░██░░░░░░█░░░░░░░█ 
                ██▒░░░░░░██▓   ▓█░░░░░░██░░░░░░█░░░░░░░█ 
            ██░░░░░░░██     ▓█░░░░░░██░░░░░░█░░░░░░░█ 
            ██░░░░░░░██      ▓█░░░░░░██░░░░░░█░░░░░░░█ 
            ███░░░░░░██▓      ▓█░░░░░░█████████░░░░░░░█ 
            ██▒░░░░░░███       ▓█░░░░░░██░░░░░░█░░░░░░░█ 
        ▓█░░░░░░░██▓        ▓█░░░░░░██▓██████░░░░░░░█ 
        █████░░░░███         ▓█░░░░░░██░░░░░░█░░░░░░░█ 
        ▓█░░░░░█████          ▓█░░░░░░██░░░░░░█████████ 
        ▓█░░░░░░░█▓           ▓█████████░░░░░░██░▓▓▓░██ 
        ████░░██            ▓█░░░░░░██░░░░░░█▓░░░░░██ 
            ███             ▓███████████████████████▓ 

                                    
                        ''') 
        print(Fore.CYAN + centrar_texto_ascii(ascii_libros) + Style.RESET_ALL)
        submenu_libros =    [[1, "Registrar libro"], [2, "Eliminar libro"], [3, "Mostrar libros"], [4, "Buscar libro"], [5, "Volver al menú"]]   
        print(centrar_tabla(submenu_libros, ["Opción", "Descripción"]))
        opcion_libros = input("\t\t\t\t\t\t\t\t¿Qué opción va a seleccionar?: ")
        return opcion_libros
    
    
    def submenu_usuarios_general(self):
        ascii_usuarios = (Fore.LIGHTCYAN_EX + ''' 
    
  ██████████████████████████████████████████████████████████████████████████  
 ██                                                                        ██ 
 ██         ██       █   ██████   █████      ██    █████   ██   ██         ██ 
 ██         ██       █   █    ██  ██  ██    ███    ██  ██   ██ ██          ██ 
 ██         ██       █   ██████   █████    ██ ██   ██████    ███           ██ 
 ██         ██       █   ██  ███  ████    ███████  ████      ██            ██ 
 ██         ██       █   ██  ██   ██ ██   ██   ██  ██ ██    ██             ██ 
 ██          █████   █   █████    █   █   █     █   █  █    █              ██ 
 ██                                                                        ██ 
   ████████████████████████████████████████████████████████████████████████   
       ██         ██             ██        ██             ██         ██       
       ██        ██              ██        ██              ██        ██       
        ██       ██              ███      ███              ██       ██        
         ██    ███                 ██    ███                ███    ██         
         ██     █                  ██    ██                  █     ██         
         ██     █                  ██    ██                  █     ██         
         ██     █                  ██    ██                  █     ██         
         ██     █                  ██    ██                  █     ██             
         ██     █                  ██    ██                  █     ██         
         ██     █                  ██    ██                  █     ██         
         ██     █                  ██    ██                  █     ██         
         █████████                ██████████                █████████         
        ███████████              ████████████              ███████████        
       ██        ██              ██        ██              ██        ██       
       ██         ██             ██        ██             ██         ██       
 ████████████████████████████████████████████████████████████████████████████ 
██                                                                          ██
██                                                                          ██
██████████████████████████████████████████████████████████████████████████████
                     
                            ''') 
        print(Fore.CYAN + centrar_texto_ascii(ascii_usuarios) + Style.RESET_ALL)
        
        
        submenu_usuarios = [[1, "Registrar usuario"], [2, "Eliminar usuario"], [3, "Mostrar usuarios"], [4, "Buscar usuario"], [5, "Volver al menú"]]
        print(centrar_tabla(submenu_usuarios,["Opción", "Descripción"]))
        
        opcion_usuarios = input("\t\t\t\t\t¿Qué opción va a seleccionar?: ")
        
        return opcion_usuarios
    
    
    def submenu_prestamos_general (self):
            ascii_prestamos = (Fore.LIGHTCYAN_EX + ''' 
                                                               
                                                                                          
          ███████████████                                 ██████████████████████          
          █             █                                                      █          
          █             ███████████████████████████████████      █  ██ ██ ██   █          
          █                                                       █            █          
          █   █████████                    ████                 ██  ██ ██ ██   █          
          █     ██   ██   ██████    █████   ███ ███  ██████    ███  ██ ██ ██   █          
          █     ██████   ███  ███ ███  ███  ██  ██   ██         █      █  █    █          
          █     ██   ███ ███  ███ ███  ███  ██ ██      ████   ███   ██ ██ ██   █          
          █     ██████     ████     ████    ██  ███  █████   ██      █  █  █   █          
          █                                                                    █          
          █                                                                    █          
          ██████████████████████████████████████████████████████████████████████          
                                                                     
                            
                            ''') 
            print(Fore.CYAN + centrar_texto_ascii(ascii_prestamos) + Style.RESET_ALL)

            
            submenu_prestamos = [[1, "Realizar préstamo"], [2, "Devolver libro"], [3, "Mostrar préstamos"], [4, "Volver al menú"]]
            print(centrar_tabla(submenu_prestamos,["Opción", "Descripción"],))
            
            opcion_prestamos = input("\t\t\t\t\t¿Qué opción va a seleccionar?: ")
            
            return opcion_prestamos
    
    
#CLASES DEL PROGRAMA -----------------------------------------------------------------------------------------------------------------------------------------------------------

#LIBRO -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Establezco las clases que voy a usar
class Libro:
    
    #Constructor de la clase
    def __init__(self):
        self.libros = libros_registrados 
    
    def registrar_libro(self):
        '''Esta es una función que pide datos al usuario sobre un libro y los registra en un diccionario'''
        '''Indico el ascii para que se mantenga en todas las variables del codigo'''
        
        ascii_registrarlibro = (Fore.LIGHTCYAN_EX + '''
                        
    ███████████                      ███           █████                                 
   ░░███░░░░░███                    ░░░           ░░███                                  
    ░███    ░███   ██████   ███████ ████   █████  ███████   ████████   ██████   ████████ 
    ░██████████   ███░░███ ███░░███░░███  ███░░  ░░░███░   ░░███░░███ ░░░░░███ ░░███░░███
    ░███░░░░░███ ░███████ ░███ ░███ ░███ ░░█████   ░███     ░███ ░░░   ███████  ░███ ░░░ 
    ░███    ░███ ░███░░░  ░███ ░███ ░███  ░░░░███  ░███ ███ ░███      ███░░███  ░███     
    █████   █████░░██████ ░░███████ █████ ██████   ░░█████  █████    ░░████████ █████    
    ░░░░░   ░░░░░  ░░░░░░   ░░░░░███░░░░░ ░░░░░░     ░░░░░  ░░░░░      ░░░░░░░░ ░░░░░     
                                ░███                                                      
                            ░░██████                                                       
                              ░░░░░░                                                        
    ████   ███  █████                                                                    
   ░░███  ░░░  ░░███                                                                     
    ░███  ████  ░███████  ████████   ██████                                              
    ░███ ░░███  ░███░░███░░███░░███ ███░░███                                             
    ░███  ░███  ░███ ░███ ░███ ░░░ ░███ ░███                                             
    ░███  ░███  ░███ ░███ ░███     ░███ ░███                                             
    █████ █████ ████████  █████    ░░██████                                              
    ░░░░░ ░░░░░ ░░░░░░░░  ░░░░░      ░░░░░░                                                    
                        
                        
                      ''')

        #Pido los datos al usuario
        while True:
            print(ascii_registrarlibro)
            id_libro = input(Fore.CYAN + "ID del libro: " + Style.RESET_ALL)
            
            if not id_libro.isdigit():
                print(Fore.RED + "Formato incorrecto. El ID debe ser numérico." + Style.RESET_ALL)
                input("Presiona Enter para intentarlo de nuevo...")
                os.system("cls")
                
                
            elif id_libro in self.libros:
                print(Fore.RED + "Libro ya registrado con este ID. Inténtalo de nuevo." + Style.RESET_ALL)
                input("Presiona Enter para intentarlo de nuevo...")
                os.system("cls")
            else:   
                break

        #Pido título
        while True:
            os.system("cls")
            print(ascii_registrarlibro)
            titulo = input(Fore.CYAN + "Título: " + Style.RESET_ALL).lower()
            if not titulo:
                print(Fore.RED + "Error: El titulo no puede estar vacío" + Style.RESET_ALL)
                input("Presione Enter para continuar...")
                os.system("cls")
                continue
            if titulo.isdigit():
                print("Formato incorrecto")
                input("Por favor, inténtelo de nuevo")
                os.system("cls")
            else: 
                break

        #Pido autor
        while True:
            os.system("cls")
            print(ascii_registrarlibro)
            autor = input(Fore.CYAN + "Autor: " + Style.RESET_ALL)
            if not autor:
                print(Fore.RED + "Error: El autor no puede estar vacío" + Style.RESET_ALL)
                input("Presione Enter para continuar...")
                os.system("cls")
                continue
            if autor.isdigit():
                print("Formato incorrecto")
                input("Por favor, inténtelo de nuevo")
                os.system("cls")
            else:
                break

        #Pido editorial
        while True:
            os.system("cls")
            print(ascii_registrarlibro)
            editorial = input(Fore.CYAN + "Editorial: " + Style.RESET_ALL)
            if not editorial:
                print(Fore.RED + "Error: La editorial no puede estar vacía" + Style.RESET_ALL)
                input("Presione Enter para continuar...")
                os.system("cls")
                continue
            if editorial.isdigit():
                print("Formato incorrecto")
                input("Por favor, inténtelo de nuevo")
                os.system("cls")
            else: 
                break

        #Pido género
        while True:
            os.system("cls")
            print(ascii_registrarlibro)
            genero = input(Fore.CYAN + "Género: " + Style.RESET_ALL)
            if not genero:
                print(Fore.RED + "Error: El genero no puede estar vacío" + Style.RESET_ALL)
                input("Presione Enter para continuar...")
                os.system("cls")
                continue
            if genero.isdigit():
                print("Formato incorrecto")
                input("Por favor, inténtelo de nuevo")
                os.system("cls")
            else:
                break

        #Pido número de páginas
        while True:
            os.system("cls")
            print(ascii_registrarlibro)
            num_pag = input(Fore.CYAN + "Número de páginas: " + Style.RESET_ALL)
            if not num_pag.isdigit():
                print("Formato incorrecto")
                input("Por favor, inténtelo de nuevo")
                os.system("cls")
            else:
                break

        #Guardo los datos en el diccionario
        self.libros[id_libro] = {
            "titulo": titulo,
            "autor": autor,
            "editorial": editorial,
            "genero": genero,
            "num_pag": int(num_pag)
        }
        print(Fore.CYAN + f"\nLibro '{self.libros[id_libro]['titulo']}' registrado con éxito" + Style.RESET_ALL)
        input("Redirigiendo al menú... ")
        os.system("cls")
        
        
        
    
    def eliminar_libro(self,libro_eliminar):

        os.system("cls")
        print(Fore.LIGHTRED_EX + '''  
            ██████████ ████   ███                   ███                                
           ░░███░░░░░█░░███  ░░░                   ░░░                                 
            ░███  █ ░  ░███  ████  █████████████   ████  ████████    ██████   ████████ 
            ░██████    ░███ ░░███ ░░███░░███░░███ ░░███ ░░███░░███  ░░░░░███ ░░███░░███
            ░███░░█    ░███  ░███  ░███ ░███ ░███  ░███  ░███ ░███   ███████  ░███ ░░░ 
            ░███ ░   █ ░███  ░███  ░███ ░███ ░███  ░███  ░███ ░███  ███░░███  ░███     
            ██████████ █████ █████ █████░███ █████ █████ ████ █████░░████████ █████    
            ░░░░░░░░░░ ░░░░░ ░░░░░ ░░░░░ ░░░ ░░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░░░░ ░░░░░                                                                    
        ''')
        
        if not self.libros:
            print("Aún no hay libros registrados.")
            input("Pulse ENTER para volver al menú")
            os.system("cls")
            return

        if not libro_eliminar.isdigit():
            print("Error: Debes ingresar un ID válido (número).")
            input("\nPor favor, inténtelo de nuevo")
            os.system("cls")
            return

        if libro_eliminar not in self.libros:
            print("El libro que quiere eliminar no se encuentra en la base de datos.") 
            input("\nPor favor, inténtelo de nuevo")
            os.system("cls")
            return
        
        del self.libros[libro_eliminar]
        print("Su libro ha sido eliminado correctamente.")    
        input("Pulse ENTER para continuar")
        os.system("cls")
        
    def mostrar_libro(self):
        
        if not libros_registrados:
            print("Aún no hay libros registrados")
            input("Pulse ENTER para continuar")
            os.system("cls")
        else:
            headers = [Fore.CYAN + h + Style.RESET_ALL for h in ["ID", "Título", "Autor", "Editorial", "Género", "Páginas"]]
            tabla = [
            [Fore.YELLOW + id_libro + Style.RESET_ALL] + [Fore.WHITE + str(v) + Style.RESET_ALL for v in datos.values()]
            for id_libro, datos in self.libros.items()]

            print("\n" + Fore.GREEN + "Libros Registrados:\n" + Style.RESET_ALL)
            print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))
            input("\nPresiona ENTER para continuar...")
            os.system("cls")
        
    def buscar_libro(self, id_libro):
        if not libros_registrados:
            print("Aún no hay libros registrados")
            input("Pulse ENTER para continuar")
            os.system("cls")
            
        else:
            if id_libro not in self.libros:
                print(Fore.RED + "El libro con ID " + id_libro + " no está registrado." + Style.RESET_ALL)
                input("Pulse ENTER para continuar")
                os.system("cls")
            
            else:     
                libro = self.libros[id_libro]
                headers = [Fore.CYAN + "Campo" + Style.RESET_ALL, Fore.CYAN + "Valor" + Style.RESET_ALL]
                tabla = [[Fore.YELLOW + k.capitalize() + Style.RESET_ALL, Fore.WHITE + str(v) + Style.RESET_ALL] for k, v in libro.items()]

                print("\n" + Fore.GREEN + f"Información del libro (ID: {id_libro}):\n" + Style.RESET_ALL)
                print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))
                input("\nPresiona ENTER para continuar...")
                os.system("cls")
        
#USUARIO -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
class Usuario:
    
    def __init__(self, id_usuario="", nombre_usuario="", ciudad=""):
        self.usuario = usuarios_registrados 
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.ciudad = ciudad

   
    def registrar_usuario(self):
        while True:
            self.id_usuario = input(Fore.MAGENTA + "ID del usuario: " + Style.RESET_ALL)
            
            if not self.id_usuario.isdigit():
                print(Fore.RED + "Formato incorrecto. El ID debe ser numérico." + Style.RESET_ALL)
                input("Presione Enter para intentarlo de nuevo...")
                os.system("cls")
                continue
                
            if self.id_usuario in self.usuario: 
                print(Fore.RED + "Usuario ya registrado con este ID. Inténtelo de nuevo." + Style.RESET_ALL)
                input("Presione Enter para intentarlo de nuevo...")
                os.system("cls")
                continue
                
            break


        #Pido el nombre
        while True:
            self.nombre_usuario = input(Fore.MAGENTA + "Nombre de usuario: " + Style.RESET_ALL).strip()
            if not self.nombre_usuario:
                print(Fore.RED + "Error: El nombre no puede estar vacío" + Style.RESET_ALL)
                input("Presione Enter para continuar...")
                os.system("cls")
                continue
                
            if any(c.isdigit() for c in self.nombre_usuario):
                print(Fore.RED + "Error: El nombre no puede contener números" + Style.RESET_ALL)
                input("Presione Enter para continuar...")
                os.system("cls")
                continue
                
            break

        #Pido la ciudad
        while True:
            self.ciudad = input(Fore.MAGENTA + "Ciudad: " + Style.RESET_ALL).strip()
            if not self.ciudad:
                print(Fore.RED + "Error: La ciudad no puede estar vacía" + Style.RESET_ALL)
                input("Presione Enter para continuar...")
                os.system("cls")
                continue
                
            if all(c.isdigit() for c in self.ciudad.replace(" ", "")):
                print(Fore.RED + "Error: La ciudad no puede ser solo números" + Style.RESET_ALL)
                input("Presione Enter para continuar...")
                os.system("cls")
                continue
                
            break


        #Guardo los datos en el diccionario
        self.usuario[self.id_usuario] = {
            "nombre de usuario": self.nombre_usuario,
            "ciudad": self.ciudad}
        
        print(Fore.MAGENTA + f"\nUsuario '{self.nombre_usuario}' registrado con éxito" + Style.RESET_ALL)
        input("Redirigiendo al menú... ")
        os.system("cls")
        
    
    def eliminar_usuario(self, usuario_a_eliminar):
        while True:
            if not self.usuario:
                print("Aún no hay usuarios registrados")
                input("Pulse ENTER para volver al menú")
                os.system("cls")
                break
            
            if usuario_a_eliminar not in self.usuario:
                print("El usuario que quiere eliminar no se encuentra en nuestras Bases de Datos") 
                input("\nPor favor, inténtelo de nuevo")
                os.system("cls")
                break
            elif not usuario_a_eliminar.isdigit():
                print("El formato no es adecuado")
                input("\nPor favor, inténtelo de nuevo")
                os.system("cls")
                
            else:
                
                del self.usuario[usuario_a_eliminar]
                print("El usuario ha sido eliminado correctamente")    
                input("Pulse ENTER para continuar")
                os.system("cls")
                break
    
    def mostrar_usuario(self):
        if not self.usuario:  
            print("Aún no hay usuarios registrados")
            input("Pulse ENTER para continuar")
            os.system("cls")
        else:
            headers = [Fore.CYAN + h + Style.RESET_ALL for h in ["ID", "Nombre", "Ciudad"]]
            
            tabla = []
            for id_usuario, datos in self.usuario.items():
                fila = [
                    Fore.YELLOW + id_usuario + Style.RESET_ALL,
                    Fore.WHITE + datos["nombre de usuario"] + Style.RESET_ALL,
                    Fore.WHITE + datos["ciudad"] + Style.RESET_ALL
                ]
                tabla.append(fila)
            
            print("\n" + Fore.CYAN + "Usuarios Registrados:\n" + Style.RESET_ALL)
            print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))
            input("\nPresiona ENTER para continuar...")
            os.system("cls")
            
            
    def buscar_usuario(self):
        if not self.usuario:
            print("Aún no hay usuarios registrados")
            input("Pulse ENTER para continuar")
            os.system("cls")
            return
        
        while True:
            id_usuario = input("ID del usuario que quiere buscar: ")
            if not id_usuario.isdigit():
                print("Introduzca un valor numérico")
                input("Presione Enter para continuar...")
                os.system("cls")
                continue
            break
        
        if id_usuario not in self.usuario:
            print(Fore.RED + "El usuario con ID " + id_usuario + " no está registrado." + Style.RESET_ALL)
            input("Pulse ENTER para continuar")
            os.system("cls")
            return
        
        usuario = self.usuario[id_usuario]
        headers = [Fore.CYAN + "Campo" + Style.RESET_ALL, Fore.CYAN + "Valor" + Style.RESET_ALL]
        tabla = [
            [Fore.YELLOW + "Nombre", Fore.WHITE + usuario["nombre de usuario"] + Style.RESET_ALL],
            [Fore.YELLOW + "Ciudad", Fore.WHITE + usuario["ciudad"] + Style.RESET_ALL]
        ]

        print("\n" + Fore.GREEN + f"Información del usuario (ID: {id_usuario}):\n" + Style.RESET_ALL)
        print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))
        input("\nPresiona ENTER para continuar...")
        os.system("cls")
    
#PRESTAMO  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Prestamo(Libro):
    
    def __init__(self):
        super().__init__()
        self.prestados = {}
        
    def prestamo(self):
        if not self.libros:
            print("Aún no hay libros registrados")
            input("Pulse ENTER para continuar")
            os.system("cls")
            return

        #Mostrar libros disponibles
        print(Fore.GREEN + "\nLibros disponibles para préstamo:\n" + Style.RESET_ALL)
        headers = ["ID", "Título", "Autor"]
        tabla = [[id_libro, datos['titulo'], datos['autor']] 
                for id_libro, datos in self.libros.items()]
        print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))
        
        #Pedir ID del libro
        while True:
            id_libro = input("\nIntroduzca el ID del libro a prestar: ")
            if id_libro not in self.libros:
                print(Fore.RED + "Error: El libro no existe" + Style.RESET_ALL)
                if input("¿Desea intentar de nuevo? (s/n): ").lower() != 's':
                    os.system("cls")
                    return
                continue
            break

        #Mostrar usuarios registrados
        usuario_bib = Usuario() 
        if not usuario_bib.usuario:
            print(Fore.RED + "\nNo hay usuarios registrados" + Style.RESET_ALL)
            input("Debe registrar usuarios primero. Pulse ENTER para continuar")
            os.system("cls")
            return
        
        print(Fore.GREEN + "\nUsuarios registrados:\n" + Style.RESET_ALL)
        headers = ["ID", "Nombre"]
        tabla = [[id_user, datos['nombre de usuario']] 
                for id_user, datos in usuario_bib.usuario.items()]
        print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))

        # Pedir ID del usuario
        while True:
            id_usuario = input("\nIntroduzca el ID del usuario: ")
            if id_usuario not in usuario_bib.usuario:
                print(Fore.RED + "Error: El usuario no existe" + Style.RESET_ALL)
                if input("¿Desea intentar de nuevo? (s/n): ").lower() != 's':
                    os.system("cls")
                    return
                continue
            break

        #Realizo el préstamo
        libro = self.libros.pop(id_libro)
        self.prestados[id_libro] = libro
        self.prestados[id_libro]["usuario"] = usuario_bib.usuario[id_usuario]["nombre de usuario"]
        self.prestados[id_libro]["id_usuario"] = id_usuario 
        
        print(Fore.GREEN + f"\nPréstamo realizado con éxito:")
        print(f"Libro: {libro['titulo']}")
        print(f"Usuario: {usuario_bib.usuario[id_usuario]['nombre de usuario']}" + Style.RESET_ALL)
        input("\nPulse ENTER para continuar")
        os.system("cls")
            
    def devolucion(self):
        if not self.prestados:
            print("No hay libros en préstamo actualmente.")
            input("Pulse ENTER para continuar")
            os.system("cls")
            return
        
        id_libro = input("Introduzca el ID del libro a devolver: ")
        if id_libro not in self.prestados:
            print("El libro no está registrado como prestado.")
            input("Pulse ENTER para continuar")
            os.system("cls")
            return
        
        self.libros[id_libro] = self.prestados.pop(id_libro)
        self.libros[id_libro].pop("usuario")
        print(f"El libro '{self.libros[id_libro]['titulo']}' ha sido devuelto correctamente.")
        input("Pulse ENTER para continuar")
        os.system("cls")
    
    def mostrar_prestamos(self):
        if not self.prestados:
            print("No hay libros en préstamo actualmente.")
            input("Pulse ENTER para continuar")
            os.system("cls")
            return
        
        headers = ["ID", "Título", "Autor", "Editorial", "Usuario"]
        tabla = [[id_libro, datos['titulo'], datos['autor'], datos['editorial'], datos['usuario']] for id_libro, datos in self.prestados.items()]
        
        print("\nLibros en Préstamo:\n")
        print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))
        input("\nPresiona ENTER para continuar...")
        os.system("cls")
    
        
#MENU --------------------------------------------------------------------------------------------------


def menu():
    libro_usuario = Libro()
    usuario_biblioteca = Usuario(id_usuario="", nombre_usuario="", ciudad="")
    libro_prestado = Prestamo()

    while True:
        os.system("cls")
        ascii_menu = (Fore.GREEN + '''
            
    ███████████   ███  █████     ████   ███            █████                               
   ░░███░░░░░███ ░░░  ░░███     ░░███  ░░░            ░░███                                
    ░███    ░███ ████  ░███████  ░███  ████   ██████  ███████    ██████   ██████   ██████  
    ░██████████ ░░███  ░███░░███ ░███ ░░███  ███░░███░░░███░    ███░░███ ███░░███ ░░░░░███ 
    ░███░░░░░███ ░███  ░███ ░███ ░███  ░███ ░███ ░███  ░███    ░███████ ░███ ░░░   ███████ 
    ░███    ░███ ░███  ░███ ░███ ░███  ░███ ░███ ░███  ░███ ███░███░░░  ░███  ███ ███░░███ 
    ███████████  █████ ████████  █████ █████░░██████   ░░█████ ░░██████ ░░██████ ░░████████
    ░░░░░░░░░░░  ░░░░░ ░░░░░░░░  ░░░░░ ░░░░░  ░░░░░░     ░░░░░   ░░░░░░   ░░░░░░   ░░░░░░░░ 

                █████         
                ░░███          
              ███████   ██████ 
             ███░░███  ███░░███
            ░███ ░███ ░███████ 
            ░███ ░███ ░███░░░  
            ░░████████░░██████ 
            ░░░░░░░░  ░░░░░░  

      █████████                  █████           ████                       ███           
     ███░░░░░███                ░░███           ░░███                      ░░░            
    ░███    ░███  ████████    ███████   ██████   ░███  █████ ████  ██████  ████   ██████  
    ░███████████ ░░███░░███  ███░░███  ░░░░░███  ░███ ░░███ ░███  ███░░███░░███  ░░░░░███ 
    ░███░░░░░███  ░███ ░███ ░███ ░███   ███████  ░███  ░███ ░███ ░███ ░░░  ░███   ███████ 
    ░███    ░███  ░███ ░███ ░███ ░███  ███░░███  ░███  ░███ ░███ ░███  ███ ░███  ███░░███ 
    █████   █████ ████ █████░░████████░░████████ █████ ░░████████░░██████  █████░░████████
    ░░░░░   ░░░░░ ░░░░ ░░░░░  ░░░░░░░░  ░░░░░░░░ ░░░░░   ░░░░░░░░  ░░░░░░  ░░░░░  ░░░░░░░░ 
            
            ''')

        print(Fore.CYAN + centrar_texto_ascii(ascii_menu) + Style.RESET_ALL)
        
        menu_principal = [  
                          [1,"Libros"], 
                          [2,"Usuarios"], 
                          [3,"Préstamos y Disponibilidad"], 
                          [4,"Salir"]
                          ]
        print(Fore.GREEN + "\t\t\t\t\t\t\t\tMenú Principal:" + Style.RESET_ALL)
        print(centrar_tabla(menu_principal, ["Opción", "Descripción"])) 

        opcion_menu = input("¿Qué opción va a seleccionar?: ")
        os.system("cls")
        
        #LIBROS
        if opcion_menu == "1":
            
            
            menu_libros = Menus()
            
            while True:
                opcion_libros = menu_libros.submenu_libros_general()
            
            
                if opcion_libros == "1":
                    os.system("cls")
                    
                    libro_usuario = Libro()
            
                    libro_usuario.registrar_libro()
                    os.system("cls")
                    
                    
                elif opcion_libros == "2":
                    os.system("cls")
                    print(Fore.LIGHTRED_EX + '''  
            ██████████ ████   ███                   ███                                
           ░░███░░░░░█░░███  ░░░                   ░░░                                 
            ░███  █ ░  ░███  ████  █████████████   ████  ████████    ██████   ████████ 
            ░██████    ░███ ░░███ ░░███░░███░░███ ░░███ ░░███░░███  ░░░░░███ ░░███░░███
            ░███░░█    ░███  ░███  ░███ ░███ ░███  ░███  ░███ ░███   ███████  ░███ ░░░ 
            ░███ ░   █ ░███  ░███  ░███ ░███ ░███  ░███  ░███ ░███  ███░░███  ░███     
            ██████████ █████ █████ █████░███ █████ █████ ████ █████░░████████ █████    
            ░░░░░░░░░░ ░░░░░ ░░░░░ ░░░░░ ░░░ ░░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░░░░ ░░░░░                                                                    
        ''')
                    libro_a_eliminar = input("Introduce el ID del libro a eliminar: ")
                    libro_usuario.eliminar_libro(libro_a_eliminar)
                    os.system("cls")
                    
                elif opcion_libros == "3":
                    os.system("cls")
                    print(Fore.LIGHTMAGENTA_EX + '''
                        
    █████        ███  █████                               
   ░░███        ░░░  ░░███                                
    ░███        ████  ░███████  ████████   ██████   █████ 
    ░███       ░░███  ░███░░███░░███░░███ ███░░███ ███░░  
    ░███        ░███  ░███ ░███ ░███ ░░░ ░███ ░███░░█████ 
    ░███      █ ░███  ░███ ░███ ░███     ░███ ░███ ░░░░███
    ███████████ █████ ████████  █████    ░░██████  ██████ 
    ░░░░░░░░░░░ ░░░░░ ░░░░░░░░  ░░░░░      ░░░░░░  ░░░░░░  
                        
                        ''')
                    
                    libro_usuario.mostrar_libro()
                
                elif opcion_libros == "4":
                    os.system("cls")
                    print(Fore.LIGHTCYAN_EX + '''
    ███████████                                                 
   ░░███░░░░░███                                                
    ░███    ░███ █████ ████  █████   ██████   ██████   ████████ 
    ░██████████ ░░███ ░███  ███░░   ███░░███ ░░░░░███ ░░███░░███
    ░███░░░░░███ ░███ ░███ ░░█████ ░███ ░░░   ███████  ░███ ░░░ 
    ░███    ░███ ░███ ░███  ░░░░███░███  ███ ███░░███  ░███     
    ███████████  ░░████████ ██████ ░░██████ ░░████████ █████    
    ░░░░░░░░░░░    ░░░░░░░░ ░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░░     
                                                                                                    
    ████   ███  █████                                           
   ░░███  ░░░  ░░███                                            
    ░███  ████  ░███████  ████████   ██████   █████             
    ░███ ░░███  ░███░░███░░███░░███ ███░░███ ███░░              
    ░███  ░███  ░███ ░███ ░███ ░░░ ░███ ░███░░█████             
    ░███  ░███  ░███ ░███ ░███     ░███ ░███ ░░░░███            
    █████ █████ ████████  █████    ░░██████  ██████             
    ░░░░░ ░░░░░ ░░░░░░░░  ░░░░░      ░░░░░░  ░░░░░░              
                        ''')
                    
                    id_libro = input("Digame el ID del libro que quiere buscar: ")
                    
                    libro_usuario.buscar_libro(id_libro)
                    os.system("cls")
                    
                elif opcion_libros == "5":
                    os.system("cls")
                    break
                    
                else:
                    input("Por favor, seleccione un número adecuado ")
                    os.system("cls")
            
        elif opcion_menu == "2":
            
            menu_usuario = Menus()
            while True:
                opcion_usuarios = menu_usuario.submenu_usuarios_general()  
                
                if opcion_usuarios == "1":
                    os.system("cls")
                    print(Fore.LIGHTCYAN_EX + '''


    ███████████                      ███           █████                                 
   ░░███░░░░░███                    ░░░           ░░███                                  
    ░███    ░███   ██████   ███████ ████   █████  ███████   ████████   ██████   ████████ 
    ░██████████   ███░░███ ███░░███░░███  ███░░  ░░░███░   ░░███░░███ ░░░░░███ ░░███░░███
    ░███░░░░░███ ░███████ ░███ ░███ ░███ ░░█████   ░███     ░███ ░░░   ███████  ░███ ░░░ 
    ░███    ░███ ░███░░░  ░███ ░███ ░███  ░░░░███  ░███ ███ ░███      ███░░███  ░███     
    █████   █████░░██████ ░░███████ █████ ██████   ░░█████  █████    ░░████████ █████    
    ░░░░░   ░░░░░  ░░░░░░   ░░░░░███░░░░░ ░░░░░░     ░░░░░  ░░░░░      ░░░░░░░░ ░░░░░     
                                 ███                                                      
                            ░░██████                                                       
                              ░░░░░░                                                        
                                                       ███                               
                                                    ░░░                                
    █████ ████  █████  █████ ████  ██████   ████████  ████   ██████                      
   ░░███ ░███  ███░░  ░░███ ░███  ░░░░░███ ░░███░░███░░███  ███░░███                     
    ░███ ░███ ░░█████  ░███ ░███   ███████  ░███ ░░░  ░███ ░███ ░███                     
    ░███ ░███  ░░░░███ ░███ ░███  ███░░███  ░███      ░███ ░███ ░███                     
    ░░████████ ██████  ░░████████░░████████ █████     █████░░██████                      
    ░░░░░░░░ ░░░░░░    ░░░░░░░░  ░░░░░░░░ ░░░░░     ░░░░░  ░░░░░░                       
                    ''')

                    usuario_biblioteca.registrar_usuario()

                elif opcion_usuarios == "2":
                    os.system("cls")
                    print(Fore.LIGHTCYAN_EX + '''

    ██████████ ████   ███                   ███                                
   ░░███░░░░░█░░███  ░░░                   ░░░                                 
    ░███  █ ░  ░███  ████  █████████████   ████  ████████    ██████   ████████ 
    ░██████    ░███ ░░███ ░░███░░███░░███ ░░███ ░░███░░███  ░░░░░███ ░░███░░███
    ░███░░█    ░███  ░███  ░███ ░███ ░███  ░███  ░███ ░███   ███████  ░███ ░░░ 
    ░███ ░   █ ░███  ░███  ░███ ░███ ░███  ░███  ░███ ░███  ███░░███  ░███     
    ██████████ █████ █████ █████░███ █████ █████ ████ █████░░████████ █████    
    ░░░░░░░░░░ ░░░░░ ░░░░░ ░░░░░ ░░░ ░░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░░░░ ░░░░░     
                                                                                
                                                                                
                                                                                
                                                        ███                     
                                                    ░░░                      
    █████ ████  █████  █████ ████  ██████   ████████  ████   ██████            
   ░░███ ░███  ███░░  ░░███ ░███  ░░░░░███ ░░███░░███░░███  ███░░███           
    ░███ ░███ ░░█████  ░███ ░███   ███████  ░███ ░░░  ░███ ░███ ░███           
    ░███ ░███  ░░░░███ ░███ ░███  ███░░███  ░███      ░███ ░███ ░███           
    ░░████████ ██████  ░░████████░░████████ █████     █████░░██████            
    ░░░░░░░░ ░░░░░░    ░░░░░░░░  ░░░░░░░░ ░░░░░     ░░░░░  ░░░░░░             
                    ''')
                    usuario_a_eliminar = input("¿Qué usuario desea eliminar?, indique su ID: ")
                    
                    usuario_biblioteca.eliminar_usuario(usuario_a_eliminar)
                elif opcion_usuarios == "3":
                    os.system("cls")
                    print(Fore.LIGHTCYAN_EX + '''

    █████  █████                                         ███                  
   ░░███  ░░███                                         ░░░                   
    ░███   ░███   █████  █████ ████  ██████   ████████  ████   ██████   █████ 
    ░███   ░███  ███░░  ░░███ ░███  ░░░░░███ ░░███░░███░░███  ███░░███ ███░░  
    ░███   ░███ ░░█████  ░███ ░███   ███████  ░███ ░░░  ░███ ░███ ░███░░█████ 
    ░███   ░███  ░░░░███ ░███ ░███  ███░░███  ░███      ░███ ░███ ░███ ░░░░███
    ░░████████   ██████  ░░████████░░████████ █████     █████░░██████  ██████ 
    ░░░░░░░░   ░░░░░░    ░░░░░░░░  ░░░░░░░░ ░░░░░     ░░░░░  ░░░░░░  ░░░░░░  

                    ''')
                    usuario_biblioteca.mostrar_usuario()
                elif opcion_usuarios == "4":
                    os.system("cls")
                    print(Fore.LIGHTCYAN_EX + '''

    ███████████                                                     
   ░░███░░░░░███                                                    
    ░███    ░███ █████ ████  █████   ██████   ██████   ████████     
    ░██████████ ░░███ ░███  ███░░   ███░░███ ░░░░░███ ░░███░░███    
    ░███░░░░░███ ░███ ░███ ░░█████ ░███ ░░░   ███████  ░███ ░░░     
    ░███    ░███ ░███ ░███  ░░░░███░███  ███ ███░░███  ░███         
    ███████████  ░░████████ ██████ ░░██████ ░░████████ █████        
    ░░░░░░░░░░░    ░░░░░░░░ ░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░░         
                                                                    
                                                                    
                                                                    
                                                        ███          
                                                    ░░░           
    █████ ████  █████  █████ ████  ██████   ████████  ████   ██████ 
   ░░███ ░███  ███░░  ░░███ ░███  ░░░░░███ ░░███░░███░░███  ███░░███
    ░███ ░███ ░░█████  ░███ ░███   ███████  ░███ ░░░  ░███ ░███ ░███
    ░███ ░███  ░░░░███ ░███ ░███  ███░░███  ░███      ░███ ░███ ░███
    ░░████████ ██████  ░░████████░░████████ █████     █████░░██████ 
    ░░░░░░░░ ░░░░░░    ░░░░░░░░  ░░░░░░░░ ░░░░░     ░░░░░  ░░░░░░       
                        
                        ''')
                    usuario_biblioteca.buscar_usuario()
                elif opcion_usuarios == "5":
                    break
                    
                else:
                    print("Número no valido")
                    input("Por favor, seleccione un número adecuado ")
                    os.system("cls")
                
            
        
        elif opcion_menu == "3":
            menu_prestamos= Menus()
            while True:
                opcion_prestamos=menu_prestamos.submenu_prestamos_general()
            
                if opcion_prestamos == "1":
                    os.system("cls")
                    print(Fore.LIGHTCYAN_EX + '''
    ███████████                              █████                                              
   ░░███░░░░░███                            ░░███                                               
    ░███    ░███ ████████   ██████   █████  ███████    ██████   █████████████    ██████ 
    ░██████████ ░░███░░███ ███░░███ ███░░  ░░░███░    ░░░░░███ ░░███░░███░░███  ███░░███  
    ░███░░░░░░   ░███ ░░░ ░███████ ░░█████   ░███      ███████  ░███ ░███ ░███ ░███ ░███
    ░███         ░███     ░███░░░   ░░░░███  ░███ ███ ███░░███  ░███ ░███ ░███ ░███ ░███ 
    █████        █████    ░░██████  ██████   ░░█████ ░░████████ █████░███ █████░░██████  
    ░░░░░        ░░░░░      ░░░░░░  ░░░░░░     ░░░░░   ░░░░░░░░ ░░░░░ ░░░ ░░░░░  ░░░░░░  

    ''')
                    
                    libro_prestado.prestamo()
                
                elif opcion_prestamos == "2":
                    os.system("cls")
                    print(Fore.LIGHTCYAN_EX + '''

    ██████████                                 ████                                
   ░░███░░░░███                               ░░███                                
    ░███   ░░███  ██████  █████ █████  ██████  ░███  █████ █████  ██████  ████████ 
    ░███    ░███ ███░░███░░███ ░░███  ███░░███ ░███ ░░███ ░░███  ███░░███░░███░░███
    ░███    ░███░███████  ░███  ░███ ░███ ░███ ░███  ░███  ░███ ░███████  ░███ ░░░ 
    ░███    ███ ░███░░░   ░░███ ███  ░███ ░███ ░███  ░░███ ███  ░███░░░   ░███     
    ██████████  ░░██████   ░░█████   ░░██████  █████  ░░█████   ░░██████  █████    
    ░░░░░░░░░░    ░░░░░░     ░░░░░     ░░░░░░  ░░░░░    ░░░░░     ░░░░░░  ░░░░░     
    ''')
                    libro_prestado.devolucion()
                elif opcion_prestamos == "3":
                    os.system("cls")
                    print(Fore.LIGHTCYAN_EX + '''
    ███████████                              █████                                              
   ░░███░░░░░███                            ░░███                                               
    ░███    ░███ ████████   ██████   █████  ███████    ██████   █████████████    ██████   █████ 
    ░██████████ ░░███░░███ ███░░███ ███░░  ░░░███░    ░░░░░███ ░░███░░███░░███  ███░░███ ███░░  
    ░███░░░░░░   ░███ ░░░ ░███████ ░░█████   ░███      ███████  ░███ ░███ ░███ ░███ ░███░░█████ 
    ░███         ░███     ░███░░░   ░░░░███  ░███ ███ ███░░███  ░███ ░███ ░███ ░███ ░███ ░░░░███
    █████        █████    ░░██████  ██████   ░░█████ ░░████████ █████░███ █████░░██████  ██████ 
    ░░░░░        ░░░░░      ░░░░░░  ░░░░░░     ░░░░░   ░░░░░░░░ ░░░░░ ░░░ ░░░░░  ░░░░░░  ░░░░░░  

    ''')
                    libro_prestado.mostrar_prestamos()
                elif opcion_prestamos == "4":
                    os.system("cls")
                    input("Presione Enter para confirmar... ")
                    break
                    
                else:
                    os.system("cls")
                    print("Por favor elija un número adecuado ")
                    input()
            
        elif opcion_menu == "4": 
                os.system("cls")
                print(Fore.YELLOW + "Saliendo del sistema de biblioteca..." + Style.RESET_ALL)
                input("Presione Enter para confirmar... ")
                break
        
        else:
            print("ERROR 404")
            input()
            os.system("cls")
            
        
        
        


menu()


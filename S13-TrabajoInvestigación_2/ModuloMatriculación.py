import os

'''
    CREACION DE CLASES
'''


class Carrera:
    def __init__(self, id, descripcion):
        self.__id = id
        self.descripcion = descripcion

    @property
    def id(self):
        return self.__id

    def getCarrera(self):
        return str(self.id)+"%"+self.descripcion


class Materia:
    def __init__(self, id, descripcion):
        self.__id = id
        self.descripcion = descripcion

    @property
    def id(self):
        return self.__id

    def getMateria(self):
        return str(self.id)+"%"+self.descripcion


class Periodo:
    def __init__(self, periodo, descripcion):
        self.periodo = periodo     # 202111
        self.descripcion = descripcion  # Segundo semestre 2021

    def getPeriodo(self):
        return str(self.periodo)+"%"+self.descripcion


class Profesor:
    def __init__(self, id, nombre, cedula, carrera, titulo, telefono):
        self.__id = id
        self.nombre = nombre
        self.cedula = cedula
        self.titulo = titulo
        self.telefono = telefono
        self.carrera = carrera

    @property
    def id(self):
        return self.__id

    def getProfesor(self):
        return str(self.id)+"%"+self.nombre+"%"+self.cedula+"%"+self.titulo+"%"+self.telefono+"%"+str(self.carrera.id)


class Estudiante:
    def __init__(self, id, nombre, cedula, direccion, telefono):
        self.__id = id
        self.nombre = nombre
        self.cedula = cedula
        self.direccion = direccion
        self.telefono = telefono

    @property
    def id(self):
        return self.__id

    def getEstudiante(self):
        return str(self.id)+"%"+self.nombre+"%"+self.cedula+"%"+self.direccion+"%"+self.telefono


class Matricula:
    def __init__(self, id, estudiante, carrera, periodo, valor):
        self.__id = id
        self.periodo = periodo
        self.estudiante = estudiante
        self.carrera = carrera
        self.valor = valor

    @property
    def id(self):
        return self.__id

    def getMatricula(self):
        return str(self.id)+"%"+str(self.periodo.periodo)+"%"+str(self.estudiante.id)+"%"+str(self.carrera.id)+"%"+str(self.valor)


class Notas:
    def __init__(self, id, periodo, estudiante, materia, profesor, nota1, nota2):
        self.__id = id
        self.periodo = periodo
        self.estudiante = estudiante
        self.materia = materia
        self.profesor = profesor
        self.nota1 = nota1
        self.nota2 = nota2

    @property
    def id(self):
        return self.__id

    def getNota(self):
        return str(self.id)+"%"+str(self.estudiante.id)+"%"+str(self.materia.id)+"%"+str(self.profesor.id)+"%"+str(self.nota1)+"%"+str(self.nota2)


'''
    CREACION DE FUNCIONES
'''


def contarCarreras():
    f = open("archivos/carreras.txt")
    contador = 0
    for _ in f:
        contador += 1
    f.close()

    return contador


def contarMaterias():
    f = open("archivos/materias.txt")
    contador = 0
    for _ in f:
        contador += 1
    f.close()

    return contador


def contarProfesores():
    f = open("archivos/profesores.txt")
    contador = 0
    for _ in f:
        contador += 1
    f.close()

    return contador


def contarEstudiantes():
    f = open("archivos/estudiantes.txt")
    contador = 0
    for _ in f:
        contador += 1
    f.close()

    return contador


def contarMatriculas():
    f = open("archivos/matriculas.txt")
    contador = 0
    for _ in f:
        contador += 1
    f.close()

    return contador


def contarNotas():
    f = open("archivos/notas.txt")
    contador = 0
    for _ in f:
        contador += 1
    f.close()

    return contador


def leerCarrera():
    os.system("cls")
    print("\tINGRESO DE CARRERA\n")

    _id = contarCarreras() + 1
    _descripcion = input("DESCRIPCION: ")
    carrera = Carrera(_id, _descripcion)

    f = open("archivos/carreras.txt", "a")
    f.write(carrera.getCarrera()+"\n")
    print("\nSe agrego la carrera satisfactoriamente!")
    f.close()


def leerMateria():
    os.system("cls")
    print("\tINGRESO DE MATERIA\n")
    _id = contarMaterias() + 1
    _descripcion = input("DESCRIPCION: ")
    materia = Materia(_id, _descripcion)

    f = open("archivos/materias.txt", "a")
    f.write(materia.getMateria()+"\n")
    print("\nSe agrego la materia satisfactoriamente!")
    f.close()


def buscarExistenciaPeriodo(p):
    f = open("archivos/periodos.txt")
    bandera = False

    for linea in f:
        _lectura = linea.split("%")
        if int(_lectura[0]) == p:
            bandera = True

    f.close()
    return bandera


def leerPeriodo():
    os.system("cls")
    print("\tINGRESO DE PERIODO\n")
    _periodo = input("    PERIODO: ")

    if buscarExistenciaPeriodo(_periodo):
        print(f"\nEl periodo {_periodo} ya existe!")
    else:
        _descripcion = input("DESCRIPCION: ")
        periodo = Periodo(_periodo, _descripcion)

        f = open("archivos/periodos.txt", "a")
        f.write(periodo.getPeriodo()+"\n")
        print("\nSe agrego el periodo satisfactoriamente!")
        f.close()


def buscarCarrera(_id):
    f = open("archivos/carreras.txt")
    carrera = None

    for linea in f:
        _lectura = linea.split("%")
        if int(_lectura[0]) == _id:
            carrera = Carrera(int(_lectura[0]), _lectura[1])

    f.close()
    return carrera


def leerProfesor():
    os.system("cls")
    print("\tINGRESO DE PROFESOR\n")
    _id = contarProfesores() + 1
    _nombre = input("  NOMBRE: ")
    _cedula = input("  CEDULA: ")
    _titulo = input("  TITULO: ")
    _telefono = input("TELEFONO: ")
    _carrera_id = int(input("ID DE CARRERA: "))
    _carrera = buscarCarrera(_carrera_id)

    if _carrera is None:
        print("\nERROR! No existe ese ID de carrera!")
    else:
        print("DESCRIPCION: " + _carrera.descripcion)

        opcion = input("\nEsta seguro de grabar el registro? (s/n): ")

        if opcion in ['s', 'S']:
            profesor = Profesor(_id, _nombre, _cedula,
                                _carrera, _titulo, _telefono)

            f = open("archivos/profesores.txt", "a")
            f.write(profesor.getProfesor()+"\n")
            print("\nSe agrego el profesor satisfactoriamente!")
            f.close()
        else:
            print("\nRegistro eliminado!")


def leerEstudiante():
    os.system("cls")
    print("\tINGRESO DE ESTUDIANTE\n")
    _id = contarEstudiantes() + 1
    _nombre = input("   NOMBRE: ")
    _cedula = input("   CEDULA: ")
    _direccion = input("DIRECCION: ")
    _telefono = input(" TELEFONO: ")

    opcion = input("\nEsta seguro de grabar el registro? (s/n): ")

    if opcion in ['s', 'S']:
        estudiante = Estudiante(_id, _nombre, _cedula, _direccion, _telefono)

        f = open("archivos/estudiantes.txt", "a")
        f.write(estudiante.getEstudiante()+"\n")
        print("\nSe agrego al estudiante satisfactoriamente!")
        f.close()
    else:
        print("\nRegistro eliminado!")


def buscarPeriodo(_id):
    f = open("archivos/periodos.txt")
    periodo = None

    for linea in f:
        _lectura = linea.split("%")
        if int(_lectura[0]) == _id:
            periodo = Periodo(int(_lectura[0]), _lectura[1])

    f.close()
    return periodo


def buscarEstudiante(_id):
    f = open("archivos/estudiantes.txt")
    estudiante = None

    for linea in f:
        _lectura = linea.split("%")
        if int(_lectura[0]) == _id:
            estudiante = Estudiante(
                int(_lectura[0]), _lectura[1], _lectura[2], _lectura[3], _lectura[4])

    f.close()
    return estudiante


def matricular():
    os.system("cls")
    print("\tREGISTRO DE MATRICULA\n")
    _id = contarMatriculas() + 1
    _periodo_id = int(input("ID DE PERIODO: "))
    _periodo = buscarPeriodo(_periodo_id)

    if _periodo is None:
        print("\nERROR! No existe ese ID de periodo!")
        return

    print("DESCRIPCION: " + _periodo.descripcion)

    _estudiante_id = int(input("ID DE ESTUDIANTE: "))
    _estudiante = buscarEstudiante(_estudiante_id)

    if _estudiante is None:
        print("\nERROR! No existe ese ID de estudiante!")
        return

    print("NOMBRE: " + _estudiante.nombre)

    _carrera_id = int(input("\nID DE CARRERA: "))
    _carrera = buscarCarrera(_carrera_id)

    if _carrera is None:
        print("\nERROR! No existe ese ID de carrera!")
        return

    print("DESCRIPCION: " + _carrera.descripcion)

    _valor = int(input("VALOR: "))

    opcion = input("\nEsta seguro de grabar el registro? (s/n): ")

    if opcion in ['s', 'S']:
        matricula = Matricula(_id, _estudiante, _carrera, _periodo, _valor)

        f = open("archivos/matriculas.txt", "a")
        f.write(matricula.getMatricula()+"\n")
        print("\nSe agrego la matricula satisfactoriamente!")
        f.close()
    else:
        print("\nRegistro eliminado!")


def buscarMateria(_id):
    f = open("archivos/materias.txt")
    materia = None

    for linea in f:
        _lectura = linea.split("%")
        if int(_lectura[0]) == _id:
            materia = Materia(int(_lectura[0]), _lectura[1])

    f.close()
    return materia


def buscarProfesor(_id):
    f = open("archivos/profesores.txt")
    profesor = None

    for linea in f:
        _lectura = linea.split("%")
        if int(_lectura[0]) == _id:
            _carrera_id = int(_lectura[5])
            _carrera = buscarCarrera(_carrera_id)
            profesor = Profesor(
                int(_lectura[0]), _lectura[1], _lectura[2], _carrera, _lectura[3], _lectura[4])

    f.close()
    return profesor


def notas():
    os.system("cls")
    print("\tREGISTRO DE NOTAS\n")
    _id = contarNotas() + 1
    _periodo_id = int(input("ID DE PERIODO: "))
    _periodo = buscarPeriodo(_periodo_id)

    if _periodo is None:
        print("\nERROR! No existe ese ID de periodo!")
        return

    print("DESCRIPCION: " + _periodo.descripcion)

    _estudiante_id = int(input("ID DE ESTUDIANTE: "))
    _estudiante = buscarEstudiante(_estudiante_id)

    if _estudiante is None:
        print("\nERROR! No existe ese ID de estudiante!")
        return

    print("NOMBRE: " + _estudiante.nombre)

    _materia_id = int(input("\nID DE MATERIA: "))
    _materia = buscarMateria(_materia_id)

    if _materia is None:
        print("\nERROR! No existe ese ID de materia!")
        return

    print("DESCRIPCION: " + _materia.descripcion)

    _profesor_id = int(input("ID DE PROFESOR: "))
    _profesor = buscarProfesor(_profesor_id)

    if _profesor is None:
        print("\nERROR! No existe ese ID de profesor!")
        return

    print("NOMBRE: " + _profesor.nombre)

    _nota1 = float(input("\nNOTA 1: "))
    _nota2 = float(input("NOTA 2: "))

    opcion = input("\nEsta seguro de grabar el registro? (s/n): ")

    if opcion in ['s', 'S']:
        nota = Notas(_id, _periodo, _estudiante,
                     _materia, _profesor, _nota1, _nota2)

        f = open("archivos/notas.txt", "a")
        f.write(nota.getNota()+"\n")
        print("\nSe agrego la nota satisfactoriamente!")
        f.close()
    else:
        print("\nRegistro eliminado!")


'''
    CREACION DE MENUS ITERACTIVOS
'''

while True:
    os.system('cls')
    print("=========================================")
    print("  Bienvenido al Modulol de Matriculación ")
    print("=============Menu Principal==============")
    print("\t[1] Mantenimiento                      ")
    print("\t[2] Matriculacion                      ")
    print("\t[3] Notas                              ")
    print("\t[0] Salir                              ")
    print("=========================================")

    opcion = int(input("Selecciona una opcion: "))
    if(opcion == 1):
        while True:
            os.system('cls')
            print("=========================================")
            print("           Menu Mantenimiento            ")
            print("=========================================")
            print("\t[1] Carrera                            ")
            print("\t[2] Materia                            ")
            print("\t[3] Periodo                            ")
            print("\t[4] Profesor                           ")
            print("\t[5] Estudiante                         ")
            print("\t[0] Salir                              ")
            print("=========================================")

            opcion = int(input("Selecciona una opcion: "))
            if(opcion == 1):
                leerCarrera()
            elif (opcion == 2):
                leerMateria()
            elif (opcion == 3):
                leerPeriodo()
            elif (opcion == 4):
                leerProfesor()
            elif (opcion == 5):
                leerEstudiante()
            elif (opcion == 0):
                break
            else:
                print("\nPor favor, selecciona las opciones correctas")
            os.system('pause')
    elif (opcion == 2):
        while True:
            os.system('cls')
            print("=========================================")
            print("           Menu Matriculacion            ")
            print("=========================================")
            print("\t[1] Matricula                          ")
            print("\t[0] Salir                              ")
            print("=========================================")

            opcion = int(input("Selecciona una opcion: "))
            if(opcion == 1):
                matricular()
            elif (opcion == 0):
                break
            else:
                print("\nPor favor, selecciona las opciones correctas")
            os.system('pause')
    elif (opcion == 3):
        while True:
            os.system('cls')
            print("=========================================")
            print("              Menu Notas                 ")
            print("=========================================")
            print("\t[1] Notas                              ")
            print("\t[0] Salir                              ")
            print("=========================================")

            opcion = int(input("Selecciona una opcion: "))
            if(opcion == 1):
                notas()
            elif (opcion == 0):
                break
            else:
                print("\nPor favor, selecciona las opciones correctas")
            os.system('pause')
    elif (opcion == 0):
        print("\nGracias por usar el programa!")
        break
    else:
        print("\nPor favor, selecciona las opciones correctas")

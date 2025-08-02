students = {'EST1507325':
                {'name': 'Rodrigo', 'career': 'Ingenieria En Informatica Y Sistemas',
                 'subjects': {'Calculo': 10, 'Física': 62}}}

def input_integer(message): #INGRESAR UN ENTERO Y VERIFICAR QUE SU ENTRADA SEA VALIDA
    while True:
        try:
            value = int(input(message))
            break
        except ValueError: print('-'*50+'\n'+"❌"*5+"   Lo siento valor no valido, intentelo nuevamente   "+"❌"*5)
    return value

def add_student():
    print("-"*20+" AÑADIR ESTUDIANTE "+"-"*20)
    while True:
        id_add = input("▶ Ingresa el codigo del nuevo estudiante: ")
        if id_add not in students: break
        else: print("\nError, codigo ya registrado, porfavor, crea un codigo no existente")
    name = input("▶ Ingresa el nombre nuevo estudiante: ").capitalize()
    career = input("▶ Ingresa el nombre de la carrera del nuevo estudiante: ").capitalize()

    students[id_add] = {
        'name': name,
        'career': career,
        'subjects': {}
    }

    print(f"\n  ✔️ ¡El estudiante {name}({id_add}) ha sido agregado correctamente!")

def check_id(option: str): #HACE LA VERIFICACIÓN DE ID DEL ESTUDIANTE (PARA NO HACER EL MISMO CODIGO OTRA VEZ EN LA OPCIÓN 2 Y 3)
    while True:
        print("-" * 20 + f" {option} " + "-" * 20)
        id_select = input("▶ Ingresa el codigo del estudiante: ")
        if id_select in students: break #SALE DIRECTAMENTE EL BUCLE SOLO SI EL ID ESTÁ REGISTRADO
        else:
            print(f"\n ❌ Lo sentimos, no tenemos registrado el codigo {id}")
            while True:
                print("  1) Volver a intentar\n  2) Volver al menú principal")
                op_cancel_notes = input("▶ ¿Qué deseas hacer?: ")
                match op_cancel_notes:
                    case '1': break #VOLVER A INTENTAR
                    case '2':
                        id_select = None #DEJA EL ID COMO NONE PARA SABER QUE EL USUARIO QUIERE VOLVER AL MENÚ PRINCIAPAL (ALGO FORZADO)
                        break
                    case _: print("-"*25+"\nEntrada no valida, intente de nuevo\n"+"-"*25)
        if id_select is None: break #VOLVER AL MENU PRINCIPAL
    return id_select

def add_note():
    id_select = check_id("AÑADIR NOTA A ESTUDIANTE")

    if id_select in students: #PARA EVITAR QUE AL VOLVER AL MENÚ PRINCIAPAL SE EJECUTE ESTO
        print(f"Para el estudiante {students[str(id_select)]['name']}: ")
        name_subject = input("   ▶ Ingresa el nombre del curso: ").capitalize()
        while True:
            note = input_integer("   ▶ Ingresa la nota final del curso: ")
            if 0<= note <= 100: break #SI LA NOTA ESTÁ ENTRE 0 Y 100 EL PROGRAMA CONTINUAR SI NO VUELVE A PEDIR LA NOTA
            else: print("-"*25+"\nEntrada no valida, la nota debe estar en el rango entre 0 y 100\n"+"-"*25)

        students[str(id_select)]['subjects'][name_subject.lower()] = note #SE GUARDA EN EL DICCIONARIO SUBJECTS COMO CLAVE EL NOMBRE DEL CURSO Y COMO VALOR LA NOTA
        print(f"\n  ✔️ ¡El curso {name_subject}({note} pts) ha sido añadido al estudiante {students[str(id_select)]['name']}({id_select})!") #SE AGREGA AL DICCIONARIO
        print(students)

def select_student():
    id_select = check_id("CONSULTAR ESTUDIANTE")
    if id_select in students:  # PARA EVITAR QUE AL VOLVER AL MENÚ PRINCIAPAL SE EJECUTE ESTO
        print(f"  Nombre: {students[id_select]['name']}\n  Carrera: {students[id_select]['career']}\n  Cursos: ")
        if len(students[id_select]['subjects']) > 0: #Si existen cursos
            for name,note in students[id_select]['subjects'].items():
                print(f"     ⏺ {name}: {note}")
        else: print("    Sin cursos registrados")

def media_note_student():
    id_select = check_id("CONSULTAR ESTUDIANTE")
    if id_select in students:  # PARA EVITAR QUE AL VOLVER AL MENÚ PRINCIAPAL SE EJECUTE ESTO
        try:
            sum_notes = 0
            for i in students[id_select]['subjects'].values(): sum_notes += i
            print(f"El promedio del estudiante es: {sum_notes/len(students[id_select]['subjects']):.2f}")
        except ZeroDivisionError: print("\nEl estudiante seleccionado no posee cursos asignados")

def approve_subject():
    id_select = check_id("CONSULTAR ESTUDIANTE")
    if id_select in students:
        print(f"{'Curso':<25}{'Nota':<15}{'Estado'}")
        for name,note in students[id_select]['subjects'].items():
            if note >= 61: state = 'Aprovado'
            else: state = 'Reprobado'
            print(f"{name:<25}{note:<15}{state}")

while True:
    print("═"*20+" BIENVENIDO "+"═"*20)
    print("1) Agregar estudiante\n2) Agregar curso con nota\n3) Consultar estudiante\n4) Calcular promedio de estudiante\n5) Verificar si aprueba\n6) Mostrar todos los estudiantes\n7) Salir")
    try:
        op = input("▶ Ingresa una de las opciones: ")
        match op:
            case '1': add_student()
            case '2': add_note()
            case '3': select_student()
            case '4': media_note_student()
            case '5':approve_subject()
            case '7': #EL PROGRAMA MARCA UN MENSAJE DE DESPEDIDA Y GUARDA LOS DATOS
                print("\n  ⌂ Hasta pronto!")
                break
            case _: print("-"*25+"\nEntrada no valida, intente de nuevo\n"+"-"*25)
    #except KeyboardInterrupt: print("\n\n"+ "❌ Error en el programa, usted intentó salir de manera bruzca\n   Redirigiendo al menú principal") #ERROR CUANDO SE FUERZA EL CIERRE DEL PROGRAMA
    except Exception as e:  print("\n\n"+ f"❌ Error en el programa, hubo un fallo inesperado, {e}\n   Redirigiendo al menú principal") #EVITAR CUALQUIER TIPO DE ERROR NO PREVISTO
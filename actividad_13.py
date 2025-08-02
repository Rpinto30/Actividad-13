students = {}

def input_integer(message): #INGRESAR UN ENTERO Y VERIFICAR QUE SU ENTRADA SEA VALIDA
    while True:
        try:
            value = int(input(message))
            break
        except ValueError: print('-'*50+'\n'+"❌"*5+"   Lo siento valor no valido, intentelo nuevamente   "+"❌"*5)
    return value

def load_data():
    try:
        with open("data.txt", 'r') as data_load:
            data = []
            for num, linea in enumerate(data_load, 0):
                if linea.strip() != "": data.append(linea.strip())
                else:
                    id_std = data[0]
                    students[id_std] = {
                        'name' : data[1],
                        'career': data[2],
                        'subjects': {}
                    }
                    for subject_line in data[3:]:
                        parts = subject_line.rsplit("   ", 1)
                        if len(parts) == 2:
                            subjet, note = parts
                            students[id_std]['subjects'][subjet] = int(note)
                    data = []
    except FileNotFoundError:
        with open('data.txt', 'w') as archivo:
            archivo.write("")  # Crear el archivo vacío

def save_data():
    with open('data.txt', 'w') as data:
        for id_std, values in students.items():
            data.write(id_std +'\n')
            data.write(values['name']+"\n")
            data.write(values['career']+"\n")
            for subjet, note in values['subjects'].items():
                data.write(f"{subjet}   {note}\n")
            data.write('\n')
        data.write('.')


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
            print(f"\n ❌ Lo sentimos, no tenemos registrado el codigo '{id_select}'")
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
    if students:
        id_select = check_id("AÑADIR NOTA A ESTUDIANTE")

        if id_select in students: #PARA EVITAR QUE AL VOLVER AL MENÚ PRINCIAPAL SE EJECUTE ESTO
            print(f"Para el estudiante {students[str(id_select)]['name']}: ")
            name_subject = input("   ▶ Ingresa el nombre del curso: ")
            while True:
                note = input_integer("   ▶ Ingresa la nota final del curso: ")
                if 0<= note <= 100: break #SI LA NOTA ESTÁ ENTRE 0 Y 100 EL PROGRAMA CONTINUAR SI NO VUELVE A PEDIR LA NOTA
                else: print("-"*25+"\nEntrada no valida, la nota debe estar en el rango entre 0 y 100\n"+"-"*25)

            students[str(id_select)]['subjects'][name_subject] = note #SE GUARDA EN EL DICCIONARIO SUBJECTS COMO CLAVE EL NOMBRE DEL CURSO Y COMO VALOR LA NOTA
            print(f"\n  ✔️ ¡El curso {name_subject}({note} pts) ha sido añadido al estudiante {students[str(id_select)]['name']}({id_select})!") #SE AGREGA AL DICCIONARIO
            print(students)
    else: print(" 😲 No hay estudiantes registrados!")

def select_student():
    if students:
        id_select = check_id("CONSULTAR ESTUDIANTE")
        if id_select in students:  # PARA EVITAR QUE AL VOLVER AL MENÚ PRINCIAPAL SE EJECUTE ESTO
            print(f"  Nombre: {students[id_select]['name']}\n  Carrera: {students[id_select]['career']}\n  Cursos: ")
            if len(students[id_select]['subjects']) > 0: #Si existen cursos
                for name,note in students[id_select]['subjects'].items():
                    print(f"     ⏺ {name}: {note}")
            else: print("    Sin cursos registrados")
    else: print(" 😲 No hay estudiantes registrados!")

def media_note_student():
    if students:
        id_select = check_id("CONSULTAR PROMEDIO DEL ESTUDIANTE")
        if id_select in students:  # PARA EVITAR QUE AL VOLVER AL MENÚ PRINCIAPAL SE EJECUTE ESTO
            try:
                sum_notes = 0
                for i in students[id_select]['subjects'].values(): sum_notes += i
                print(f"El promedio del estudiante es: {sum_notes/len(students[id_select]['subjects']):.2f}")
            except ZeroDivisionError: print("\nEl estudiante seleccionado no posee cursos asignados")
    else: print(" 😲 No hay estudiantes registrados!")

def approve_subject():
    if students:
        id_select = check_id("CONSULTAR ESTADO DE LOS CURSOS DEL ESTUDIANTE")
        if id_select in students:
            print(f"{'Curso':<25}{'Nota':<15}{'Estado'}")
            for name,note in students[id_select]['subjects'].items():
                if note >= 61: state = 'Aprovado'
                else: state = 'Reprobado'
                print(f"{name:<25}{note:<15}{state}")
    else: print(" 😲 No hay estudiantes registrados!")

def show_students():
    if students:
        print(f"\n{'Carnet':<20}{'Nombre':<25}{'Carrera':<50}{'Notas'}")
        for id_std, values in students.items():
            print(f"{id_std:<20}{values['name']:<25}{values['career']:<50}", end="")
            if len(values['subjects']) > 0:  # Si existen cursos
                for name, note in values['subjects'].items(): print(f"⏺{name}: {note}  ", end=' ')
                print(" ")
            else: print("Sin cursos registrados")
    else: print(" 😲 No hay estudiantes registrados!")

def delete_id(): #UNA ADICIONAL SOLO PARA DAR LA OPCION
    if students:
        id_select = check_id("BORRAR ESTUDIANTE")
        if id_select in students:
            print("\nBorrando al estudiante...")
            del students[id_select]
            print("️  🗑️ Estudiante eliminado!")
    else: print(" 😲 No hay estudiantes registrados!")

load_data()
while True:
    print("═"*20+" BIENVENIDO "+"═"*20)
    print("1) Agregar estudiante\n2) Agregar curso con nota\n3) Consultar estudiante\n4) Calcular promedio de estudiante\n5) Verificar si aprueba\n6) Mostrar todos los estudiantes\n7) Borrar un estudiante\n8) Salir")
    try:
        op = input("▶ Ingresa una de las opciones: ")
        match op:
            case '1': add_student()
            case '2': add_note()
            case '3': select_student()
            case '4': media_note_student()
            case '5': approve_subject()
            case '6': show_students()
            case '7': delete_id()
            case '8': #EL PROGRAMA MARCA UN MENSAJE DE DESPEDIDA Y GUARDA LOS DATOS
                print("  ⚙️ Gurdando datos...")
                save_data()
                print("  ✔️ Los datos se guardaron correctamente!")
                print("\n  ⌂ Hasta pronto!")
                break
            case _: print("-"*25+"\nEntrada no valida, intente de nuevo\n"+"-"*25)
    except KeyboardInterrupt: print("\n\n"+ "❌ Error en el programa, usted intentó salir de manera bruzca\n   Redirigiendo al menú principal") #ERROR CUANDO SE FUERZA EL CIERRE DEL PROGRAMA
    except Exception as e:  print("\n\n"+ f"❌ Error en el programa, hubo un fallo inesperado, {e}\n   Redirigiendo al menú principal") #EVITAR CUALQUIER TIPO DE ERROR NO PREVISTO
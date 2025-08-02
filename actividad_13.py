students = {}

def add_student():
    print("-"*20+" AÑADIR ESTUDIANTE "+"-"*20)
    while True:
        id = input("▶ Ingresa el codigo del nuevo estudiante: ")
        if id not in students: break
        else: print("\nError, codigo ya registrado, porfavor, crea un codigo no existente")
    name = input("▶ Ingresa el nombre nuevo estudiante: ")
    career = input("▶ Ingresa el nombre de la carrera del nuevo estudiante: ")

    students[id] = {
        'name': name,
        'career': career,
        'subjects': []
    }

    print(f"\n  ✔️ ¡El estudiante {name}({id}) ha sido agregado correctamente!")


def input_integer(message): #INGRESAR UN ENTERO Y VERIFICAR QUE SU ENTRADA SEA VALIDA
    while True:
        try:
            value = int(input(message))
            break
        except ValueError: print('-'*50+'\n'+"❌"*5+"   Lo siento valor no valido, intentelo nuevamente   "+"❌"*5)
    return value


while True:
    print("═"*20+" BIENVENIDO "+"═"*20)
    print("1) Agregar estudiante\n2) Agregar curso con nota\n3) Consultar estudiante\n4) Calcular promedio de estudiante\n5)Verificar si aprueba\n6) Mostrar todos los estudiantes\n7) Salir")
    try:
        op = input("▶ Ingresa una de las opciones: ")
        match op:
            case '1': add_student()
            case '7': #EL PROGRAMA MARCA UN MENSAJE DE DESPEDIDA Y GUARDA LOS DATOS
                print("\n  ⌂ Hasta pronto!")
                break
            case _: print("-"*25+"\nEntrada no valida, intente de nuevo\n"+"-"*25)
    except KeyboardInterrupt: print("\n\n"+ "❌ Error en el programa, usted intentó salir de manera bruzca\n   Redirigiendo al menú principal") #ERROR CUANDO SE FUERZA EL CIERRE DEL PROGRAMA
    except Exception as e:  print("\n\n"+ f"❌ Error en el programa, hubo un fallo inesperado, {e}\n   Redirigiendo al menú principal") #EVITAR CUALQUIER TIPO DE ERROR NO PREVISTO
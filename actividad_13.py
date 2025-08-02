

def input_integer(message): #INGRESAR UN ENTERO Y VERIFICAR QUE SU ENTRADA SEA VALIDA
    while True:
        try:
            value = int(input(message))
            break
        except ValueError: print('-'*50+'\n'+"✖"*5+"   Lo siento valor no valido, intentelo nuevamente   "+"✖"*5)
        except Exception as e: print('-'*50+'\n'+"✖"*5+"   Lo siento, ocurrió un error inesperado, intentelo nuevamente   "+f":{e}"+"✖"*5)
    return value


while True:
    print("═"*20+" BIENVENIDO "+"═"*20)
    print("1) Agregar estudiante\n2) Agregar curso con nota\n3) Consultar estudiante\n4) Calcular promedio de estudiante\n5)Verificar si aprueba\n6) Mostrar todos los estudiantes\n7) Salir")
    try:
        op = input("▶ Ingresa una de las opciones: ")
        match op:
            case '7':
                print("\n  ⌂ Hasta pronto!")
                break
            case _: print("-"*25+"\nEntrada no valida, intente de nuevo\n"+"-"*25)
    except KeyboardInterrupt: print("\n\n"+ "❌ Error en el programa, usted intentó salir de manera bruzca\n   Redirigiendo al menú principal")
    except Exception as e:  print("\n\n"+ f"❌ Error en el programa, hubo un fallo inesperado, {e}\n   Redirigiendo al menú principal")
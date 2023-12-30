datos_triangulo = []
datos_prisma = []
datos_cuadrado = []
datos_cubo = []
datos_circulo = []
datos_esfera = []

def inicio():
    
    # importamos funciones de cálculo
    import funciones_calculo as fc

    lista_aux = [0,1]

    # función salir de la calculadora
    def salir():
        import sys
        print("Adiós.")
        sys.exit()

    # función que nos permitirá navegar entre las opciones de cálculo
    def comprobacion_lista():
        comprobar_forma = 3

        #comprobamos que la selección está disponible
        while comprobar_forma !=0 and comprobar_forma != 1:
            try:
                comprobar_forma = int(input(f"Ha seleccionado {forma_lista[eleccion_forma]}, ¿quiere continuar? Indique:\n1 - SI\n0 - NO\n"))
            except:
                continue

        if comprobar_forma == 1:
            forma_elegida = eleccion_forma
        elif comprobar_forma == 0:
            print("Volviendo a la pantalla inicial\n")
            inicio()

        (f"\nPara calcular el {forma_lista[forma_elegida]} necesitamos que introduzcas el valor las siguientes características")
        print("\n**NOTA**\tIntroducir solamente valores enteros o decimales mayores que 0. Comparación triángulos solo acepta valores entre 2 y 5\n")

        # codigo para el cálculo del area del triangulo
        if forma_elegida == 1:
            aux = 0
            while aux == 0:
                try:
                    base = float(input("Introduce el valor de la base en centímetros:"))
                    altura = float(input("Introduce el valor de la altura en centímetros:"))
                    assert(base>0)
                    assert(altura>0)
                    while True:
                        comprobacion = int(input(f"Los valores introducidos son:\n\tbase = {base}\n\taltura = {altura}\n¿Es correcto? Indique:\n1 - SI\n0 - NO\n"))
                        if comprobacion in lista_aux:
                            break
                        else:
                            print ("No has confirmado correctamente\n")

                    aux = 1
                    if comprobacion == 0:
                        aux = 0
                except ValueError:
                    print("Los valores de base o altura introducidos no se corresponden con un valor numérico o no ha confirmado de manera adecuada.\n")
                except AssertionError:
                    print("\nAlguno de los parámetros introducidos es menor o igual a 0, por favor introduce valores positivos\n")

            resultado = fc.area_triangulo(base, altura)
            print(f"\nPárametros de entrada:\n\tBase = {base} cm\t\t Altura = {altura} cm\n\nResultado:\n\t{forma_lista[forma_elegida]} = {resultado} cm^2.")
            datos_triangulo.append([base, altura, resultado])
            datos_triangulo_resultado=[]
            for i in datos_triangulo:
                datos_triangulo_resultado.append(i[-1])            
            conteo1 = fc.contar(datos_triangulo_resultado)
            media = fc.media(datos_triangulo_resultado)
            minimo = fc.minimo(datos_triangulo_resultado)
            maximo = fc.maximo(datos_triangulo_resultado)
            print(f"Número de veces realizada esta consulta: {conteo1} veces")
            print(f"Media de los resultados: {media} cm")
            print(f"Resultado más pequeño: {minimo} cm")
            print(f"Resultado más grande: {maximo} cm")

        # código para el calculo del volumen del prisma triangular
        elif forma_elegida == 2:
            aux = 0
            while aux == 0:
                try:
                    base = float(input("Introduce el valor de la base en centímetros: "))
                    altura1= float(input("Introduce el valor de la altura del triángulo que forma la base en centímetros: "))
                    altura2 = float(input("Introduce el valor de la altura del prisma en centímetros: "))
                    assert(base>0)
                    assert(altura1>0)
                    assert(altura2>0)
                    while True:
                        comprobacion = int(input(f"Los valores introducidos son:\n\tbase = {base}\n\taltura1 = {altura1}\n\taltura2 = {altura2}\n¿Es correcto? Indique:\n1 - SI\n0 - NO\n")) 
                        if comprobacion in lista_aux:
                            break
                        else:
                            print ("No has confirmado correctamente\n")
                    
                    aux = 1
                    if comprobacion == 0:
                        aux = 0
                except ValueError:
                    print("Los valores de base o altura introducidos no se corresponden con un valor numérico o no ha confirmado de manera adecuada.\n")
                except AssertionError:
                    print("\nAlguno de los parámetros introducidos es menor o igual a 0, por favor introduce valores positivos\n")

            resultado = fc.volumen_prisma(base, altura1, altura2)
            print(f"\nPárametros de entrada:\n\tBase = {base} cm\t\t Altura1 = {altura1} cm\t\t Altura2 = {altura1} cm\n\nResultado:\n\t{forma_lista[forma_elegida]} = {resultado} cm^3.")
            datos_prisma.append([base, altura1, altura2, resultado])
            datos_prisma_resultado = []
            for i in datos_prisma:
                datos_prisma_resultado.append(i[-1])
            conteo2 = fc.contar(datos_prisma_resultado)
            media = fc.media(datos_prisma_resultado)
            minimo = fc.minimo(datos_prisma_resultado)
            maximo = fc.maximo(datos_prisma_resultado)
            print(f"Número de veces realizada esta consulta: {conteo2} veces")
            print(f"Media de los resultados: {media} cm")
            print(f"Resultado más pequeño: {minimo} cm")
            print(f"Resultado más grande: {maximo} cm")

        # código para el cálculo del área del cuadrado
        elif forma_elegida == 3:
            aux = 0
            while aux == 0:
                try:
                    lado = float(input("Introduce el valor del lado del cuadrado en centímetros."))
                    assert(lado>0)
                    while True:
                        comprobacion = int(input(f"El valor introducido es:\n\tlado = {lado}\n¿Es correcto? Indique:\n1 - SI\n0 - NO\n"))
                        if comprobacion in lista_aux:
                            break
                        else:
                            print ("No has confirmado correctamente\n")
                    
                    aux = 1
                    if comprobacion == 0:
                        aux = 0
                except ValueError:
                    print("Los valores de lado introducido no se corresponde con un valor numérico o no ha confirmado de manera adecuada.\n")
                except AssertionError:
                    print("\nAlguno de los parámetros introducidos es menor o igual a 0, por favor introduce valores positivos\n")

            resultado = fc.area_cuadrado(lado)
            print(f"\nPárametros de entrada:\n\tLado = {lado} cm\n\nResultado:\n\t{forma_lista[forma_elegida]} = {resultado} cm^2.")

            datos_cuadrado.append([lado, resultado])
            datos_cuadrado_resultado = []
            for i in datos_cuadrado:
                datos_cuadrado_resultado.append(i[-1])            
            conteo3 = fc.contar(datos_cuadrado_resultado)
            media = fc.media(datos_cuadrado_resultado)
            minimo = fc.minimo(datos_cuadrado_resultado)
            maximo = fc.maximo(datos_cuadrado_resultado)
            print(f"Número de veces realizada esta consulta: {conteo3} veces")
            print(f"Media de los resultados: {media} cm")
            print(f"Resultado más pequeño: {minimo} cm")
            print(f"Resultado más grande: {maximo} cm")

        # codigo para el calculo del volumen del cubo    
        elif forma_elegida == 4:
            aux = 0
            while aux == 0:
                try:
                    lado = float(input("Introduce el valor del lado del cubo en centímetros."))
                    assert(lado>0)
                    while True:
                        comprobacion = int(input(f"El valor introducido es:\n\tlado = {lado}\n¿Es correcto? Indique:\n1 - SI\n0 - NO\n"))
                        if comprobacion in lista_aux:
                            break
                        else:
                            print ("No has confirmado correctamente\n")
                    
                    aux = 1
                    if comprobacion == 0:
                        aux = 0
                except ValueError:
                    print("Los valores de lado introducido no se corresponde con un valor numérico o no ha confirmado de manera adecuada.\n")    
                except AssertionError:
                    print("\nAlguno de los parámetros introducidos es menor o igual a 0, por favor introduce valores positivos\n")

            resultado = fc.volumen_cubo(lado)
            print(f"\nPárametros de entrada:\n\tLado = {lado} cm\n\nResultado:\n\t{forma_lista[forma_elegida]} = {resultado} cm^3.")

            datos_cubo.append([lado, resultado])
            datos_cubo_resultado=[]
            for i in datos_cubo:
                datos_cubo_resultado.append(i[-1])            
            conteo4 = fc.contar(datos_cubo_resultado)
            media = fc.media(datos_cubo_resultado)
            minimo = fc.minimo(datos_cubo_resultado)
            maximo = fc.maximo(datos_cubo_resultado)
            print(f"Número de veces realizada esta consulta: {conteo4} veces")
            print(f"Media de los resultados: {media} cm")
            print(f"Resultado más pequeño: {minimo} cm")
            print(f"Resultado más grande: {maximo} cm")

        # código para el cálculo del área de círculo
        elif forma_elegida == 5:
            aux = 0
            while aux == 0:
                try:
                    radio = float(input("Introduce el valor del radio de la circunferencia en centímetros."))
                    assert(radio>0)
                    while True:
                        comprobacion = int(input(f"El valor introducido es:\n\tradio = {radio}\n¿Es correcto? Indique:\n1 - SI\n0 - NO\n")) 
                        if comprobacion in lista_aux:
                            break
                        else:
                            print ("No has confirmado correctamente\n")
                    
                    aux = 1
                    if comprobacion == 0:
                        aux = 0
                except ValueError:
                    print("Los valores de radio introducido no se corresponde con un valor numérico o no ha confirmado de manera adecuada.\n")
                except AssertionError:
                    print("\nAlguno de los parámetros introducidos es menor o igual a 0, por favor introduce valores positivos\n")

            resultado = fc.area_circulo(radio)
            print(f"\nPárametros de entrada:\n\tRadio = {radio} cm\n\nResultado:\n\t{forma_lista[forma_elegida]} = {resultado} cm^2.")

            datos_circulo.append([radio, resultado])
            datos_circulo_resultado=[]
            for i in datos_circulo:
                datos_circulo_resultado.append(i[-1])            
            conteo5 = fc.contar(datos_circulo_resultado)
            media = fc.media(datos_circulo_resultado)
            minimo = fc.minimo(datos_circulo_resultado)
            maximo = fc.maximo(datos_circulo_resultado)
            print(f"Número de veces realizada esta consulta: {conteo5} veces")
            print(f"Media de los resultados: {media} cm")
            print(f"Resultado más pequeño: {minimo} cm")
            print(f"Resultado más grande: {maximo} cm")

        # código para el cálculo del volumen de la esfera
        elif forma_elegida == 6:
            aux = 0
            while aux == 0:
                try:
                    radio = float(input("Introduce el valor del radio de la esfera en centímetros."))
                    assert(radio>0)
                    while True:
                        comprobacion = int(input(f"El valor introducido es:\n\tradio = {radio}\n¿Es correcto? Indique:\n1 - SI\n0 - NO\n"))
                        if comprobacion in lista_aux:
                            break
                        else:
                            print ("No has confirmado correctamente\n")
                    
                    aux = 1
                    if comprobacion == 0:
                        aux = 0
                except ValueError:
                    print("Los valores de radio introducido no se corresponde con un valor numérico o no ha confirmado de manera adecuada.\n")
                except AssertionError:
                    print("\nAlguno de los parámetros introducidos es menor o igual a 0, por favor introduce valores positivos\n")

            resultado = fc.volumen_esfera(radio)
            print(f"\nPárametros de entrada:\n\tRadio = {radio} cm\n\nResultado:\n\t{forma_lista[forma_elegida]} = {resultado} cm^3.")

            datos_esfera.append([radio, resultado])
            datos_esfera_resultado=[]
            for i in datos_esfera:
                datos_esfera_resultado.append(i[-1])            
            conteo6 = fc.contar(datos_esfera_resultado)
            media = fc.media(datos_esfera_resultado)
            minimo = fc.minimo(datos_esfera_resultado)
            maximo = fc.maximo(datos_esfera_resultado)
            print(f"Número de veces realizada esta consulta: {conteo6} veces")
            print(f"Media de los resultados: {media} cm")
            print(f"Resultado más pequeño: {minimo} cm")
            print(f"Resultado más grande: {maximo} cm")

        # código para comparar áreas de triángulos
        if forma_elegida == 7:
            while True:
                try:
                    num_comparacion = int(input("¿Cuántos triángulos quieres comparar? Elige un valor entre 2 y 5: "))
                    assert(num_comparacion >1)
                    assert(num_comparacion <6)
                    break
                except ValueError:
                    print("Valor introducido no es un número o es incorrecto")
                except AssertionError:
                    print("El valor introducido es demasiado grande o demasiado pequeño")

            aux_triang = 1
            base_altura_lista = []
            area_lista = []
            while num_comparacion != 0:
                
                try:
                    base = float(input(f"Introduce el valor de la base en centímetros del triángulo {aux_triang}:"))
                    assert(base>0)
                    altura = float(input(f"Introduce el valor de la altura en centímetros del triángulo {aux_triang}:"))
                    assert(altura>0)
                    num_comparacion -=1
                    aux_triang +=1
                    lista = [base, altura]
                    base_altura_lista.append(lista)

                except ValueError:
                    print("Los valores de base o altura introducidos no se corresponden con un valor numérico o no ha confirmado de manera adecuada.\n")
                except AssertionError:
                    print("\nAlguno de los parámetros introducidos es menor o igual a 0, por favor introduce valores positivos\n")
            
            area_lista = list(map(fc.area_triangulo2, base_altura_lista))
            print(f"Los cálculos de área para las base / altura {base_altura_lista} de los triángulos son: {area_lista}")

        print("\n¿Quiere realizar algún cálculo más?\n")
        inicio()

    print("-"*20)
    print("-"*7+" APLICACION PARA EL CÁLCULO DE ÁREAS Y VOLÚMENES DE DIFERENTES FORMAS GEOMÉTRICAS "+"-"*7)
    print("-"*20)

    while True:
        eleccion_forma = input("Marque la opción 1, 2, 3, 4, 5, 6 o 7 entre las siguientes\n1 - Área Triángulo\n2 - Volumen Prisma Triangular\n3 - Área Cuadrado\n4 - Volumen Cubo\n5 - Área Círculo\n6 - Volumen Esfera\n7 - Comparación Triángulos\n9 - Salir\n")

        try:
            eleccion_forma = int(eleccion_forma)
            break
        except:
            print("\nEl valor introducido no se corresponde con ninguna de las opciones, por favor elija la opción introduciendo su valor numérico\n")
        

    forma_lista = {1:"Área Triángulo", 2:"Volumen Prisma Triangular", 3:"Área Cuadrado", 4:"Volumen Cubo", 5:"Área Círculo", 6:"Volumen Esfera", 7:"Comparación Triángulos", 9:"Salir"}

    while eleccion_forma not in forma_lista:
        print(f"Selección: {eleccion_forma} no disponible, por favor, elija entre las opciones disponibles\n")
        inicio()
        
    if eleccion_forma == 9:
        salir()        
    else:
        comprobacion_lista()

inicio()
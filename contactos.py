'''Este  codigo  imita la aplicacion de contactos
Autor : Juan  Felipe  Corrales  Toro
ULTIMA  ACTUALIZACION : 25  de  Octubre  /  2021'''
opciones=""
contactos={}


while opciones !="4":#usamos un while para que la "app" de contactos se cierre cuando el usuario lo pida
    opciones=input("menu\n (1)agregar\n (2)mostrar\n (3)eliminar\n (4)terminar\n")#menu
    
    
    if opciones =="1":
        nombre =input("ingrese el nombre del contacto ")
        while nombre=="":
            print("no puede estar vacio")
            nombre =input("ingrese el nombre del contacto ")
        if nombre in contactos:
            print("este contacto ya existe")
            opcion=input("quieres modificarlo si/no?")
            if opcion=="si":
                telefono =input("ingrese el numero del contacto ")
                while telefono=="":
                    print("no puede estar vacio")
                    telefono =input("ingrese el numero del contacto ")
                contactos[nombre]=int(telefono)#ingresamos el resultado al diccionario
                print("se guardo con exito el contacto de ",nombre)
            else:
                print("el contacto ",nombre," quedo igual")
                print(contactos[nombre])
        else:
            telefono =input("ingrese el numero del contacto ")
            while telefono=="":
                print("no puede estar vacio")
                telefono =input("ingrese el numero del contacto ")
            contactos[nombre]=int(telefono)#ingresamos el resultado al diccionario
            print("se guardo con exito el contacto de ",nombre)
            
            
    if opciones =="2":
        verificaciones =input("desea ver toda la lista de contactos si/no? ")
        if verificaciones == "si":
            print(contactos)
        else:
            nombre=input("ingrese el nombre del usuario que desea mostrar ")
            if nombre in contactos:
                print(nombre, ":",contactos[nombre])
            else:
                print("este contacto no existe ")
                
                
    if opciones=="3":
            nombre=input("ingrese el nombre del usuario que desea eliminar ")
            if nombre in contactos:
                del contactos[nombre]#en esta linea eliminamos el contacto nombre
                print("este contacto fue eliminado con exito")
            else:
                print("este contacto no existe")
    

    if opciones=="4":
        with open('contactos.txt', 'w') as archivo:
            archivo.write(str(contactos))

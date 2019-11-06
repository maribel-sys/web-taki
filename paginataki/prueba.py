import speech_recognition as sr
import mysql.connector

r = sr.Recognizer()

mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="o.a.m.l.l",
   database="taki"
)
mycursor = mydb.cursor()

def reconocer(texto):
    with sr.Microphone() as source:
        print(texto)
        audio = r.listen(source)
    reconocimiento=""
    try:
        reconocimiento=r.recognize_google(audio, language="es-CO")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return reconocimiento

while True:
    #palabraMagica = reconocer("Esperando palabra magica")
    palabraMagica = input("Esperando palabra magica ")
    #print("La palabra magica es:",palabraMagica)
    if palabraMagica == "taki" or palabraMagica=="Taki":
        while True:
            #categoria = reconocer("Esperando categoria")
            categoria = input("Esperando categoria ")
            #print("La categoria es: ",categoria)
            if categoria == "Mercado" or categoria == "mercado":
               # print("Lista de mercado")
                mercado=[]
                while True:
                    producto=reconocer("Que producto de mercado deseas guardar:")
                    if producto=="salir" or producto=='no':
                        break
                    print("El producto:", producto, "quedo almacenado de manera exitosa")
                    sql = "INSERT INTO listas_mercado (producto) VALUES ('"+ str(producto)+"')"
                    mycursor.execute(sql)
                    mydb.commit()
                    mercado.append(producto)
                    print(mercado)
            elif categoria == "producto" or categoria=="Productos" or categoria=="Producto" or categoria=="productos":
               # print("Lista de productos")
                productos=[]
                while True:
                    producto=reconocer("Que producto deseas guardar:")
                    if producto=="no" or producto=="salir":
                        break
                    print("el producto:", producto ,"quedo almacenado de manera exitosa")
                    sql = "INSERT INTO listas_productos (producto) VALUES ('"+ str(producto)+"')"
                    mycursor.execute(sql)
                    mydb.commit()
                    productos.append(producto)
                    print(productos)
            elif categoria == "recetario" or categoria=="Recetario":
               # print("Recetario")
                recetario=[]
                while True:
                    #producto=reconocer("Que producto deseas guardar:")
                    producto=input("Que producto deseas guardar: ")
                    #recetario.append(producto)
                    if producto=="no" or producto=="salir":
                        break
                    #cantidades=reconocer("que cantidades del producto:")
                    cantidades=input("que cantidades del producto: ")
                    print(cantidades,producto, "quedo almacenado de manera exitosa")
                    sql = "INSERT INTO listas_recetario (cantidad,producto) VALUES (%s, %s)"
                    val = (cantidades,producto)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    recetario.append([cantidades, producto])
                    print(recetario)
            elif categoria == "recuerdame" or categoria=="Recuerdame" or categoria=="recuérdame" or categoria=="Recuérdame":
                #print("Recuerdame")
                recuerdame=[]
                while True:
                    recordatorio=reconocer("Que deseas recordar:")
                    if recordatorio=="no" or recordatorio=="salir":
                        break
                    print(recordatorio, "quedo almacenado de manera exitosa")
                    sql = "INSERT INTO listas_recuerdame (recordatorio) VALUES ('"+ str(recordatorio)+"')"
                    mycursor.execute(sql)
                    mydb.commit()
                    recuerdame.append(recordatorio)
                    print(recuerdame)
            elif categoria == "salir":
                print("Salir")
                break  
    if palabraMagica=="salir" or palabraMagica=="no":
        break            


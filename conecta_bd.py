#Importar librerias
import pymysql
#Procedimiento para conectar y extraer informacion de la BD
def recupera_categoria():
    #se crea un bojeto de coneccion a la BD
    conn=pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
    #se crea un cursor para ejecutar consultas a la base de datos
    cursor=conn.cursor()
    #se utiliza el cursor para ejecutar la consulta sobre la tabla de categorias
    cursor.execute('select descripcion from categoria')
    #se crea una lista para contener las categorias extraidas de la base de datos
    categorias=cursor.fetchall()
    #cerrar la base de datos
    conn.close()
    print(categorias)
    return categorias

def recupera_preguntas(cat):
    #se crea un objeto de coneccion a la BD
    conn=pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
    #se crea un cursor para ejecutar consultas a la base de datos
    cursor=conn.cursor()
    #consulta de busqueda
    consulta='select b.id_pregunta,b.pregunta,b.opcion_1,b.opcion_2,b.opcion_3,b.opcion_4,b.correcto,b.id_categoria '
    consulta=consulta+'from categoria a, pregunta b '
    consulta=consulta+'where a.descripcion="'+cat+'" and b.id_categoria=a.id_categoria'
    #se utiliza el cursor para ejecutar la consulta sobre la tabla de preguntas
    cursor.execute(consulta)
    #se crea una lista para contener las categorias extraidas de la base de datos
    preguntas=cursor.fetchall()
    print(preguntas)
    #cerrar la base de datos
    conn.close()
    return preguntas #hvbfevjhbfekvhb k kbvkfehbvhfev
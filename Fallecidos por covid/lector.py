import pandas as pd
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
#lee el archivo csv
file = pd.read_csv('210516COVID19MEXICO.csv')

#obtener el total de registros
registros = len(file)
print(f"La cantidad de registros es {registros}")

#cantidad de registros que usarán el maestro y el esclavo
mitad = int(registros / 2)
print(f'Cada dataset nuevo tendrá {mitad} registros')

muertes1 = 0
muertes2 = 0
promedio1 = 0
promedio2 = 0


#rank 1
#----------M A E S T R O-----------

#crear los archivos para cada uno
if rank == 0:
    file1 = file.head(mitad) #head toma los primeros 3426041 del archivo original
    print('Registros del archivo1 = ',len(file1))

    #se vuelven a crear otros archivos pero que contengan solo las columnas de nuestro interés
    new_file1 = file1[['EDAD','FECHA_DEF']]

    #para este caso, la única manera de conocer las defunciones, es viendo si tienen fecha de muerte. 
    #los que no murieron, en la columna FECHA_DEF tienen '9999-99-99' como valor, así que estos se excluyen
    maestro = new_file1[new_file1['FECHA_DEF'] != '9999-99-99']
    maestro.head(10) #mostrar los primeros 10 datos que obtuvo el maestro

    #contabilizar las muertes
    muertes1 = len(maestro)
    print(f'Muertes contadas en el programa 1: {muertes1}')

    #promedio de edades 
    promedio1 = maestro['EDAD'].mean()
    print(f"Promedio 1 = {promedio1}")
    comm.send(muertes1, dest=0)
    comm.send(promedio1, dest=0)

    #resultados1 = [muertes1, promedio1]
    #comm.send(resultados1, dest=0)

#rank 2
#----------E S C L A V O---------

if rank == 1: 
    file2 = file.tail(mitad) #tail toma los últimos 3426041 del archivo original
    print('Registros del archivo2 = ',len(file2))

    #se vuelven a crear otros archivos pero que contengan solo las columnas de nuestro interés
    new_file2 = file2[['EDAD','FECHA_DEF']]

    #para este caso, la única manera de conocer las defunciones, es viendo si tienen fecha de muerte. 
    #los que no murieron, en la columna FECHA_DEF tienen '9999-99-99' como valor, así que estos se escluyen
    esclavo = new_file2[new_file2['FECHA_DEF'] != '9999-99-99']
    esclavo.head(10) #mostrar los primeros 10 datos que obtuvo el esclavo

    #contabilizar las muertes
    muertes2 = len(esclavo)
    print(f'Muertes contadas en el programa 2: {muertes2}')

    #promedio de edades
    promedio2 = esclavo['EDAD'].mean()
    print(f"Promedio 2 = {promedio2}")

    #resultados2 = [muertes2, promedio2]
    #comm.send(resultados2, dest=0)
    comm.send(muertes2, dest=0)
    comm.send(promedio2, dest=0)


# comm.send(muertes2, dest=0)
#--------AL recibir los datos de cada programa----------

data1=comm.recv(source=0)
print(data1)
data2=comm.recv(source=1)
print(data2)

print(f'TOTAL de muertes: {muertes1+muertes2}')

promedio_total = int((promedio1+promedio2 )/ 2)
print(f"Promedio TOTAL = {promedio_total}")

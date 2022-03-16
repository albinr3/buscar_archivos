import os, shutil, xlrd

#creamos una lista vacia para almacenar los codigos posteriormente
files_to_find = []
lista_imagenes_total=[]
ruta_destino = 'C:/Users/Albin Rodriguez/Pictures/carpeta4' #'input("Digite la ruta de la carpeta destino: ")

#Abrimos el archivo excel y cargamos todos los codigos en la lista vacia.
data = xlrd.open_workbook(input("Digite el nombre del archivo excel y su extension: "))
sheet1 = data.sheet_by_index(0)
for i in range(sheet1.nrows):
    files_to_find.append(sheet1.cell_value(i, 0))
    
#Buscamos los codigos en esta ruta
for root, dirs, files in os.walk('C:/Users/Albin Rodriguez/Desktop/FOTOS PRODUCTOS/'):
    for _file in files:
        if _file in files_to_find:
            print (f'{_file} Encontrado en esta ruta: ' + str(root)) # Si lo encontramos nos dira que fue encontrado en esta ruta
            shutil.copy(os.path.abspath(root + '/' + _file), 'C:/Users/Albin Rodriguez/Pictures/carpeta4')
        lista_imagenes_total.append(_file)

#Verificamos cuales archivos no fueron encontrados y lo imprimimos
for elementos in files_to_find:
    if elementos not in lista_imagenes_total:
        print(f"El archivo {elementos} no fue encontrado!")        
        
 
   
            
           
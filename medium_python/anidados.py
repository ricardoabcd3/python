def list():
    my_list = [1,"hola",True,5.5]
    mi_dic = {"primer nombre": "ricardo","apellido": "ramirez"}

    super_lista =[
        {"primer nombre": "ricardo","apellido": "ramirez"},
        {"primer nombre": "isabel","apellido": "ortega"},
        {"primer nombre": "david","apellido": "osmar"},
        {"primer nombre": "carlos","apellido": "coman"},
        {"primer nombre": "pablo","apellido": "ramirez"}
    ]
    super_dici= {
        "numeros_natu": [1,2,3,4,5],
        "negativos_nums": [-1,-2,0,1,2],
        "numeros_decimales": [1.1,4.5,6.43]
    }

    for i in super_lista:
        for llave, valor in i.items():

            print(llave,":"," ", valor)

if __name__ == '__main__':
    list()
    


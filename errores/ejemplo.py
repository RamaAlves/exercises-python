'''elabore un programa que dada una lista de 15 elementos, 
copie en otra lista los elementos pares multiplicados por 2'''

lista_numeros=[1,2,3,4,5,0,6,7,8,9,10,11,12,13,"aaa",15]
lista_resultado=[]

# try:
#     for i in lista_numeros:
#         if i%2==0:
#             lista_resultado.append(i*2)
# except:
#     print("la operacion no ha finalizado correctamente")
# else:
#     print("Todo funciono de manera correcta")
# finally:
#     print("continua")

# print(lista_resultado)
# print("El programa sigue")

try:
    for i in lista_numeros:
        lista_resultado.append(100/i)
except ZeroDivisionError:
    print("No se puede dividir por cero, pruebe con otro numero")
except:
    print("La operacion no finalizo correctamente")
else:
    print("La operacion finalizo correctamente")
finally:
    print("esto se debe ejecutar si o si")

print(lista_resultado)
print("Mi programa sigue")
print('CLACULADORA IMC')

NomeUsuario = input("Nome do Usuario: ")
metros = float(input("Quantos metro tem ? : ".format(NomeUsuario)))
peso = float(input("Quantos quilos você tem? : "))
IMC =  float ( peso / (metros * metros))

if IMC <= 18.5: 
    print("magreza")
elif IMC >=  18.5 or IMC <= 24.9:
    print("Normal ")
elif IMC >= 25 or IMC <= 29:
     print(" sobre peso grau I ")
elif IMC >= 30 or IMC <= 39:
    print("Obesidade II")
elif IMC >= 40:
    print("Obesidade III")
else:
    ("ERRO")

print("valor do IMC é {:.f2}".format(IMC))


"""IMC Classificação     Obesidade        (grau)
Menor que 18,5        Magreza 	        0
Entre 18,5 e 24,9     Normal            0
Entre 25,0 e 29,9     Sobrepeso 	    I
Entre 30,0 e 39,9     Obesidade 	    II
Maior que 40,0        Obesidade Grave 	III  """

window.close()

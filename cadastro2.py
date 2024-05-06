print("Faça o cadastro da primeira pessoa aqui a baixo:")
nome=input("Insira seu nome: ")
sexo=input("Insira seu sexo: ")
idade=int(input("Insira sua idade: "))

if(idade<18):
    print("A primeira pessoa é menor de idade")
else:
    print("A primeira pessoa é maior de idade")    


print("Faça o cadastro da segunda pessoa aqui a baixo:")
nome2=input("Insira seu nome: ")
sexo2=input("Insira seu sexo: ")
idade2=int(input("Insira sua idade: "))

if(idade2<18):
    print("A segunda pessoa é menor de idade")
else:
    print("A segunda pessoa é maior de idade") 

print("Faça o cadastro da terceira pessoa aqui a baixo:")


nome3=input("Insira seu nome: ")
sexo3=input("Insira seu sexo: ")
idade3=int(input("Insira sua idade: "))

if(idade3<18):
    print("A terceira pessoa é menor de idade")
else:
    print("A terceira pessoa é maior de idade") 

print("PRIMEIRO CADASTRO")
print("nome:", nome)
print("sexo:", sexo)
print("idade:", idade)
if(idade<18):
    print("É menor de idade")
else:
    print("É maior de idade")    

print("SEGUNDO CADASTRO")
print("nome:", nome2)
print("idade:", idade2)
print("sexo:", sexo2)
if(idade2<18):
    print("É menor de idade")
else:
    print("É maior de idade")  

print("TERCEIRO CADASTRO")
print("nome", nome3)
print("sexo:", sexo3)
print("idade:", idade3)
if(idade3<18):
    print("É menor de idade")
else:
    print("É maior de idade")  

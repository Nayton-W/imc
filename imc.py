
def Conteudo():
    
    nome = input('Informe seu nome: ')
    print('=================================================')
    idade= int(input("Informe sua idade: "))
    print('=================================================')
    alt = float(input("Informe sua altura: "))
    print('=================================================')
    peso = float(input("Informe seu peso: "))
    print('=================================================')
    imc= Imc(alt,peso)
    resultado=''


    if(imc<=16.9):
        resultado="Muito Abaixo do peso"
    elif(imc>16.9 and imc<=18.4 ):    
        resultado="Abaixo do peso"
    elif(imc>18.4 and imc<=24.9):    
        resultado="Peso normal"    
    elif(imc>24.9 and imc<= 29.9):  
        resultado="Acima do peso"   
    elif(imc>29.9 and imc<=34.9):    
        resultado="Obesidade grau I"     
    elif(imc>34.9 and imc<=40):    
       resultado="Obesidade grau II" 
    else:  
       resultado="Obesidade grau III"    

  
    print('{} tem : {} anos, seu IMC: {:.2f} !\n           [>> Classificação]:\n     >{}       '.format(nome,idade,imc, resultado))        
    print('=================================================')
def Imc(alt,peso):
    return peso/(alt*alt)

def Opcao():
 while(True):
    Conteudo()
    opcao=input("Deseja continuar: (sim,não)?\n")
    if(opcao=="n"or opcao=="não"):
        break


print("====== IMC ======")
Opcao()

# Pesquisa de Atendimento ao Cliente

# Entrada

print('Bem vindo à pesquisa de satisfação ao cliente!')

excelente = 0
bom = 0 
ruim = 0

for i in range(50):
   nome = input('Qual o seu nome?')
   idade = input('Qual a sua idade?')
   opçao = input("Digite seu grau de satisfação com o atendimento prestado(1 - Excelente, 2 - Bom, 3 - Ruim): ")

   print('A opção digitada foi:', opçao)

   match opçao:
    case '1':
     print('Você selecionou a opção Excelente.')
     excelente += 1
    case '2':
     print('Você selecionou a opção Bom.')
     bom += 1
    case '3':
     print('Você selecionou a opção Ruim.')
     ruim += 1 

   print('Resultado da pesquisa de satisfação ao cliente:') 
   print('Excelente:', excelente)
   print('Ruim:', ruim)

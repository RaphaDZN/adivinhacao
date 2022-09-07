# Jogo da adivinhação
# Actor: Rafael Isaac - 21-05-2022
import random

# Variáveis usadas
# nvl = Nível desejado do jogo
# nmbr = Número a ser adivinhado
# tries = Número de tentativas restantes



tries = 0
nmbr = 0
count = 0

play = 1
while play == 1:
	
	print('**** Bem vindo ao jogo da adivinhação, escolha o nível desejado digitando o número correpondente ****')
	
	nvl = (int(input("\n[1] Fácil: Números entre 1 e 15, 5 tentativas \n[2] Médio: Números entre 1 e 40, 4 tentativas \n"
	                 "[3] Difícil: Números entre -10 e 100, 3 tentativas \n\nNível desejado: ")))
	
	if nvl == 1:
	    print("\n\tNível selecionado: Fácil\n")
	    nmbr = random.randint(1, 15)
	    tries = 5
	
	elif nvl == 2:
	    print("\n\tNível selecionado: Médio\n")
	    nmbr = random.randint(1, 40)
	    tries = 4
	
	elif nvl == 3:
	    print("\n\tNível selecionado: Díficil\n")
	    nmbr = random.randint(-10, 100)
	    tries = 3
	else:
	    exit()
	
	while count < tries:
	    count += 1
	
	
	    x = int(input("Digite um número: "))
	    if x == nmbr:
	        print("Parabéns, você acertou e precisou de ",
	              count, "tentativas")
	        break
	
	    elif x < nmbr:
	        print("Tente um número maior\n")
	    elif x > nmbr:
	        print("Tente um número menor\n")
	
	if count >= tries and x != nmbr:
	    print("\tO número era: ", nmbr)
	    print("\tMais sorte da próxima vez")

	play = int(input("\n\nResponda 1 para jogar novamente e 0 para sair do jogo: "))
	if play == 0:
		print('O jogador decidiu sair')
		exit()
	else: 
		print ('\n')
		play = 1
		
		
		

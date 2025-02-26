'''
Peça ao usuário pra digitar seu nome:
Peça ao usuário pra digitar sua idade:
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é: {nome invertido}
        Seu nome contém ou não espaços
        Seu nome tem X letras
        A primeira letra do seu nome é:
        A última letra do seu nome é:
Se nada for digitado em nome e idade, exiba: "Desculpe, você deixou campos vazios
'''

def linha():
    print()
    print('-'* 40) # função apenas para dividir os conteúdos exibidos no terminal
    print()


nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

# Verificação se ambos os campos de nome e idade forem preenchidos usando o IF / ELSE
if nome and idade: 
    linha()
    print(f'Seu nome é {nome}.')
    linha()
    print(f'Sua idade é {idade} anos.')
    linha()
    print(f'Seu nome invertido é: {nome[::-1]}.') # nome invertido
    linha()

    if ' ' in nome: # verificando se o nome contém ou não espaços
        print(f'Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços')
    linha()

    print(f'Seu nome contém {len(nome)} letras.') # contagem de letras totais 
    linha()
    print(f'A primeira letra do seu nome é {nome[0]}') # primeira letra da string
    linha()
    print(f'A última letra do seu nome é {nome[-1]}') # última letra da string
else:
    print('Desculpe, você deixou campos vazios, informe seu nome e idade para prosseguir..')

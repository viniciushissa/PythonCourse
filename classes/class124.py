def listar(tarefa, lista):
    lista.append(tarefa)
    return lista

def desfazer(lista):
    tarefas_temp.append(lista[-1])
    lista.pop()
    return lista

def refazer(lista):
    lista.append(tarefas_temp[-1])
    tarefas_temp.pop()
    return lista

def print_lista(lista):
    for tarefa in lista:
        print(f'-{tarefa}')
    print()

lista_tarefas = []
tarefas_temp = []

while True:
    opcao = input('Escolha a opção:\n[l]istar [d]esfazer [r]efazer\n: ').lower()
    if opcao == 'l':
        tarefa = input('Digite a tarefa: ')
        listar(tarefa, lista_tarefas)
        print_lista(lista_tarefas)
    elif opcao == 'd':
        if lista_tarefas == []:
            print('Nada para desfazer')
            continue
        desfazer(lista_tarefas)
        print_lista(lista_tarefas)
    elif opcao == 'r':
        if tarefas_temp == []:
            print('Nada para refazer')
            continue
        refazer(lista_tarefas)
        print_lista(lista_tarefas)
    else:
        print('Digite uma opção correta!')
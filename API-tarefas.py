""" Ola, quando rodar o programa, selecione um valor em relação ao menu principal. Quando finalizar a ação,
o menu principal aparecera"""
"""Ocorreu muitas dificuldades devido ao fato de nunca ter programado em python"""


escolha=0;
tarefas=[]
numero=0;

def mostrar_lista():
    for j in tarefas:
        print(j)

while(escolha!=5):
    escolha=int(input("O que deseja fazer: 1-adicionar tarefas, 2-excluir tarefas, 3-mudar status, 4-mostrar lista, 5 sair:  "))
    if(escolha==1):
        tarefa = input("Nome da tarefa: ")
        status = False
        #tarefas.insert (w,y)
        tarefas.append([numero, tarefa, status])
        numero+=1
    elif(escolha==2):
        mostrar_lista()
        p = int(input("Qual tarefa deseja excluir"))
        tarefas.pop(p)
        print("Você exclui a tarefa numero:", p)
    elif(escolha==3):
        mostrar_lista()
        w = int(input("qual tarefa deseja mudar status: "))
        e = int(input("A tarefa foi feita? 1-sim, 2-não"))
        if(e==1):
            tarefas[w][2] =True
        elif(e==2):
            tarefas[w][2] =False
        print("Você mudou o status da tarefa numero: ",w )
    elif(escolha==4):
        mostrar_lista()
    elif(escolha==5):
        break


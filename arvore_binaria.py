# IMPLEMENTAÇÃO DE ÁRVORE BINÁRIA EM PYTHON
# RAFAELA AMORIM PESSIN

################################# MÉTODOS - LEGENDA #################################
''' ---------------------------------------------------------------------------------
def lendoArquivo(arq)           ----->              lê o arquivo texto
def inserir(self, no)           ----->              insere um objeto na árvore
def buscar(self, no)            ----->              busca por um objeto na árvore
def remover(self, no)           ----->              remove um objeto da árvore
def emOrdem(self, no)           ----->              caminha em ordem
def emNivel(self, no)           ----->              caminhar em nível
def altura(self, no)            ----->              obtém a altura da árvore
def quantidadeNos(self, no)     ----->              obtém a quantidade de elementos (nós) da árvore
def maiorValor(self)            ----->              encontra maior elemento da árvore
def menorValor(self)            ----->              encontra menor elemento da árvore
def piorCaso(self, no)          ----->              encontra o elemento mais profundo da árvore
def caminhar(self)              ----->              caminha pela árvore, em nível e depois em ordem
--------------------------------------------------------------------------------- ''' 
#####################################################################################

from queue import Queue
from dis import dis
import os
from pathlib import Path
import pathlib

# A função vai abrir e ler o arquivo e colocar cada linha do arquivo em uma lista com 3 posições (matrícula, nome e nota)
# Ao final, é criada a estrutura de um dicionário com a chave do dicionário sendo a matrícula de cada aluno e o dicionário é retornado na função
def lendoArquivo(arq):
    arquivo = open(arq, encoding="utf-8")
    dictAlunos = {}
    for linha in arquivo:
        line = linha.strip().split(";")
        if len(line) > 1:
            dictAlunos[int(line[0])] = [int(line[0]), line[1], float(line[2])]
    arquivo.close()
    return dictAlunos

# Nó para alocar fila
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Classe fila
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    # a função insere na fila
    def push(self, elem):
        """Insere um elemento na fila"""
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size = self._size + 1

    # a função remove da fila
    def pop(self):
        # Remove o elemento do topo da pilha 
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            if self.first is None:
                self.last = None
            self._size = self._size - 1
            return elem
        raise IndexError("The queue is empty")
    
    # a função retorna o tamanho da lista
    def __len__(self):
        
        return self._size

# Criando a classe nó
class No:
    # self representa a instância da classe, sendo possível acessar os atributos e métodos da classe No
    def __init__(self, entrada, direita, esquerda):
        self.objeto = entrada         # pega a matrícula do dicionário de alunos
        self.dir = direita      # None         
        self.esq = esquerda     # None

# Criando a classe Arvore
class Arvore:

    def __init__(self):
        self.root = No(None, None, None)
        self.root = None

    # Função para inserir um objeto (Nó genérico) na árvore
    def inserir(self, no):

        novoNo = No(no, None, None)     # criando um novo Nó
        if self.root == None:
            self.root = novoNo
        else:       # se o nó não for a raiz da árvore
            noAtual = self.root
            while True:
                noAnterior = noAtual
                if no <= noAtual.objeto:      # ir para esquerda
                        noAtual = noAtual.esq
                        if noAtual == None:
                            noAnterior.esq = novoNo
                            return

                else: # ir para direita
                        noAtual = noAtual.dir
                        if noAtual == None:
                                noAnterior.dir = novoNo
                                return
    
    # Função para buscar por um objeto na árvore
    # Se o elemento estiver na árvore, retorna o próprio elemento, caso contrário, retorna None
    def buscar(self, no):
        # retorna None se a árvore estiver vazia
        if self.root == None:
            return None     
        # a busca inicia na raiz da árvore, onde o noAtual é o primeiro elemento (raiz)
        noAtual = self.root    
        # o loop continua enquanto não encontrar o elemento
        qtd = 0
        while noAtual.objeto[0] != no:
            if no < noAtual.objeto[0]:
                noAtual = noAtual.esq       # caminha para esquerda da árvore
            else:
                noAtual = noAtual.dir       # caminha para direita da árvore
            if noAtual == None:
                return None 
            qtd = qtd + 1
        return noAtual, qtd

    # O noSucessor é o Nó mais a esquerda da subarvore a direita do No passado como parâmetro na função para que seja removido
    def noSucessor(self, apaga): # O parametro é a referencia para o No que deseja-se apagar
        paidosucessor = apaga
        noSucessor = apaga
        noAtual = apaga.dir       # vai para a subarvore a direita

        # o loop continua até chegar no nó mais a esquerda
        while noAtual != None: 
            paidosucessor = noSucessor
            noSucessor = noAtual
            noAtual = noAtual.esq # caminha para a esquerda

        if noSucessor != apaga.dir: # se sucessor nao é o filho a direita do Nó que deverá ser apagado
            paidosucessor.esq = noSucessor.dir # pai herda os filhos do sucessor
            noSucessor.dir = apaga.dir # guarda a referência a direita do sucessor para quando ele assumir a posição correta na árvore
        return noSucessor

    # Função para remover um objeto da árvore
    def remover(self, no):

            # Retorna False se a árvore estiver vazia
            if self.root == None:
                return False 
            
            # noAtual = Referência ao nó que será removido da árvore
            # pai = Referência ao pai do nó que será removido da árvore
            # filhoEsquerda = True se o noAtual é filho a esquerda do pai
            noAtual = self.root
            pai = self.root
            filhoEsquerda = True
            # Procurando o valor na árvore
            while noAtual.objeto[0] != no:
                pai = noAtual
                # vai para esquerda
                if no < noAtual.objeto[0]:     
                    noAtual = noAtual.esq
                    filhoEsquerda = True
                # vai para direita
                else:   
                    noAtual = noAtual.dir 
                    filhoEsquerda = False
                if noAtual == None:
                    return False # encontrou uma folha -> sai

            # Aqui encontrou o valor a ser removido da árvore

            # Se o nó não não tem filhos (é uma folha), elimine-o
            if noAtual.esq == None and noAtual.dir == None:
                if noAtual == self.root:
                    self.root = None        # se raiz
                else:
                    if filhoEsquerda:
                            pai.esq =  None     # filho a esquerda do pai
                    else:
                            pai.dir = None      # filho a direita do pai

            # Se o nó é pai e não possui um filho a direita, substitui pela subárvore a direita
            elif noAtual.dir == None:
                if noAtual == self.root:
                    self.root = noAtual.esq     # raiz
                else:
                    if filhoEsquerda:
                            pai.esq = noAtual.esq       # filho a esquerda do pai
                    else:
                            pai.dir = noAtual.esq       # filho a direita do pai
            
            # Se o nó é pai e não possui um filho a esquerda, substitui pela subárvore a esquerda
            elif noAtual.esq == None:
                if noAtual == self.root:
                    self.root = noAtual.dir     # raiz
                else:
                    if filhoEsquerda:
                            pai.esq = noAtual.dir       # filho a esquerda do pai
                    else:
                            pai.dir = noAtual.dir       # filho a direita do pai

            # Se o nó possui mais de um filho
            else:
                sucessor = self.noSucessor(noAtual)
                if noAtual == self.root:
                    self.root = sucessor        # raiz
                else:
                    if filhoEsquerda:
                            pai.esq = sucessor      # filho a esquerda do pai
                    else:
                            pai.dir = sucessor      # filho a direita do pai
                sucessor.esq = noAtual.esq # acertando o ponteiro a esquerda do sucessor agora que ele assumiu a posição correta na arvore   

            return True

    def emOrdem(self, no):
        arq = open("arqSaida.txt", "w")
        arq.write("teste")
        if no != None:
            self.emOrdem(no.esq)        # visita o filho a esquerda
            print(no.objeto,end=" ")    # nó
            # print(no.objeto[0],";",no.objeto[1],";",no.objeto[2])
            arq.write(str(no.objeto[0])+";"+str(no.objeto[1])+";"+str(no.objeto[2]))
            # arq.write(str(no.objeto[1]))
            # arq.write(str(no.objeto[2]))
            self.emOrdem(no.dir)        # visita o filho a direita
        
    def emNivel(self, no):
        if no != None:
            no = self.root
            fila = Queue()
            fila.push(no)
            while len(fila):
                no = fila.pop()
                if no.esq:
                    fila.push(no.esq)
                if no.dir:
                    fila.push(no.dir)
                # print(no.objeto, end=" ")
        return no.objeto
            
    # a função retorna a altura da árvore
    def altura(self, no):
        if no == None or no.esq == None and no.dir == None:
            return 0
        else:
            if self.altura(no.esq) > self.altura(no.dir):
              return  1 + self.altura(no.esq) 
            else:
                return  1 + self.altura(no.dir) 

    # a função retorna a quantidade de folhas da árvore
    def folhas(self, no):
        if no == None:
            return 0
        if no.esq == None and no.dir == None:
            print(no.objeto)
            return 1
        return self.folhas(no.esq) + self.folhas(no.dir)

    def verificaFolha(self, no): 
        if no.esq == None and no.dir == None:
            print(no.objeto)
            return True
        else:
            return False
    
    # A função retorna o pior caso: elemento mais profundo
    # O pior caso é a travessia de todos os elementos até a folha de nível mais baixo
    def piorCaso(self, no):
        pior =  self.emNivel(self.root)
        return pior

    # a função retorna a quantidade total de nós da [arvore]
    def quantidadeNos(self, no):
        if no == None:
                return 0
        else:
            return  1 + self.quantidadeNos(no.esq) + self.quantidadeNos(no.dir)

    # a função retorna o menor valor da árvore
    def menorValor(self):
        no = self.root
        anterior = None
        while no != None:
            anterior = no
            no = no.esq
        return anterior

    # a função retorna o maior valor da árvore
    def maiorValor(self):
        no = self.root
        anterior = None
        while no != None:
            anterior = no
            no = no.dir
        return anterior

    # a função caminha pela árvore, em nível e depois em ordem
    def caminhar(self):
        print("\nCaminhando em nível\n",end="")
        self.emNivel(self.root)
        print("\n\nCaminhando em ordem\n",end="")
        self.emOrdem(self.root)
        print("\n")
    
    # a função exibe estatísticas: a quantidade total de elementos, a altura da árvore, o maior e o menor elemento e o pior caso de busca
    def exibirEstatisticas(self):
        if self.root != None:       # se arvore nao estiver vazia
            print("Quantidade de nós da árvore: %d" %(self.quantidadeNos(self.root)))
            print("Altura da árvore: %d" %(self.altura(self.root)))
            print("Menor valor da árvore: %d" %(self.menorValor().objeto[0]))
            print("Maior valor da árvore: %d" %(self.maiorValor().objeto[0]))
            pior = self.piorCaso(self.root)
            print("Pior caso: ", pior)
            
    def sair(self):
        self.emOrdem(self.root)
 
# criando a árvore
arvore = Arvore()
# lendo arquivo txt para inserir os elementos na árvore
print("AQUI", pathlib.Path(__file__).parent.absolute()) 
dictAlunos = lendoArquivo("C:/Users/rafae/OneDrive/Área de Trabalho/TPA/alunos.txt")
for no in dictAlunos:
    arvore.inserir(dictAlunos[no])

# caminhando pela árvore
arvore.caminhar()

opcao = 0
while opcao != 6:
    print("\n***********************************\n")
    print("     ESCOLHA A OPÇÃO")
    print(" --- 1: EXIBIR ESTATÍSTICAS")
    print(" --- 2: EFETUAR BUSCA POR MATRÍCULA")
    print(" --- 3: EXCLUIR POR MATRÍCULA")
    print(" --- 4: INCLUIR ALUNO")
    print(" --- 5: SAIR")
    print("\n***********************************\n")
    opcao = int(input("Opção -> "))

    if opcao == 1:
        # EXIBIR ESTATÍSTICAS: -----------> falta o pior caso
        # Exibe a quantidade total de elementos, a altura da árvore, o maior e o menor elemento e o pior caso de busca.
        arvore.exibirEstatisticas()
    elif opcao == 2:
        # EFETUAR BUSCA POR MATRÍCULA -----------> OK
        # Bucando elementos na árvore. O programa solicita a matrícula do aluno, busca o aluno e imprime na tela os dados do aluno (se encontrado) e a quantidade de elementos que foram percorridos até encontrá-lo.  
        matricula = int(input("Matrícula que deseja buscar na árvore: "))
        if arvore.buscar(matricula) != None:
            noAtual, qtd = arvore.buscar(matricula)
            print("Aluno cadastrado.")
            print("Matrícula: ", noAtual.objeto[0], "\nNome: ", noAtual.objeto[1], "\nNota: ", noAtual.objeto[2])
            print("Quantidade nós que foram percorridos até encontrar: ", qtd)
            
        else:
            print("A matrícula não foi encontrada na árvore.")
    
    elif opcao == 3:
        # EXCLUIR POR MATRÍCULA -----------> OK
        # Removendo elementos da árvore. O programa solicita uma matrícula e exclui o aluno, imprimindo na tela os dados do aluno excluído ou uma mensagem falando que não o encontrou.
        matricula = int(input("Matrícula que deseja remover da árvore: "))
        if arvore.remover(matricula) == False:
            print("A matrícula não foi encontrada.")
        else:
            print("\nALUNO EXCLUÍDO\nMatrícula:", dictAlunos[matricula][0], "\nNome: ", dictAlunos[matricula][1], "\nNota:", dictAlunos[matricula][2])
    
    elif opcao == 4:
        # INCLUIR ALUNO:
        # O programa solicita matrícula, nome e nota do aluno e o inclui na árvore. ---> OK
        matricula = int(input("Digite a matrícula do aluno que deseja incluir: "))
        nome = input("Digite o nome do aluno que deseja incluir: ")
        nota = float(input("Digite a nota do aluno que deseja incluir: "))
        if matricula not in dictAlunos:
            dictAlunos[matricula] = [matricula, nome, nota]
            arvore.inserir(dictAlunos[no])
            print("Aluno cadastrado com sucesso.")
        else:
            print("Não é possível inserir esta matrícula pois ela já existe.")

    elif opcao == 5:
        # SAIR
        # O programa deve percorrer a árvore usando caminhamento "em ordem" e gera um arquivo em que cada linha apresenta a matrícula, o nome e a nota de um aluno, sempre separados por ;. 
        arvore.sair()
        break
            
    elif opcao == 6:
        # TERMINA O PROGRAMA ---> OK
        break

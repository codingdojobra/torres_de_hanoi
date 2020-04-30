# http://dojopuzzles.com/problemas/exibe/torres-de-hanoi/

def aplica_padrao(disposicao, padrao_desejado):
    padrao_amarelo = ["A","B","E","A","D","C","A"]
    padrao_azul = ["B","A","C","B","F","E","B"]
    padrao_salmao = ["C","D","F","C","B","A","C"]
    padrao_laranja = ["E","F","D","E","A","B","E"]
    padrao_rosa = ["D","C","A","D","E","F","D"]
    padrao_bege = ["F","E","B","F","C","D","F"]

    if padrao_desejado == "amarelo":
        padrao = padrao_amarelo

    if padrao_desejado == "azul":
        padrao = padrao_azul

    if padrao_desejado == "salmao":
        padrao = padrao_salmao

    if padrao_desejado == "laranja":
        padrao = padrao_laranja

    if padrao_desejado == "rosa":
        padrao = padrao_rosa

    if padrao_desejado == "bege":
        padrao = padrao_bege

    disposicao_calculada = disposicao
    
    for movimento in padrao:
        
        if movimento == "A":
            #print("A")
            disposicao_calculada[2].append(disposicao_calculada[0].pop(-1))
        
        if movimento == "B":
            #print("B")
            disposicao_calculada[1].append(disposicao_calculada[0].pop(-1))
        
        if movimento == "C":
            #print("C")
            disposicao_calculada[2].append(disposicao_calculada[1].pop(-1))
        
        if movimento == "D":
            #print("D")
            disposicao_calculada[0].append(disposicao_calculada[1].pop(-1))
        
        if movimento == "E":
            #print("E")
            disposicao_calculada[1].append(disposicao_calculada[2].pop(-1))
        
        if movimento == "F":
            #print("F")
            disposicao_calculada[0].append(disposicao_calculada[2].pop(-1))
    
    return disposicao_calculada

def aplica_movimento_verde(disposicao):
    movimentou = 0
    
    if movimentou == 0 and len(disposicao[0]) == 0:
        movimentou = 1
        if disposicao[1][-1] > disposicao[2][-1]:
            disposicao[0].append(disposicao[1].pop(-1))
            #print("D")
        else:
            disposicao[0].append(disposicao[2].pop(-1))
            #print("F")

    if movimentou == 0 and len(disposicao[1]) == 0:
        movimentou = 1
        if disposicao[0][-1] > disposicao[2][-1]:
            disposicao[1].append(disposicao[0].pop(-1))
            #print("B")
        else:
            disposicao[1].append(disposicao[2].pop(-1))
            #print("E")

    if movimentou == 0 and len(disposicao[2]) == 0:
        movimentou = 1
        if disposicao[0][-1] > disposicao[1][-1]:
            disposicao[2].append(disposicao[0].pop(-1))
            #print("A")
        else:
            disposicao[2].append(disposicao[1].pop(-1))
            #print("C")
    
    if movimentou == 0 and disposicao[0][-1] > disposicao[1][-1] > disposicao[2][-1]:
        movimentou = 1
        disposicao[0].append(disposicao[1].pop(-1))
        #print("D")
    
    if movimentou == 0 and disposicao[0][-1] > disposicao[2][-1] > disposicao[1][-1]:
        movimentou = 1
        disposicao[0].append(disposicao[2].pop(-1))
        #print("F")
    
    if movimentou == 0 and disposicao[1][-1] > disposicao[2][-1] > disposicao[0][-1]:
        movimentou = 1
        disposicao[1].append(disposicao[2].pop(-1))
        #print("E")
    
    if movimentou == 0 and disposicao[1][-1] > disposicao[0][-1] > disposicao[2][-1]:
        movimentou = 1
        disposicao[1].append(disposicao[0].pop(-1))
        #print("B")
    
    if movimentou == 0 and disposicao[2][-1] > disposicao[1][-1] > disposicao[0][-1]:
        movimentou = 1
        disposicao[2].append(disposicao[1].pop(-1))
        #print("C")
    
    if movimentou == 0 and disposicao[2][-1] > disposicao[0][-1] > disposicao[1][-1]:
        movimentou = 1
        disposicao[2].append(disposicao[0].pop(-1))
        #print("A")
                    
    return disposicao


def encontra_numero_minimo_movimentos(quantidade_discos):
    
    quantidade_movimentos = 0

    sequencia_impar = ["amarelo", "laranja", "rosa"]
    sequencia_par = ["azul", "salmao", "bege"]

    disposicao = [list(reversed(range(1,quantidade_discos + 1))),[],[]]

    if quantidade_discos % 2 == 0:
        sequencia = sequencia_par
    else: 
        sequencia = sequencia_impar

    contador = 0
    while len(disposicao[0]) != 0 or len(disposicao[1]) != 0:
        if contador == 3:
            contador = 0
        disposicao = aplica_padrao(disposicao,sequencia[contador])
        quantidade_movimentos = quantidade_movimentos + 7
        contador = contador + 1

        if len(disposicao[0]) != 0 or len(disposicao[1]) != 0:
            aplica_movimento_verde(disposicao)
            quantidade_movimentos = quantidade_movimentos + 1
    
    return quantidade_movimentos


def testa_tres_discos():
    quantidade_discos = 3
    esperado = 7

    assert esperado == encontra_numero_minimo_movimentos(quantidade_discos)

def testa_quatro_discos():
    quantidade_discos = 4
    esperado = 15

    assert esperado == encontra_numero_minimo_movimentos(quantidade_discos)

def testa_cinco_discos():
    quantidade_discos = 5
    esperado = 31

    assert esperado == encontra_numero_minimo_movimentos(quantidade_discos)

def testa_seis_discos():
    quantidade_discos = 6
    esperado = 63

    assert esperado == encontra_numero_minimo_movimentos(quantidade_discos)

def testa_sete_discos():
    quantidade_discos = 7
    esperado = 127

    assert esperado == encontra_numero_minimo_movimentos(quantidade_discos)

def testa_oito_discos():
    quantidade_discos = 8
    esperado = 255

    assert esperado == encontra_numero_minimo_movimentos(quantidade_discos)

def testa_dez_discos():
    quantidade_discos = 10
    esperado = 1023 #2**10-1

    assert esperado == encontra_numero_minimo_movimentos(quantidade_discos)

def testa_vinte_discos():
    quantidade_discos = 20
    esperado = 1048575 #2**10-1

    assert esperado == encontra_numero_minimo_movimentos(quantidade_discos)

def testa_trinta_discos():
    quantidade_discos = 30
    esperado = 1073741823 #2**10-1

    assert esperado == encontra_numero_minimo_movimentos(quantidade_discos)

def testa_padrao_amarelo():
    disposicao_anterior = [[3,2,1],[],[]]
    disposicao_esperada = [[],[],[3,2,1]]
    padrao = "amarelo"

    disposicao_calculada = aplica_padrao(disposicao_anterior, padrao)

    assert disposicao_esperada == disposicao_calculada

def testa_padrao_azul():
    disposicao_anterior = [[3,2,1],[],[]]
    disposicao_esperada = [[],[3,2,1],[]]
    padrao = "azul"

    disposicao_calculada = aplica_padrao(disposicao_anterior, padrao)

    assert disposicao_esperada == disposicao_calculada

def testa_padrao_salmao():
    disposicao_anterior = [[],[3,2,1],[4]]
    disposicao_esperada = [[],[],[4,3,2,1]]
    padrao = "salmao"

    disposicao_calculada = aplica_padrao(disposicao_anterior, padrao)

    assert disposicao_esperada == disposicao_calculada

def testa_padrao_laranja():
    disposicao_anterior = [[],[4],[3,2,1]]
    disposicao_esperada = [[],[4,3,2,1],[]]
    padrao = "laranja"

    disposicao_calculada = aplica_padrao(disposicao_anterior, padrao)

    assert disposicao_esperada == disposicao_calculada

def testa_padrao_rosa():
    disposicao_anterior = [[],[4,3,2,1],[5]]
    disposicao_esperada = [[3,2,1],[4],[5]]
    padrao = "rosa"

    disposicao_calculada = aplica_padrao(disposicao_anterior, padrao)

    assert disposicao_esperada == disposicao_calculada

def testa_padrao_bege():
    disposicao_anterior = [[],[5],[4,3,2,1]]
    disposicao_esperada = [[3,2,1],[5],[4]]
    padrao = "bege"

    disposicao_calculada = aplica_padrao(disposicao_anterior, padrao)

    assert disposicao_esperada == disposicao_calculada

def testa_movimento_verde_torre_2_vazia():
    disposicao_anterior = [[4],[3,2,1],[]]
    disposicao_esperada = [[],[3,2,1],[4]]

    disposicao_calculada = aplica_movimento_verde(disposicao_anterior)

    assert disposicao_calculada == disposicao_esperada

def testa_movimento_verde_torre_1_vazia():
    disposicao_anterior = [[6,5],[],[4,3,2,1]]
    disposicao_esperada = [[6],[5],[4,3,2,1]]

    disposicao_calculada = aplica_movimento_verde(disposicao_anterior)

    assert disposicao_calculada == disposicao_esperada

def testa_movimento_verde_torre_0_vazia():
    disposicao_anterior = [[],[5,4],[6,3,2,1]]
    disposicao_esperada = [[4],[5],[6,3,2,1]]

    disposicao_calculada = aplica_movimento_verde(disposicao_anterior)

    assert disposicao_calculada == disposicao_esperada

def testa_movimento_verde_sem_torre_vazia():
    disposicao_anterior = [[],[5,4],[6,3,2,1]]
    disposicao_esperada = [[4],[5],[6,3,2,1]]

    disposicao_calculada = aplica_movimento_verde(disposicao_anterior)

    assert disposicao_calculada == disposicao_esperada


testa_tres_discos()
testa_quatro_discos()
testa_cinco_discos()
testa_seis_discos()
testa_sete_discos()
testa_oito_discos()
testa_dez_discos()
testa_vinte_discos()
#     testa_trinta_discos() demora muito
testa_padrao_amarelo()
testa_padrao_azul()
testa_padrao_salmao()
testa_padrao_laranja()
testa_padrao_rosa()
testa_padrao_bege()
testa_movimento_verde_torre_2_vazia()
testa_movimento_verde_torre_1_vazia()
testa_movimento_verde_torre_0_vazia()
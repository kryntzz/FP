
###################################TAD-POSICAO################################

####################AUX###################



def col_to_num(col):

    """
    Devolve o índice correspondente a uma coluna dada (por exemplo, 'a' retorna 1).

    Args:
        col (str): A letra da coluna.

    Returns:
        int: O índice correspondente à coluna fornecida.
    """


    return ord(col)-ord('a')+1



def num_to_col(x_pos):

    """
    Devolve a coluna correspondente a um índice dado (por exemplo, 1 retorna 'a').

    Args:
        x_pos (int): O índice da coluna.

    Returns:
        str: A letra correspondente à coluna associada ao índice fornecido.
    """


    return chr(x_pos+ord('a')-1)



def distancia(pos1,pos2):

    """
    Devolve a distância entre duas posições.

    Args:
        pos1 (posicao): A primeira posição.
        pos2 (posicao): A segunda posição.

    Returns:
        int: A distância entre `pos1` e `pos2`.
    """


    cord1    = (col_to_num(obtem_pos_col(pos1)),obtem_pos_lin(pos1))         #Cordenadas da posicao1
    cord2    = (col_to_num(obtem_pos_col(pos2)),obtem_pos_lin(pos2))         #Cordenadas da posicao2 
         
    return (max(abs(cord1[0]-cord2[0]),abs(cord1[1]-cord2[1])))



def obtem_orbita(pos,n):

    """
    Devolve a órbita à qual a posição pertence, calculando a distância entre a posição e todas as 4 posições centrais,
    e escolhendo o máximo dessas distâncias.

    Args:
        pos (posicao): A posição cuja órbita será determinada.
        n (int): Numero de orbitas do tabuleiro.

    Returns:
        int: A órbita correspondente à posição fornecida.

    """


    return max(distancia(pos,cria_posicao(num_to_col(n),n)),\
        distancia(pos,cria_posicao(num_to_col(n+1),n)),\
        distancia(pos,cria_posicao(num_to_col(n),n+1)),\
        distancia(pos,cria_posicao(num_to_col(n+1),n+1)))



######CONSTRUTOR######



def cria_posicao(col,lin):

    """
    Recebe um caractere e um inteiro correspondentes à coluna ('col') e à linha ('lin') e devolve a posição correspondente.

    Verifica a validade dos argumentos e gera um 'ValueError' se forem inválidos.

    Args:
        col (str): O caractere representando a coluna.
        lin (int): O inteiro representando a linha.

    Returns:
        posicao: A posição correspondente aos argumentos fornecidos.

    Raises:
        ValueError: Se os argumentos não forem válidos.
    """
    

    if type(col) != str or type(lin)!= int or len(col)!=1 or ord(col)<97 or ord(col)>106\
        or lin >10 or lin<1:
        raise ValueError('cria_posicao: argumentos invalidos')

    return (col,lin)



######SELETORES######



def obtem_pos_col(p):

    """
    Obtém a coluna de uma posição.

    Args:
        p (posicao): A posição da qual a coluna será extraída.

    Returns:
        str: A coluna correspondente à posição fornecida.
    """


    return p[0]



def obtem_pos_lin(p):

    """
    Obtém a linha de uma posição.

    Args:
        p (posicao): A posição da qual a linha será extraída.

    Returns:
        int: A linha correspondente à posição fornecida.
    """


    return p[1]



######RECONHECEDOR######



def eh_posicao(arg):

    """
    Verifica se o argumento fornecido é um TAD posição, retornando 'True' se for e 'False' caso contrário, sem gerar erros.

    Args:
        arg (universal): O argumento a ser verificado.

    Returns:
        bool: 'True' se o argumento for um TAD posição, caso contrário, 'False'.
    """


    return isinstance(arg,tuple) and len(arg)==2 and type(obtem_pos_col(arg))==str\
    and len (obtem_pos_col(arg)) ==1 and type(obtem_pos_lin(arg))==int and 0<col_to_num(obtem_pos_col(arg))<=10\
    and 0<obtem_pos_lin(arg)<=10



#########TESTE#########



def posicoes_iguais(p1,p2):

    """
    Verifica se 'p1' e 'p2' são posições iguais.

    Args:
        p1 (universal): Primeira posição a ser comparada.
        p2 (universal): Segunda posição a ser comparada.

    Returns:
        bool: Retorna 'True' se 'p1' e 'p2' são posições e são iguais, caso contrário, 'False'.
    """


    return eh_posicao(p1) and eh_posicao(p2) and obtem_pos_col(p1)==obtem_pos_col(p2)\
    and obtem_pos_lin(p1)==obtem_pos_lin(p2)



######TRANSFORMADOR######



def posicao_para_str(p):

    """
    Converte a posição 'p' em uma string correspondente.

    Args:
        p (posicao): A posição que será convertida em string.

    Returns:
        str: A string correspondente à posição fornecida.
    """


    return obtem_pos_col(p)+str(obtem_pos_lin(p))



def str_para_posicao(s):
    """
    Converte a string 's' em uma posição no tabuleiro.

    Args:
        s (str): String que representa a posição.

    Returns:
        posicao: A posição correspondente à string fornecida.
    """


    return cria_posicao(s[0],int(s[1:]))



######ALTO-NIVEL#######



def eh_posicao_valida(p,n):

    """
    Verifica se a posição 'p' é válida dentro do tabuleiro de Orbito-n.

    Args:
        p (posicao): A posição a ser verificada.
        n (int): Numero de orbitas do tabuleiro.

    Returns:
        bool: 'True' se 'p' é uma posição válida dentro do tabuleiro, caso contrário, 'False'.
    """


    return eh_posicao(p) and n<=5 and n>=2 and type(n) == int and ord(obtem_pos_col(p))>=ord('a') and \
    ord(obtem_pos_col(p))<=ord('a')+(n*2) and obtem_pos_lin(p) <=n*2  and obtem_pos_lin(p)>0  



def obtem_posicoes_adjacentes(p,n,d):

    """
    Obtém as posições adjacentes a uma posição 'p' no tabuleiro de Orbito-n.

    Se 'd' é 'True', retorna as posições adjacentes (em todas as direções); se 'd' é 'False', 
    retorna apenas as posições adjacentes ortogonais. As posições do tuplo são ordenadas 
    em sentido horário, começando pela posição acima de 'p'.

    Args:
        p (posicao): A posição cuja adjacência será verificada.
        n (int): Numero de orbitas do tabuleiro.
        d (bool): Indica o tipo de representação.

    Returns:
        tuple: Um tuplo com as posições adjacentes à posição 'p'.
    """


    res             = ()                                                        #Resultado Final
    x_pos           = col_to_num(obtem_pos_col(p))                              #Abcissa da posição
    y_pos           = obtem_pos_lin(p)                                          #Ordenada da posição
    vetores         = ((0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1))   #Vetores ordenados em sentido horario

    for x,y in vetores:

        if  not (2*n>=x_pos+x>0 and 2*n>=y_pos+y>0):                            #Verificação se pertence ao tabuleiro
            continue

        if x==0 or y==0:                                                        #Posicoes ortogonais
            res     += (cria_posicao(num_to_col(x_pos+x),y_pos+y),)

        else:
            if d:
                res += (cria_posicao(num_to_col(x_pos+x),y_pos+y),)             #Posicoes diagonais
    return res



def ordena_posicoes(tuplo,n):

    """
    Ordena um tuplo de posições de acordo com a ordem de leitura do tabuleiro de Orbito-n.

    Args:
        t (tuple): Um tuplo contendo as posições a serem ordenadas.
        n (int): Numero de orbitas do tabuleiro.

    Returns:
        tuple: Um tuplo de posições ordenadas conforme a ordem de leitura do tabuleiro.
    """


    res            = ()                                                         #Resultado
    tuplo          = sorted(list(tuplo),key=lambda x:(x[1],x[0]))               #Tuplo com as com as linhas e colunas organizadas

    for orbita in range(1,n+1):
        for p in tuplo:
            if obtem_orbita(p,n) == orbita:
                res+=(p,)

    return res



###################################TAD-PEDRA################################

######CONSTRUTOR######



def cria_pedra_branca():
    """
    Cria uma pedra pertencente ao jogador branco.

    Returns:
        pedra: Uma instância de pedra branca.
    """


    return -1



def cria_pedra_preta():

    """
    Cria uma pedra pertencente ao jogador preta.

    Returns:
        pedra: Uma instância de pedra preta.
    """
    

    return 1



def cria_pedra_neutra():

    """
    Cria uma pedra neutra.

    Returns:
        pedra: Uma instância de pedra neutra.
    """


    return 0



######RECONHECEDOR######



def eh_pedra(arg):

    """
    Verifica se o argumento fornecido é um TAD pedra.

    Args:
        arg (universal): O argumento a ser verificado.

    Returns:
        bool: True se o argumento é um TAD pedra, caso contrário, False.
    """


    return any((cria_pedra_preta()==arg,cria_pedra_branca()==arg,cria_pedra_neutra()==arg))



def eh_pedra_branca(p):

    """
    Verifica se a pedra fornecida pertence ao jogador branco.

    Args:
        p (pedra): A pedra a ser verificada.

    Returns:
        bool: True se a pedra p é do jogador branco, caso contrário, False.
    """


    return p==cria_pedra_branca()



def eh_pedra_preta(p):

    """
    Verifica se a pedra fornecida pertence ao jogador preto.

    Args:
        p (pedra): A pedra a ser verificada.

    Returns:
        bool: True se a pedra p é do jogador preto, caso contrário, False.
    """


    return p==cria_pedra_preta()



#########TESTE#########



def pedras_iguais(p1,p2):

    """
    Verifica se duas pedras são iguais.

    Args:
        p1 (universal): A primeira pedra a ser comparada.
        p2 (universal): A segunda pedra a ser comparada.

    Returns:
        bool: True se p1 e p2 são pedras e são iguais, caso contrário, False.
    """


    return p1==p2 if (eh_pedra(p1)and eh_pedra(p2)) else False



######TRANSFORMADOR######




def pedra_para_str(p):

    """
    Converte uma pedra na sua representação em string.

    Args:
        p (pedra): A pedra a ser convertida.

    Returns:
        str: A cadeia de caracteres que representa o jogador da pedra, 
            sendo 'O' para o jogador branco, 'X' para o jogador preto, 
            ou ' ' para pedras neutras.
    """


    if p == cria_pedra_preta():
        return 'X'

    if p == cria_pedra_branca():
        return 'O'

    return ' '



######ALTO-NIVEL#######



def eh_pedra_jogador(p):

    """
    Verifica se a pedra fornecida pertence a um jogador.

    Args:
        p (pedra): A pedra a ser verificada.

    Returns:
        bool: True se a pedra p é de um jogador; caso contrário, False.
    """


    return any((eh_pedra_branca(p),eh_pedra_preta(p)))




def pedra_para_int(p):

    """
    Converte uma pedra em um valor inteiro correspondente.

    Args:
        p (pedra): A pedra a ser convertida.

    Returns:
        int: O valor inteiro correspondente à pedra, onde:
            1 representa uma pedra do jogador preto,
            -1 representa uma pedra do jogador branco,
            0 representa uma pedra neutra.
    """


    if p == cria_pedra_preta():
        return 1

    if p == cria_pedra_branca():
        return -1

    return 0



###################################TAD-TABULEIRO################################

######CONSTRUTOR######



def cria_tabuleiro_vazio(n):

    """
    Cria um tabuleiro vazio para o jogo Orbito.

    Esta função cria um tabuleiro de Orbito com 'n' órbitas, sem posições ocupadas.
    O número de órbitas deve ser especificado pelo argumento 'n'.

    Args:
        n (int): O número de órbitas do tabuleiro.

    Returns:
        tabuleiro: Um tabuleiro vazio, representando a estrutura do jogo, 
        onde cada órbita está vazia.

    Raises:
        ValueError: Se n não estiver entre 2 e 5.
"""


    tab         = []                                                     #Tabuleiro

    if type(n)!=int or not 5>=n>=2:
        raise ValueError('cria_tabuleiro_vazio: argumento invalido')

    for i in range(n*2):
        linha   = [pedra_para_int(cria_pedra_neutra())]*(n*2)            #Linha do tabuleiro
        tab     += [linha]

    return tab



def cria_tabuleiro(n,tp,tb):

    """
    Cria um tabuleiro de Orbito com pedras pretas e brancas.

    Esta função cria um tabuleiro de Orbito com 'n' órbitas. As posições 
    especificadas pelo tuplo 'tp' são ocupadas por pedras pretas, e as posições 
    especificadas pelo tuplo 'tb' são ocupadas por pedras brancas.

    Args:
        n (int): O número de órbitas do tabuleiro..
        tp (tuple): Um tuplo contendo as posições ocupadas por pedras pretas.
        tb (tuple): Um tuplo contendo as posições ocupadas por pedras brancas.

    Returns:
        tabuleiro: Um tabuleiro com 'n' órbitas, com as posições de 'tp' 
        ocupadas por pedras pretas e as posições de 'tb' ocupadas por pedras brancas.

    Raises:
        ValueError: Se 'n', 'tp' ou 'tb' não forem válidos.
    """


    erro    = ValueError('cria_tabuleiro: argumentos invalidos')        #Mensagem de erro

    if not 5>=n>=2:
        raise erro
    
    if type(tp)!=tuple or type(tb)!=tuple:
        raise erro
    
    for p in tp:
        if not eh_posicao_valida(p,n) or p in tb:
            raise erro
        
    for p in tb:
        if not eh_posicao_valida(p,n):
            raise erro
    
    if len(tp)+len(tb)>((n*2)**2):
        raise erro

    #Verificar posicoes duplicadas

    rep     = ()                                            #Tuplo contendo as posicoes de tp
    for pos in tp:
        if pos in rep:
            raise erro
        rep+=(pos,)

    rep     = ()                                            #Tuplo contendo as posicoes de tb

    for pos in tb:
        if pos in rep:
            raise erro
        rep+=(pos,)

    linha   = []                                            #Linha do tabuleiro
    t       = []                                            #Tabuleiro

    for y in range(1,n*2+1):

        for x in range(1,n*2+1):

            if cria_posicao(num_to_col(x),y) in tp:
                linha+=[pedra_para_int(cria_pedra_preta())]

            elif cria_posicao(num_to_col(x),y) in tb:
                linha+=[pedra_para_int(cria_pedra_branca())]

            else:
                linha+=[pedra_para_int(cria_pedra_neutra())]  

        t       += [linha]
        linha   = []

    return t
    


def cria_copia_tabuleiro(t):

    """
    Cria uma cópia de um tabuleiro de Orbito.

    Esta função recebe um tabuleiro e devolve uma cópia desse tabuleiro, 
    preservando a estrutura e o estado do tabuleiro original.

    Args:
        t (tabuleiro): O tabuleiro a ser copiado.

    Returns:
        tabuleiro: Uma cópia do tabuleiro fornecido.
    """


    linha_tab     = []                                          #Linha do novo tabuleiro
    tab_nv        = []                                          #Tabuleiro novo

    for linha in t:

        for valor in linha:
            linha_tab += [valor]
        tab_nv      += [linha_tab]
        linha_tab   = []

    return tab_nv


######SELETORES######


def obtem_numero_orbitas(t):

    """
    Esta função recebe um tabuleiro e devolve o seu número de órbitas.

    Args:
        t (tabuleiro): O tabuleiro.

    Returns:
        int: O número de órbitas do tabuleiro fornecido.
    """


    return len(t)//2
    


def obtem_pedra(t,p):

    """
    Obtém a pedra na posição especifica de um tabuleiro.

    Se a posição não estiver ocupada, a função retorna uma pedra neutra.

    Args:
        t (tabuleiro): O tabuleiro do qual se deseja obter a pedra.
        p (posição): A posição da pedra no tabuleiro.

    Returns:
        pedra: A pedra na posição 'p' do tabuleiro.
    """


    valor_pos = t[obtem_pos_lin(p)-1][col_to_num(obtem_pos_col(p))-1]       #Valor da posicao p

    if valor_pos==pedra_para_int(cria_pedra_branca()):
        return cria_pedra_branca()

    elif valor_pos==pedra_para_int(cria_pedra_preta()):
        return cria_pedra_preta()

    else:
        return cria_pedra_neutra() 



def obtem_linha_horizontal(t,p):

    """
    Obtém a linha horizontal de uma posciao especifica do tabuleiro.
    Ordenadas de esquerda para a direita.

    Args:
        t (tabuleiro): O tabuleiro do qual se deseja obter a linha horizontal.
        p (posição): A posição especifica.

    Returns:
        tuple: Um tuplo contendo tuplos de dois elementos, onde cada tuplo é
        composto pela posição e pelo valor correspondente na linha horizontal do tabuleiro.
    """


    n               = obtem_numero_orbitas(t)                               #Numero de orbitas do tabuleiro
    res             = ()                                                    #Resultado
    linha           = obtem_pos_lin(p)                                      #Linha do tabuleiro

    for col in range(1,n*2+1):

        pos      = cria_posicao(num_to_col(col),linha)
        res     += (((pos),obtem_pedra(t,pos)),)

    return res



def obtem_linha_vertical(t,p):

    """
    Obtém a linha vertical de uma posciao especifica do tabuleiro.
    Ordenadas de esquerda para a direita.

    Args:
        t (tabuleiro): O tabuleiro do qual se deseja obter a linha vertical.
        p (posição): A posição especifica.

    Returns:
        tuple: Um tuplo contendo tuplos de dois elementos, onde cada tuplo é
        composto pela posição e pelo valor correspondente na linha vertical do tabuleiro.
    """


    n                   = obtem_numero_orbitas(t)                               #Numero de orbitas do tabuleiro
    valores_coluna      = ()                                                    #Pedras da coluna
    res                 = ()                                                    #Resultado
    var                 = 0                                                     #Variavel que identifica a coluna atual

    for linha in range(1,n*2+1):
        valores_coluna  += (obtem_pedra(t,cria_posicao(obtem_pos_col(p),linha)),)

    for valor in valores_coluna:
        var             += 1
        res             += (((cria_posicao(obtem_pos_col(p),var)),valor),)

    return res

def obtem_linhas_diagonais(t,p):

    """
    Obtém as linhas diagonais de um tabuleiro na posição especificada.

    Args:
        t (tabuleiro): O tabuleiro do qual se deseja obter as linhas diagonais.
        p (posição): A posição no tabuleiro a partir da qual as diagonais serão obtidas.

    Returns:
        tuple: Um tuplo contendo dois tuplos. O primeiro tuplo representa a diagonal
        descendente e o segundo tuplo representa a antidiagonal, cada um consistindo
        de tuplos de dois elementos (posição, valor).
    """


    n               = obtem_numero_orbitas(t)                                   #Numero de orbitas do tabuleiro
    res_d           = ()                                                        #Resultado da diagonal principal
    res_ad          = ()                                                        #Resultado da antidiagonal
    x_pos           = col_to_num(obtem_pos_col(p))                              #Abcissa da posição
    y_pos           = obtem_pos_lin(p)                                          #Ordenada da posição

    while x_pos !=1 and y_pos!=1:                                               #Uso do vetor (-1,-1)
        x_pos   += -1
        y_pos   += -1

    while x_pos<=n*2 and y_pos<=n*2:                                            #Uso do vetor (1,1)
        pos      = cria_posicao(num_to_col(x_pos),y_pos)
        res_d   += (((pos),obtem_pedra(t,pos)),)
        x_pos   += 1
        y_pos   += 1

    x_pos   = col_to_num(obtem_pos_col(p))                                      #Abcissa da posição
    y_pos   = obtem_pos_lin(p)                                                  #Ordenada da posição

    while x_pos!=1 and y_pos!=n*2:                                              #Uso do vetor (-1,1)
        x_pos   += -1
        y_pos   +=  1

    while x_pos<=n*2 and y_pos>=1:                                              #Uso do vetor (1,-1)
        pos      = cria_posicao(num_to_col(x_pos),y_pos)
        res_ad  += (((pos),obtem_pedra(t,pos)),)
        x_pos   += 1
        y_pos   += -1

    return (res_d,res_ad)



def obtem_posicoes_pedra(t,j):

    """
    Obtém as posições ocupadas por uma determinada pedra em um tabuleiro.

    Args:
        t (tabuleiro): O tabuleiro do qual se deseja obter as posições.
        j (pedra): A pedra cujas posições no tabuleiro devem ser obtidas.

    Returns:
        tuple: Um tuplo contendo todas as posições ocupadas pela pedra 'j' 
        no tabuleiro, ordenadas em ordem de leitura.
    """


    n           = obtem_numero_orbitas(t)                                       #Numero de orbitas do tabuleiro
    res         = ()                                                            #Resultado
    posicoes    = obtem_todas_posicoes(t)                                       #Todas as posicoes do tabuleiro

    for pos in posicoes:

        if obtem_pedra(t,pos) ==j:
            res+=(pos,)

    return ordena_posicoes(res,n)



######MODIFICADORES######



def coloca_pedra(t,p,j):

    """
    Coloca uma pedra em uma posição específica de um tabuleiro.

    Esta função modifica destrutivamente o tabuleiro 't' colocando a pedra 'j' 
    na posição 'p'.

    Args:
        t (tabuleiro): O tabuleiro no qual a pedra será colocada.
        p (posição): A posição no tabuleiro onde a pedra deve ser colocada.
        j (pedra): A pedra que será colocada no tabuleiro.

    Returns:
        tabuleiro: O tabuleiro modificado após a colocação da pedra.
    """


    x       = col_to_num(obtem_pos_col(p))                                      #Abcissa da posição
    y       = obtem_pos_lin(p)                                                  #Ordenada da posição

    t[y-1][x-1] = pedra_para_int(j)

    return t



def remove_pedra(t,p):

    """
    Remove uma pedra de uma posição específica de um tabuleiro.

    Esta função modifica destrutivamente o tabuleiro 't' removendo a pedra 
    da posição 'p'.

    Args:
        t (tabuleiro): O tabuleiro do qual a pedra será removida.
        p (posição): A posição no tabuleiro de onde a pedra deve ser removida.

    Returns:
        tabuleiro: O tabuleiro modificado após a remoção da pedra.
    """


    x       = col_to_num(obtem_pos_col(p))                                      #Abcissa da posição
    y       = obtem_pos_lin(p)                                                  #Ordenada da posição

    t[y-1][x-1] = pedra_para_int(cria_pedra_neutra())

    return t



######RECONHECEDOR######



def eh_tabuleiro(arg):

    """
    Esta função verifica se o argumento 'arg' é um representa TAD tabuleiro. 

    Args:
        arg (universal): O argumento a ser verificado.

    Returns:
        bool: True se 'arg' é um tabuleiro, caso contrário, False.
    """


    if type(arg)!=type(cria_tabuleiro_vazio(2)) or not 4<=len(arg)<=10:
        return False
    
    for l in arg:
        if type(l)!= list or not len(arg)==len(l):
            return False
        
        for valor_col in l:
            if type(valor_col)!=type(pedra_para_int(cria_pedra_branca())) or valor_col not in \
            (pedra_para_int(cria_pedra_branca()),pedra_para_int(cria_pedra_preta()),pedra_para_int(cria_pedra_neutra())):
                return False

    return True


#########TESTE#########



def tabuleiros_iguais(t1,t2):

    """
    Verifica se dois tabuleiros são iguais.

    Args:
        t1 (universal): O primeiro tabuleiro a ser comparado.
        t2 (universal): O segundo tabuleiro a ser comparado.

    Returns:
        bool: True se 't1' e 't2' são tabuleiros, e são iguais, caso contrário, False.
    """


    return t1==t2 if (eh_tabuleiro(t1)and eh_tabuleiro(t2)) else False



######TRANSFORMADOR######



def tabuleiro_para_str(t):

    """
    Converte um tabuleiro em uma representação de string.

    Args:
        t (tabuleiro): O tabuleiro a ser convertido em string.

    Returns:
        str: Cadeia de caracteres que representa o tabuleiro 
            't', formatada de acordo com os exemplos fornecidos.
    """


    res     = '    a'                                                                               # variavel com o resultado do print
    a       = 0                                                                                     # variavel auxiliar (incremento)
    n       = obtem_numero_orbitas(t)                                                               # numero de orbitas

    for col in range(2,(n*2)+1):
        res +=f'   {num_to_col(col)}'
    res     += '\n'

    for linha in range(1,(2*n)+1):
        a   += 1
        valor_p=obtem_pedra(t,cria_posicao('a',linha))

        if linha !=10:
            res +=(f'0{linha} '+f'[{pedra_para_str(valor_p)}]')

        else:
            res +=(f'{linha} '+f'[{pedra_para_str(valor_p)}]')

        for valor in range(2,n*2+1):
            res += f'-[{pedra_para_str(obtem_pedra(t,cria_posicao(num_to_col(valor),linha)))}]'

        if a != 2*n:
            res += '\n'+ '    |   ' +'|   '*((n*2)-2) +'|\n'

    return res


#############################AUX#####################################



def obtem_todas_posicoes(t):

    """
    Obtém todas as posições do tabuleiro e coloca-as num tuplo.

    Args:
        t (tabuleiro): O tabuleiro do qual as posições serão obtidas.

    Returns:
        tuple: Um tuplo contendo todas as posições do tabuleiro.
    """


    res     = ()                                                        #Resultado
    n       = obtem_numero_orbitas(t)                                   #Numero de orbitas do tabuleiro

    for y in range(1,n*2+1):

        for x in range(1,n*2+1):

            res+=(cria_posicao(num_to_col(x),y),)

    return res



def obtem_posicoes_livres(t):

    """
    Obtém todas as posições livres no tabuleiro.

    Args:
        t (tabuleiro): O tabuleiro do qual as posições livres serão obtidas.

    Returns:
        tuple: Um tuplo contendo todas as posições livres no tabuleiro.
    """


    res         = ()                                                    #Resultado
    posicoes    = obtem_todas_posicoes(t)                               #Todas as posicoes do tabuleiro

    for pos in posicoes:

        if obtem_pedra(t,pos) == cria_pedra_neutra():
            res+=(pos,)

    return res



######ALTO-NIVEL######



def move_pedra(t,p1,p2):

    """
    Move uma pedra de uma posição para outra em um tabuleiro.

    Esta função modifica destrutivamente o tabuleiro 't', movendo a pedra 
    da posição 'p1' para a posição 'p2'.

    Args:
        t (tabuleiro): O tabuleiro no qual a pedra será movida.
        p1 (posição): A posição de onde a pedra será movida.
        p2 (posição): A posição para onde a pedra será movida.

    Returns:
        tabuleiro: O tabuleiro modificado após o movimento da pedra.
    """

    j   = obtem_pedra(t,p1)                                             #Pedra da posicao1

    remove_pedra(t,p1)
    coloca_pedra(t,p2,j) 

    return t



def obtem_posicao_seguinte(t,p,s):

    """
    Obtém a posição seguinte em um tabuleiro a partir de uma posição especificada.

    Args:
        t (tabuleiro): O tabuleiro no qual a posição deve ser obtida.
        p (posição): A posição a partir da qual se deseja obter a próxima posição.
        s (bool): Indica a direção do movimento. True para horário e False para anti-horário.

    Returns:
        posicao: A posição seguinte na mesma órbita de 'p', na direção especificada.
    """


    n           = obtem_numero_orbitas(t)                               #Numero de orbitas do tabuleiro
    orbita      = obtem_orbita(p,n)                                     #Orbita da posicao p
    res         = ()                                                    #Resultado
    x           = col_to_num(obtem_pos_col(p))                          #Abcissa da posição
    y           = obtem_pos_lin(p)                                      #Ordenada da posição

    for pos in obtem_posicoes_adjacentes(p,n,False):                    #Obtem as duas posicoes ortogonais na mesma orbita
        if obtem_orbita(pos,n) == orbita:
            res+=(pos,)

    if s:

        if x==((n-orbita)+1) or y==(n-orbita)+1:                        #((n-orbita)+1) = primeira linha/coluna da orbita
            return res[0]

        else:
            return res[1]

    if not s:

        if x==((n-orbita)+1) or y==(n-orbita)+1:
            return res[1]

        else:
            return res[0]



def roda_tabuleiro(t):

    """
    Roda todas as pedras do tabuleiro uma posição em sentido anti-horário.

    Esta função modifica destrutivamente o tabuleiro 't'.

    Args:
        t (tabuleiro): O tabuleiro a ser rodado.

    Returns:
        tabuleiro: O tabuleiro modificado após a rotação das pedras.
    """


    tab = cria_copia_tabuleiro(t)                                       #Copia do tabuleiro(somente para verificar as posições)

    for pos in obtem_todas_posicoes(t): 

        pos_seguinte    = obtem_posicao_seguinte(t, pos, False)         #Posicao seguinte
        pedra           = obtem_pedra(tab, pos)                         #Pedra a colocar na posicao seguinte
        coloca_pedra(t, pos_seguinte, pedra)  

    return t



def verifica_linha_pedras(t,p,j,k):

    """
    Verifica se existe uma linha com k ou mais pedras consecutivas de um jogador.

    Args:
        t (tabuleiro): O tabuleiro a ser verificado.
        p (posição): A posição no tabuleiro a partir da qual a verificação é realizada.
        j (pedra): A pedra do jogador.
        k (int): O de pedras consecutivas a serem verificadas.

    Returns:
        bool: True se existe uma linha com k ou mais pedras consecutivas de 'j', 
        caso contrário, False.
    """


    tab     = (obtem_linha_horizontal(t,p),obtem_linha_vertical(t,p),obtem_linhas_diagonais(t,p)[0],obtem_linhas_diagonais(t,p)[1])
    seq     = 0

    for direcao in tab:
        pos_p=False

        for pos in direcao:
            if posicoes_iguais(pos[0],p):               #Quando passa na posição pos_r = True
                pos_p    = True

            if pedras_iguais((pos[1]),(j)):
                seq     += 1

            else:
                seq      = 0

            if seq >= k and pos_p:
                return True

            if seq == 0 and pos_p:
                break
        seq   = 0

    return False


########################################################################################################



def eh_vencedor(t,j):

    """
    Verifica se um jogador é o vencedor em um tabuleiro.

    Args:
        t (tabuleiro): O tabuleiro a ser verificado.
        j (pedra): A pedra do jogador.

    Returns:
        bool: True se o jogador é o vencedor, caso contrário, False.
    """


    n   = obtem_numero_orbitas(t)                           #Numero de orbitas do tabuleiro  

    for pos in obtem_posicoes_pedra(t,j):

        if verifica_linha_pedras(t,pos,j,n*2):
            return True

    return False



def eh_fim_jogo(t):

    """
    Verifica se o jogo terminou em um tabuleiro.

    Args:
        t (tabuleiro): O tabuleiro a ser verificado.

    Returns:
        bool: True se o jogo terminou, caso contrário, False.
    """


    posicoes                = obtem_todas_posicoes(t)                       #Todas as posições do tabuleiro
    posicoes_livres         = obtem_posicoes_livres(t)                      #Todas as posições livres do tabuleiro
    k                       = obtem_numero_orbitas(t)*2                     #Numero de pedras seguidas necessario para ganhar o jogo

    if len(posicoes_livres)==0:
        return True

    for pos in posicoes:

        if pos not in posicoes_livres:
            j   = obtem_pedra(t,pos)

            if verifica_linha_pedras(t,pos,j,k):
                return True

    return False



def escolhe_movimento_manual(t):

    """
    Permite ao jogador escolher uma posição livre em um tabuleiro.

    A função não modifica o tabuleiro  e devolve a posição escolhida. 
    Mensagens são apresentadas ao jogador e repetidas até 
    que uma jogada válida seja introduzida.

    Args:
        t (tabuleiro): O tabuleiro onde o jogador escolherá uma posição livre.

    Returns:
        posicao: A posição escolhida pelo jogador.
    """


    n = obtem_numero_orbitas(t)
    posicoes_livres     = obtem_posicoes_livres(t)                                      #Todas as posições do tabuleiro
    letras_possiveis    = ''                                                            #Colunas possiveis

    for a in range(1, n * 2 + 1):

        letras_possiveis += num_to_col(a)

    res = "" 
    while not (res and res[0] in letras_possiveis and res[1:].isdigit() and \
               int(res[1:]) in range(1, 11) and \
               eh_posicao_valida(str_para_posicao(res), n) and \
               str_para_posicao(res) in posicoes_livres):
        
        res = input('Escolha uma posicao livre:') 

        if not res:                                                                     #Previne EOF
            continue 

    return str_para_posicao(res)



def escolhe_movimento_auto(t,j,lvl):

    """
    Escolhe automaticamente uma posição em um tabuleiro baseado em uma estratégia.

    A função não modifica nenhum dos seus argumentos. 

    As estratégias devem ser identificadas pelas cadeias de caracteres 'facil' ou 'normal'.

    Args:
        t (tabuleiro): O tabuleiro onde a jogada será realizada.
        j (pedra): A pedra do jogador.
        lvl (str): A estratégia de movimento.

    Returns:
        posicao: A posição escolhida automaticamente com base na estratégia.
"""


    if eh_fim_jogo(t):
        return 0

    if lvl =='facil':
        return modo_facil(t,j)
        
    if lvl =='normal':
        return modo_normal(t,j)



############################AUX######################



def modo_facil(t,j):

    """
    Estratégia fácil do escolhe_movimento_auto.

    Esta função implementa a estratégia de jogo fácil.

    Args:
        t (tabuleiro): O tabuleiro onde a jogada será realizada.
        j (pedra): A pedra do jogador.

    Returns:
        posicao: A posição escolhida automaticamente com base na estratégia fácil.
    """



    res         = ()                                                        #Resultado
    n           = obtem_numero_orbitas(t)                                   #Numero de orbitas do tabuleiro
    tab_roda    = roda_tabuleiro(cria_copia_tabuleiro(t))                   #Tabuleiro depois de rodar
    pos_livres  = obtem_posicoes_livres(tab_roda)                           #Posicoes livres do tabuleiro após rodar

    for pos in obtem_posicoes_pedra(tab_roda,j):

        for pos_adj in obtem_posicoes_adjacentes(pos,n,True):

            if pos_adj in pos_livres:
                res+=(obtem_posicao_seguinte(t,pos_adj,True),)

    if len(res)==0:
        return ordena_posicoes(pos_livres,n)[0]

    return ordena_posicoes(res,n)[0]

def modo_normal(t,j):

    """
    Estratégia normal do escolhe_movimento_auto.

    Esta função implementa a estratégia de jogo normal.

    Args:
        t (tabuleiro): O tabuleiro onde a jogada será realizada.
        j (pedra): A pedra do jogador.

    Returns:
        posicao: A posição escolhida automaticamente com base na estratégia normal.
    """


    if eh_pedra_branca(j):
        j_op    = cria_pedra_preta()                                        #Pedra do oponente

    else:
        j_op    = cria_pedra_branca()                                       #Pedra do oponente

    res         = ()                                                        #Resultado
    k           = obtem_numero_orbitas(t)*2                                 #Numero de pedras seguidas necessario para ganhar o jogo
    L           = k                                                         #Variavel L que vai reduzindo
    n           = obtem_numero_orbitas(t)                                   #Numero de orbitas do tabuleiro
    tab_roda    = roda_tabuleiro(cria_copia_tabuleiro(t))                   #Tabuleiro após rodar uma vez
    tab_roda2   = roda_tabuleiro(cria_copia_tabuleiro(tab_roda))            #Tabuleiro após rodar duas vezes

    
    while L !=0:

        res     = ()
        for pos_livre in obtem_posicoes_livres(tab_roda):

            tab_nv      = cria_copia_tabuleiro(tab_roda)
            coloca_pedra(tab_nv,pos_livre,j)

            if verifica_linha_pedras(tab_nv,pos_livre,j,L):
                res     += (obtem_posicao_seguinte(t,pos_livre,True),)

        if len(res)!=0:
            return ordena_posicoes(res,n)[0]

        res =()

        for pos_livre in obtem_posicoes_livres(tab_roda2):

            tab_nv      = cria_copia_tabuleiro(tab_roda2)
            coloca_pedra(tab_nv,pos_livre,j_op)

            if verifica_linha_pedras(tab_nv,pos_livre,j_op,L) :
                res    += (obtem_posicao_seguinte(t,obtem_posicao_seguinte(t,pos_livre,True),True),)

        if len(res)!=0:
            return ordena_posicoes(res,n)[0]

        L-=1

    return ()



######################################################################



def orbito(n,modo,jg):

    """
    Joga uma partida completa do jogo Orbiton.

    Esta função principal permite jogar um jogo completo de Orbito-n. 

    O jogo começa sempre com o jogador com pedras pretas e desenvolve-se
    até ao fim.

    Args:
        n (int): O número de órbitas do tabuleiro (mínimo 2, máximo 5).
        modo (str): O modo de jogo ('facil', 'normal' ou '2jogadores').
        jog (str): Pedra do jogador (preta ou branca).

    Returns:
        int: Identificador do jogador vencedor (1 para preto, -1 para branco, 0 para empate).

    Raises:
        ValueError: Se os argumentos fornecidos forem inválidos.
        Com a mensagem 'orbito: argumentos invalidos'.
    """


    jg_possiveis    =('X','O')                                                  #Jogadores possiveis
    erro            = ValueError('orbito: argumentos invalidos')                #Mensagem de erro
    modos           =('facil','2jogadores','normal')                            #Modos de jogo possiveis
    if type(n)!=int:
        raise erro

    if not 5>=n>=2:
        raise erro

    if modo not in modos:
        raise erro

    if jg not in jg_possiveis:
        raise erro

    t = cria_tabuleiro_vazio(n)
    if jg=='X':
        jogador     =cria_pedra_preta()
        computador  =cria_pedra_branca()
    else:
        jogador     =cria_pedra_branca()
        computador  =cria_pedra_preta()

    if modo =='facil' or modo=='normal': 
        print(f'Bem-vindo ao ORBITO-{n}.')
        print(f'Jogo contra o computador ({modo}).')
        print(f"O jogador joga com '{jg}'.")
        print(tabuleiro_para_str(t))

        if jogador ==cria_pedra_preta():

            while not eh_fim_jogo(t):
                print('Turno do jogador.')
                pos     = escolhe_movimento_manual(t)
                coloca_pedra(t,pos,jogador)
                roda_tabuleiro(t)
                print(tabuleiro_para_str(t))

                if eh_fim_jogo(t):
                    break

                print(f'Turno do computador ({modo}):')
                pos_comp    = escolhe_movimento_auto(t,computador,modo)
                coloca_pedra(t,pos_comp,computador)
                roda_tabuleiro(t)
                print(tabuleiro_para_str(t))

            if eh_vencedor(t,jogador) and eh_vencedor(t,computador):
                print('EMPATE')
                return pedra_para_int(cria_pedra_neutra())
            
            elif eh_vencedor(t,jogador):
                print('VITORIA')
                return pedra_para_int(jogador)
            
            elif eh_vencedor(t,computador):
                print('DERROTA')
                return pedra_para_int(computador)
            
            else:
                print('EMPATE')
                return pedra_para_int(cria_pedra_neutra())
        else:

            while not eh_fim_jogo(t):

                print(f'Turno do computador ({modo}):')
                pos_comp    = escolhe_movimento_auto(t,computador,modo)
                coloca_pedra(t,pos_comp,computador)
                roda_tabuleiro(t)
                print(tabuleiro_para_str(t))

                if eh_fim_jogo(t):
                    break

                print('Turno do jogador.')
                pos     = escolhe_movimento_manual(t)
                coloca_pedra(t,pos,jogador)
                roda_tabuleiro(t)
                print(tabuleiro_para_str(t))

            if eh_vencedor(t,jogador) and eh_vencedor(t,computador):
                print('EMPATE')
                return pedra_para_int(cria_pedra_neutra())
            
            elif eh_vencedor(t,jogador):
                print('VITORIA')
                return pedra_para_int(jogador)
            
            elif eh_vencedor(t,computador):
                print('DERROTA')
                return pedra_para_int(computador)
            
            else:
                print('EMPATE')
                return pedra_para_int(cria_pedra_neutra())

    print(f'Bem-vindo ao ORBITO-{n}.')
    print('Jogo para dois jogadores.')
    print(tabuleiro_para_str(t))

    while not eh_fim_jogo(t):

        print("Turno do jogador 'X'.")
        pos     = escolhe_movimento_manual(t)
        coloca_pedra(t,pos,cria_pedra_preta())
        roda_tabuleiro(t)
        print(tabuleiro_para_str(t))

        if eh_fim_jogo(t):
            break

        print("Turno do jogador 'O'.")
        pos     = escolhe_movimento_manual(t)
        coloca_pedra(t,pos,cria_pedra_branca())
        roda_tabuleiro(t)
        print(tabuleiro_para_str(t))

    if eh_vencedor(t,jogador) and eh_vencedor(t,computador):
        print('EMPATE')
        return pedra_para_int(cria_pedra_neutra())

    if eh_vencedor(t,cria_pedra_preta()):
        print ("VITORIA DO JOGADOR 'X'")
        return pedra_para_int(cria_pedra_preta())
        
    if eh_vencedor(t,cria_pedra_branca()):
        print("VITORIA DO JOGADOR 'O'")
        return pedra_para_int(cria_pedra_branca())
    else:
        print('EMPATE')
        return pedra_para_int(cria_pedra_neutra())


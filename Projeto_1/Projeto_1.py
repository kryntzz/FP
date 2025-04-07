
#Funções auxiliares
def linha(tab,pos):
    """
    Devolve a linha onde se encontra a pos

    linha:tab,pos-->int
    """
    return (pos-1)//(len(tab[0]))
def coluna(tab,pos):
    """
    Devolve o indice da coluna de pos

    coluna:tab,pos-->int
    """
    return (pos-1)%(len(tab[0]))
def eh_jogador_valido(jg):
    """
    Devolve Verdadeiro se o argumento for um jogador
    e falso caso contrario

    eh_jogador_valido:int-->boolean
    """
    return type(jg)==int and jg in (1,-1)
def eh_k(tab,k):
    """
    Devolve Verdadeiro se o argumento 
    k for valido em tab

    eh_k:tab,k -->boolean
    """ 
    return isinstance(k,int)and k>0 and k<100
def all_pos(tab):
    """
    Devolve o numero de posicoes de
    um tabuleiro

    all_pos:universal-->int
    """
    return len(tab)*len(tab[0])
def distancia(tab,pos1,pos2):
    """
    Devolve a distância entre dois 
    pontos no tabuleiro

    distancia:tab,pos1,pos2 -->int 
    """

    cord1 = (linha(tab,pos1),coluna(tab,pos1))
    cord2 = (linha(tab,pos2),coluna(tab,pos2))
    return (max(abs(cord1[0]-cord2[0]),abs(cord1[1]-cord2[1]))) 
def coluna_pos(tab,pos):
    """
    Devolve a coluna em que pos
    se encontra no tabuleiro (tab)

    coluna_pos:tab,pos -->int
    """
    c = pos%len(tab[0])
    if c==0:c=len(tab[0])
    return c
def modo_normal_aux(tab,jg,k):
    """
    Retorna, caso existam, as posicoes candidatas á
    jogada em modo normal do jg

    modo_normal_aux:tab,int,int -->tuple
    """
    L,tab_nv,res_jg,res_op=k,tab,(),()
    while L !=0:
        for i in obtem_posicoes_livres(tab):
            tab_nv=marca_posicao_aux(tab,i,jg)
            if verifica_k_linhas_aux(tab_nv,i,jg,L):
                res_jg+=(i,)
            tab_nv=tab
            tab_nv=marca_posicao_aux(tab,i,-jg)
            if verifica_k_linhas_aux(tab_nv,i,-jg,L):
                res_op+=(i,)
            tab_nv=tab
        if len(res_jg)!=0:
            return (ordena_posicoes_tabuleiro_aux(tab,res_jg)[0],)
        elif len(res_jg)==0 and len(res_op)!=0:
            return (ordena_posicoes_tabuleiro_aux(tab,res_op)[0],)
        L-=1
    return ()

#2.1.1
def eh_tabuleiro(tab):
    """
    Devolve True se o argumento corresponde a
    um tabuleiro e False caso contrario

    eh_tabuleiro:universal -->boolean    
    """
    n_base = (1,0,-1)
    if type(tab)!=tuple or not(2<=len(tab)<=100):
        return False
    for i in tab:
        if type(i)!=tuple or not (2<=len(i)<=100):
            return False
        for j in i:
            if j not in n_base or type(j)!=int:
                return False
    for i in range(len(tab)-1):
        if len(tab[i])!=len(tab[i+1]):
            return False
    return True

#2.1.2
def eh_posicao(pos):
    """
    Devolve True se pos for uma posição valida
    e False caso contrario

    eh_posicao:universal --> boolean
    """
    return type(pos)==int and 10000>pos>0

#2.1.3
def obtem_dimensao(tab):
    """
    Se tab for um tabuleiro, devolve
    as dimensões do tabuleiro(mxn)

    obtem_dimensao:tab -->tuple
    """

    if eh_tabuleiro(tab):
        return (len(tab),len(tab[0]))

#2.1.4
def obtem_valor(tab,pos):
    """
    Recebe um tabuleiro e uma posiçãoao do tabuleiro, 
    e devolve o valor contido nessa posição

    obtem_valor:tab,pos -->int     
    """
    colunas = len(tab[0])
    if eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab,pos):
        return tab[linha(tab,pos)][coluna(tab,pos)] 

#2.1.5
def obtem_coluna(tab, pos):
    """
    Recebe um tabuleiro e uma posiçãoao do tabuleiro,
    e devolve um tuplo com todas as posições que formam
    a coluna em que esta contida a posição, ordenadas
    de menor a maior.

    obtem_coluna:tab,pos -->tuple
    """
    
    res,c,x=(),len(tab[0]),0
    coluna = coluna_pos(tab,pos)
    if eh_posicao(pos)and eh_tabuleiro(tab) and eh_posicao_valida(tab,pos): 
        while x !=len(tab):
            res+=(coluna+x*c,)
            x+=1
        return res

#2.1.6
def obtem_linha(tab, pos):
    """
    Recebe um tabuleiro e uma posição do tabuleiro, e devolve um tuplo
    com todas as posições que formam a linha em que esta contida a posição,
    ordenadas de menor a maior.

    obtem_linha:tab,pos -->tuple
    """

    res,i,c =(),0,len(tab[0])
    tup = linha(tab,pos) 
    if eh_posicao(pos)and eh_tabuleiro(tab) and eh_posicao_valida(tab,pos):
        while i != (len(tab[0])):
            res+= (c*tup+i+1,)
            i+=1
        return res

#2.1.7
def obtem_diagonais(tab,pos):
    """
    Recebe um tabuleiro e uma posição do tabuleiro, e devolve o
    tuplo formado por dois tuplos de posições correspondentes à diagonal (descendente da
    esquerda para a direita) e antidiagonal (ascendente da esquerda para a direita) que
    passam pela posição, respetivamente.

    obtem_diagonais:tab,pos -->tuple
    """

    if eh_posicao(pos)and eh_tabuleiro(tab):
        c,colunas,l = coluna(tab,pos),len(tab[0]),linha(tab,pos)
        d,i,ad =(),0,()
        while l-i>=0 and c -i>=0 :
            d = ((l-i)*colunas+c-i+1,) +d
            i+=1
        i=1
        while l+i<len(tab) and c+i<colunas and pos%len(tab[0])!=0:
            d +=((l+i)*colunas+c+i+1,)
            i+=1
        i =0
        while l+i<len(tab) and c-i>=0:
            ad =((l+i)*colunas+c-i+1,)+ad
            i+=1
        i=1
        while l-i>=0 and c+i<colunas  and pos%len(tab[0])!=0:
            ad += ((l-i)*colunas+c+i+1,)
            i+=1
        return (d ,ad)     

#2.1.8
def tabuleiro_para_str(tab):
    """
    Recebe um tabuleiro e devolve a cadeia de caracteres que o representa
    (a representação externa ou representação “para os nossos olhos”)

    tabuleiro_para_str:tab -->str(cadeia de carateres)
    """
    res,c='',0
    if  not eh_tabuleiro(tab):
        return  
    for i in tab:
        res += '+' if i[0] == 0 else 'X' if i[0] == 1 else 'O'
        c+=1
        for j in range(len(tab[0])-1):
            res += '---+' if i[j + 1] == 0 else '---X' if i[j + 1] == 1 else '---O'
            c+=1
        if c != (len(tab)*len(tab[0])):
            res += '\n' + '|   ' * (len(tab[0])-1) +'|'+'\n'          
    return res

#2.2.1
def eh_posicao_valida(tab,pos):
    """
    Recebe um tabuleiro e uma posição, e devolve True se a
    posição corresponde a uma posição do tabuleiro, e False
    caso contrário. Se algum dos argumentos dados for inválido,
    a função deve gerar um erro com a mensagem
    'eh_posicao_valida: argumentos invalidos'.

    eh_posicao_valida:tab,pos -->boolean
    """
    if eh_posicao(pos)and eh_tabuleiro(tab):
        return pos <=len(tab[0])*len(tab)
    raise ValueError('eh_posicao_valida: argumentos invalidos')

#2.2.2
def eh_posicao_livre(tab, pos):
    """
    Recebe um tabuleiro e uma posição do tabuleiro, e devolve True
    se a posição corresponde a uma posição livre (não ocupada por pedras), e False caso
    contrário. Se algum dos argumentos dado for inválido, a função deve gerar um erro com
    a mensagem 'eh_posicao_livre: argumentos invalidos'.

    eh_posicao_livre:tab,pos -->boolean
    """

    if not(eh_posicao(pos)and eh_tabuleiro(tab) and eh_posicao_valida(tab,pos)):
        raise ValueError('eh_posicao_livre: argumentos invalidos')
    return obtem_valor(tab,pos)==0

#2.2.3
def obtem_posicoes_livres(tab):
    """
    Recebe um tabuleiro e devolve o tuplo com todas as posições
    livres do tabuleiro, ordenadas de menor a maior. Se o argumento dado for inválido, a
    função deve gerar um erro com a mensagem 'obtem_posicoes_livres: argumento invalido'.

    obtem_posicoes_livres:tab -->tuple
    """
    if not eh_tabuleiro(tab):
        raise ValueError('obtem_posicoes_livres: argumento invalido')
    res = ()
    for i in range(1,all_pos(tab)+1):
        if obtem_valor(tab,i)==0:
            res+=(i,)
    return res

#2.2.4
def obtem_posicoes_jogador(tab,jg):
    """
    Recebe um tabuleiro e um inteiro identificando um jogador e
    devolve o tuplo com todas as posições do tabuleiro ocupadas por pedras do jogador,
    ordenadas de menor a maior. 
    Se algum dos argumentos dados for inválidos, a função deve
    gerar um erro com a mensagem 'obtem_posicoes_jogador: argumentos invalidos'.

    obtem_posicoes_jogador:tab,int -->tuple
    """
    res = ()
    if not (eh_tabuleiro(tab) and eh_jogador_valido(jg)):
        raise ValueError('obtem_posicoes_jogador: argumentos invalidos')
    for i in range(1,len(tab[0])*len(tab)+1):
        if obtem_valor(tab,i)==jg:
            res+=(i,)
    return res

#2.2.5
def obtem_posicoes_adjacentes(tab,pos):
    """
    Recebe um tabuleiro e uma posição do tabuleiro, e
    devolve o tuplo formado pelas posições do tabuleiro adjacentes (horizontal, vertical e
    diagonal), ordenadas de menor a maior.
    Se algum dos argumentos dado for inválido, a função deve gerar um erro com a mensagem 
    'obtem_posicoes_adjacentes: argumentos invalidos'.

    obtem_posicoes_adjacentes:tab,pos -->tuple
    """
    if  not (eh_tabuleiro(tab) and eh_posicao(pos)and eh_posicao_valida(tab,pos)):
        raise ValueError('obtem_posicoes_adjacentes: argumentos invalidos')
    res,pos_c,coluna,linha,diagonais= (),0,obtem_coluna(tab,pos),obtem_linha(tab,pos),obtem_diagonais(tab,pos)
    colunas,linhas = range(len(coluna)),range(len(linha))
    for i in colunas:
        if coluna[i]==pos:
            if i-1 in colunas:res+=(coluna[i-1],)
            if i+1 in colunas:res+=(coluna[i+1],)
    for j in linhas:
        if linha[j]==pos:
            if j-1 in linhas:res+=(linha[j-1],)
            if j+1 in linhas:res+=(linha[j+1],)
    for d in diagonais:
        for i in range(len(d)):
            if d[i]==pos:
                if i-1 in range(len(d)):res+=(d[i-1],)
                if i+1 in range(len(d)):res+=(d[i+1],)
    return tuple(sorted(res))

#2.2.6
def ordena_posicoes_tabuleiro(tab,tup):
    """
    Recebe um tabuleiro e um tuplo de posições do tabuleiro (potencialmente vazio),
    e devolve o tuplo com as posições em ordem ascendente de
    distância à posição central do tabuleiro. Posições com igual distância à posição central,
    são ordenadas de menor a maior de acordo com a posição que ocupam no tabuleiro. Se
    algum dos argumentos dado for inválido, a função deve gerar um erro com a mensagem
    'ordena_posicoes_tabuleiro: argumentos invalidos'.

    ordena_posicoes_tabuleiro:tab,tuple -->tuple
    """
    if not (eh_tabuleiro(tab) and type(tup)==tuple):
        raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')
    for i in tup:
        if type(i)!=int or not eh_posicao(i) or not eh_posicao_valida(tab,i):
            raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')
    pos=((len(tab))//2)*len(tab[0])+(len(tab[0])//2)+1
    res,d=(),0
    if len(tup)==1:
        return (tup[0],)
    while d<=distancia(tab,pos,1):
        for pos_t in tup:
            if distancia(tab,pos_t,pos)==d:
                res+=(pos_t,)
        d+=1
    return res 

def ordena_posicoes_tabuleiro_aux(tab,tup):
    """
    Recebe um tabuleiro e um tuplo de posições do tabuleiro (potencialmente vazio),
    e devolve o tuplo com as posições em ordem ascendente de
    distância à posição central do tabuleiro. Posições com igual distância à posição central,
    são ordenadas de menor a maior de acordo com a posição que ocupam no tabuleiro.
    
    ordena_posicoes_tabuleiro:tab,tuple -->tuple
    """
    pos=((len(tab))//2)*len(tab[0])+(len(tab[0])//2)+1
    res,d=(),0
    tup = sorted(tup)
    if len(tup)==1:
        return (tup[0],)
    while d<=distancia(tab,pos,1):
        for pos_t in tup:
            if distancia(tab,pos_t,pos)==d:
                res+=(pos_t,)
        d+=1
    return res   
#2.2.7
def marca_posicao(tab,pos,jg):
    """
    Recebe um tabuleiro, uma posição livre do tabuleiro e um
    inteiro identificando um jogador, e devolve um novo tabuleiro com uma nova pedra do
    jogador indicado nessa posição. Se algum dos argumentos dados for inválidos, a função
    deve gerar um erro com a mensagem 'marca_posicao: argumentos invalidos'.

    marca_posicao:tab,pos,int -->tab
    """
    if not(eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab,pos)\
        and eh_jogador_valido(jg) and eh_posicao_livre(tab,pos)):
        raise ValueError('marca_posicao: argumentos invalidos')
    tab_f,res,l,c=(),(),linha(tab,pos),coluna(tab,pos)
    for i in range(len(tab[0])):
        if i==c:
            res+=(jg,)
        else:
            res+=(tab[l][i],)
    return tab[:l] + (res,)+tab[l+1:]

def marca_posicao_aux(tab,pos,jg):
    """
    Recebe um tabuleiro, uma posição livre do tabuleiro e um
    inteiro identificando um jogador, e devolve um novo tabuleiro com uma nova pedra do
    jogador indicado nessa posição.

    marca_posicao:tab,pos,int -->tab
    """
    tab_f,res,l,c=(),(),linha(tab,pos),coluna(tab,pos)
    for i in range(len(tab[0])):
        if i==c:
            res+=(jg,)
        else:
            res+=(tab[l][i],)
    return tab[:l] + (res,)+tab[l+1:]

#2.2.8
def verifica_k_linhas(tab,pos,jg,k):
    """
    Recebe um tabuleiro, uma posição do tabuleiro, um
    valor inteiro identificando um jogador , e um valor inteiro positivo k,
    e devolve True se existe pelo menos uma linha (horizontal, vertical ou diagonal)
    que contenha a posição com k ou mais pedras consecutivas do jogador indicado,
    e False caso contrário. Se algum dos argumentos dado for inválido, a função 
    deve gerar um erro com a mensagem 'verifica_k_linhas: argumentos invalidos'.

    verifica_k_linhas:tab,pos,int,int -->boolean
    """
    if not(eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab,pos)\
        and eh_jogador_valido(jg)and eh_k(tab,k)):
        raise ValueError('verifica_k_linhas: argumentos invalidos')
    if not pos in obtem_posicoes_jogador(tab,jg):
        return False
    t,c =(obtem_linha(tab,pos),obtem_coluna(tab,pos),obtem_diagonais(tab,pos)[0],obtem_diagonais(tab,pos)[1]),0
    for i in t:
        pos_r=False
        for valor in i:
            if valor==pos:
                pos_r = True
            if obtem_valor(tab,valor) == jg:
                c+=1
            else:
                c=0
            if c == k and pos_r:
                return True
            if c == 0 and pos_r:
                break
        c=0
    return False

def verifica_k_linhas_aux(tab,pos,jg,k):
    """
    Recebe um tabuleiro, uma posição do tabuleiro, um
    valor inteiro identificando um jogador , e um valor inteiro positivo k,
    e devolve True se existe pelo menos uma linha (horizontal, vertical ou diagonal)
    que contenha a posição com k ou mais pedras consecutivas do jogador indicado,
    e False caso contrário.

    verifica_k_linhas:tab,pos,int,int -->boolean 
    """
    t,c =(obtem_linha(tab,pos),obtem_coluna(tab,pos),obtem_diagonais(tab,pos)[0],obtem_diagonais(tab,pos)[1]),0
    for i in t:
        pos_r=False
        for valor in i:
            if valor==pos:
                pos_r = True
            if obtem_valor(tab,valor) == jg:
                c+=1
            else:
                c=0
            if c == k and pos_r:
                return True
            if c == 0 and pos_r:
                break
        c=0
    return False

#2.3.1
def eh_fim_jogo(tab,k):
    """
    Recebe um tabuleiro e um valor inteiro positivo k, e devolve um
    booleano a indicar se o jogo terminou (True) ou não (False). Um jogo pode terminar
    caso um dos jogadores tenha k pedras consecutivas, ou caso já não existam mais posições
    livres para marcar. Se algum dos argumentos dado for inválido, a função deve gerar um
    erro com a mensagem 'eh_fim_jogo: argumentos invalidos'.

    eh_fim_jogo:tab,int -->boolean
    """
    if not(eh_tabuleiro(tab) and eh_k(tab,k)):
        raise ValueError('eh_fim_jogo: argumentos invalidos')
    if len(obtem_posicoes_livres(tab))==0:
        return True
    for i in obtem_posicoes_jogador(tab,1):
        if verifica_k_linhas_aux(tab,i,1,k):
            return True
    for i in obtem_posicoes_jogador(tab,-1):
        if verifica_k_linhas_aux(tab,i,-1,k):
            return True
    return False

#2.3.2
def escolhe_posicao_manual(tab):
    """
    Recebe um tabuleiro e devolve uma posição introduzida manualmente pelo jogador.
    A função deve apresentar a mensagem do exemplo a seguir, repetindo a mensagem até
    o jogador introduzir uma posição livre. Se o argumento dado for
    inválido, a função deve gerar um erro com a mensagem 
    'escolhe_posicao_manual: argumento invalido'.
    
    escolhe_posicao_manual:tab -->pos
    """

    if not eh_tabuleiro(tab):
        raise ValueError('escolhe_posicao_manual: argumento invalido')
    res= input('Turno do jogador. Escolha uma posicao livre: ')
    while not res.isdigit() or 0>=int(res) or int(res)> all_pos(tab) or not eh_posicao_livre(tab,int(res)):
        res= input('Turno do jogador. Escolha uma posicao livre: ')
    res = int(res)
    return res

#2.3.3
def escolhe_posicao_auto(tab,jg,k,lvl):
    """
    Recebe um tabuleiro (em que o jogo não terminou
    ainda), um inteiro identificando um jogador, um inteiro positivo correspondendo ao valor k dum
    jogo m, n, k, e a cadeia de carateres correspondente à estratégia, e devolve a posição
    escolhida automaticamente de acordo com a estratégia selecionada.
    Sempre que houver mais do que uma posição que cumpra um dos critérios definidos nas estratégias
    anteriores, deve escolher a posição mais próxima da posição central do tabuleiro. 
    Se algum dos argumentos dados for inválidos, a função deve gerar um erro com a mensagem
    'escolhe_posicao_auto: argumentos invalidos'.

    escolhe_posicao_auto:tab,int,int,str -->pos
    """
    modos_jg=('facil','normal','dificil')
    if not(eh_tabuleiro(tab) and eh_k(tab,k) and eh_jogador_valido(jg) and lvl in modos_jg) or eh_fim_jogo(tab,k):
        raise ValueError('escolhe_posicao_auto: argumentos invalidos')
    if lvl =='facil':
        return modo_facil(tab,jg)
    if lvl =='normal':
        return modo_normal(tab,jg,k)
    if lvl =='dificil':
        return modo_dificil(tab,jg,k)
    
def modo_facil(tab,jg):
    """
    Função auxiliar da função "escolhe_posicao_auto", que devolve o valor
    da posição a ser utilizado na estrategia facil

    modo_facil:tab,int -->pos
    """
    res=()
    for i in obtem_posicoes_jogador(tab,jg):
        for j in obtem_posicoes_adjacentes(tab,i):
            if j in obtem_posicoes_livres(tab):
                res+=(j,)
    if len(res)==0:
        return ordena_posicoes_tabuleiro_aux(tab,obtem_posicoes_livres(tab))[0]
    else:
        return ordena_posicoes_tabuleiro_aux(tab,res)[0]

def modo_normal(tab,jg,k):
    """
    Função auxiliar da função "escolhe_posicao_auto", que devolve o valor
    da posição a ser utilizado na estrategia normal

    modo_normal:tab,int,int -->pos
 
    """
    Res_T = modo_normal_aux(tab,jg,k)
    if len(Res_T)==0:
        return ordena_posicoes_tabuleiro_aux(tab,obtem_posicoes_livres(tab))[0]
    else:
        return Res_T[0]

def vencedor(tab,k,jg):
    """
    Devolve True se o jg for vencedor de um jogo e False caso contrario

    vencedor:tab,int,int -->boolean
    """
    for i in obtem_posicoes_jogador(tab,jg):
        if verifica_k_linhas_aux(tab,i,jg,k):
            return True
    return False

def modo_dificil_aux(tab,jg,k):
    """
    Função auxiliar da função "modo_dificil", que devolve,
    se houver uma posição em que o jogador complete k linhas, ou que o oponente
    complete k linhas

    modo_dificil_aux:tab,int,int-->tuple
    """
    tab_nv,res_jg,jg_o,res_op=tab,(),jg,()
    for i in obtem_posicoes_livres(tab):
        tab_nv=marca_posicao_aux(tab,i,jg_o)
        if verifica_k_linhas_aux(tab_nv,i,jg_o,k):
            res_jg+=(i,)
        tab_nv =marca_posicao_aux(tab,i,-jg_o)
        if verifica_k_linhas_aux(tab_nv,i,-jg_o,k):
            res_op+=(i,)
        tab_nv=tab
    if len(res_jg)!=0:
        return ordena_posicoes_tabuleiro_aux(tab,res_jg)
    elif len(res_op)!=0:
        return ordena_posicoes_tabuleiro_aux(tab,res_op)
    else:
        return ()

def modo_dificil(tab,jg,k):
    """
    Função auxiliar da função "escolhe_posicao_auto" que devolve
    um posicao segundo a estratedia de jogo 'dificil'

    modo_dificil:tab,int,int -->pos
    """
    jg_o,jg_vdd=jg,jg
    res = modo_dificil_aux(tab,jg,k)
    if len(res)>0:
        return res[0]
    else:
        res,res_e,res_op=(),(),()
        for i in ordena_posicoes_tabuleiro(tab,obtem_posicoes_livres(tab)):
            tab_nv=marca_posicao_aux(tab,i,jg_vdd)
            jg_o=jg_vdd
            while not eh_fim_jogo(tab_nv,k):
                jg_o*=-1
                posicao_nova=modo_normal(tab_nv,jg_o,k)
                tab_nv=marca_posicao_aux(tab_nv,modo_normal(tab_nv,jg_o,k,),jg_o)
                if verifica_k_linhas_aux(tab_nv,posicao_nova,jg_o,k):
                    if jg_o == jg_vdd:
                        return i
                    else:
                        res_op +=(i,)
            if i not in res_op:
                res_e+=(i,)
    if len(res)!=0:
        return ordena_posicoes_tabuleiro_aux(tab,res)[0]
    elif len(res_e)!=0:                 
        return ordena_posicoes_tabuleiro_aux(tab,res_e)[0]
    else:
        return ordena_posicoes_tabuleiro_aux(tab,obtem_posicoes_livres(tab))[0]

def jogo_mnk(mnk,jg,lvl):
    """
    Função principal que permite jogar um jogo completo m, n, k
    de um jogador contra o computador. A função recebe um tuplo de três valores inteiros
    correspondentes aos valores de configuração do jogo m, n e k; um inteiro identificando
    a cor das pedras do jogador humano e uma cadeia de caracteres identificando a estratégia de jogo utilizada pela
    máquina. O jogo começa sempre com o jogador com pedras pretas a marcar uma posição
    livre e termina quando um dos jogadores vence ou se não existirem posições livres no
    tabuleiro. A função mostra o resultado do jogo (VITORIA, DERROTA ou EMPATE) e devolve
    um inteiro identificando o jogador vencedor (1 para preto ou -1 para branco), ou 0 em
    caso de empate. A função deve verificar a validade dos seus argumentos, gerando um
    erro com a mensagem 'jogo_mnk: argumentos invalidos'.

    jogo_mnk:tuple,int,str -->int
    """

    if type(mnk)!=tuple or len(mnk)!=3:
        raise ValueError('jogo_mnk: argumentos invalidos')
    for i in mnk:
        if type(i)!=int:
            raise ValueError('jogo_mnk: argumentos invalidos')
    tab,modos_jogo=(),('facil','normal','dificil')
    for a in range(mnk[1]):
        tab+=(0,)
    tab=(tab,)*mnk[0]
    k,jg_o,jg_vdd=mnk[2],jg,jg
    if not (eh_tabuleiro(tab) and eh_jogador_valido(jg)and lvl in modos_jogo and eh_k(tab,k)):
        raise ValueError('jogo_mnk: argumentos invalidos')
    if jg==1:jogador='X'
    else:jogador='O'
    print('Bem-vindo ao JOGO MNK.')
    print(f"O jogador joga com '{jogador}'.")
    print(tabuleiro_para_str(tab))
    if jg ==1:
        while not eh_fim_jogo(tab,k):
            pos = escolhe_posicao_manual(tab)
            tab =marca_posicao_aux(tab,pos,jg)
            print(tabuleiro_para_str(tab))
            if eh_fim_jogo(tab,k):
                break
            print(f'Turno do computador ({lvl}):')
            pos_c=escolhe_posicao_auto(tab,-jg,k,lvl)
            tab=marca_posicao_aux(tab,pos_c,-jg)
            print(tabuleiro_para_str(tab))
        if vencedor(tab,k,jg):
            print('VITORIA')
            return jg
        elif vencedor(tab,k,-jg):
            print('DERROTA')
            return -jg
        else:
            print('EMPATE')
            return 0
    else:
        while not eh_fim_jogo(tab,k):
            print(f'Turno do computador ({lvl}):')
            pos_c=escolhe_posicao_auto(tab,-jg,k,lvl)
            tab=marca_posicao(tab,pos_c,-jg)
            print(tabuleiro_para_str(tab))
            if eh_fim_jogo(tab,k):
                break
            pos = escolhe_posicao_manual(tab)
            tab =marca_posicao(tab,pos,jg)
            print(tabuleiro_para_str(tab))
        if vencedor(tab,k,jg_o):
            print('VITORIA')
            return jg_vdd
        elif vencedor(tab,k,-jg_o):
            print('DERROTA')
            return -jg_vdd
        else:
            print('EMPATE')
            return 0
jogo_mnk((3,3,3),-1,'dificil')
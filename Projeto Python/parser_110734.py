# -*- coding: utf-8 -*-
"""
Created on Sat May 24 12:35:45 2025

@author: Thyago
"""
#----------------------------- GRAMATICA -----------------------------
# endpoints -> endpoint | endpoints endpoint
# endpoint -> API_CONST ENDPOINT_CUSTOM METODO MUDA_LINHA descricao parametros headers resposta
# descricao -> DESCRICAO_CONST TEXTO_CUSTOM MUDA_LINHA | DESCRICAO_CONST TEXTO_CUSTOM
# parametros -> PARAMETROS_CONST MUDA_LINHA parametro_list | PARAMETROS parametro_list | $
# parametro_list -> parametro | parametro_list parametro
# parametro -> VARIAVEIS_CUSTOM DOIS_PONTOS_CONST TIPO_VARIAVEL MUDA_LINHA | VARIAVEIS_CUSTOM DOIS_PONTOS_CONST TIPO_VARIAVEL
# headers -> HEADERS_CONST MUDA_LINHA header_list | HEADERS header_list | $
# header_list -> header | header_list header
# header -> VARIAVEIS_CUSTOM DOIS_PONTOS_CONST TIPO_VARIAVEL MUDA_LINHA | VARIAVEIS_CUSTOM DOIS_PONTOS_CONST TIPO_VARIAVEL
# resposta -> RESPOSTA_CONST MUDA_LINHA resposta_list | RESPOSTA_CONST resposta_list
# resposta_list -> resposta_item | resposta_list resposta_item
# resposta_item -> STATUS_CODE : TEXTO_CUSTOM MUDA_LINHA | STATUS_CODE : TEXTO_CUSTOM


from lexer_110734 import inicializar_lexer
from classe_output_110734 import criar_arquivo_default
import sys

meu_lexer = None
lookahead = None

def inicializar_parser_generic(entrada_texto_ou_arquivo, eh_arquivo):
    global meu_lexer
    global lookahead

    if eh_arquivo:
        with open(entrada_texto_ou_arquivo, encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
    else:
        conteudo = entrada_texto_ou_arquivo

    meu_lexer = inicializar_lexer(conteudo)

    lookahead = meu_lexer.token()  # Inicializando o lookAhead

    # Início do parser
    return endpoints()


def inicializar_parser_arquivo(arquivo):
    try:
        open(arquivo, 'r+')
    except FileNotFoundError:
        criar_arquivo_default(arquivo)

    return inicializar_parser_generic(arquivo, True)


def inicializar_parser_texto(texto):
    return inicializar_parser_generic(texto, False)


def match(esperado):
    global lookahead
    if lookahead is not None and esperado == lookahead.type:
        lookahead = meu_lexer.token() # continua o processo.
        return
    
    print('Erro sintático na linha', lookahead.lineno, 'Esperado', esperado, 'lido', lookahead)
    sys.exit(1)
    

# endpoint -> API_CONST ENDPOINT_CUSTOM METODO MUDA_LINHA descricao parametros headers resposta
def endpoint():
    global lookahead

    match('API_CONST')
    _end_point = lookahead.value
    match('ENDPOINT_CUSTOM')
    _metodo = lookahead.value
    match('METODO_CUSTOM')
    if lookahead is not None and lookahead.type == 'MUDA_LINHA':
        match('MUDA_LINHA')
    _desc = descricao()
    _params = parametros()
    _headers = headers()
    _resp = resposta()
    return {
        'end_point': _end_point,
        'metodo': _metodo,
        'descricao': _desc,
        'parametros': _params,
        'headers': _headers,
        'respostas': _resp
    }


# descricao -> DESCRICAO_CONST TEXTO_CUSTOM MUDA_LINHA | DESCRICAO_CONST TEXTO_CUSTOM
def descricao():
    global lookahead

    match('DESCRICAO_CONST')
    texto = lookahead.value
    match('TEXTO_CUSTOM')
    if lookahead is not None and lookahead.type == 'MUDA_LINHA':
        match('MUDA_LINHA')
    return texto


# parametros -> PARAMETROS_CONST MUDA_LINHA parametro_list | PARAMETROS parametro_list | $
def parametros():
    global lookahead

    if lookahead.type == 'PARAMETROS_CONST':
        match('PARAMETROS_CONST')
        if lookahead is not None and lookahead.type == 'MUDA_LINHA':
            match('MUDA_LINHA')
        return parametro_list()
    return ''


# parametro_list -> parametro | parametro_list parametro
def parametro_list():
    global lookahead

    lista = [parametro()]
    while lookahead is not None and lookahead.type == 'VARIAVEIS_CUSTOM':
        lista.append(parametro())
    return lista


# parametro -> VARIAVEIS_CUSTOM DOIS_PONTOS_CONST TIPO_VARIAVEL MUDA_LINHA | VARIAVEIS_CUSTOM DOIS_PONTOS_CONST TIPO_VARIAVEL
def parametro():
    global lookahead

    nome = lookahead.value
    match('VARIAVEIS_CUSTOM')
    match('DOIS_PONTOS_CONST')
    tipo = lookahead.value
    match('TIPO_VARIAVEL')
    if lookahead is not None and lookahead.type == 'MUDA_LINHA':
        match('MUDA_LINHA')
    return nome, tipo


# headers -> HEADERS_CONST MUDA_LINHA header_list | HEADERS header_list | $
def headers():
    global lookahead

    if lookahead.type == 'HEADERS_CONST':
        match('HEADERS_CONST')
        if lookahead is not None and lookahead.type == 'MUDA_LINHA':
            match('MUDA_LINHA')
        return header_list()
    return ''


# header_list -> header | header_list header
def header_list():
    global lookahead

    lista = [header()]
    while lookahead is not None and lookahead.type == 'VARIAVEIS_CUSTOM':
        lista.append(header())
    return lista


# header -> VARIAVEIS_CUSTOM DOIS_PONTOS_CONST TIPO_VARIAVEL MUDA_LINHA | VARIAVEIS_CUSTOM DOIS_PONTOS_CONST TIPO_VARIAVEL
def header():
    global lookahead

    nome = lookahead.value
    match('VARIAVEIS_CUSTOM')
    match('DOIS_PONTOS_CONST')
    tipo = lookahead.value
    match('TIPO_VARIAVEL')
    if lookahead is not None and lookahead.type == 'MUDA_LINHA':
        match('MUDA_LINHA')
    return nome, tipo


# resposta -> RESPOSTA_CONST MUDA_LINHA resposta_list | RESPOSTA_CONST resposta_list
def resposta():
    global lookahead

    match('RESPOSTA_CONST')
    if lookahead is not None and lookahead.type == 'MUDA_LINHA':
        match('MUDA_LINHA')
    return resposta_list()


# resposta_list -> resposta_item | resposta_list resposta_item
def resposta_list():
    global lookahead

    lista = [resposta_item()]
    while lookahead is not None and lookahead.type == 'STATUS_CODE':
        lista.append(resposta_item())
    return lista


# resposta_item -> STATUS_CODE DOIS_PONTOS_CONST TEXTO_CUSTOM MUDA_LINHA | STATUS_CODE DOIS_PONTOS_CONST TEXTO_CUSTOM
def resposta_item():
    global lookahead

    numero = lookahead.value
    match('STATUS_CODE')
    match('DOIS_PONTOS_CONST')
    texto = lookahead.value
    match('TEXTO_CUSTOM')
    if lookahead is not None and lookahead.type == 'MUDA_LINHA':
        match('MUDA_LINHA')
    return numero, texto


# endpoints -> endpoint | endpoints endpoint
def endpoints():
    global lookahead
    lista_endpoints = []

    while lookahead is not None:
        lista_endpoints.append(endpoint())

    return lista_endpoints

















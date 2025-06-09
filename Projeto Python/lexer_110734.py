# -*- coding: utf-8 -*-
"""
Created on Sat May 24 12:26:35 2025

@author: Thyago
"""

from lex import lex
import sys

tokens = ('API_CONST', 'ENDPOINT_CUSTOM', 'METODO_CUSTOM', 'DESCRICAO_CONST', 'TEXTO_CUSTOM', 'PARAMETROS_CONST',
          'HEADERS_CONST', 'VARIAVEIS_CUSTOM', 'DOIS_PONTOS_CONST', 'TIPO_VARIAVEL', 'RESPOSTA_CONST', 'STATUS_CODE')

t_API_CONST = 'API|api'
t_RESPOSTA_CONST = 'resposta|RESPOSTA'
t_TIPO_VARIAVEL = 'string|STRING|integer|INTEGER|float|FLOAT|date|DATE|boolean|BOOLEAN'
t_METODO_CUSTOM = 'GET|get|POST|post|PUT|put|DELETE|delete'
t_DESCRICAO_CONST = 'descricao|DESCRICAO'
t_PARAMETROS_CONST = 'parametros|PARAMETROS'
t_HEADERS_CONST = 'headers|HEADERS'
t_DOIS_PONTOS_CONST = ':'
t_STATUS_CODE = '[0-9][0-9][0-9]'
# t_VARIAVEIS_CUSTOM = '[a-zA-Z_][a-zA-Z0-9_]*'
# t_ENDPOINT_CUSTOM = '[a-zA-Z0-9_][a-zA-Z0-9_]*\/*'
# t_TEXTO_CUSTOM = '"[^"\n]*"'


def t_TEXTO_CUSTOM(t):
    '"[^"\n]*"'

    if str(t.value).upper() == 'RESPOSTA':
        t.type = 'RESPOSTA_CONST'
    elif str(t.value).upper() in ['STRING', 'INTEGER', 'FLOAT', 'DATE', 'BOOLEAN']:
        t.type = 'TIPO_VARIAVEL'
    elif str(t.value).upper() in ['GET', 'POST', 'PUT', 'DELETE']:
        t.type = 'METODO_CUSTOM'
    elif str(t.value).upper() == 'DESCRICAO':
        t.type = 'DESCRICAO_CONST'
    elif str(t.value).upper() == 'PARAMETROS':
        t.type = 'PARAMETROS_CONST'
    elif str(t.value).upper() == 'HEADERS':
        t.type = 'HEADERS_CONST'
    elif str(t.value).upper() == 'API':
        t.type = 'API_CONST'
    return t


def t_ENDPOINT_CUSTOM(t):
    '/[a-zA-Z0-9_\-\/\{\}]*'

    if str(t.value).upper() == 'RESPOSTA':
        t.type = 'RESPOSTA_CONST'
    elif str(t.value).upper() in ['STRING', 'INTEGER', 'FLOAT', 'DATE', 'BOOLEAN']:
        t.type = 'TIPO_VARIAVEL'
    elif str(t.value).upper() in ['GET', 'POST', 'PUT', 'DELETE']:
        t.type = 'METODO_CUSTOM'
    elif str(t.value).upper() == 'DESCRICAO':
        t.type = 'DESCRICAO_CONST'
    elif str(t.value).upper() == 'PARAMETROS':
        t.type = 'PARAMETROS_CONST'
    elif str(t.value).upper() == 'HEADERS':
        t.type = 'HEADERS_CONST'
    elif str(t.value).upper() == 'API':
        t.type = 'API_CONST'
    return t


def t_VARIAVEIS_CUSTOM(t):
    '[a-zA-Z_][a-zA-Z0-9_]*'

    if str(t.value).upper() == 'RESPOSTA':
        t.type = 'RESPOSTA_CONST'
    elif str(t.value).upper() in ['STRING','INTEGER', 'FLOAT', 'DATE', 'BOOLEAN']:
        t.type = 'TIPO_VARIAVEL'
    elif str(t.value).upper() in ['GET', 'POST', 'PUT', 'DELETE']:
        t.type = 'METODO_CUSTOM'
    elif str(t.value).upper() == 'DESCRICAO':
        t.type = 'DESCRICAO_CONST'
    elif str(t.value).upper() == 'PARAMETROS':
        t.type = 'PARAMETROS_CONST'
    elif str(t.value).upper() == 'HEADERS':
        t.type = 'HEADERS_CONST'
    elif str(t.value).upper() == 'API':
        t.type = 'API_CONST'
    return t

t_ignore = ' \t'


def t_error(t):
    print(t, "não foi reconhecido!")
    sys.exit(1)


def t_MUDA_LINHA(t):
    r"\n"
    t.lexer.lineno += 1


def inicializar_lexer(conteudo):
    l1 = lex()
    l1.input(conteudo)
    return l1
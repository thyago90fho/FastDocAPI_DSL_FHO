# -*- coding: utf-8 -*-
"""
Created on Sat May 24 13:29:35 2025

@author: Thyago
"""

import json
import yaml

def criar_arquivo_default(arquivo):
    with open(arquivo, 'w+', encoding="utf-8") as arquivo:
        arquivo.write('''
        api /usuarios GET
        descricao "Retorna lista de usuários"
        headers
          token: String
        resposta
          200: "1 OK"
          400: "1 Erro de parâmetros"
          500: "1 Erro no servidor"
        
        api /usuarios/{id} GET
        descricao "Retorna dados do usuário"
        headers
          token: String
        resposta
          200: "2 OK"
          400: "2 Erro de parâmetros"
          500: "2 Erro no servidor"
        
        api /usuarios POST
        descricao "Inserir um usuário"
        parametros
          nome: string
          idade: integer
        headers
          token: String
        resposta
          200: "3 OK"
          400: "3 Erro de parametros"
          500: "3 Erro no servidor"
        
        api /usuarios/{id} PUT
        descricao "Editar um usuário"
        parametros
          nome: string
          idade: integer
        headers
          token: String
        resposta
          200: "4 OK"
          400: "4 Erro de parametros"
          500: "4 Erro no servidor"
        
        api /usuarios/{id} DELETE
        descricao "Apagar um usuário"
        headers
          token: String
        resposta
          200: "5 OK"
          400: "5 Erro de parametros"
          500: "5 Erro no servidor"
        ''')


def gerar_documentacao_html_layout1(endpoints):
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Documentação da API - Thyago Noventa RA: 110734</title>
      <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
      <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        .endpoint {
            max-width: 800px;
            margin: 20px auto;
            border: 1px solid #ccc;
            border-left: 8px solid;
            padding: 10px 15px;
            margin-bottom: 15px;
            border-radius: 5px;
        }
        .GET { border-color: #61affe; background-color: #f0f8ff; }
        .POST { border-color: #49cc90; background-color: #f3fff5; }
        .PUT { border-color: #fca130; background-color: #fffaf0; }
        .DELETE { border-color: #f93e3e; background-color: #fff5f5; }
        .title {
            font-weight: bold;
            font-size: 18px;
        }
        .desc {
            font-size: 14px;
            color: #333;
            margin: 5px 0 10px;
        }
        .section {
            font-weight: bold;
            margin-top: 10px;
        }
        ul {
            margin: 5px 0 10px;
            padding-left: 20px;
        }
        h1 {
            text-align: center;
            color: #2c3e50;
        }
      </style>
    </head>
    <body>
      <h1>Documentação da API - Thyago Noventa RA: 110734</h1>
    '''
    for ep in endpoints:
        html += f'''
        <div class="endpoint {ep['metodo']}"> 
          <div class="title">{ep['metodo']} {ep['end_point']}</div> 
          <div class="desc">{ep['descricao']}</div> '''

        html += '<div class="section">Headers:</div></ul>'
        for nome, tipo in ep['headers']:
            html += f'<li><code>{nome}</code>: {tipo}</li>'
        html += '</ul>'

        html += '<div class="section">Parâmetros:</div></ul>'
        for nome, tipo in ep['parametros']:
            html += f'<li><code>{nome}</code>: {tipo}</li>'
        html += '</ul>'

        html += '<div class="section">Respostas:</div><ul>'
        for codigo, msg in ep['respostas']:
            html += f'<li><code>{codigo}</code>: {msg}</li>'
        html += '</ul>'

        html += '</div>\n'

    html += '</body></html>'
    return html


def gerar_documentacao_html_layout2(endpoints):
    html = '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
      <meta charset="UTF-8">
      <title>Documentação da API - Thyago Noventa RA: 110734</title>
      <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
      <style>
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f9f9f9;
            padding: 40px;
            color: #333;
        }

        h1 {
            text-align: center;
            color: #2c3e50;
        }

        .endpoint {
            max-width: 800px;       
            margin: 20px auto;
            background: #ffffff;
            border-left: 8px solid;
            margin-bottom: 25px;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
            padding: 20px;
            transition: 0.3s ease;
        }

        .GET { border-color: #61affe; }
        .POST { border-color: #49cc90; }
        .PUT { border-color: #fca130; }
        .DELETE { border-color: #f93e3e; }

        .endpoint:hover {
            transform: scale(1.02);
            box-shadow: 0 6px 14px rgba(0, 0, 0, 0.1);
        }

        .title {
            font-size: 20px;
            font-weight: 700;
            color: #34495e;
            margin-bottom: 10px;
        }

        .method-label {
            display: inline-block;
            font-size: 12px;
            padding: 4px 8px;
            border-radius: 4px;
            margin-right: 10px;
            color: white;
        }

        .GET .method-label { background-color: #61affe; }
        .POST .method-label { background-color: #49cc90; }
        .PUT .method-label { background-color: #fca130; }
        .DELETE .method-label { background-color: #f93e3e; }

        .desc {
            font-size: 17px;
            margin-bottom: 15px;
            color: #555;
        }

        .section {
            font-size: 16px;
            font-weight: 600;
            margin-top: 10px;
            color: #2c3e50;
        }

        ul {
            list-style: disc;
            margin: 5px 0 15px 20px;
            padding-left: 0;
        }
        
        ul li {
            margin-bottom: 6px;
        }

        code {
            background: #ecf0f1;
            padding: 2px 5px;
            border-radius: 3px;
        }
      </style>
    </head>
    <body>
      <h1>Documentação da API - Thyago Noventa RA: 110734</h1>
    '''
    for ep in endpoints:
        html += f'''
        <div class="endpoint {ep['metodo']}">
          <div class="title">
            <span class="method-label">{ep['metodo']}</span> {ep['end_point']}
          </div>
          <div class="desc">{ep['descricao']}</div>'''

        html += '<div class="section">Headers:</div><ul>'
        for nome, tipo in ep['headers']:
            html += f'<li><code>{nome}</code>: {tipo}</li>'
        html += '</ul>'

        html += '<div class="section">Parâmetros:</div><ul>'
        for nome, tipo in ep['parametros']:
            html += f'<li><code>{nome}</code>: {tipo}</li>'
        html += '</ul>'

        html += '<div class="section">Respostas:</div><ul>'
        for codigo, msg in ep['respostas']:
            html += f'<li><code>{codigo}</code>: {msg}</li>'
        html += '</ul></div>\n'

    html += '</body></html>'
    return html


def gerar_documentacao_html_layout3(endpoints):
    html = '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
      <meta charset="UTF-8">
      <title>Documentação da API - Thyago Noventa RA: 110734</title>
      <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
      <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <style>
        body {
            font-family: Arial, sans-serif;
            padding: 40px 20px;
            background-color: #f7f9fc;
        }
        h1 {
            text-align: center;
            color: #2c3e50;
            max-width: 800px;
            margin: 0 auto 40px auto;
        }
        .endpoint {
            max-width: 800px;
            margin: 20px auto;
            border-left: 8px solid;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .endpoint:hover {
            background-color: #f0f4f8;
            transform: scale(1.0001);
            box-shadow: 0 6px 14px rgba(0, 0, 0, 0.08);
        }
        .GET { border-color: #61affe; }
        .POST { border-color: #49cc90; }
        .PUT { border-color: #fca130; }
        .DELETE { border-color: #f93e3e; }

        .header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 16px 20px;
            font-size: 18px;
            font-weight: bold;
            background-color: #f0f0f0;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
        }
        .material-icons {
            font-size: 24px;
            transition: transform 0.3s ease;
        }

        .details {
            display: none;
            padding: 20px;
            font-size: 15px;
            color: #333;
        }
        .desc {
            font-size: 16px;
            margin-bottom: 10px;
        }
        .section {
            font-weight: bold;
            margin-top: 10px;
        }
        ul {
            margin: 5px 0 10px;
            padding-left: 20px;
        }
        ul li {
            margin-bottom: 6px;
        }
      </style>
      <script>
        function toggleDetails(id, iconId) {
            const details = document.getElementById(id);
            const icon = document.getElementById(iconId);
            const isHidden = details.style.display === 'none' || details.style.display === '';
            details.style.display = isHidden ? 'block' : 'none';
            icon.textContent = isHidden ? 'expand_less' : 'expand_more';
        }
      </script>
    </head>
    <body>
      <h1>Documentação da API - Thyago Noventa RA: 110734</h1>
    '''
    for i, ep in enumerate(endpoints):
        block_id = f"detalhes{i}"
        icon_id = f"icone{i}"
        html += f'''
        <div class="endpoint {ep['metodo']}" onclick="toggleDetails('{block_id}', '{icon_id}')">
          <div class="header">
            <span>{ep['metodo']} {ep['end_point']}</span>
            <span class="material-icons" id="{icon_id}">expand_more</span>
          </div>
          <div class="details" id="{block_id}">
            <div class="desc">{ep['descricao']}</div>'''

        html += '<div class="section">Headers:</div><ul>'
        for nome, tipo in ep['headers']:
            html += f'<li><code>{nome}</code>: {tipo}</li>'
        html += '</ul>'

        html += '<div class="section">Parâmetros:</div><ul>'
        for nome, tipo in ep['parametros']:
            html += f'<li><code>{nome}</code>: {tipo}</li>'
        html += '</ul>'

        html += '<div class="section">Respostas:</div><ul>'
        for codigo, msg in ep['respostas']:
            html += f'<li><code>{codigo}</code>: {msg}</li>'
        html += '</ul></div></div>\n'

    html += '</body></html>'
    return html


def gerar_documentacao_json_propria(endpoints):
    estrutura = []

    for ep in endpoints:
        dados = {
            "metodo": ep["metodo"],
            "endpoint": ep["end_point"],
            "descricao": ep["descricao"],
            "headers": [{"nome": nome, "tipo": tipo} for nome, tipo in ep["headers"]],
            "parametros": [{"nome": nome, "tipo": tipo} for nome, tipo in ep["parametros"]],
            "respostas": [{"codigo": int(codigo), "mensagem": msg} for codigo, msg in ep["respostas"]]
        }
        estrutura.append(dados)

    return json.dumps(estrutura, indent=2, ensure_ascii=False)


def gerar_documentacao_postman_collection(endpoints, nome_colecao):
    collection = {
        "info": {
            "name": nome_colecao,
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "item": []
    }

    for ep in endpoints:
        metodo = ep["metodo"].upper()
        url = f"http://localhost:8000{ep['end_point']}"
        item = {
            "name": f"{metodo} {ep['end_point']}",
            "request": {
                "method": metodo,
                "header": [],
                "url": {
                    "raw": url,
                    "protocol": "http",
                    "host": ["localhost"],
                    "port": "8000",
                    "path": ep["end_point"].strip("/").split("/")
                },
                "description": ep["descricao"]
            }
        }

        headers = []
        for nome, tipo in ep.get("headers", []):
            headers.append({
                "key": nome,
                "value": "",
                "type": "text"
            })
        item["request"]["header"] = headers

        if metodo in ("POST", "PUT"):
            body_content = {}
            for nome, tipo in ep["parametros"]:
                body_content[nome] = ""

            item["request"]["body"] = {
                "mode": "raw",
                "raw": json.dumps(body_content, indent=2),
                "options": {"raw": {"language": "json"}}
            }

        collection["item"].append(item)

    return json.dumps(collection, indent=2)


def gerar_documentacao_openapi(endpoints):
    swagger = {
        "openapi": "3.0.0",
        "info": {
            "title": "Documentação da API",
            "version": "1.0"
        },
        "paths": {}
    }

    for ep in endpoints:
        metodo = ep["metodo"].lower()
        path = ep["end_point"]
        swagger["paths"].setdefault(path, {})
        swagger["paths"][path][metodo] = {
            "summary": ep["descricao"],
            "parameters": [],
            "responses": {}
        }

        for nome, tipo in ep["headers"]:
            swagger["paths"][path][metodo]["parameters"].append({
                "name": nome,
                "in": "header",
                "required": False,
                "schema": {
                    "type": tipo.lower()
                }
            })

        for nome, tipo in ep["parametros"]:
            swagger["paths"][path][metodo]["parameters"].append({
                "name": nome,
                "in": "query",
                "required": False,
                "schema": {
                    "type": tipo.lower()
                }
            })

        for codigo, mensagem in ep["respostas"]:
            swagger["paths"][path][metodo]["responses"][str(codigo)] = {
                "description": mensagem
            }

    yaml_output = yaml.dump(swagger, sort_keys=False, allow_unicode=True)
    json_output = json.dumps(swagger, indent=2, ensure_ascii=False)

    return yaml_output, json_output


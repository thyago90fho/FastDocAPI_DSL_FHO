from parser_110734 import inicializar_parser_arquivo, inicializar_parser_texto
from classe_output_110734 import *

def gerar_saidas():
    for item_endpoint in resultado:
        print(item_endpoint)

    json_txt = gerar_documentacao_json_propria(resultado)
    with open('documentacao_api_json_propria.json', 'w', encoding='utf-8') as f:
        f.write(json_txt)

    html = gerar_documentacao_html_layout1(resultado)
    with open('documentacao_api_html_layout_1.html', 'w', encoding='utf-8') as f:
        f.write(html)

    html = gerar_documentacao_html_layout2(resultado)
    with open('documentacao_api_html_layout_2.html', 'w', encoding='utf-8') as f:
        f.write(html)

    html = gerar_documentacao_html_layout3(resultado)
    with open('documentacao_api_html_layout_3.html', 'w', encoding='utf-8') as f:
        f.write(html)

    postman_json = gerar_documentacao_postman_collection(resultado, 'minha_colecao')
    with open('documentacao_api_postman_collection.json', 'w', encoding='utf-8') as f:
        f.write(postman_json)

    openapi_yaml, openapi_json = gerar_documentacao_openapi(resultado)
    with open('documentacao_api_openapi_yaml.yaml', 'w', encoding='utf-8') as f:
        f.write(openapi_yaml)
    with open('documentacao_api_openapi_json.json', 'w', encoding='utf-8') as f:
        f.write(openapi_json)

    print('\nArquivos de modelos gerados com sucesso:')

if __name__ == "__main__":
    # Se arquivo.txt não existir, o programa cria um ficticio automaticamente
    resultado = inicializar_parser_arquivo('arquivo.dsl')

    print('Sintaticamente correto!\n')

    gerar_saidas()




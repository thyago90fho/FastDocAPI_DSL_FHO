# *FastDocAPI:* Uma DSL para Escrita e Geração Rápida de Documentação de APIs REST

## Objetivo: 
O projeto tem como objetivo criar uma linguagem própria (DSL) que permite descrever APIs REST de forma simples e textual, sem a necessidade de escrever código tradicional. A partir dessas descrições, o sistema faz a leitura e interpretação automática do conteúdo, gerando arquivos úteis para desenvolvedores e equipes de documentação. Isso torna o processo de criação e documentação de APIs mais rápido, padronizado e acessível até para quem não tem tanta experiência com programação.

## Ciclo de Vida Gramatical:

![image](https://github.com/user-attachments/assets/7a6d59f0-562f-42a8-9c0f-a7a26f5184a5)

## Exemplo de Entrada:
(**OBS:** Poderão ser concatenadas várias entradas do exemplo mostrado abaixo em um único arquivo de entrada).

(**OBS 2:** Headers e Parâmetros são opcionais).

![image](https://github.com/user-attachments/assets/b81f08ea-00c1-43f8-b8ce-8253cea6ee80)

## Saídas:

Este projeto conta com algumas saídas prontas, como:

**-->** Arquivo JSON e YAML para importação via OpenAPI;

**-->** Arquivo JSON para importação via Postman;

**-->** Arquivos HTML para visualização básica ao usuário;

**-->** Arquivo JSON de saída própria da DSL desenvolvida;

**-->** Caso o usuário tenha tal conhecimento, poderá utilizar a DSL desenvolvida a seu favor e criar suas saídas como bem desejar. As saídas existentes apenas são exemplificações de como poderão ser utilizadas em um ambiente profissional.

## Exemplo de Saída HTML:

![image](https://github.com/user-attachments/assets/4ab2a72d-2a62-49d1-bcb8-7ec49ff84040)





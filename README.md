# Documentação | bot-cnep Cadastro Nancional de Empresas Punidas

<br/>

## 1. Introdução

O bot cnep foi desenvolvido para coletar dados abertos, seção do Cadastro Nacional de Empresas Punidas, diariamente, no endereço específico: 
[CNEP](https://dados.gov.br/dataset/cnep)

Os dados são fornecidos através de um único endereço:

* URL: http://transparencia.gov.br/download-de-dados/cnep/20210609 (exemplo de data para consulta)

O endereço retorna os dados em arquivo compactado (zip), contendo um arquivo csv. O csv é extraído e armazenado na stage área.

OBS: A cada dia o site irá conter um novo arquivo para download. A data usada para consultar o arquivo e baixar, deve ser sempre de 1 dia(s) antes da data atual.

<br/>

## 2. Resultado do bot (Outputs)

O bot irá gerar dois arquivos no final da execução.

* cnep.csv: Contém os dados das empresas punidas, com cadastro efetuado no CNEP.

```
-Formatação:
    Delimitação: ";"
    codificação: "ISO-8859-1"

root
 |-- TIPO DE PESSOA: string (nullable = true)
 |-- CPF OU CNPJ DO SANCIONADO: long (nullable = true)
 |-- NOME INFORMADO PELO ÓRGÃO SANCIONADOR: string (nullable = true)
 |-- RAZÃO SOCIAL  CADASTRO RECEITA: string (nullable = true)
 |-- NOME FANTASIA  CADASTRO RECEITA: string (nullable = true)
 |-- NÚMERO DO PROCESSO: string (nullable = true)
 |-- TIPO SANÇÃO: string (nullable = true)
 |-- DATA INÍCIO SANÇÃO: string (nullable = true)
 |-- DATA FINAL SANÇÃO: string (nullable = true)
 |-- ÓRGÃO SANCIONADOR: string (nullable = true)
 |-- UF ÓRGÃO SANCIONADOR: string (nullable = true)
 |-- ORIGEM INFORMAÇÕES: string (nullable = true)
 |-- DATA ORIGEM INFORMAÇÕES: string (nullable = true)
 |-- DATA PUBLICAÇÃO: string (nullable = true)
 |-- PUBLICAÇÃO: string (nullable = true)
 |-- DETALHAMENTO: string (nullable = true)
 |-- VALOR DA MULTA: string (nullable = true)
 |-- FUNDAMENTAÇÃO LEGAL: string (nullable = true)
 |-- DESCRIÇÃO DA FUNDAMENTAÇÃO LEGAL: string (nullable = true)
 |-- DATA DO TRÂNSITO EM JULGADO: string (nullable = true)
 |-- COMPLEMENTO DO ÓRGÃO: string (nullable = true)
```

* cnep.log: contém informações de log e tempo de execução do bot.
Obs.: Os arquivos contém uma "string" padrão no nome, com data e hora de execução.

```log
2021-06-10 11:39:01,652 - INFO - Conectado com sucesso no Bucket: bvs-bigdata-datalake-stage-external-cadastral-rf-dev
2021-06-10 11:40:25,819 - INFO - Download finalizado. URL: http://transparencia.gov.br/download-de-dados/cnep/20210609: 
2021-06-10 11:41:35,042 - INFO - Arquivo salvo no BUCKET: <Bucket: bvs-bigdata-datalake-stage-external-cadastral-rf-dev> e BLOB: <Blob: bvs-bigdata-datalake-stage-external-cadastral-rf-dev, datalake/stage/external/cadastral/rf/data/cnep/partitions/daily/2021/06/20210610_113900_cnep.csv, 1623336093444048>
2021-06-10 11:41:36,206 - INFO - Aplicação finalizada. Tempo de execução: 155.86598253250122s
```

<br/>

## 3. Funcionalidades

* O bot acessa a URL fornecida para baixar o arquivo compactado (zip) contendo o arquivo csv de dados.
* Valida a conexão com o bucket e projeto no GCP, em seguida cria o blob para o a sequência do trabalho.
* Realiza a descompactação do arquivo zip.
* Aciona a função de upload para o GCP, que subir os dados em um arquivo CSV.
* Armazena o log de processamento/execução do bot, no mesmo bucket e blob do arquivo CSV

<br/>

## 4. Conteúdo

O bot é composto por quatro arquivos:

* bot_cnep.py: programação python para download e upload de dados.
* gcp_connect.py: programação python para fornecer conexão com o GCP.
* bot_config.py: programação python para fornecer os parametros e as configurações do bot.
    * GCP project, Bucket and Blob;
    * Nome dos arquivos;
    * Parametros de requisição.
* Dockerfile: script Docker para construir o container da aplicação.
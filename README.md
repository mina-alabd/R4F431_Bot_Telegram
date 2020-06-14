# R4F431_Bot_Telegram
Um Bot para telegram que pesquisa produtos na Amazon, Mercado Livre, vídeos do YouTube, entre outros

Instalar:

- Python3
- pip install mechanize
- pip install bs4
- pip install telethon

Configuraração:

Editar o arquivo configuracao.py e colocar seu APP_ID e APP_HASH, obtidos nosite https://my.telegram.org
- Crie um Bot no @BOTFATHER no Telegram
- Na primeira execução insira o Api id (fornecido pelo @BOTFATHER) do seu Bot criado

Uso: 
<pre>
python R4F431_BOT.py
</pre>

Como utilizar:

com o bot iniciado, entre na janela de chat do seu Bot no telegram, e digite um dos comandos disponiveis abaixo

<pre>
amazon <nome do produto a buscar>
youtube <nome do video a buscar>
mercadolivre <produto a buscar>
olhardigital
hora
</pre>

Exemplos:

<pre>

amazon Cama de casal
Retornara uma lista de camas de casal encontrados no site da Amazon

youtube aulas de python
Retorna uma lista de vídeos de aulas de python encontrados no site do youtube

mercadolivre playstation 4
Retorna uma lista de produtos relacionados a playstation 4 encontrados no site do mercadolivre

olhardigital
Retorna as principais noticias do site Olhar Digital.

hora
Retorna a data e hora Atual

</pre>

Obs: Os comandos não são case sensitive, podendo misturar maiusculas, e minusculas, exemplo YouTube MERCADOLIVRE OlHaRdIgItAl.

Bugs conhecidos:

- Por algum motivo desconhecido o site da Amazon não realizou a busca, retornando erro de Algo deu errado, quando executado o bot a partir de uma hospedagem VPS.
- O Youtube apresentou também alguma instabilidade não funcionando em algumas vezes na hospedagem VPS.

  

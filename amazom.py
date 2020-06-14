import mechanize
from bs4 import BeautifulSoup as bs
import http.cookiejar as cookielib
import sys
import requests

#if len(sys.argv) < 3 :
#    print("Falta argumentos:")
#    print("Uso: "+sys.argv[0]+" <login> <senha>")
#    exit(1)

#login = sys.argv[1]
#senha = sys.argv[2]

def buscaProduto(txt) :

    txt = txt.replace(' ','+')

    cookies = cookielib.CookieJar()  # cria um repositório de cookies
    browser = mechanize.Browser()    # inicia um browser
    browser.set_cookiejar(cookies)   # aponta para o seu repositório de cookies

    # carrega a pagina
    browser.open('https://www.amazon.com.br/s?k='+txt)

    #browser.select_form(nr=1)      # o formulário de senha é o segundo
    #browser.form['usuario'] = login     # seu e-mail de login
    #browser.form['senha'] = senha  # sua senha
    #browser.submit()               # submissão dos dados

    # carrega a pagina do perfil logado
    #browser.open('https://www.devmedia.com.br/perfil/')
    pagina = browser.response().read()  # pega o HTML 
    #pagina = requests.get('https://www.amazon.com.br/s?k='+txt).text
    
    #print(pagina)
    # Beautiful Soup aqui
    soup = bs(pagina,'html.parser')
    #codigo = soup.find_all(True,{"class":"a-size-base-plus"})
    codigo = soup.find_all(True,{"class":"a-section a-spacing-medium"})

    #print(codigo)


    #print("-------------------")

    retorno = ""
    listaRetorno = []

    for dados in codigo :
        
        #print(dados)
        #print("-------------------")
        nomeProduto = dados.find(class_='a-size-base-plus').text
        #print(nomeProduto)

        try:
            precoProduto = dados.find(class_='a-offscreen').text
            #print(precoProduto)
        except AttributeError:
            precoProduto = "Valor indisponivel"
        
        linkProduto = "https://www.amazon.com.br"+dados.find('a').get('href')
        #print(linkProduto)
        #print("-------------------")
        retorno = nomeProduto+"\n"
        retorno += precoProduto+"\n"
        retorno += linkProduto+"\n"
        #retorno += '---------------'
        listaRetorno.append(retorno)

    return listaRetorno

if __name__ == '__main__' :

    if len(sys.argv) < 2 :
        print("Falta argumentos:")
        print("Uso: "+sys.argv[0]+" <produto>")
        exit(1)

    strBusca = ""

    for argumento in sys.argv[1:] :
        strBusca += argumento+" "

    resultado = buscaProduto(strBusca)

    for linha in resultado :
        print(linha)

    

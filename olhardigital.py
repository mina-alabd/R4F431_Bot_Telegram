import mechanize
from bs4 import BeautifulSoup as bs
import http.cookiejar as cookielib
import sys


def busca_olhardigital() :
        
    cookies = cookielib.CookieJar()  # cria um repositório de cookies
    browser = mechanize.Browser()    # inicia um browser
    browser.set_cookiejar(cookies)   # aponta para o seu repositório de cookies
    browser.set_handle_robots(False)

    # carrega a pagina
    browser.open('https://olhardigital.com.br/')

    # carrega a pagina
    pagina = browser.response().read()  # pega o HTML 

    #print(pagina)
    # Beautiful Soup aqui
    soup = bs(pagina,'html.parser')
    codigo = soup.find_all(True,{"class":"blk-item"})

     
    #print(codigo)
    
    strResultado = ""
    listaResultado = []
    
    for dados in codigo :
        #print(dados)
        print(dados.get("title") )
        print(dados.get("href") )
        nomeNoticia = dados.get("title")
        linkNoticia = "https:"+dados.get("href")
        strResultado = nomeNoticia + "\n" + linkNoticia + "\n"
        listaResultado.append(strResultado)

    return listaResultado


if __name__ == "__main__" :
    
    retorno = busca_olhardigital()

    for dados in retorno :
        print(dados)


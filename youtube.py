import mechanize
from bs4 import BeautifulSoup as bs
import http.cookiejar as cookielib
import sys

#senha = sys.argv[2]

def busca_youtube(txt) :
        
    txt = txt.replace(' ','+')

    cookies = cookielib.CookieJar()  # cria um repositório de cookies
    browser = mechanize.Browser()    # inicia um browser
    browser.set_cookiejar(cookies)   # aponta para o seu repositório de cookies
    browser.set_handle_robots(False)

    # carrega a pagina
    browser.open('https://www.youtube.com/results?search_query='+txt)

    #browser.select_form(nr=1)      # o formulário de senha é o segundo
    #browser.form['usuario'] = login     # seu e-mail de login
    #browser.form['senha'] = senha  # sua senha
    #browser.submit()               # submissão dos dados

    # carrega a pagina do perfil logado
    #browser.open('https://www.devmedia.com.br/perfil/')
    pagina = browser.response().read()  # pega o HTML 

    #print(pagina)
    # Beautiful Soup aqui
    soup = bs(pagina,'html.parser')
    codigo = soup.find_all(True,{"class":"yt-uix-tile-link"},{"class":"yt-ui-ellipsis"})

    print(codigo[1])

    strResultado = ""
    listaResultado = []
    
    for dados in codigo :
        print(dados.text)
        print("https://www.youtube.com"+dados.get("href"))
        nomeVideo = dados.text
        linkVideo = "https://www.youtube.com"+dados.get("href")

        listaResultado.append( nomeVideo +"\n"+linkVideo+"\n")

    return listaResultado
    

    exit(0)

    print("Login da DevMedia: "+login)
    print("---------------------------------------------")
    print("\nEstatisticas:")
    for item in codigo :
        titulo = item.text.split('\t')[4].split('\r')[0]
        valor = item.text.split('\t')[-3]
        print(titulo+" - "+ valor)

    #codigo = soup.find_all(True,{"class":"box-tecnologias"})
    codigo = soup.findAll(class_='box-tecnologias')

    #print(codigo)

    print("Tecnologias:\n")
    for item in codigo :

        listTec = item.findAll(class_='tags')
        #print(listTec)
        for tec in listTec :
            print(tec.text)

if __name__ == "__main__" :
    if len(sys.argv) < 2 :
        print("Falta argumentos:")
        print("Uso: "+sys.argv[0]+" <busca+video>")
        exit(1)

    strBusca = ""

    for argumento in sys.argv[1:] :
        strBusca += argumento + " "
    

    busca_youtube(strBusca[0:-1])



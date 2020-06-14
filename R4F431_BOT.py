from telethon import TelegramClient, events, sync
from datetime import datetime
import configuracao
import time
import amazom
import youtube
import mercadolivre
import olhardigital




# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = configuracao.api_id
api_hash = configuracao.api_hash
session_name = configuracao.session_name


client = TelegramClient(session_name, api_id, api_hash)
client.start()



#Doing stuff
print(client.get_me().stringify())

#client.send_message('usuario', 'Hello! Talking to you from Telethon')
#client.send_file('username', '/home/myself/Pictures/holidays.jpg')

#client.download_profile_photo('me')
#messages = client.get_messages('usuario')
#messages[0].download_media()


@client.on(events.NewMessage)
async def handler(event):
    print(event.message.message)
    
    msg = event.message.message

    msg = msg.split(" ")

    
    #print(numero)
    #await event.respond("Numero de msg recebidas")

    if msg[0].lower() == 'horas' :
        data_atual = datetime.now()
        data_em_texto = data_atual.strftime('%d/%m/%Y %H:%M:%S')
        await event.respond(data_em_texto)
        #numero = somaNumero() 
        return

    if msg[0].lower() == 'olhardigital' :

        strBusca = ""

        for dados in msg[1:] :
            strBusca += dados+" "

        texto = olhardigital.busca_olhardigital()
        
        await event.respond("Encontrei "+ str( len(texto) )+" resultados para "+strBusca.replace('-',' ')+" no Olhar Digital :" )
        time.sleep(2)

        for dados in texto :
            time.sleep(1)
            await event.respond( dados )
        await event.respond('Pronto, isso é tudo.')
        await event.respond('Estarei aqui sempre que precisar. :-)\n')


    if msg[0].lower() == 'mercadolivre' :

        strBusca = ""

        for dados in msg[1:] :
            strBusca += dados+" "

        texto = mercadolivre.busca_mercadolivre(strBusca[0:-1])
        
        await event.respond("Encontrei "+ str( len(texto) )+" resultados para "+strBusca.replace('-',' ')+" no Mercado Livre :" )
        time.sleep(2)

        for dados in texto :
            time.sleep(1)
            await event.respond( dados )
        await event.respond('Pronto, isso é tudo.')
        await event.respond('Estarei aqui sempre que precisar. :-)\n')

    if msg[0].lower() == 'amazon' :

        strBusca = ""

        for dados in msg[1:] :
            strBusca += dados+" "

        texto = amazom.buscaProduto(strBusca[0:-1])

        await event.respond("Encontrei "+ str( len(texto) )+" resultados para "+strBusca.replace('+',' ')+" na Amazon:" )
        time.sleep(2)

        for dados in texto :
            time.sleep(1)
            await event.respond( dados )
        await event.respond('Pronto, isso é tudo.')
        await event.respond('Estarei aqui sempre que precisar. :-)\n')

    if msg[0].lower() == 'youtube' :

        strBusca = ""

        for dados in msg[1:] :
            strBusca += dados+" "

        texto = youtube.busca_youtube(strBusca[0:-1])
        #print(texto)
        #await sync.asyncio.sleep(5)
        #texto = """*Console PlayStation 4 1TB Bundle Hits 9  - GTA V, Death Stranding, The Last Of Us - PlayStation 4*R$2.649,00https://www.amazon.com.br/Console-PlayStation-1TB-Bundle-Hits/dp/B08458VCZ1/ref=ice_ac_b_dpb?dchild=1---------------
        #"""

        await event.respond("Encontrei "+ str( len(texto) )+" resultados para "+strBusca.replace('+',' ')+" no YouTube :" )
        time.sleep(2)

        for dados in texto :
            time.sleep(1)
            await event.respond( dados )
        await event.respond('Pronto, isso é tudo.')
        await event.respond('Estarei aqui sempre que precisar. :-)\n')



client.run_until_disconnected()
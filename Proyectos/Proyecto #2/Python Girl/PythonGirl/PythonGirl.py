# Import
import discord
from discord.ext import commands
import random
import os
import requests
import json

# Cliente

client = discord.Client()
bot = commands.Bot(command_prefix= '$')

# Embed

embed = discord.Embed(title="Comandos", description="""La lista de comandos disponibles de momento es: \n 
*Juegos:\n-> $iq\n-> $roll\n-> $F2P\n-> $animal\n-> $BBQuote\n-> $BBCharacter \n-> $FN10 \n-> $FNRandom \n 
*Utilidad:\n-> $dolar\n-> $redes\n-> $BTC""", color=0xFFFFFF)

# Login
@client.event
async def on_ready():
    print('Inicie sesion como: {0.user}'.format(client))

# Eventos con mensajes
@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    # Brinda el link de la pagina dolarhoy para ver el valor del dolar en Argentina

    if message.content.startswith('$dolar'):
        await message.channel.send('💰Podes ver el valor del dolar aqui💰 -> https://www.dolarhoy.com/')

    elif message.content.startswith('cheri'):
        await message.channel.send('Ta chiquita y no puede')

    # Muestra el clima en la ciudad de buenos aires

    elif message.content.startswith('$WeatherBA'):
        headers = {
            'access_key': '8b4686495642933410b020b117f497f8',
            'query': 'Buenos Aires'
            }

        api_result = requests.get('http://api.weatherstack.com/current', headers)

        weather = api_result.json()

        await message.channel.send(f'Ciudad: {weather["location": "name"]}')

    # Muestra los primeros 10 items de la tienda de Fortnite
    
    elif message.content.startswith('$FN10'): 
        headers = {
            "Content-Type":"Application/json",
            'TRN-Api-Key': os.environ.get('Fortnite_API')
            }
        url = 'https://api.fortnitetracker.com/v1/store'
        r = requests.get(url, headers=headers)
        fn = r.json()
        
        for x in range(10):
            await message.channel.send(f'📌Nombre: {fn[x]["name"]}')
            await message.channel.send(f'🔥vBucks: {fn[x]["vBucks"]}')
            await message.channel.send(f'{fn[x]["imageUrl"]}')

    # Muestra un objeto random de la tienda

    elif message.content.startswith('$FNRandom'):
        headers = {
            "Content-Type":"Application/json",
            'TRN-Api-Key': os.environ.get('Fortnite_API')
            }
        num = random.randint(1, 45)
        url = 'https://api.fortnitetracker.com/v1/store'
        r = requests.get(url, headers=headers)
        fn = r.json()

        await message.channel.send(f'📌Nombre: {fn[num]["name"]}')
        await message.channel.send(f'🔥vBucks: {fn[num]["vBucks"]}')
        await message.channel.send(f'{fn[num]["imageUrl"]}')

    # Muestra juegos gratis de computadora aleatoriamente, tomados de la pagina Freetogame.com

    elif message.content.startswith('$F2P'):
        num = random.randint(1, 250)
        response7 = requests.get('https://www.freetogame.com/api/games?platform=pc')
        free = response7.json()
        await message.channel.send(f'{free[num]["title"]}')
        await message.channel.send(f'{free[num]["short_description"]}')
        await message.channel.send(f'{free[num]["game_url"]}')
        
    # Muestra el valor de BTC/USD, valor tomado de coinlore

    elif message.content.startswith('$BTC'):
        response4 = requests.get('https://api.coinlore.net/api/ticker/?id=90')
        BTC = response4.json()
        await message.channel.send(f'💰El precio de BTC en USD: {BTC[0]["price_usd"]}💰')

    # Frase random de Breaking Bad

    elif message.content.startswith('$BBQuote'):

        response5 = requests.get('https://breakingbadapi.com/api/quotes')
        BBQ = response5.json()
        select = random.randint(1, 50)
        await message.channel.send(f'{BBQ[select]["quote"]}')
    
    # Muestra un personaje random de breaking bad, junto con su nombre, apodo e imagen
    
    elif message.content.startswith('$BBCharacter'):
        response6 = requests.get('https://breakingbadapi.com/api/characters')
        BBC = response6.json()
        select = random.randint(1, 50)
        await message.channel.send(f'Nombre: {BBC[select]["name"]}\nApodo: {BBC[select]["nickname"]}\n{BBC[select]["img"]}')

    # Muestra fotos aleatorias de Gatitos, Perritos, Zorros

    elif message.content.startswith('$animal'):

        elegir_animal = random.choice(['Gatitos', 'Perritos', 'Zorros'])
        
        if elegir_animal == 'Gatitos':

            response2 = requests.get('https://aws.random.cat/meow')
            gatito = response2.json()
            await message.channel.send(gatito['file'])

        elif elegir_animal == 'Perritos':

            response3 = requests.get('https://random.dog/woof.json')
            perrito = response3.json()
            await message.channel.send(perrito['url'])

        elif elegir_animal == 'Zorros':

            response = requests.get('https://randomfox.ca/floof')
            zorro = response.json()
            await message.channel.send(zorro['image'])

    # Promocion a mi mismo
                
    elif message.content.startswith('$redes'):
        await message.channel.send('Redes -> https://linktr.ee/jd_apprentice')

    # Roll con respuestas dependiendo el numero que salga (0 - 200)

    elif message.content.startswith('$iq'):

        tu_iq = random.randint(0, 200)
        tu_iq_real = random.randint(0, 200)

        await message.channel.send (f'🧠Tu IQ ahora mismo es [{tu_iq}] \n🧠no mentira en realidad es [{tu_iq_real}]')

        if tu_iq_real == 200:
            await message.channel.send('BIG BRAIN 🧠🧠🧠🧠🧠')
        elif tu_iq_real == 0:
            await message.channel.send('BALAZO POR FAVOR 🔪🔪🔪🔪🔪')
        elif tu_iq_real >= 150:
            await message.channel.send('SALIS DE LATINOAMERICA🧠🧠')
        elif tu_iq_real >= 100:
            await message.channel.send('Bien ahi tenes mas de dos neuronas 👍')
        elif tu_iq_real <= 20:
            await message.channel.send('TU UNICA NEURONA ESTA PELEANDO POR SU VIDA 🦍')
        elif tu_iq_real <= 50:
            await message.channel.send('🦍 Tremendo mono 🦍')
        elif tu_iq_real <= 99:
            await message.channel.send('Esta dificil conectar dos neuronas?')
        
    # Lista de comandos disponibles
        
    elif message.content.startswith('$ayuda'):
        await message.channel.send(embed=embed)

    # Roll

    elif message.content.startswith('$roll'):
        dice = random.randint(1, 20)
        await message.channel.send(f' Tu roll fue de {dice}')

# Run
client.run(os.environ.get('DB_KEY'))

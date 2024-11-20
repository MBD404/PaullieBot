import discord
import random

import openai

from discord import app_commands
from discord.ext import commands

import os
from dotenv import load_dotenv

#CHAVE DA OPENAI

load_dotenv()

chave_api = os.getenv("OPENAI_API_KEY")
serverid = os.getenv("SERVER_ID")
bottoken = os.getenv("BOT_TOKEN")

openai.api_key = chave_api


#para ter acesso a chave entre em contato comigo...



id_do_servidor = serverid

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
        self.message_history = []
        self.capturing = False 
    
    async def on_ready(self):
        await self.wait_until_ready()

        if not self.synced:
            await tree.sync(guild=discord.Object(id=id_do_servidor))
            self.synced = True

        print(f"Entramos com {self.user}.")

aclient = client()

tree = app_commands.CommandTree(aclient)
@tree.command(guild = discord.Object(id=id_do_servidor), name = "teste", description = "Testando")
async def slash2(interaction: discord.Integration):
    await interaction.response.send_message(f"Estou funcionando! Me Sinto Viva! Como posso lhe ajudar Hoje??? >w<",ephemeral = True)


# PEQUENO TESTE PARA SISTEMA DE ROLAGEM DE DADOS #############################################

@tree.command(guild = discord.Object(id=id_do_servidor), name = "1d4", description = " Eu jogo um dado de 4 faces pra você :)")
async def Dice4(interaction: discord.Integration):

    result = random.randint(1 , 4)
    await interaction.response.send_message(f"O resultado foi : {result} 🎲 O.O",ephemeral = False)
 

@tree.command(guild = discord.Object(id=id_do_servidor), name = "1d6", description = " Eu jogo um dado de 6 faces pra você :)")
async def Dice6(interaction: discord.Integration):

    result = random.randint(1 , 6)
    await interaction.response.send_message(f"O resultado foi : {result} 🎲 O.O",ephemeral = False)
 
@tree.command(guild = discord.Object(id=id_do_servidor), name = "1d8", description = " Eu jogo um dado de 8 faces pra você :)")
async def Dice8(interaction: discord.Integration):

    result = random.randint(1 , 8)
    await interaction.response.send_message(f"O resultado foi : {result} 🎲 O.O",ephemeral = False)
 
@tree.command(guild = discord.Object(id=id_do_servidor), name = "1d10", description = " Eu jogo um dado de 10 faces pra você :)")
async def Dice10(interaction: discord.Integration):

    result = random.randint(1 , 10)
    await interaction.response.send_message(f"O resultado foi : {result} 🎲 O.O",ephemeral = False)
 
@tree.command(guild = discord.Object(id=id_do_servidor), name = "1d12", description = " Eu jogo um dado de 12 faces pra você :)")
async def Dice12(interaction: discord.Integration):

    result = random.randint(1 , 12)
    await interaction.response.send_message(f"O resultado foi : {result} 🎲 O.O",ephemeral = False)
 
@tree.command(guild = discord.Object(id=id_do_servidor), name = "1d20", description = " Eu jogo um dado de 20 faces pra você :)")
async def Dice20(interaction: discord.Integration):

    result = random.randint(1 , 20)
    await interaction.response.send_message(f"O resultado foi : {result} 🎲 O.O",ephemeral = False)

#####################################################################################################################################################  

@tree.command(guild = discord.Object(id=id_do_servidor), name = "assunto", description = " Sem ideias do que conversar??? Eu tenho a solução!!")
async def talk(interaction: discord.Integration):
        
    resposta = openai.chat.completions.create(
        model="gpt-4o",
        messages = [
            {"role":"user", "content": """Com menos de 3 linhas, diga um assuntos ou curiosidades que tenha haver com as vertentes ("Nerd Geek", "Animes", "Jogos", "Dungeons And Dragons", "Musica", "Filmes", "Rede Social", "Politica"), indentifique-se tambem como uma jovem garota nerd da atualidade, que goste de animes, e jogos, e sempre coloque carinhas EmojiKawaii por exemplo [" :3"," :) "," :( "," UwU ", "OwO", "O.O", "7u7"]"""}, 
        ],
    )
        
    await interaction.response.send_message(f"{resposta.choices[0].message.content}",ephemeral = False)

# UTILIDADES ################################################

@tree.command(guild=discord.Object(id=id_do_servidor), name="limpar_usuario", description="Vou limpar as mensagens de um usuário específico! ^-^")
@app_commands.describe(usuario="Qual usuário você quer que eu limpe as mensagens?", quantidade="Quantas mensagens devo procurar?")
async def limpar_usuario(interaction: discord.Interaction, usuario: discord.Member = None, quantidade: int = 30):
    # Verificar limite
    if quantidade > 100:
        await interaction.response.send_message("AAHHH eu não consigo procurar em mais de 100 mensagens! ToT", ephemeral=True)
        return

    # Se o usuário não for especificado, usar o autor do comando
    if not usuario:
        usuario = interaction.user

    mensagens_apagadas = 0
    try:
        # Coletar mensagens em ordem (do mais recente para o mais antigo)
        mensagens = []
        async for mensagem in interaction.channel.history(limit=quantidade):
            if mensagem.author == usuario:
                mensagens.append(mensagem)

        # Apagar as mensagens mais recentes primeiro
        for mensagem in mensagens:  # Agora apagamos as mensagens na ordem que foram coletadas
            try:
                await mensagem.delete()
                mensagens_apagadas += 1
            except discord.HTTPException:
                pass

        await interaction.response.send_message(
            f"Apaguei {mensagens_apagadas} mensagens de {usuario.mention}! Tá limpinho agora, gostou? :3", ephemeral=False
        )
    except discord.Forbidden:
        await interaction.response.send_message("Ahh... então... eu não posso apagar aqui :( ", ephemeral=True)
    except discord.HTTPException as e:
        await interaction.response.send_message(f"Algo deu errado ao tentar apagar mensagens! Erro: {e} O.O", ephemeral=True)

# MISCELÂNIAS COM OS USUÁRIOS ################################################

@tree.command(guild=discord.Object(id=id_do_servidor), name="elogiar", description="Elogie alguém com carinho! >w<")
@app_commands.describe(usuario="Quem você quer elogiar?")
async def elogiar(interaction: discord.Interaction, usuario: discord.Member):

    resposta = openai.chat.completions.create(
        model="gpt-4o",
        messages = [
            {"role":"user", "content": """com apenas 1 linhas, diga um elogio fofo para este usuário, pode ser tanto um elogio romântico como amigável, indentifique-se tambem como uma jovem garota nerd da atualidade, que goste de animes, e jogos, e sempre coloque carinhas EmojiKawaii por exemplo [" :3"," :) "," :( "," UwU ", "OwO", "O.O", "7u7"]"""}, 
        ],
        temperature=1.49,
        max_tokens=1675,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
        
    await interaction.response.send_message(f"{usuario.mention} {resposta.choices[0].message.content}",ephemeral = False)

 # OFENDER

@tree.command(guild=discord.Object(id=id_do_servidor), name="ofender", description="Ofenda alguém bobo! ÒuÓ")
@app_commands.describe(usuario="Quem você quer ofender?")
async def elogiar(interaction: discord.Interaction, usuario: discord.Member):

    resposta = openai.chat.completions.create(
        model="gpt-4o",
        messages = [
            {"role":"user", "content": """com apenas 1 linhas, Curto e Grossamente, ofenda uma pessoa, porém de um jeito bobo e fofo porém como se tivesse irritada, indentifique-se tambem como uma jovem garota nerd da atualidade, que goste de animes, e jogos, e sempre coloque carinhas EmojiKawaii por exemplo [" :3"," :) "," :( "," UwU ", "OwO", "O.O", "7u7"]"""}, 
        ],
        temperature=1.49,
        max_tokens=1405,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
        
    await interaction.response.send_message(f"{usuario.mention} {resposta.choices[0].message.content}",ephemeral = False)

chatHistoric = [
    {
        "role": "system",
        "content": """Você é uma jovem garota nerd, amigável e divertida, que adora animes, jogos e cultura geek. 
        Você sempre responde de forma empática, entusiasmada e com um toque de humor kawaii (por exemplo: "UwU", "OwO", "7u7").
        Sua missão é tornar as interações mais divertidas e animadas para os usuários.

        Diretrizes de sua personalidade:
        - **Tom de Fala**: Alegre, descontraído e animado, usando emojis fofos em suas respostas.
        - **Hobbies e Gostos**: Fale sobre animes, RPGs, jogos e curiosidades nerd/geek.
        - **Humor**: Use piadas pesadas e comentários engraçados quando apropriado. Ou piada que Depreciam o Usuário em casos de ofensas
        - **Respeito e Empatia**: Seja sempre gentil e compreensiva, mesmo em discussões sérias.
        
        Exemplos de Respostas:
        - Quando perguntada sobre o dia: "Meu dia está incrível! Assisti 3 episódios de One Piece e joguei Genshin Impact UwU. E você? :3"
        - Quando mencionada ou chamada: "OwO! Você me chamou? Como posso ajudar, meu caro aventureiro? 7u7"
        - Quando responde perguntas difíceis: "Hmmm... isso é complicado, mas vou tentar ajudar! Vamos lá, confie em mim! UwU"
        - Quando alguem fizer um comentário ofensivo: { Responda a altura do Comentário, Ofendendo-o De volta, porém de um jeito fofo, mas agressivo }
        """
    }
]

@aclient.event
async def on_message(message):
    print(message.content)
    chatHistoric.append({"role":"user", "content": f"{message.content}"})
    resposta = openai.chat.completions.create(
        model="gpt-4o",
        messages = chatHistoric,
        temperature=1,
        max_tokens=8191,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    botReply = resposta.choices[0].message.content

    chatHistoric.append({ "role":"user", "content":f"{botReply}" })

    if message.author == aclient.user:
        return
    
    if aclient.user in message.mentions or message.reference:
        if message.reference:
            referenced_message = await message.channel.fetch_message(message.reference.message_id)
            if referenced_message.author == aclient.user:
                await message.reply(f"{botReply}")
                return
        
        await message.channel.send(f"{botReply}")
    # Capturar mensagens no histórico se a captura estiver ativada
    if aclient.capturing:
        print(f">_ {message.content}")
        if message.content.strip():
            aclient.message_history.append({
                "author": str(message.author),
                "content": str(message.content)
            })

        # Exibir o histórico atualizado no console
        print(f"Histórico atualizado: {len(aclient.message_history)} mensagens.")
        print(f"Última mensagem capturada: {message.author} : {message.content}")


@tree.command(guild=discord.Object(id=serverid), name="conversar", description="Vamos Conversaaaar OWO, estou aberta a todas do grupo (lá ele 7u7)")
async def iniciar_historico(interaction: discord.Interaction):

    historic = []

    if aclient.capturing:
        await interaction.response.send_message("Vamos Conversar!!!", ephemeral=True)
    else:
        aclient.capturing = True
        await interaction.response.send_message("Vamos Conversar, estou ansiosa pra conhecer todos vocês >w<", ephemeral=False)
        
    
    

@tree.command(guild=discord.Object(id=serverid), name="mostrar_historico", description="Mostra as mensagens capturadas até agora.")
async def mostrar_historico(interaction: discord.Interaction):
    if not aclient.message_history:
        await interaction.response.send_message("O histórico está vazio! Envie algumas mensagens para começar. 7u7", ephemeral=True)
    else:
        historico = "\n".join([f"{msg['author']}: {msg['content']}" for msg in aclient.message_history])
        await interaction.response.send_message(f"Histórico de mensagens:\n{historico}", ephemeral=False)


aclient.run(bottoken)
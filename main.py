import discord
import asyncio

TOKEN = ""
CHANNEL_ID = 123456789  # Remplace avec l'ID du salon
EMOJI = "✅"
BASE_NUMBER = 1  # Commence à 1 (int)

intents = discord.Intents.default()
intents.message_content = True  

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    global BASE_NUMBER  
    print(f"✅ Connecté en tant que {client.user}")

    channel = client.get_channel(CHANNEL_ID)
    
    if not channel:
        print("❌ Salon introuvable.")
        await client.close()
        return

    # 🔹 Envoi du premier message "1" au démarrage
    first_message = await channel.send(str(BASE_NUMBER))
    print(f"📤 Premier message envoyé : {first_message.content}")

@client.event
async def on_message(message):
    global BASE_NUMBER

    if message.channel.id != CHANNEL_ID or message.author == client.user:
        return  # Ignore les messages d'autres salons ou du bot lui-même

    print(f"📩 Nouveau message ! ID: {message.id} | Contenu: {message.content}")

    try:
        message_number = int(message.content)  

        if message_number == BASE_NUMBER + 1:  
            await message.add_reaction(EMOJI)  
            BASE_NUMBER = message_number  
            print(f"✅ Réaction ajoutée et BASE_NUMBER mis à jour : {BASE_NUMBER}")
        else:
            print(f"🛑 Mauvais numéro ({message_number} ≠ {BASE_NUMBER + 1}), suppression...")
            await message.delete()  # ❌ Supprime uniquement le dernier message incorrect

    except ValueError:
        print("⚠️ Message invalide (pas un nombre), suppression...")
        await message.delete()  

client.run(TOKEN)

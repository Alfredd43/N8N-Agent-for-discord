import discord
import aiohttp
import logging

# --- CONFIG ---
DISCORD_TOKEN = "YOUR_DISCORD_BOT_TOKEN"  # <-- put your bot token here
N8N_WEBHOOK_URL = "https://alfredd43.app.n8n.cloud/webhook/discord-bot"

# --- LOGGING ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- DISCORD SETUP ---
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logger.info(f"✅ Bot is ready! Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    # Only respond to DMs or if bot is mentioned
    if not (client.user in message.mentions or isinstance(message.channel, discord.DMChannel)):
        return

    # Remove bot mention from message
    clean_content = message.content
    for mention in message.mentions:
        clean_content = clean_content.replace(f'<@{mention.id}>', '').replace(f'<@!{mention.id}>', '')
    clean_content = clean_content.strip()
    if not clean_content:
        clean_content = "Hello, how can I help you?"

    logger.info(f"📝 Processing: '{clean_content}' from {message.author}")

    async with message.channel.typing():
        try:
            payload = {
                "message": clean_content,
                "author": str(message.author),
                "channel": str(message.channel.id)
            }
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    N8N_WEBHOOK_URL,
                    json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=30
                ) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        ai_response = data.get("response", "⚠️ No response from AI")
                        # Discord message limit is 2000 chars
                        for i in range(0, len(ai_response), 2000):
                            await message.channel.send(ai_response[i:i+2000])
                    else:
                        await message.channel.send("⚠️ AI service unavailable")
        except Exception as e:
            logger.error(f"Error: {e}")
            await message.channel.send("⚠️ Something went wrong")


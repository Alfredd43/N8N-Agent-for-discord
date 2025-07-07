<h1 align="center">🤖 Discord AI Sidekick</h1>

<p align="center">
  <b>Smart Discord bot powered by n8n + Cohere</b><br>
  💬 Context-aware, dynamic answers | ⚡️ Easy to run | 🧠 Replies scale with your question
</p>

---

## ✨ What is this?

**Discord AI Sidekick** is a plug-and-play Discord bot that:
- 📨 Relays your messages to n8n
- 🧠 Gets smart answers from Cohere AI
- 📏 Gives short or long replies depending on your question
- 🛠️ Is super easy to set up and hack

---

## 🚀 Features

- 💬 **DM or Mention** – Bot replies in DMs or when mentioned
- 🧠 **Dynamic Answer Length** – Short for simple, long for deep questions
- 🔗 **n8n Workflow** – All logic and API calls handled in n8n
- 🦾 **Cohere LLM** – Real AI, not just canned responses
- 🛠️ **Customizable** – Tweak keywords, thresholds, or add your own flair

---

## 🛠️ Tech Stack

| Layer      | Tech                |
|------------|---------------------|
| 🤖 Bot     | discord.py + aiohttp|
| 🔄 Backend | n8n (cloud or local)|
| 🧠 AI      | Cohere (command-r-plus)|

---

## ⚡️ Quickstart

1. **Clone this repo**
2. `pip install discord.py aiohttp`
3. Set your Discord bot token in `discord_bot.py`
4. Import `n8n_discord_ai_workflow.json` into n8n
5. Add your Cohere API key in the n8n HTTP node
6. Run the bot: `python discord_bot.py`

---

## 🧙‍♂️ How it Works

1. You DM or mention the bot
2. Bot sends your message to n8n
3. n8n decides how long the answer should be (smart logic!)
4. Cohere generates a reply
5. Bot sends it back to Discord

---

## 🎛️ Dynamic Answers

- Short/simple questions? Quick replies.
- Deep/complex/"explain" questions? Long, detailed answers.
- Tweak the logic in the n8n "Build Cohere Request" node to fit your vibe.

---



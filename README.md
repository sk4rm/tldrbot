# TL;DR Bot

bcs i dw scroll up 10 light-years of conversation and read allat slop.

## Development

Use Python 3.12.

```pwsh
python -m venv .venv
.venv/scripts/activate
pip install -r requirements.txt
```

Create a `.env` file for your secrets. Venv will read from it once when you activate.

```pwsh
# Discord bot config
TOKEN= # required bot token
DEV_GUILD_ID=000000000000000000

# Ollama config
OLLAMA_HOST=127.0.0.1
OLLAMA_PORT=11434
OLLAMA_MODEL=llama3.1:8b
```

Start the ollama server.

```pwsh
ollama serve
```

Start the bot.

```pwsh
# In another session
python tldrbot.py
```
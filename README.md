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

```
TOKEN=<bot token>
DEV_GUILD_ID=000000000000000000
OLLAMA_HOST=127.0.0.1
OLLAMA_PORT=11434
```

Start the ollama server.

```pwsh
ollama serve

# In another session
ollama run llama3.2
```

Start the bot.

```pwsh
# In yet another session
python tldrbot.py
```
# TL;DR Bot

cos idw scroll up 10 light-years of conversation and read allat slop every morning

## Prerequisites

* Python 3.12.8
* [Ollama](https://ollama.com/download)

## Quickstart

Download a copy of the repository. then:

* **Windows:** Edit and execute `run.ps1`.

## Commands

| Command         | Description                                    |
| --------------- | ---------------------------------------------- |
| `/tldr`         | Summarizes up to the user's last sent message. |
| `/tldr <limit>` | Summarize the latest `<limit>` messages        |

## Manual

Install packages.

```pwsh
python -m venv .venv
.venv/scripts/activate
pip install -r requirements.txt
```

Supply these environmental variables:

```
TOKEN=                       # required bot token
GUILD_ID=000000000000000000  # optional guild id
OLLAMA_MODEL=llama3.1
```

Start the ollama server.

```pwsh
ollama serve
```

Start the bot.

```pwsh
python tldrbot.py
```

The bot will pull and use 

## Docker

Build and run the bot.

```pwsh
docker compose up --build
```

### Using another model

The bot will pull and use [`llama3.1:8b`](https://ollama.com/library/llama3.1) by default.

You can choose other models by modifying the environment variable `OLLAMA_MODEL` in `compose.yaml`.

See [ollama's library](https://ollama.com/library) for supported models.
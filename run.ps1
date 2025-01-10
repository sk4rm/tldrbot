param(
    [string]$Token = "bot token goes here",
    [string]$GuildId = "000000000000000000",
    [string]$Model = "llama3.1",
    [string]$OllamaHost = "localhost:11434"
)

$env:TOKEN = $Token
$env:GUILD_ID = $GuildId
$env:OLLAMA_MODEL = $Model
$env:OLLAMA_HOST = $OllamaHost

Start-Process -NoNewWindow ollama serve

python -m venv .venv
.venv/scripts/activate

pip install -r requirements.txt

python tldrbot.py

.venv/scripts/deactivate
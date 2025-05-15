import requests
from datetime import datetime
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

JOB_BOARDS = {
    "JobStash": "https://jobstash.xyz/jobs?tags=remote",
    "FindWeb3": "https://findweb3.com/jobs?remote=true",
    "CryptoJobsList": "https://cryptojobslist.com/?remote=true",
    "Web3.career": "https://web3.career/?remote=true",
    "CryptocurrencyJobs.co": "https://cryptocurrencyjobs.co/engineering/?remote=true",
    "Wellfound": "https://wellfound.com/remote-jobs/blockchain-development-jobs",
}

GOOGLE_SEARCH_URL = (
    "https://www.google.com/search?q="
    '("Frontend Developer" OR "Frontend Engineer" OR "Smart Contract Developer" OR "Solidity Developer" '
    'OR "Junior DeFi Engineer" OR "DeFi Developer") '
    '("web3" OR "blockchain" OR "solidity") ("Remote") '
    '(site:greenhouse.io OR site:lever.co OR site:bamboohr.com OR site:workable.com) '
    '(intitle:"Careers" OR intitle:"Jobs" OR inurl:jobs)'
)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown',
        'disable_web_page_preview': True
    }
    response = requests.post(url, json=payload)
    if not response.ok:
        print(f"❌ Failed to send message: {response.text}")
    else:
        print("✅ Message sent to Telegram.")

def build_message():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    message = f"🚨 *Web3 Remote Job Digest* ({now})\n\n"
    message += "Here are some boards listing remote Web3/DeFi roles:\n\n"
    for name, url in JOB_BOARDS.items():
        message += f"• [{name}]({url})\n"
    message += "\n🔍 [Search traditional ATS platforms](%s)" % GOOGLE_SEARCH_URL
    return message

if TELEGRAM_TOKEN and CHAT_ID:
    msg = build_message()
    send_telegram_message(msg)
else:
    print("❗ Missing TELEGRAM_TOKEN or CHAT_ID environment variables.")

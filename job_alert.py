# job_alert.py
import requests
import datetime

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown'
    }
    response = requests.post(url, json=payload)
    if not response.ok:
        print(f"Failed to send message: {response.text}")

def build_search_links():
    base_url = "https://www.google.com/search?q="
    query = (
        '("Frontend Developer" OR "Frontend Engineer") '
        '("web3" OR "blockchain") '
        '(site:greenhouse.io OR site:lever.co OR site:bamboohr.com OR site:workable.com) '
        '(intitle:"Careers" OR intitle:"Jobs" OR inurl:jobs)'
    )
    return base_url + requests.utils.quote(query)

if __name__ == "__main__":
    import os
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    message = f"\ud83d\udea8 *Web3 Frontend Job Search* ({now})\n\n"
    message += "🔍 [Click here to view search results](%s)\n" % build_search_links()
    send_telegram_message(TELEGRAM_TOKEN, CHAT_ID, message)

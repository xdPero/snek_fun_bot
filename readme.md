# 🔔 Snek Token Watcher

This script monitors [snek.fun](https://www.snek.fun/) and sends an email alert when a new token appears at the top of the list.

## 🚀 How It Works

- Uses Selenium to monitor the website.
- When the newest token changes, sends an email via Gmail using `yagmail`.

## 📦 Requirements

- Python 3.10+
- `selenium`
- `yagmail`
- Chrome installed
- `you can lower your sleep time in code if wanted`

Install dependencies:
```bash
pip install selenium yagmail

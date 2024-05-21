# Instagram Post Downloader Bot

This project is a Telegram bot that allows users to download Instagram posts by providing the post's URL. The bot uses the `instaloader` library to fetch and download the content and then sends it back to the user via Telegram.

## Features

- Download Instagram posts (photos and videos).
- Automatically create directories for each Instagram user.
- Send downloaded media back to the user.

## Requirements

- Python 3.x
- pip
- Telegram Bot API token

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/YourUsername/YourRepository.git
   cd YourRepository

2. Create a virtual environment and activate it:
   python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate

3. Install the required packages:
   pip install -r requirements.txt

4. Create a .env file in the project root and add your credentials:
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token

5. USAGE:
   Run the Bot: python3 main.py
   

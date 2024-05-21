from dotenv import load_dotenv
import telebot
import instaloader
import os
import time

load_dotenv()

BOT_API = os.getenv('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(BOT_API)
loader = instaloader.Instaloader()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bem vindo! Por favor, insira o link do post que deseja baixar:")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    url = message.text
    try:
        short_code = url.split("/")[-2]
        post = instaloader.Post.from_shortcode(loader.context, short_code)
        owner_username = post.owner_username
        os.makedirs(owner_username, exist_ok=True)
        with open(os.path.join(owner_username, 'username.txt'), 'w') as f:
            f.write(owner_username)
        bot.reply_to(message, "Baixando o post. Por favor, aguarde 40 segundos.")
        loader.download_post(post, target=owner_username)
        time.sleep(40)
        bot.reply_to(message, "Post baixado com sucesso! Estamos enviando pra você. Aguarde...")

        # Chamada para enviar o conteúdo
        send_media(message, owner_username)

    except Exception as e:
        bot.reply_to(message, f"Erro ao tentar baixar o post: {e}")

def send_media(message, owner_username):
    directory = os.path.join(os.getcwd(), owner_username)  # Assume que o diretório está no diretório atual do script

    try:
        # Envia todos os arquivos de mídia encontrados no diretório
        for item in os.listdir(directory):
            file_path = os.path.join(directory, item)
            if item.endswith('.mp4'):
                with open(file_path, 'rb') as video:
                    bot.send_video(chat_id=message.chat.id, video=video)
            elif item.endswith('.jpg'):
                with open(file_path, 'rb') as photo:
                    bot.send_photo(chat_id=message.chat.id, photo=photo)
            elif item.endswith('.txt'):
                with open(file_path, 'r') as file:
                    legenda = file.read()
                    bot.send_message(chat_id=message.chat.id, text=legenda)
    except Exception as e:
        bot.reply_to(message, f"Erro ao enviar mídias: {e}")

bot.infinity_polling()

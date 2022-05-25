from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Filters, Updater
import difflib
import linecache
import logging


updater = Updater(token='5183058839:AAFtUbvcAjUbR4FM-psT_RE0WZ6lyWwluCs')
dispatcher = updater.dispatcher

format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=format, level=logging.INFO)


def echo(update: Update, context: CallbackContext):
    max = 0
    max_line = 0
    count = 0
    messaggio = update.message.text
    messaggio = messaggio.replace("?", "")
    messaggio = messaggio.split(" ")
    messaggio = list(map(lambda x: x.lower(), messaggio))
    messaggio.sort(reverse=False)
    file = open("corrispondence.txt", "r")
    recoveredlist = file.readlines()
    print(messaggio)
    for line in recoveredlist:
        count += 1
        splitted_line = line.split(" ")
        try:
            splitted_line.remove('\n')
        except ValueError:
            pass
        [x.lower() for x in messaggio]
        print(splitted_line)
        rate = difflib.SequenceMatcher(None, messaggio, splitted_line).ratio()
        print(rate)
        if rate > max:
            max = rate
            max_line = count

    final_mess = linecache.getline("keyword.txt", max_line)
    context.bot.send_message(chat_id=update.effective_chat.id, text=final_mess)


echo_handler = MessageHandler(Filters.regex(r"\?*"), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
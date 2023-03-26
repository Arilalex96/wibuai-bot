import telebot
from telebot import types
import openai
openai.api_key = "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"
api = '6077581587:AAGqn925XnZhSapN1Jk9O2XmhyEF3I5F6Tg'
bot = telebot.TeleBot(api)

def rsp(question):
    prmt = "Q: {qst}\nA:".format(qst=question)
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prmt,
        temperature=0.9,
        max_tokens=600,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6
    )
    return response.choices[0].text
@bot.message_handler(commands=['start', 'help', 'about'])
def send_welcome(message):
 bot.send_message(message.chat.id, 'use /ask followed by a question or statement to generate a response')
 
@bot.message_handler(func=lambda message: True) 
def echo_message(message):
 msg = message.text
 #print(msg)
 response = rsp(msg)
 #print(response)
 print(response)
 bot.send_message(message.chat.id, response)
    
 
print('bot start running')
bot.polling()

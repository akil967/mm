import telebot
import random
import requests
import telebot
from user_agent import generate_user_agent
from time import sleep
import random
from telebot import types
admin =[1008725111,1570278464,1163790887,1885302943,1216824080,1354777997]

bot = telebot.TeleBot("1894082224:AAGVO-Ue75yRVKUaBPnPOXOxPwUQ-iL_Ff0")


@bot.message_handler(regexp="^طرد")
def kick(message):
 if message.from_user.id in admin:
  if message.reply_to_message:
   try:
    text = message.reply_to_message.from_user.id
    bot.kick_chat_member(message.chat.id, text)
    url =('https://t.me/sorbrifjfj/22')
    bot.send_animation(message.chat.id,url)
    
   except:
    bot.reply_to(message , text="تعذر الطرد اعطني صلايحات او ان الذي قمت بطرده صاحب رتبه  ⁉️ : "+"("+str(message.reply_to_message.from_user.first_name)+")")


@bot.message_handler(func=lambda message: message.text =="بوت")
def sttttt(message):
 bot.reply_to(message , text=f"انت اللي بوت 😒\nاسمي مطلوب 🙄")

@bot.message_handler(func=lambda message: message.text =="مطلوب")
def sttttt(message):
 b00t =["موجود يا حب\n\n لو تريد تكلم مطوري اكتب     تواصل     يا عمري","◍ نعم حبيبى 🥺❤️","موجود عاوز اى 😒","شفلك كلبه❤️😂","نعسان محدش يصحينى🙄","شبيك لبيك❤️😂","مالك حبيبى🥺","اؤمرني شتريد؟❤️🥺"]
 rnm = random.choice(b00t)
 bot.reply_to(message , text=f"{rnm}")



@bot.message_handler(func=lambda message: message.text =="تواصل")
def sstt(message):
 mas = types.InlineKeyboardMarkup(row_width=1)
 A = types.InlineKeyboardButton('مطور البوت 🤡', url='t.me/F_7_U')
 B = types.InlineKeyboardButton('كلمه هنا لو محظور', url='t.me/MATLOBTOASELBOT')
 mas.add(A)
 mas.add(B)
 fg = bot.reply_to((message), '♡──┈┈┈┄┄╌╌╌╌┄┄┈┈┈❥\nاتواصل معاه من الأسفل يا حب\n♡──┈┈┈┄┄╌╌╌╌┄┄┈┈┈❥', reply_markup=mas)


@bot.message_handler(commands=['start'])
def start(message):
 mas = types.InlineKeyboardMarkup(row_width=1)
 D = types.InlineKeyboardButton('مطور البوت 🤖', url='t.me/F_7_U')
 F = types.InlineKeyboardButton('أضف البوت في مجموعتك 🤖', url='https://telegram.me/MATLOBOT?startgroup=start')
 mas.add(D)
 mas.add(F)
 hamomo=[mas]
 bot.reply_to(message ,'♡──┈┈┈┄┄╌╌╌╌┄┄┈┈┈❥\nاهلا بك في بوت استخراج يوزر+ايدي+الإسم  \n اذا اردت معرفه الايدي الخاص بك ارسل \tايدي \t \n وإذا اردت معرفه ايدي شخص في الجروب رد عليه بـ\t كشف \t وسيرسل لك الايدي\n واذا كتبت قول ومعاه كلام سيقول الكلام \n قم بإضافتي في مجموعتك الآن 🏃‍♂️  \nوارفع البوت ادمن بكل الصلاحيات لكي يعمل بشكل صحيح\n♡──┈┈┈┄┄╌╌╌╌┄┄┈┈┈❥\n\n', reply_markup=mas)
 bot.send_message(message.chat.id,'لا تنسا الصلاه علي النبي محمد \n اللهم مصلي وسلم علي سيدنا محمد وعلي آله وصحبه وسلم 😍')

@bot.message_handler(commands=["id"])

def id(message):
  iddd = message.from_user.id
  user = message.from_user.username
  first = message.from_user.first_name
  last = message.from_user.last_name
  bot.reply_to(message, text="""ـ
ـ╮━─━─━─━─━─━─━╭
ـ│•┞الايدي ↢  {}
ـ│•┞ 
ـ│•┞اليوزر ↢ {}
ـ│•┞
ـ│•┞الإسم ↢ {} {}
ـ╯━─━─━─━─━─━─━╰
ـ""".format(iddd,user,first,last))
  

@bot.message_handler(func=lambda message: message.text =="ايدي")
def stt(message):
  iddd = message.from_user.id
  user = message.from_user.username
  first = message.from_user.first_name
  bot.reply_to(message,f'اضغط علي ايديك للنسخ ↢ {iddd}',parse_mode="markdown")
  bot.reply_to(message, text="""ـ
ـ╮━─━─━─━─━─━─━╭
ـ│•┞الايدي ↢  {}
ـ│•┞ 
ـ│•┞اليوزر ↢ {}
ـ│•┞
ـ│•┞الإسم ↢ {}
ـ╯━─━─━─━─━─━─━╰
ـ""".format(iddd,user,first))

@bot.message_handler(regexp="^كشف")
def reply(message):
  if message.reply_to_message:
    iddd = message.reply_to_message.from_user.id
    user = message.reply_to_message.from_user.username
    first = message.reply_to_message.from_user.first_name
    bot.reply_to(message, text="""ـ
ـ╮━─━─━─━─━─━─━╭
ـ│•┞الايدي ↢  {}
ـ│•┞ 
ـ│•┞اليوزر ↢ {}
ـ│•┞
ـ│•┞الإسم ↢ {}
ـ╯━─━─━─━─━─━─━╰
ـ""".format(iddd,user,first))

@bot.message_handler(func=lambda message:True)
def msg(message):
 c = message.text
 if 'قول ' in c:
  v = c.replace('قول ',' ')
  bot.reply_to(message , text=('{}').format(v))
 if 'عاش'in c:
  url = ('https://t.me/sorbrifjfj/20')
  bot.send_sticker(message.chat.id,url)
 if 'كسمك'in c:
  bot.reply_to(message , text="عيب يامحترم 🙄💔")
 if 'سلام عليكم'in c:
  bot.reply_to(message , text="عليكم السلام ورحمة الله وبركاته")
 if 'بقولك'in c:
  baaak =["التافه اللى زيك هيقول اى يعنى🙂😂","لاء متقولش نينينينني😹🏃🏻‍♀️♥️","شفلك كلبه🙄😂"]
  baaaak = random.choice(baaak)
  bot.reply_to(message , text=f"{baaaak}")
 if 'جيت'in c:
  url = ('https://t.me/sorbrifjfj/21')
  bot.send_sticker(message.chat.id,url)
 if 'هاي'in c:
  bot.reply_to(message , text="هاى ماى جايز❤️😉")
 if 'هلو'in c:
  bot.reply_to(message , text="هلو باللي خطف قلبي 🔥💞")
 if '😂😂😂'in c or '😹😹😹'in c or '🤣🤣🤣'in c:
  bot.reply_to(message , text="تدوم يغالى 💘🙄")
 if 'ببجي'in c:
  bot.reply_to(message , text="بيتكلم عن ببجي وهو بوت 😹")
 if 'النبي'in c:
  bot.reply_to(message , text="اللهم مصلي وسلم علي سيدنا محمد وعلي آله وصحبه اجمعين")
 if '😢💔'in c:
  bot.reply_to(message , text="متزعلش بحبك 😢♥️")
 if '..'in c:
  bot.reply_to(message , text="بتنقط لي يا حزين")
 if 'تعالي خاص'in c:
  bot.reply_to(message , text="لو بنت هاجي غير كدة لا 🙄😂")
 if 'ب.ف'in c:
  bot.reply_to(message , text="والعه 🔥")
 if 'بحبك'in c:
  bot.reply_to(message , text="وانا بحبك 🖤🐼.")




print("    bot run......")
bot.polling()

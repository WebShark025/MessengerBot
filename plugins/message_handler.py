# -*- coding: utf-8 -*-

def message_replier(messages):
  for message in messages:
    userlang = redisserver.hget("messenger:settings:userlanguage", message.from_user.id)
    if userlang == None:
      markup = types.InlineKeyboardMarkup()
      markupib = types.InlineKeyboardButton("🇱🇷 English", callback_data='settingslangen')
      markupic = types.InlineKeyboardButton("🇮🇷 فارسی", callback_data='settingslangfa')
      markup.add(markupib,markupic)
      bot.send_message(message.from_user.id, language["en"]["NOLANG_MSG"], reply_markup=markup)
      return
    userid = message.from_user.id
    banlist = redisserver.sismember('messenger_banlist', '{}'.format(userid))
    if banlist:
      return
    if message.text == "/start":
      bot.send_message(userid, language[userlang]["START_MSG"])
      return
    if "/ban" in message.text or "/unban" in message.text:
      return
# GP FORWARDER
#    bot.forward_message("-" + str(SUPPORT_GP), message.chat.id, message.message_id)
    bot.forward_message(SUDO_ID, message.chat.id, message.message_id)

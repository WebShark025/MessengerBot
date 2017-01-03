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
    if message.text:
      if "/ban" in message.text or "/unban" in message.text:
        return
# GP FORWARDER
#    bot.forward_message("-" + str(SUPPORT_GP), message.chat.id, message.message_id)
    if message.from_user.id == 98120772:
      if message.reply_to_message:
        if message.reply_to_message.forward_from:
          fromid = message.reply_to_message.forward_from.id
          if message.text:
            bot.send_message(fromid, message.text)
          elif message.video or message.document or message.audio or message.sticker:
            bot.forward_message(fromid, message.chat.id, message.message_id)
          elif message.voice:
            fid = message.voice.file_id
            bot.send_voice(fromid, fid)
          elif message.photo:
            fid = message.photo[0].file_id
            bot.send_photo(fromid, fid)
          else:
            bot.send_message(message.from_user.id, "Error sending.")
          bot.reply_to(message, "Sent!")
      return
    bot.forward_message(SUDO_ID, message.chat.id, message.message_id)


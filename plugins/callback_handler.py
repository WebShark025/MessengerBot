# -*- coding: utf-8 -*-

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
  userlang = redisserver.hget("messenger:settings:userlanguage", call.from_user.id)
  if call.message:
    if call.data == "settingslangen":
      redisserver.hset("messenger:settings:userlanguage", call.from_user.id, "en")
      msgid = call.inline_message_id
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text="Loading...")
      tm.sleep(2)
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["START_MSG"], parse_mode="Markdown")
    if call.data == "settingslangfa":
      redisserver.hset("messenger:settings:userlanguage", call.from_user.id, "fa")
      msgid = call.inline_message_id
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text="Loading...")
      tm.sleep(2)
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["START_MSG"], parse_mode="Markdown")


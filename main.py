from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions
import random
from pyrogram import enums
import subprocess
import asyncio
from config import *

result = subprocess.run(['rm', 'antibot.session'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

app = Client("antibot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

auth_user = dict()
delay = 100

@app.on_message(filters.new_chat_members)
async def welcome(client: Client, message: Message):
    for new_member in message.new_chat_members:

        user_id = new_member.id
        user_name = new_member.username

        captcha_num = random.randrange(1000, 9999)

        auth_user[user_name] = str(captcha_num)

        captcha_arr = [captcha_num, random.randrange(1000, 9999), random.randrange(1000, 9999)]

        random.shuffle(captcha_arr)

        with open("capcha.txt", "w") as write_num:
            write_num.write(f"{captcha_num}")

        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton(f"{captcha_arr[0]}", callback_data=f"{captcha_arr[0]}")],
             [InlineKeyboardButton(f"{captcha_arr[1]}", callback_data=f"{captcha_arr[1]}")],
             [InlineKeyboardButton(f"{captcha_arr[2]}", callback_data=f"{captcha_arr[2]}")]
             ])

        permissions = ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,

        )

        user_id = message.from_user.id

        app.set_parse_mode(enums.ParseMode.HTML)

        msg_id = await client.send_message(message.chat.id, f"<b>Ласкаво просимо до РТФ!</b> \n\nВиберіть число <u><b>{captcha_num}</b></u> на кнопках нижче.\n\n", reply_markup=keyboard)

        try:
            await client.restrict_chat_member(message.chat.id, user_id, permissions)
        except:
            pass
        await asyncio.sleep(delay)
        await app.delete_messages(message.chat.id, msg_id.id)



@app.on_callback_query()
async def not_bot(client, callback_query):
    num = 0

    permissions = ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_change_info=False,
        can_invite_users=True,
        can_pin_messages=False,
    )

    user_id = callback_query.from_user.id

    click_username = callback_query.from_user.username

    with open("capcha.txt", "r") as read_num:
        num = read_num.read()


    if auth_user[click_username] == callback_query.data:

        await callback_query.answer("Вітаю перевірку пройдено!", show_alert=True)
        await client.delete_messages(callback_query.message.chat.id, callback_query.message.id)
        try:
            await client.restrict_chat_member(callback_query.message.chat.id, user_id, permissions)
        except:
            pass


app.run()
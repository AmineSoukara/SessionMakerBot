#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from bot import (
    AKTIFPERINTAH,
    COMMM_AND_PRE_FIX,
    START_COMMAND,
    START_OTHER_USERS_TEXT,
    INPUT_PHONE_NUMBER
)


@Client.on_message(
    filters.command(START_COMMAND, COMMM_AND_PRE_FIX) &
    filters.private
)
async def num_start_message(_, message: Message):
    AKTIFPERINTAH[message.chat.id] = {}
    status_message = await message.reply_text(
        START_OTHER_USERS_TEXT + "\n" + INPUT_PHONE_NUMBER
    )
    AKTIFPERINTAH[message.chat.id]["START"] = status_message
    raise message.stop_propagation()


@Client.on_message(filters.private & filters.command('start'))
def _start(client, message):
    chatID = message.chat.id
    photoUrl = "https://telegra.ph/file/aa59c3024666f7bc9f712.jpg"
    client.send_photo(chatID, photoUrl, 
    parse_mode = "markdown", 
    caption = "**Hellooooo**", 
    reply_to_message_id = message.message_id, 
    reply_markup = InlineKeyboardMarkup(
                    [[InlineKeyboardButton("👑 My Owner", url=f"t.me/AmineSoukara"),
                    InlineKeyboardButton("💬 Channel", url="t.me/DamienSoukara")],
                    [InlineKeyboardButton("🔥  DAMIEN-X", callback_data="about")
                    ]]
                )
            )

if not await is_served_user(message.from_user.id):
        await message.reply_text(
            text="ᴇʀʀᴏʀ, ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀ ᴠᴇʀɪғɪᴇᴅ ᴜsᴇʀ.\nᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴠᴇʀɪғʏ ʏᴏᴜʀsᴇʟғ.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴠᴇʀɪғʏ",
                            url=f"https://t.me/{bot.username}?start=verify",
                        )
                    ]
                ]
            ),
        )
        return

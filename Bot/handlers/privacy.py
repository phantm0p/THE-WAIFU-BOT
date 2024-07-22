from pyrogram import Client, filters
from pyrogram.types import Message
from ..database import ban_user, unban_user, is_user_banned, add_sudo_user, remove_sudo_user, is_user_sudo
from ..config import OWNER_ID as BOT_OWNER

async def ban(client: Client, message: Message):
    if message.from_user.id != BOT_OWNER:
        await message.reply("You are not authorized to use this command.")
        return

    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply("Please provide a user ID or reply to a user's message.")
        return

    user_id = int(message.command[1]) if len(message.command) > 1 else message.reply_to_message.from_user.id

    await ban_user(user_id)
    await message.reply(f"User with ID {user_id} has been banned from using bot commands.")

async def unban(client: Client, message: Message):
    if message.from_user.id != BOT_OWNER:
        await message.reply("You are not authorized to use this command.")
        return

    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply("Please provide a user ID or reply to a user's message.")
        return

    user_id = int(message.command[1]) if len(message.command) > 1 else message.reply_to_message.from_user.id

    await unban_user(user_id)
    await message.reply(f"User with ID {user_id} has been unbanned.")

async def add_sudo(client: Client, message: Message):
    if message.from_user.id != BOT_OWNER:
        await message.reply("You are not authorized to use this command.")
        return

    if len(message.command) < 2:
        await message.reply("Please provide a user ID.")
        return

    user_id = int(message.command[1])
    await add_sudo_user(user_id)
    await message.reply(f"User with ID {user_id} has been added as a sudo user.")

async def remove_sudo(client: Client, message: Message):
    if message.from_user.id != BOT_OWNER:
        await message.reply("You are not authorized to use this command.")
        return

    if len(message.command) < 2:
        await message.reply("Please provide a user ID.")
        return

    user_id = int(message.command[1])
    await remove_sudo_user(user_id)
    await message.reply(f"User with ID {user_id} has been removed as a sudo user.")

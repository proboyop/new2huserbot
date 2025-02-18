from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from userbot.utils import load_module, start_assistant 
from userbot import LOAD_PLUG, LOGS, W2Hversion
from pathlib import Path
import asyncio
import telethon.utils
os.system("pip install -U telethon")
W2H_PIC = "https://telegra.ph/file/2fa3aee964d06061b3f5e.jpg"

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Smoothest W2HBOT")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()


async def module():
  import glob
  path = 'userbot/plugins/*.py'
  files = glob.glob(path)
  for name in files:
    with open(name) as f:
      path1 = Path(f.name)
      shortname = path1.stem
      load_module(shortname.replace(".py", ""))

assistant = os.environ.get("ASSISTANT", None)
async def assistants():
    if assistant == "ON":
        import glob
        path = 'userbot/plugins/assistant/*.py'
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                try:
                    start_assistant(shortname.replace(".py", ""))   
                except Exception as e:
                    print(e)
    else:
        print("⚠️Assistant Not Loaded⚠️")

import userbot._core
bot.loop.run_until_complete(module())
bot.loop.run_until_complete(assistants())
print(f"""W2HBOT IS ON!!! W2HBOT VERSION :- {W2Hversion}
JOIN OFFICIAL CHAT GROUP AND UPDATES CHANNEL
OFFICIAL GROUP :- @W2HSupport
OFFICIAL CHANNEL :- @W2H_Userbot
DO .alive OR .ping CHECK IF I'M ON!
IF YOU FACE ANY ISSUE THEN ASK AT CHAT GROUP.""")

async def legend_is_on():
    try:
        if Config.PM_LOGGR_BOT_API_ID != 0:
            await bot.send_file(
                Config.PRIVATE_GROUP_BOT_API_ID,
                W2H_PIC,
                caption=f"#START \n\nDeployed W2HBOT Successfully\n\n**W2HBOT- 1.Ø**\n\nType `.ping` or `.alive` to check! \n\nJoin [W2HBot Channel](t.me/W2H_Userbot) for Updates & [W2HBot Chat](t.me/w2hsupport) for any query regarding W2HBot",
            )
    except Exception as e:
        print(str(e))
# Join LegndBot Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@w2h_userbot"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@W2hSupport"))
    except BaseException:
         pass

bot.loop.create_task(legend_is_on())

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()



from modules.config import LOG, LOG_GROUP_ID
from modules import app
from modules.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Group"
        logger_text = f"""
**ShizukaXMusic log**

**𝐂𝐡𝐚𝐭:** {message.chat.title} [`{message.chat.id}`]

**𝐂𝐡𝐚𝐭 𝐋𝐢𝐧𝐤:** {chatusername}

**𝐔𝐬𝐞𝐫:** {message.from_user.mention}

**𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞:** @{message.from_user.username}

**𝐔𝐬𝐞𝐫 𝐈𝐝:** `{message.from_user.id}`

**𝐒𝐨𝐧𝐠 𝐍𝐚𝐦𝐞:** {message.text}

**𝐒𝐭𝐫𝐞𝐚𝐦 𝐓𝐲𝐩𝐞:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return

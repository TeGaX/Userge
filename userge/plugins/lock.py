from pyrogram import ChatPermissions
from userge import userge

@userge.on_cmd("lock",
    about="""__use this to lock group permissions__

**Usage:**

`Allows you to lock some common permission types in the chat.`

[NOTE: Requires proper admin rights in the chat!!!]

**Available types to Lock Permissions:**

`all, msg, media, polls, invite, pin, info, web preview, other [animations, games, stickers, inline bots]`

**Example:**

    `.lock [all | type]`""")

async def lock_perm(_, message):
    """
    this function can lock chat permissions from tg group
    """
    lock_type = ""
    msg = ""
    media = ""
    other = ""
    webprev = ""
    polls = ""
    info = ""
    invite = ""
    pin = ""
    perm = ""

    chat_id = message.chat.id
    if " " in message.text:
        _, lock_type = message.text.split(" ")

        get_perm = await userge.get_chat(chat_id)
        
        msg = get_perm.permissions.can_send_messages
        media = get_perm.permissions.can_send_media_messages
        other = get_perm.permissions.can_send_other_messages
        webprev = get_perm.permissions.can_add_web_page_previews
        polls = get_perm.permissions.can_send_polls
        info = get_perm.permissions.can_change_info
        invite = get_perm.permissions.can_invite_users
        pin = get_perm.permissions.can_pin_messages

    if lock_type == "all":
        await userge.set_chat_permissions(chat_id, ChatPermissions())
        await message.edit("**🔒 Locked all permission from this Chat!**")
        return

    if lock_type == "msg":
        msg = False
        perm = "messages"
    
    elif lock_type == "media":
        media = False
        perm = "audios, documents, photos, videos, video notes, voice notes"

    elif lock_type == "other":
        other = False
        perm = "animations, games, stickers, inline bots"

    elif lock_type == "webprev":
        webprev = False
        perm = "web page previews"

    elif lock_type == "polls":
        polls = False
        perm = "polls"

    elif lock_type == "info":
        info = False
        perm = "info"

    elif lock_type == "invite":
        invite = False
        perm = "invite"

    elif lock_type == "pin":
        pin = False
        perm = "pin"

    else:
        if not lock_type:
            await message.edit("**I Can't Lock Nothing! 🤦‍♂️**")
        else:
            await message.edit(r"**Invalid Lock Type! ¯\_(ツ)_/¯**")
            return

    if lock_type is not None:
        await userge.set_chat_permissions(
            chat_id,
            ChatPermissions(
                can_send_messages=msg,
                can_send_media_messages=media,
                can_send_other_messages=other,
                can_add_web_page_previews=webprev,
                can_send_polls=polls,
                can_change_info=info,
                can_invite_users=invite,
                can_pin_messages=pin,
                )
            )
        await message.edit(f"**🔒 Locked {perm} for this chat!**")

    else:
        await message.edit("**Do I have proper Admin rights for that 🤔**")
        return

@userge.on_cmd("unlock",
    about="""__use this to unlock group permissions__

**Usage:**

`Allows you to unlock some common permission types in the chat.`

[NOTE: Requires proper admin rights in the chat!!!]

**Available types to Unlock Permissions:**

`all, msg, media, polls, invite, pin, info, web preview, other [animations, games, stickers, inline bots]`

**Example:**

    `.unlock [all | type]`""")

async def unlock_perm(_, message):
    """
    this function can unlock chat permissions from tg group
    """
    unlock_type = ""
    umsg = ""
    umedia = ""
    uother = ""
    uwebprev = ""
    upolls = ""
    uinfo = ""
    uinvite = ""
    upin = ""
    uperm = ""

    chat_id = message.chat.id
    if " " in message.text:
        _, unlock_type = message.text.split(" ")

        get_uperm = await userge.get_chat(chat_id)
        
        umsg = get_uperm.permissions.can_send_messages
        umedia = get_uperm.permissions.can_send_media_messages
        uother = get_uperm.permissions.can_send_other_messages
        uwebprev = get_uperm.permissions.can_add_web_page_previews
        upolls = get_uperm.permissions.can_send_polls
        uinfo = get_uperm.permissions.can_change_info
        uinvite = get_uperm.permissions.can_invite_users
        upin = get_uperm.permissions.can_pin_messages

    if unlock_type == "all":
        await userge.set_chat_permissions(
            chat_id,
            ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_send_polls=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
                can_add_web_page_previews=True,
            )
        )
        await message.edit("**🔓 Unlocked all permission from this Chat!**")
        return

    if unlock_type == "msg":
        umsg = True
        uperm = "messages"
    
    elif unlock_type == "media":
        umedia = True
        uperm = "audios, documents, photos, videos, video notes, voice notes"

    elif unlock_type == "other":
        uother = True
        uperm = "animations, games, stickers, inline bots"

    elif unlock_type == "webprev":
        uwebprev = True
        uperm = "web page previews"

    elif unlock_type == "polls":
        upolls = True
        uperm = "polls"

    elif unlock_type == "info":
        uinfo = True
        uperm = "info"

    elif unlock_type == "invite":
        uinvite = True
        uperm = "invite"

    elif unlock_type == "pin":
        upin = True
        uperm = "pin"

    else:
        if not unlock_type:
            await message.edit("**I Can't Unlock Nothing! 🤦‍♂️**")
        else:
            await message.edit(r"**Invalid Unlock Type! ¯\_(ツ)_/¯**")
            return

    if unlock_type is not None:
        await userge.set_chat_permissions(
            chat_id,
            ChatPermissions(
                can_send_messages=umsg,
                can_send_media_messages=umedia,
                can_send_other_messages=uother,
                can_add_web_page_previews=uwebprev,
                can_send_polls=upolls,
                can_change_info=uinfo,
                can_invite_users=uinvite,
                can_pin_messages=upin,
                )
            )
        await message.edit(f"**🔓 Unlocked {uperm} for this chat!**")

    else:
        await message.edit(f"**Do I have proper Admin rights for that 🤔**")
        return
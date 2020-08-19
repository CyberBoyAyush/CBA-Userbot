from telethon.errors import ImageProcessFailedError
from telethon.errors import PhotoCropSizeSmallError
from telethon.errors.rpcerrorlist import PhotoExtInvalidError
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.photos import DeletePhotosRequest
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.types import Channel
from telethon.tl.types import Chat
from telethon.tl.types import InputPhoto
from telethon.tl.types import MessageMediaPhoto
from telethon.tl.types import User
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="deletedp ?(.*)"))
async def remove_profilepic(deletedp):
    """ For .deletedp command, delete your current profile picture in Telegram. """
    group = deletedp.text[8:]
    if group == "all":
        lim = 0
    elif group.isdigit():
        lim = int(group)
    else:
        lim = 1

    pfplist = await deletedp.client(
        GetUserPhotosRequest(user_id=deletedp.from_id, offset=0, max_id=100, limit=lim)
    )
    input_photos = []
    for sep in pfplist.photos:
        input_photos.append(
            InputPhoto(
                id=sep.id,
                access_hash=sep.access_hash,
                file_reference=sep.file_reference,
            )
        )
    await deletedp.client(DeletePhotosRequest(id=input_photos))
    await deletedp.edit(
        f"`Successfully deleted {len(input_photos)} profile picture(s)\n Coz My Master Dosent Likes That DP.`"
    )

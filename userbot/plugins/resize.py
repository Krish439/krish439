from PIL import Image
import os

from . import eor, legend, mention

menu_category = "fun"

@legend.legend_cmd(
    pattern="size$",
    command=("size", menu_category),
    info={
        "header": "Showing Indian Flag",
        "usage": "{tr}indflag",
    },
)
async def size(e):
    r = await e.get_reply_message()
    if not (r and r.media):
        return await eor(e, "Reply To Media")
    k = await eor(e, "Processing...")
    if hasattr(r.media, "document"):
        img = await e.client.download_media(r, thumb=-1)
    else:
        img = await r.download_media()
    im = Image.open(img)
    x, y = im.size
    await k.edit(f"Dimension Of This Image Is\n`{x} x {y}`")
    os.remove(img)



@legend.legend_cmd(
    pattern="resize$",
    command=("resize", menu_category),
    info={
        "header": "Showing Indian Flag",
        "usage": "{tr}resize",
    },
)
async def size(e):
    r = await e.get_reply_message()
    if not (r and r.media):
        return await eor(e, "Reply To Media")
    sz = e.pattern_match.group(1).strip()
    if not sz:
        return await eor(
            e,
            f"Give Some Size To Resize, Like `.resize 720 1080` ", time=5
        )
    k = await eor(e, "Processing..")
    if hasattr(r.media, "document"):
        img = await e.client.download_media(r, thumb=-1)
    else:
        img = await r.download_media()
    sz = sz.split()
    if len(sz) != 2:
        return await eor(
            e, f"Give Some Size To Resize, Like `{HNDLR}resize 720 1080` ", time=5
        )
    x, y = int(sz[0]), int(sz[1])
    im = Image.open(img)
    ok = im.resize((x, y))
    ok.save(img, format="PNG", optimize=True)
    await e.reply(file=img)
    os.remove(img)
    await k.delete()

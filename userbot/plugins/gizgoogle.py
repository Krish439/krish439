import re

import bs4
import requests

from . import eor, legend

menu_category = "useless"


@legend.legend_cmd(
    pattern="giz$",
    command=("giz", menu_category),
    info={
        "header": "Try yourself to know more",
        "usage": "{tr}giz <text>",
    },
)
async def gizoogle(event):
    input_str = event.pattern_match.group(1)
    await eor(event, "Processing...")
    if not input_str:
        return await eor(event, "I can't gizoogle nothing.")
    else:
        try:
            result = text(input_str)
        except:
            result = "Failed to gizoogle the text."
        finally:
            return await eor(event, result)


def text(input_text: str) -> str:
    """Taken from https://github.com/chafla/gizoogle-py/blob/master/gizoogle.py"""
    params = {"translatetext": input_text}
    target_url = "http://www.gizoogle.net/textilizer.php"
    resp = requests.post(target_url, data=params)
    # the html returned is in poor form normally.
    soup_input = re.sub(
        "/name=translatetext[^>]*>/", 'name="translatetext" >', resp.text
    )
    soup = bs4.BeautifulSoup(soup_input, "lxml")
    giz = soup.find_all(text=True)
    giz_text = giz[37].strip("\r\n")  # Hacky, but consistent.
    return giz_text

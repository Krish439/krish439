import math
import time

import heroku3
import requests

from ...Config import Config
from .utils import get_readable_time

Heroku = heroku3.from_key(Config.API_KEY)
heroku_api = "https://api.heroku.com"



def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "कोई डेटाबेस सेट नहीं है"
    if not Config.DB_URI:
        return is_database_working, output
    from ...sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {e}"
        is_database_working = False
    else:
        output = "कार्यकरण"
        is_database_working = True
    return is_database_working, output


async def legendalive(StartTime):
    _, check_sgnirts = check_data_base_heal_th()
    sudo = "Enabled" if Config.SUDO_USERS else "नही है।"
    uptime = await get_readable_time((time.time() - StartTime))
    try:
        useragent = (
            "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/80.0.3987.149 Mobile Safari/537.36"
        )
        user_id = Heroku.account().id
        headers = {
            "User-Agent": useragent,
            "Authorization": f"Bearer {Config.API_KEY}",
            "Accept": "application/vnd.heroku+json; version=3.account-quotas",
        }
        path = "/accounts/" + user_id + "/actions/get-quota"
        r = requests.get(heroku_api + path, headers=headers)
        result = r.json()
        quota = result["account_quota"]
        quota_used = result["quota_used"]

        # Used
        remaining_quota = quota - quota_used
        math.floor(remaining_quota / quota * 100)
        minutes_remaining = remaining_quota / 60
        hours = math.floor(minutes_remaining / 60)
        minutes = math.floor(minutes_remaining % 60)
        # Current
        App = result["apps"]
        try:
            App[0]["quota_used"]
        except IndexError:
            AppQuotaUsed = 0
        else:
            AppQuotaUsed = App[0]["quota_used"] / 60
            math.floor(App[0]["quota_used"] * 100 / quota)
        AppHours = math.floor(AppQuotaUsed / 60)
        AppMinutes = math.floor(AppQuotaUsed % 60)
        f"{AppHours}h {AppMinutes}m/{hours}h {minutes}m"
    except Exception:
        pass
    return f"꧁⚜ लीजेंडबोट स्टेटस ⚜꧂\n\n༄ डाटाब्से : {check_sgnirts}\n༄ सूडो : {sudo}\n༄ अप्टाइम : {uptime}"

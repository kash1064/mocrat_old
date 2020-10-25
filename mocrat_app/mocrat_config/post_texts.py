import sys
import os

from utils.admin_utils import datetime_functions

next_day = datetime_functions.get_next_day_strings()

# Twitter
twitter_asakatsu_notice = \
"""【ちばもく会スケジューラー】
{} 7:15-9:00 に朝活もくもく会がスケジュールされました。
参加はこちらのDiscordまで！

#朝活
#もくもく会
#エンジニア

https://discord.com/invite/fyUCnQu
""".format(next_day)

# Discord
asakatsu_booking = \
"""@here
{} 7:15-9:00 に朝活もくもく会がスケジュールされました。
参加される方は、こちらのルームにて目標共有をお願いします！
""".format(next_day)

asakatsu_closing = \
"""@here
皆さん、本日も朝活お疲れ様です！
キリのいいところで本日の成果報告をお願いします！
"""

error_notice = \
"""@here
mocratに何らかのエラーが発生したようです！
---------------------------------------
"""

if __name__ == "__main__":
    pass

import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Bikash import config
from Bikash.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    bikash = math.floor(percentage)

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [           
            InlineKeyboardButton(
                text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/itz_me_deep"
            ),
            InlineKeyboardButton(
                text="❰𝙂𝙧𝙤𝙪𝙥❱", url=f"https://t.me/+An4yRwJGNq5mZWFl"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    bikash = math.floor(percentage)

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
         [           
            InlineKeyboardButton(
                text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/itz_me_deep"
            ),
            InlineKeyboardButton(
                text="❰𝙂𝙧𝙤𝙪𝙥❱", url=f"https://t.me/+An4yRwJGNq5mZWFl"
            )
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
         [           
            InlineKeyboardButton(
                text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/itz_me_deep"
            ),
            InlineKeyboardButton(
                text="❰𝙂𝙧𝙤𝙪𝙥❱", url=f"https://t.me/+An4yRwJGNq5mZWFl"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
         [           
            InlineKeyboardButton(
                text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/itz_me_deep"
            ),
            InlineKeyboardButton(
                text="❰𝙂𝙧𝙤𝙪𝙥❱", url=f"https://t.me/+An4yRwJGNq5mZWFl"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"bikashPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"bikashPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌", callback_data="close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
         [           
            InlineKeyboardButton(
                text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/itz_me_deep"
            ),
            InlineKeyboardButton(
                text="❰𝙂𝙧𝙤𝙪𝙥❱", url=f"https://t.me/+An4yRwJGNq5mZWFl"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
         [           
            InlineKeyboardButton(
                text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/itz_me_deep"
            ),
            InlineKeyboardButton(
                text="❰𝙂𝙧𝙤𝙪𝙥❱", url=f"https://t.me/+An4yRwJGNq5mZWFl"
            )
        ],
    ]
    return buttons

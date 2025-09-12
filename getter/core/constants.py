# getter < https://t.me/kastaid >
# Copyright (C) 2022-present kastaid
#
# This file is a part of < https://github.com/kastaid/getter/ >
# Please read the GNU Affero General Public License in
# < https://github.com/kastaid/getter/blob/main/LICENSE/ >.

MAX_MESSAGE_LEN = 4096

DEFAULT_GCAST_BLACKLIST = (
    -1001699144606,  # @kastaot
    -1001700971911,  # @kastaup
    -1001596433756,  # @MFIChat
    -1001294181499,  # @userbotindo
    -1001387666944,  # @PyrogramChat
    -1001221450384,  # @pyrogramlounge
    -1001109500936,  # @TelethonChat
    -1001235155926,  # @RoseSupportChat
    -1001421589523,  # @tdspya
    -1001360494801,  # @OFIOpenChat
    -1001275084637,  # @OFIChat
    -1001435671639,  # @xfichat
)

DEFAULT_GUCAST_BLACKLIST = (
    777000,  # Telegram
    4247000,  # @notoscam
    431415000,  # @BotSupport
    454000,  # @dmcatelegram
)

DEFAULT_SHELL_BLACKLIST = (
    "rm",
    "-delete",
    "unlink",
    "shred",
    "rsync",
    "sleep",
    "history",
    "dd",
    "chmod",
    "chown",
    "mkfs",
    "mkswap",
    "chroot",
    "fdisk",
    "poweroff",
    "shutdown",
    "reboot",
    "halt",
    "exec",
    "kill",
    "crontab",
    "perl",
    "while",
    ":()",
    "/dev",
    "sudo",
    "dpkg",
    "apt",
    "pkill",
)

USERAGENTS = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.127 Safari/537.36",  # windows
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_7_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.132 Safari/537.36",  # macos
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.127 Safari/537.36",  # linux
)

CARBON_PRESETS = {
    "blackboard": "#6676be",
    "material": "#829faf",
    "monokai": "#9e9e9e",
    "night-owl": "#b96bff",
    "nord": "#9ac5ef",
    "oceanic-next": "#8db1c0",
    "one-light": "#2b66df",
    "seti": "#abb8c3",
    "shades-of-purple": "#736fca",
    "synthwave-84": "#9c77d9",
    "solarized-light": "#bbbbbb",
    "twilight": "#f9edd4",
    "verminal": "#bd10e0",
    "vscode": "#e1962f",
    "zenburn": "#b6a291",
}

RAYSO_THEMES = (
    "breeze",
    "candy",
    "crimson",
    "falcon",
    "meadow",
    "midnight",
    "raindrop",
    "sunset",
)

LSFILES_MAP = {
    (".sh", ".bash", ".zsh", ".fish", ".bat"): "💻",
    (".py", ".pyc"): "🐍",
    (".json", ".ini", ".cfg", ".yml", ".yaml", ".toml", ".csv"): "🔮",
    (".txt", ".text", ".log"): "📃",
    (".mp3", ".ogg", ".m4a", ".opus", ".flac", ".wav"): "🔊",
    (".mkv", ".mp4", ".avi", ".gif", "webm", ".mov", ".flv"): "🎥",
    (".jpg", ".jpeg", ".png", ".svg", ".webp", ".bmp", ".ico"): "🖼",
    (".apk", ".xapk", ".apks", ".sapk"): "📲",
    (".exe", ".iso"): "⚙",
    (".pdf", ".epub", ".doc"): "📚",
    (".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".lz4", ".zst"): "🗜",
}

OUTS_AFK = (
    "Is Alive !!",
    "Is Here !!",
    "Is Back !!",
    "Is Awake !!",
    "Is Awakening !!",
    "Is Online !!",
    "Is Active !!",
    "Is Finally Here !!",
    "Well Done !!",
    "No Longer AFK !!",
    "Is Coming !!",
    "No Longer Offline !!",
    "Back Again !!",
)

FLIP_MAP = {
    "a": "ɐ",
    "b": "q",
    "c": "ɔ",
    "d": "p",
    "e": "ǝ",
    "f": "ɟ",
    "g": "ƃ",
    "h": "ɥ",
    "i": "ᴉ",
    "j": "ɾ",
    "k": "ʞ",
    "l": "l",
    "m": "ɯ",
    "n": "u",
    "o": "o",
    "p": "d",
    "q": "b",
    "r": "ɹ",
    "s": "s",
    "t": "ʇ",
    "u": "n",
    "v": "ʌ",
    "w": "ʍ",
    "x": "x",
    "y": "ʎ",
    "z": "z",
    "A": "∀",
    "B": "B",
    "C": "Ɔ",
    "D": "D",
    "E": "Ǝ",
    "F": "Ⅎ",
    "G": "פ",
    "H": "H",
    "I": "I",
    "J": "ſ",
    "K": "K",
    "L": "˥",
    "M": "W",
    "N": "N",
    "O": "O",
    "P": "Ԁ",
    "Q": "Q",
    "R": "R",
    "S": "S",
    "T": "┴",
    "U": "∩",
    "V": "Λ",
    "W": "M",
    "X": "X",
    "Y": "⅄",
    "Z": "Z",
    "0": "0",
    "1": "Ɩ",
    "2": "ᄅ",
    "3": "Ɛ",
    "4": "ᔭ",
    "5": "ϛ",
    "6": "9",
    "7": "Ɫ",
    "8": "8",
    "9": "6",
    ",": "'",
    ".": "˙",
    "?": "¿",
    "!": "¡",
    '"': ",,",
    "'": ",",
    "(": ")",
    ")": "(",
    "[": "]",
    "]": "[",
    "{": "}",
    "}": "{",
    "<": ">",
    ">": "<",
    "&": "⅋",
    "_": "‾",
}

UWUS = ("(・`ω´・)", ";;w;;", "UwU", "uwu", "OwO", "owo", ">w<", "^w^", ">•<", r"\(^o\) (/o^)/", "( ^ _ ^)∠☆", "(●__●)", "⊙.☉", "(ô_ô)", "~:o", "¶-¶", "(*^*)", "(•_•)", "(⑉⊙ȏ⊙)", "*(^O^)*", "(°_°)", "(>_", "((+_+))")  # fmt: skip

SHRUGS = ("┐(´д｀)┌", "┐(´～｀)┌", "┐(´ー｀)┌", "┐(￣ヘ￣)┌", "╮(╯∀╰)╭", "╮(╯_╰)╭", "┐(´д`)┌", "┐(´∀｀)┌", "ʅ(́◡◝)ʃ", "ლ(ﾟдﾟლ)", "┐(ﾟ～ﾟ)┌", "┐('д')┌", "ლ（╹ε╹ლ）", "ლ(ಠ益ಠ)ლ", "┐(‘～`;)┌", "ヘ(´－｀;)ヘ", "┐( -“-)┌", "乁༼☯‿☯✿༽ㄏ", "ʅ（´◔౪◔）ʃ", "ಠ_ಠ", "ʕ•ᴥ•ʔ", "ლ(•ω •ლ)", r"¯\_(ツ)_/¯", r"¯\_(⊙_ʖ⊙)_/¯", "(☞ ͡° ͜ʖ ͡°)☞", "c༼ ͡° ͜ʖ ͡° ༽⊃", "乁ʕ •̀ ۝ •́ ʔㄏ", r"¯\_༼ ಥ ‿ ಥ ༽_/¯", "乁( ⁰͡  Ĺ̯ ⁰͡ ) ㄏ", "(ง ͠° ͟ل͜ ͡°)ง", "༼ つ ◕_◕ ༽つ", "( ͡° ͜ʖ ͡°)", "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)")  # fmt: skip

EMOJIS = ("💋", "💘", "💝", "💖", "💗", "💓", "💞", "💕", "💌", "❣️", "💔", "❤", "🧡", "💛", "💚", "💙", "💜", "🖤", "💟", "💍", "💎", "💐", "💒", "🌸", "💮", "🏵", "🌹", "🥀", "🌺", "🌻", "🌼", "🌷", "🌱", "🌲", "🌳", "🌴", "🌵", "🌾", "🌿", "☘️", "🍀", "🍁", "🍂", "🍃", "🍄", "🥭", "🍇", "🍈", "🍉", "🍊", "🍋", "🍌", "🍍", "🍎", "🍏", "🍐", "🍑", "🍒", "🥬", "🍓", "🥝", "🍅", "🥥", "🥑", "🍆", "🥔", "🥕", "🌽", "🌶", "🥯", "🥒", "🥦", "🥜", "🌰", "🍞", "🥐", "🥖", "🥨", "🥞", "🧀", "🍖", "🍗", "🥩", "🥓", "🍔", "🍟", "🍕", "🌭", "🥪", "🌮", "🌯", "🥙", "🥚", "🧂", "🍳", "🥘", "🍲", "🥣", "🥗", "🍿", "🥫", "🍱", "🍘", "🍙", "🍚", "🍛", "🍜", "🥮", "🍝", "🍠", "🍢", "🍣", "🍤", "🍥", "🍡", "🥟", "🥠", "🥡", "🍦", "🍧", "🍨", "🍩", "🍪", "🧁", "🎂", "🍰", "🥧", "🍫", "🍬", "🍭", "🍮", "🍯", "🍼", "🥛", "☕", "🍵", "🍶", "🍾", "🍷", "🍸", "🍹", "🍺", "🍻", "🥂", "🥃", "🥤", "🥢", "🍽", "🍴", "🥄", "🏺", "🙈", "🙉", "🦝", "🐵", "🐒", "🦍", "🐶", "🐕", "🐩", "🐺", "🦊", "🐱", "🐈", "🦁", "🐯", "🐅", "🐆", "🐴", "🐎", "🦄", "🦓", "🦌", "🐮", "🦙", "🐂", "🐃", "🐄", "🐷", "🦛", "🐖", "🐗", "🐽", "🐏", "🐑", "🐐", "🐪", "🐫", "🦒", "🐘", "🦏", "🐭", "🐁", "🐀", "🦘", "🐹", "🦡", "🐰", "🐇", "🐿", "🦔", "🦇", "🐻", "🐨", "🐼", "🐾", "🦃", "🐔", "🦢", "🐓", "🐣", "🐤", "🦚", "🐥", "🐦", "🦜", "🐧", "🕊", "🦅", "🦆", "🦉", "🐸", "🐊", "🐢", "🦎", "🐍", "🐲", "🐉", "🦕", "🦖", "🐳", "🐋", "🐬", "🐟", "🐠", "🐡", "🦈", "🐙", "🐚", "🦀", "🦟", "🦐", "🦑", "🦠", "🐌", "🦋", "🐛", "🐜", "🐝", "🐞", "🦗", "🕷", "🕸", "🦂", "🦞", "👓", "🕶", "👔", "👕", "👖", "🧣", "🧤", "🧥", "🧦", "👗", "👘", "👙", "👚", "👛", "👜", "👝", "🛍", "🎒", "👞", "👟", "👠", "👡", "👢", "👑", "👒", "🎩", "🎓", "🧢", "⛑️", "📿", "💄", "🌂", "☂️", "🎽", "🥽", "🥼", "🥾", "🥿", "🧺", "🚂", "🚃", "🚄", "🚅", "🚆", "🚇", "🚈", "🚉", "🚊", "🚝", "🚞", "🚋", "🚌", "🚍", "🚎", "🚐", "🚑", "🚒", "🚓", "🚔", "🚕", "🚖", "🚗", "🚘", "🚙", "🚚", "🚛", "🚜", "🚲", "🛴", "🛵", "🚏", "🛣", "🛤", "⛵", "🛶", "🚤", "🛳", "⛴", "🛥", "🚢", "✈️", "🛩", "🛫", "🛬", "🚁", "🚟", "🚠", "🚡", "🛰", "🚀", "🛸", "🌍", "🌎", "🌏", "🌐", "🗺", "🗾", "🏔", "⛰", "🗻", "🏕", "🏖", "🏜", "🏝", "🏞", "🏟", "🏛", "🏗", "🏘", "🏚", "🏠", "🏡", "🏢", "🏣", "🏤", "🏥", "🏦", "🏨", "🏩", "🏪", "🏫", "🏬", "🏭", "🏯", "🏰", "🗼", "🗽", "⛪", "🕌", "🕍", "⛩", "🕋", "⛲", "⛺", "🏙", "🎠", "🎡", "🎢", "🎪", "⛳", "🗿", "💦", "🌋", "🌁", "🌃", "🌄", "🌅", "🌆", "🌇", "🌉", "🌌", "🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘", "🌙", "🌚", "🌛", "🌜", "🌡", "☀", "🌝", "🌞", "🌟", "🌠", "☁", "⛅", "⛈️", "🌤", "🌥", "🌦", "🌧", "🌨", "🌩", "🌪", "🌫", "🌬", "🌀", "🌈", "☔", "❄", "☃️", "⛄️", "☄️", "💧", "🌊", "🎑", "👁️‍🗨️", "💤", "💥", "💨", "💫", "💬", "🗨", "🗯", "💭", "🕳", "🚨", "🛑", "⭐", "🎃", "🎄", "✨", "🎈", "🎉", "🎊", "🎋", "🎍", "🎎", "🎏", "🎐", "🎀", "🎁", "🃏", "🀄", "🦷", "🦴", "🛀", "👣", "💣", "🔪", "🧱", "🛢", "⛽", "🛹", "🚥", "🚦", "🚧", "??", "🧳", "⛱️", "🔥", "🧨", "🎗", "🎟", "🎫", "🧧", "🔮", "🎲", "🎴", "🎭", "🖼", "🎨", "🎤", "🔍", "🔎", "🕯", "💡", "🔦", "🏮", "📜", "🧮", "🔑", "🗝", "🔨", "⛏️", "⚒️", "🛠", "🗡", "⚔️", "🔫", "🏹", "🛡", "🔧", "🔩", "⚙️", "🗜", "⚖️", "⛓️", "⚗️", "🔬", "🔭", "📡", "💉", "💊", "🚪", "🛏", "🛋", "🚽", "🚿", "🛁", "🛒", "🚬", "⚰️", "⚱️", "🧰", "🧲", "🧪", "🧴", "🧷", "🧹", "🧻", "🧼", "🧽", "🧯", "💠", "♟️", "⌛", "⏳", "⚡", "🎆", "🎇")  # fmt: skip

# https://cloud.google.com/translate/docs/languages
LANG_CODES = {
    "af": "Afrikaans",
    "sq": "Albanian",
    "am": "Amharic",
    "ar": "Arabic",
    "hy": "Armenian",
    "az": "Azerbaijani",
    "eu": "Basque",
    "be": "Belarusian",
    "bn": "Bengali",
    "bs": "Bosnian",
    "bg": "Bulgarian",
    "ca": "Catalan",
    "ceb": "Cebuano",
    "zh": "Chinese (Simplified)",
    "zh-CN": "Chinese (Simplified)",
    "zh-TW": "Chinese (Traditional)",
    "co": "Corsican",
    "hr": "Croatian",
    "cs": "Czech",
    "da": "Danish",
    "nl": "Dutch",
    "en": "English",
    "eo": "Esperanto",
    "et": "Estonian",
    "fi": "Finnish",
    "fr": "French",
    "fy": "Frisian",
    "gl": "Galician",
    "ka": "Georgian",
    "de": "German",
    "el": "Greek",
    "gu": "Gujarati",
    "ht": "Haitian Creole",
    "ha": "Hausa",
    "haw": "Hawaiian",
    "iw": "Hebrew",
    "hi": "Hindi",
    "hmn": "Hmong",
    "hu": "Hungarian",
    "is": "Icelandic",
    "ig": "Igbo",
    "id": "Indonesian",
    "ga": "Irish",
    "it": "Italian",
    "ja": "Japanese",
    "jv": "Javanese",
    "kn": "Kannada",
    "kk": "Kazakh",
    "km": "Khmer",
    "rw": "Kinyarwanda",
    "ko": "Korean",
    "ku": "Kurdish",
    "ky": "Kyrgyz",
    "lo": "Lao",
    "la": "Latin",
    "lv": "Latvian",
    "lt": "Lithuanian",
    "lb": "Luxembourgish",
    "mk": "Macedonian",
    "mg": "Malagasy",
    "ms": "Malay",
    "ml": "Malayalam",
    "mt": "Maltese",
    "mi": "Maori",
    "mr": "Marathi",
    "mn": "Mongolian",
    "my": "Myanmar (Burmese)",
    "ne": "Nepali",
    "no": "Norwegian",
    "ny": "Nyanja (Chichewa)",
    "or": "Odia (Oriya)",
    "ps": "Pashto",
    "fa": "Persian",
    "pl": "Polish",
    "pt": "Portuguese (Portugal, Brazil)",
    "pa": "Punjabi",
    "ro": "Romanian",
    "ru": "Russian",
    "sm": "Samoan",
    "gd": "Scots Gaelic",
    "sr": "Serbian",
    "st": "Sesotho",
    "sn": "Shona",
    "sd": "Sindhi",
    "si": "Sinhala (Sinhalese)",
    "sk": "Slovak",
    "sl": "Slovenian",
    "so": "Somali",
    "es": "Spanish",
    "su": "Sundanese",
    "sw": "Swahili",
    "sv": "Swedish",
    "tl": "Tagalog (Filipino)",
    "tg": "Tajik",
    "ta": "Tamil",
    "tt": "Tatar",
    "te": "Telugu",
    "th": "Thai",
    "tr": "Turkish",
    "tk": "Turkmen",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "ug": "Uyghur",
    "uz": "Uzbek",
    "vi": "Vietnamese",
    "cy": "Welsh",
    "xh": "Xhosa",
    "yi": "Yiddish",
    "yo": "Yoruba",
    "zu": "Zulu",
}

FUN_APIS = {
    "cat": {
        "url": "https://api.thecatapi.com/v1/images/search",
        "type": "url",
        "value": "url",
    },
    "dog": {
        "url": "https://api.thedogapi.com/v1/images/search",
        "type": "url",
        "value": "url",
    },
    "food": {
        "url": "https://foodish-api.herokuapp.com/api",
        "type": "url",
        "value": "image",
    },
    "neko": {
        "url": "https://api.waifu.pics/sfw/neko",
        "type": "url",
        "value": "url",
    },
    "waifu": {
        "url": "https://api.waifu.pics/sfw/waifu",
        "type": "url",
        "value": "url",
    },
    "neko18": {
        "url": "https://api.waifu.pics/nsfw/neko",
        "type": "url",
        "value": "url",
    },
    "waifu18": {
        "url": "https://api.waifu.pics/nsfw/waifu",
        "type": "url",
        "value": "url",
    },
    "blowjob": {
        "url": "https://api.waifu.pics/nsfw/blowjob",
        "type": "url",
        "value": "url",
    },
    "cringe": {
        "url": "https://api.waifu.pics/sfw/cringe",
        "type": "url",
        "value": "url",
    },
    "cry": {
        "url": "https://api.waifu.pics/sfw/cry",
        "type": "url",
        "value": "url",
    },
    "dance": {
        "url": "https://api.waifu.pics/sfw/dance",
        "type": "url",
        "value": "url",
    },
    "happy": {
        "url": "https://api.waifu.pics/sfw/happy",
        "type": "url",
        "value": "url",
    },
    "fact": {
        "url": "https://asli-fun-fact-api.herokuapp.com",
        "type": "text",
        "value": "data.fact",
    },
    "quote": {
        "url": "http://api.quotable.io/random",
        "type": "text",
        "value": "content",
        "source": "author",
    },
}

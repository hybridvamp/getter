# getter < https://t.me/kastaid >
# Copyright (C) 2022 kastaid
#
# This file is a part of < https://github.com/kastaid/getter/ >
# PLease read the GNU Affero General Public License in
# < https://github.com/kastaid/getter/blob/main/LICENSE/ >.

from . import (
    Root,
    kasta_cmd,
    plugins_help,
    choice,
    suppress,
    mentionuser,
    get_media_type,
    Carbon,
    CARBON_PRESETS,
    RAYSO_THEMES,
)


@kasta_cmd(
    pattern=r"carbon(?: |$)([\s\S]*)",
)
async def _(kst):
    ga = kst.client
    match = kst.pattern_match.group(1)
    args = match.split(" ")
    if args[0] in CARBON_PRESETS:
        is_theme, theme = True, args[0]
    else:
        is_theme, theme = False, choice(list(CARBON_PRESETS))
    if kst.is_reply:
        reply = await kst.get_reply_message()
        if reply.media and get_media_type(reply.media) == "text":
            file = await reply.download_media()
            code = (Root / file).read_text()
            (Root / file).unlink(missing_ok=True)
        else:
            code = reply.message
    else:
        try:
            code = match.split(maxsplit=1)[1] if is_theme else match
        except IndexError:
            code = match
    if not code:
        return await kst.eod("`Reply to text message or readable file.`")
    yy = await kst.eor("`Processing...`")
    backgroundColor = CARBON_PRESETS[theme]
    windowTheme = choice(("none", "sharp", "bw"))
    carbon = await Carbon(
        code.strip(),
        file_name="carbon",
        download=True,
        fontFamily="Fira Code",
        theme=theme,
        backgroundColor=backgroundColor,
        dropShadow=windowTheme != "bw",
        windowTheme=windowTheme,
    )
    if not carbon:
        await yy.eod("`Carbon API not responding.`")
        return
    with suppress(BaseException):
        await kst.respond(
            "Carboniz by {}".format(mentionuser(ga.uid, ga.full_name, html=True)),
            file=carbon,
            parse_mode="html",
            force_document=False,
            allow_cache=False,
            reply_to=kst.reply_to_msg_id,
            silent=True,
        )
    await yy.try_delete()
    (Root / carbon).unlink(missing_ok=True)


@kasta_cmd(
    pattern=r"rayso(?: |$)([\s\S]*)",
)
async def _(kst):
    ga = kst.client
    match = kst.pattern_match.group(1)
    args = match.split(" ")
    if args[0] in RAYSO_THEMES:
        is_theme, theme = True, args[0]
    else:
        is_theme, theme = False, choice(RAYSO_THEMES)
    if kst.is_reply:
        reply = await kst.get_reply_message()
        if reply.media and get_media_type(reply.media) == "text":
            file = await reply.download_media()
            code = (Root / file).read_text()
            (Root / file).unlink(missing_ok=True)
        else:
            code = reply.message
    else:
        try:
            code = match.split(maxsplit=1)[1] if is_theme else match
        except IndexError:
            code = match
    if not code:
        return await kst.eod("`Reply to text message or readable file.`")
    yy = await kst.eor("`Processing...`")
    darkMode = choice((True, False))
    rayso = await Carbon(
        code,
        file_name="rayso",
        download=True,
        rayso=True,
        theme=theme,
        darkMode=darkMode,
    )
    if not rayso:
        await yy.eod("`Rayso API not responding.`")
        return
    with suppress(BaseException):
        await kst.respond(
            "Raysoniz by {}".format(mentionuser(ga.uid, ga.full_name, html=True)),
            file=rayso,
            parse_mode="html",
            force_document=False,
            allow_cache=False,
            reply_to=kst.reply_to_msg_id,
            silent=True,
        )
    await yy.try_delete()
    (Root / rayso).unlink(missing_ok=True)


@kasta_cmd(
    pattern="theme$",
    no_crash=True,
)
async def _(kst):
    carbon = "**Carbon Themes:**\n" + "\n".join([f"- `{x}`" for x in CARBON_PRESETS.keys()])
    rayso = "**Rayso Themes:**\n" + "\n".join([f"- `{x}`" for x in RAYSO_THEMES])
    await kst.sod(carbon)
    await kst.sod(rayso)


plugins_help["beautify"] = {
    "{i}carbon [theme] [text]/[reply (text or readable file)]": "Carboniz the text with choosing theme or random themes.",
    "{i}rayso [theme] [text]/[reply (text or readable file)]": "Raysoniz the text with choosing theme or random themes.",
    "{i}theme": "List all themes name.",
}
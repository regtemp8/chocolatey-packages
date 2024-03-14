# -*- coding: utf-8 -*-

import argparse


message_for_one_version = """
The latest version ({}) of #{} {}is now available on @chocolateynuget {}

{} #chocolatey
{}
"""

message_for_several_versions = """
The latest versions ({}) of #{} {}are now available on @chocolateynuget {}

{} #chocolatey
{}
"""

DATABASE = {
    "2fast": {
        "twitter_id": "jpweber8",
        "emojis": "🔐🔑🪪",
        "tags": [
            "android",
            "csharp",
            "authentication",
            "password",
            "microsoft",
            "windows",
            "windows10",
            "uwp",
            "apps",
            "totp",
            "authenticator",
        ],
    },
    "64gram": {
        "twitter_id": "",
        "emojis": "🖥️📱📞💬",
        "tags": ["telegram", "desktop", "windows"],
    },
    "aemulusmodmanager": {
        "twitter_id": "",
        "emojis": "🧑‍💻🖥️🎮🕹️👾",
        "tags": [
            "mod",
            "package",
            "manager",
            "persona",
            "pc",
            "windows",
        ],
    },
    "antidupl": {
        "twitter_id": "",
        "emojis": "🧑‍💻🖥️📋🔂",
        "tags": [
            "graphic",
            "deduplication",
            "image",
        ],
    },
    "arrowdl": {
        "twitter_id": "ArrowDLApp",
        "emojis": "🧑‍💻🖥️⬇️",
        "tags": [
            "crawler",
            "streaming",
            "download",
            "video",
            "webextensions",
            "magnetlink",
            "client",
            "youtube",
            "torrent",
            "downloader",
            "firefox",
            "nativeclient",
        ],
    },
    "biglybt-no-java": {
        "twitter_id": "BiglyBT",
        "emojis": "🧑‍💻🖥️⬇️",
        "tags": [
            "torrent",
            "torrentmanagement",
            "bittorrent",
            "p2p",
            "bittorrentclient",
            "torrentclient",
            "client",
            "torrentdownloader",
            "downloader",
            "i2p",
        ],
    },
    "ccache": {
        "twitter_id": "",
        "emojis": "🧑‍💻🖥️",
        "tags": [
            "ccache",
            "cpp",
            "cplusplus",
            "programming",
            "cache",
            "compiler",
            "gcc",
            "clang",
            "msvc",
        ],
    },
    "cider": {
        "twitter_id": "UseCider",
        "emojis": "🎼🎵🎧🔊",
        "tags": [
            "electron",
            "audio",
            "music",
            "windows",
            "opensource",
            "community",
            "performance",
            "player",
            "discord",
            "lyrics",
            "audioplayer",
            "audiostreaming",
            "cider",
            "electron",
        ],
    },
    "comictagger": {
        "twitter_id": "ComicTagger",
        "emojis": "🏷️",
        "tags": ["comics", "comic", "metadata", "tagging", "tagger"],
    },
    "conan": {
        "twitter_id": "conan_io",
        "emojis": "🐸🧑‍💻🖥️",
        "tags": [
            "conan",
            "cpp",
            "cplusplus",
            "package",
            "manager",
            "packagemanager",
            "cmake",
        ],
    },
    "crowtranslate": {
        "twitter_id": "",
        "emojis": "🧑‍💻🖥️",
        "tags": [
            "windows",
            "google",
            "translator",
            "ocr",
            "yandex",
            "bing",
            "qt5",
            "dbusapi",
            "libretranslate",
            "lingva",
        ],
    },
    "discord-history-tracker": {
        "twitter_id": "chylexmc",
        "emojis": "📰🔍🕵️👾",
        "tags": ["javascript", "css", "discord", "bookmark"],
    },
    "dosbox-x": {
        "twitter_id": "greatcodeholio",
        "emojis": "🖥️🎮🕹️👾",
        "tags": ["dosbox", "dos", "emulator"],
    },
    "fanficfare": {
        "twitter_id": "",
        "emojis": "🖥️📖📚🤓",
        "tags": [
            "python",
            "cli",
            "downloader",
            "ebook",
            "epub",
            "fanfiction",
            "calibre",
            "calibreplugin",
        ],
    },
    "faust": {
        "twitter_id": "grame_lyon",
        "emojis": "🖥️🎹🎵🎶🎧",
        "tags": [
            "audio",
            "c",
            "rust",
            "cplusplus",
            "csharp",
            "compiler",
            "cpp",
            "programming",
            "dsp",
            "llvm",
            "dlang",
            "julia",
            "wasm",
            "faust",
            "cmajor",
        ],
    },
    "hidhide": {
        "twitter_id": "NefariusMaximus",
        "emojis": "🖥️🎮🕹️👾",
        "tags": [
            "controller",
            "game",
            "gamepad",
            "videogame",
            "emulation",
            "peripherals",
            "device",
            "input",
            "gaming",
        ],
    },
    "internxt-drive": {
        "twitter_id": "Internxt",
        "emojis": "🧑‍💻🖥️🪙",
        "tags": [
            "windows",
            "macos",
            "linux",
            "cloud",
            "storage",
            "decentralized",
            "blockchain",
            "desktop",
            "cloudstorage",
        ],
    },
    "keepassxc-legacy": {
        "twitter_id": "KeePassXC",
        "emojis": "🧑‍💻🖥️✅🔑🔒",
        "tags": [
            "windows",
            "security",
            "privacy",
            "crossplatform",
            "manager",
            "yubikey",
            "password",
            "keepass",
            "keepassxc",
        ],
    },
    "magpie": {
        "twitter_id": "",
        "emojis": "🧑‍💻🖥️🔍🕵️",
        "tags": [
            "capture",
            "hlsl",
            "superresolution",
            "magnifier",
            "cppwinrt",
            "fsr",
            "anime4k",
        ],
    },
    "mgba": {
        "twitter_id": "mGBA_emu",
        "emojis": "🖥️🎮🕹️👾",
        "tags": [
            "mgba",
            "gba",
            "gameboy",
            "emulator",
            "gameboyadvance",
            "gameboycolor",
        ],
    },
    "monitorian": {
        "twitter_id": "",
        "emojis": "🧑‍💻🖥️🔆🕶️",
        "tags": [
            "monitor",
            "display",
            "brightness",
            "luminance",
            "ddcci",
        ],
    },
    "openproject": {
        "twitter_id": "openproject",
        "emojis": "🖥️🕒🗓️⏳",
        "tags": [
            "project",
            "planning",
            "roadmap",
            "bug",
            "tracker",
            "management",
            "kanban",
            "scrum",
            "opensource",
            "chart",
            "workflows",
            "gantt",
        ],
    },
    "phantombot": {
        "twitter_id": "PhantomBot",
        "emojis": "🖥️🎮🕹️👾",
        "tags": [
            "twitter",
            "X",
            "moderation",
            "game",
            "java",
            "streamlabs",
            "youtube",
            "twitchtv",
            "sfx",
            "discord",
            "twitch",
            "bot",
        ],
    },
    "qrcp": {
        "twitter_id": "qrcp_dev",
        "emojis": "🖥️🧑‍💻⤵️",
        "tags": [
            "cli",
            "golang",
            "utility",
            "commandline",
            "qrcode",
        ],
    },
    "rare": {
        "twitter_id": "legendary_gl",
        "emojis": "🎮🕹️👾",
        "tags": [
            "linux",
            "games",
            "frontend",
            "pyqt5",
            "epicgames",
            "legendary",
            "epicgameslauncher",
        ],
    },
    "sophia": {
        "twitter_id": "",
        "emojis": "🧑‍💻🖥️",
        "tags": [
            "windows",
            "gui",
            "script",
            "powershell",
            "tweaks",
            "windows10",
            "sophia",
            "debloat",
            "debloating",
            "windows11",
            "debloater",
            "sophiascript",
        ],
    },
    "super-productivity": {
        "twitter_id": "",
        "emojis": "🧑‍💻🖥️⏳🕒📅🗓️",
        "tags": [
            "productivity",
            "todo",
            "jira",
            "todolist",
            "electronapp",
            "timetracker",
            "taskmanager",
            "hacktoberfest",
            "timetracking",
            "hacktoberfest2021",
        ],
    },
}


class Package:
    def __init__(self, name, version):
        if name not in DATABASE:
            print(
                'Error: No configuration found for the package "{}" in the database.'.format(
                    name
                )
            )
            exit(-1)

        self.name = name

        if DATABASE[name]["twitter_id"] != "":
            self.twitter_id = "(@{}) ".format(DATABASE[name]["twitter_id"])
        else:
            self.twitter_id = ""

        self.version = str(version).strip("[]").replace("'", "")
        self.emojis = DATABASE[name]["emojis"]
        self.tags = "#" + " #".join(DATABASE[name]["tags"])
        self.url = "https://community.chocolatey.org/packages/" + name
        self.message_template = message_for_several_versions
        if len(version) == 1:
            self.message_template = message_for_one_version

    def __str__(self):
        return self.message_template.format(
            self.version, self.name, self.twitter_id, self.emojis, self.tags, self.url
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Twitter message generator",
        description="Generates a twitter message for a specified package and version",
        epilog="",
    )

    parser.add_argument(
        "package", metavar="package", type=str, nargs=1, help="name of the package"
    )

    parser.add_argument(
        "version",
        metavar="version",
        type=str,
        nargs="+",
        help="version(s) of the package",
    )

    args = parser.parse_args()

    p = Package(args.package[0], args.version)
    print(p)

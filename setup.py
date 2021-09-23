from setuptools import setup

setup(
    name = "Wireguard Watchdog",
    packages = ["wireguard-watchdog"],
    entry_points = {
        "console_scripts": ['wgwd=wireguardwatchdog.wgwd_cmd:main']
        },
    version = "0.1",
    description = "Command line tool to watch over wireguard endpoints.",
    long_description = "Command line tool to watch over wireguard endpoints.",
    author = "Marco Antonio",
    author_email = "marcocspc@hotmail.com",
    url = "https://github.com/marcocspc/wireguard-watchdog",
)

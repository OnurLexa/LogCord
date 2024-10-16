import atexit
import logging
import DiscordWebhookLogger
import time
import os
import sys
from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = DiscordWebhookHandler(webhook_url='<webhook urlsi>')
logger.addHandler(handler)

from threading import Semaphore
from time import sleep

import requests

def clear():

    if name == 'nt':
    _ = system('cls')

else:

    _ = system('clear')
    clear()

banner1 = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡴⠶⠶⠶⠶⠶⠤⠤⠤⢤⣤⣠⡶⠻⠉⢹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⠀⢀⣀⡠⠤⠤⠤⠤⢄⣴⠟⠀⠀⠀⢀⣿⣿⣖⠶⠤⠤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡄⠀⣀⣀⣀⣀⣀⣴⣿⠏⠀⠀⠀⡇⢘⣿⣿⣝⣧⣐⣒⣤⣬⠭⣉⣛⠒⠦⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠈⡍⠁⠀⠀⡾⢱⡟⠀⠀⠀⠀⡗⠈⢿⡿⠙⠚⢿⡄⠈⠉⠉⠓⠚⠿⢵⣖⣪⣭⣓⠢⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡜⠀⣷⠀⠀⢸⠃⣿⣇⠀⢀⢀⣈⣀⣀⡈⢷⣶⣷⣶⣿⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠑⠶⠤⣉⡳⢦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⡄⠸⡄⠀⢸⢠⣟⣧⣶⣿⣛⢿⣿⣿⣿⢷⣿⣿⡿⠿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠺⢷⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡍⠀⣇⠀⣿⠻⣿⣿⣿⣿⣷⣦⡙⣿⣿⣿⣿⣯⣡⣤⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⢸⠀⣿⢼⣿⣿⠷⠋⡙⣟⣿⣉⠉⠹⢿⣿⣏⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠘⣆⣿⢸⣻⣿⣾⡏⣡⡄⣀⣉⣹⣶⣾⣿⡏⠟⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡀⢻⡿⣌⣿⣿⣿⣿⠟⢛⣉⠁⠈⣿⣿⡟⠁⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⠁⠘⣧⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣿⡟⣤⣴⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⣿⣀⠀⢿⡏⢧⡈⣿⣿⣿⣿⣿⣿⣿⢿⠟⠛⠻⣿⠿⠙⣗⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⠏⠁⢀⣿⡏⡀⢸⣷⣸⣿⡙⠿⣿⣿⣿⣿⣟⢮⡞⠀⠀⠋⠀⢘⣿⠟⠈⠉⠳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠁⣀⣀⣸⣿⣷⢷⠀⣿⣷⡱⣝⠒⣿⣿⢿⡿⣷⣿⠆⠀⣠⠂⢠⡟⡁⠀⠀⠈⠙⢿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣿⣩⠠⠤⣀⣭⣿⣿⣞⡆⢹⣷⡿⣍⠓⠦⣼⣿⣿⡋⢁⣤⡞⣁⠴⠿⢋⣕⠀⡀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣼⠿⠏⢀⠀⠀⢸⣿⣿⣿⣿⢃⠀⣿⣿⠈⠣⡀⠨⣿⣿⣾⣛⣽⡟⠁⠛⣿⡿⠿⠀⡇⠀⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⠟⣿⠤⣄⠈⣳⣼⣿⣿⠝⠃⣿⣾⡀⢹⣌⡓⠦⠬⠿⠿⢿⣿⣯⣭⡔⠒⡛⠁⠀⡤⣠⣿⠀⡄⠀⢠⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⡏⠀⡏⣴⣟⣿⣿⣿⡿⠏⠀⠀⠘⣷⣧⣀⣏⣛⡲⠤⠿⣿⣿⣯⣭⣽⣶⠞⠁⣠⢞⣽⣿⡟⢨⠁⠀⢸⡆⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⠁⣸⠃⠙⠛⣿⢦⣀⣀⣤⢶⣶⣿⣿⣿⣿⣶⣶⡏⠀⢀⠉⢻⣟⣫⠿⠊⢁⡾⠁⠉⣾⣿⣧⣾⣏⠀⢸⡇⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⡯⢰⠋⠀⣰⣿⣿⣿⡿⣿⡏⡠⣯⡈⣹⣟⣿⣝⣙⡇⠈⢩⣭⣿⣿⠇⢀⡴⠋⠀⠀⠐⣻⣿⢿⣿⠃⠀⣿⡇⠻⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⡿⢠⠏⠀⢀⣻⣿⠏⢿⣿⣸⢸⠁⠸⣿⣿⣿⢿⠛⣿⣷⣿⣿⣿⣷⠶⠚⠉⠀⠀⠀⠀⠘⢿⣿⣿⡷⡄⢸⣹⠇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡟⢀⣴⣶⣾⣿⣿⡏⣰⢸⠇⣇⡏⠀⠀⠙⣿⣿⣟⡄⢹⡿⠿⠛⠛⣿⣶⣶⡦⠤⢔⣂⣀⠀⣾⡟⠻⡿⠁⢌⡿⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠀⣸⠿⠟⠟⠙⡿⠀⡇⡾⢠⣏⢣⣄⢲⣄⡘⣿⣿⣷⠘⣇⢀⣒⡯⠉⠉⠁⠈⠓⠿⣿⠟⢰⣿⡇⠴⠁⠀⣼⡽⠁⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⢘⣇⠉⠀⠀⣀⡼⠁⢸⣱⠇⢠⢻⡄⣿⣿⣿⣿⣿⣿⣏⠀⢻⣿⣷⣄⡄⠀⠀⢀⡤⠞⠁⢠⣿⣿⡀⠀⢀⣾⣵⡗⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠾⢾⣆⣰⣶⣷⡄⠀⢡⠏⠀⠀⠈⠀⠉⠙⢿⢱⠙⢿⣿⣄⡸⣿⣿⣿⣿⡿⠟⢉⡠⠆⣰⢿⣿⢿⠁⣠⠋⠐⣾⠇⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠻⣌⠻⣿⡿⠿⣯⡶⠇⠀⠀⢠⠀⠀⠸⣿⠀⠀⣿⡏⠁⣿⠋⠁⣁⣤⠞⠉⠀⠰⢛⣿⠋⣠⡞⠁⢀⡀⠉⠀⢠⢿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠓⠧⣤⣄⣉⣀⣀⡈⠐⢪⣷⡄⠀⡇⣧⡀⣾⣧⠁⢻⣶⣾⣿⡄⠀⠀⠀⠀⣿⣯⣾⣿⡾⠛⢉⣀⡅⠀⡜⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢹⣟⣷⣦⣾⣷⠀⣿⣿⣧⣿⢿⣇⠀⣿⣿⠛⠀⡀⢀⠀⣠⣿⣫⣾⡽⠞⠛⠛⠾⠁⣸⢁⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⢸⡟⣿⡿⣿⣷⢿⣿⣿⣿⡜⣷⠄⢸⡘⣊⣭⡾⢋⡾⣿⣿⣿⣵⠶⠚⠁⠀⠀⠀⣿⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⢸⣧⢻⣷⢻⢿⣧⡻⣿⣿⢷⣽⡆⠈⣧⠡⢄⣼⡿⠞⣻⢿⡭⠆⠀⢀⣠⣴⠀⢰⣏⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

print(Fore.LIGHTRED_EX + banner1)
time.sleep(0.5)
welcome = Fore.CYAN + "Welcome to LogCord!"
for char in welcome:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(0.5)

def _flush(self: logging.Logger):
    for handler in self.handlers:
        if isinstance(handler, DiscordWebhookHandler):
            handler.send()
setattr(logging.Logger, 'flush', _flush)


class DiscordWebhookFormatter(logging.Formatter):
    MAX_DISCORD_MESSAGE_LEN = 2000
    DISCORD_MESSAGE_TEMPLATE = '```diff\n{}```'
    DISCORD_MESSAGE_TEMPLATE_LEN = len(DISCORD_MESSAGE_TEMPLATE.format(''))
    MAX_LOG_LEN = MAX_DISCORD_MESSAGE_LEN - DISCORD_MESSAGE_TEMPLATE_LEN

    _LEVEL_PREFIX_LENGTH = 3
    _LEVEL_PREFIX = {
        'DEBUG': '===',
        'INFO': '+  ',
        'WARNING': 'W  ',
        'ERROR': '-  ',
        'CRITICAL': '-!!',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for v in DiscordWebhookFormatter._LEVEL_PREFIX.values():
            assert len(v) == DiscordWebhookFormatter._LEVEL_PREFIX_LENGTH

    def format(self, record: logging.LogRecord):
        lines = record.msg.split('\n')

        try:
            level_prefix = DiscordWebhookFormatter._LEVEL_PREFIX[record.levelname]
        except KeyError:
            level_prefix = ' ' * DiscordWebhookFormatter._LEVEL_PREFIX_LENGTH

        formatted_lines = []
        formatted_lines_len = 0

        for i in range(len(lines)):
            if i == 0:
                separator = '│'
            elif i == len(lines) - 1:
                separator = '└'
            else:
                separator = '├'

            split_len = DiscordWebhookFormatter.MAX_LOG_LEN - DiscordWebhookFormatter._LEVEL_PREFIX_LENGTH - 1  # -1 = separator
            if len(lines[i]) > split_len:
                formatted_lines.append(level_prefix + separator + lines[i][:split_len])
                formatted_lines_len += split_len
                separator = '↳'
                for line in [lines[i][x:x+split_len] for x in range(split_len, len(lines[i]), split_len)]:
                    formatted_lines.append(level_prefix + separator + line)
                    formatted_lines_len += len(formatted_lines[-1])
            else:
                formatted_lines.append(level_prefix + separator + lines[i])
                formatted_lines_len += len(formatted_lines[-1])
        formatted_lines_len += len(formatted_lines) - 1

        return formatted_lines, formatted_lines_len


class DiscordWebhookHandler(logging.Handler):

    def __init__(self, webhook_url: str, auto_flush=False):
        super().__init__()
        self.webhook_url = webhook_url
        self.formatter: DiscordWebhookFormatter = DiscordWebhookFormatter()
        self._lock = Semaphore(5)

        self.auto_flush = auto_flush
        self.buffer = []
        self.buffer_message_len = 0
        atexit.register(self.send)

    def emit(self, record: logging.LogRecord):
        try:
            formatted_lines, formatted_lines_len = self.format(record)

            if formatted_lines_len >= self.formatter.MAX_LOG_LEN:
                for line in formatted_lines:
                    if self.buffer_message_len + len(line) >= self.formatter.MAX_LOG_LEN:
                        self.send()

                        self.buffer.append((record, [line]))
                        self.buffer_message_len += len(line) + 1
                    else:
                        self.buffer.append((record, [line]))
                        self.buffer_message_len += len(line) + 1

                self.send()
            elif self.buffer_message_len + formatted_lines_len >= self.formatter.MAX_LOG_LEN:
                self.send()

                self.buffer.append((record, formatted_lines))
                self.buffer_message_len += formatted_lines_len + 1
            else:
                self.buffer.append((record, formatted_lines))
                self.buffer_message_len += formatted_lines_len + 1

            if self.auto_flush:
                self.send()
        except Exception:
            self.handleError(record)
    
    def send(self):
        if self.buffer_message_len == 0:
            return
    
        max_retries = 3

        # log mesajı
        log_message = ''
        for b in self.buffer:
            for line in b[1]:
                log_message += line + '\n'

        record = self.buffer[-1][0]

        json_data = {
            'content': self.formatter.DISCORD_MESSAGE_TEMPLATE.format(log_message[:-1])
        }

        for retries in range(max_retries - 1):
            with self._lock:
                r = requests.post(self.webhook_url, json=json_data)

            if r.status_code == 429:
                retry_after = int(r.headers.get('Retry-After', 500)) / 100.0
                sleep(retry_after)
                continue
            elif r.status_code < 400:
                break
            else:
                continue

        self.buffer.clear()
        self.buffer_message_len = 0

        try:
            r.raise_for_status()
        except Exception:
            self.handleError(record)

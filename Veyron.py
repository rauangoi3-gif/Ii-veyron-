"""
FREEZE AND ZOMELEZZ HELP BOT
База данных: freeze_zomelezz.db
"""

import asyncio
import logging
import random
import aiosqlite
import json
import re

from datetime import datetime, timedelta
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    ChatPermissions,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)
from aiogram.utils.keyboard import (
    ReplyKeyboardBuilder,
    InlineKeyboardBuilder
)
from aiogram.enums import ChatMemberStatus

# ==================== НАСТРОЙКИ ====================

# Вставь новый токен бота, полученный через BotFather
TOKEN = "ВСТАВЬ_СВОЙ_ТОКЕН"

GLOBAL_ADMIN_IDS = [6508695310]
BOT_NAME = "VeyronHELP BOT"
VERSION = "6.0.0 FIXED"
DB_NAME = "freeze_zomelezz.db"

START_BALANCE = 50000
DAILY_BONUS_BASE = 100
DAILY_STREAK_BONUS = 20
MAX_STREAK = 7
TRANSFER_TAX = 0.05
LOAN_INTEREST = 0.15
ROB_COOLDOWN_HOURS = 4
ROB_SUCCESS_CHANCE = 0.35
ROB_MAX_AMOUNT = 5000

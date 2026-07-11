"""
CNC Speeds & Feeds Manager
Configuration Module

Central location for application configuration,
paths, database settings, unit defaults, and
calculation constants.

Python Version:
3.12+

Author:
TreySeesU
"""

from pathlib import Path


# ==========================================================
# APPLICATION INFORMATION
# ==========================================================

APP_NAME = "CNC Speeds & Feeds Manager"

APP_VERSION = "1.0.0"

APP_AUTHOR = "TreySeesU"


# ==========================================================
# PROJECT PATHS
# ==========================================================

# Location of this file:
# cnc-speeds-feeds/python/config.py

PYTHON_DIR = Path(__file__).resolve().parent

PROJECT_ROOT = PYTHON_DIR.parent


DATABASE_DIR = PROJECT_ROOT / "database"

DATABASE_FILE = DATABASE_DIR / "cnc.db"


UPLOAD_DIR = PROJECT_ROOT / "uploads"

LOG_DIR = PROJECT_ROOT / "logs"


# ==========================================================
# LOGGING SETTINGS
# ==========================================================

LOG_FILE = LOG_DIR / "application.log"

LOG_LEVEL = "INFO"


# ==========================================================
# DEFAULT UNITS
# ==========================================================

DEFAULT_UNIT_SYSTEM = "metric"


METRIC_UNITS = {

    "distance": "mm",

    "feed_rate": "mm/min",

    "speed": "m/min",

    "diameter": "mm"

}


IMPERIAL_UNITS = {

    "distance": "inch",

    "feed_rate": "in/min",

    "speed": "surface feet/min",

    "diameter": "inch"

}


# ==========================================================
# CALCULATION DEFAULTS
# ==========================================================

# These are safety defaults.
# Actual values will come from the database.

DEFAULT_CHIPLOAD = 0.15


DEFAULT_DEPTH_FACTOR = 0.50


DEFAULT_STEPOVER_PERCENT = 40


DEFAULT_PLUNGE_PERCENT = 50


# ==========================================================
# SAFETY LIMITS
# ==========================================================

# These are general CNC router protection limits.
# They are not replacements for manufacturer data.

MAX_WARNING_LEVELS = {

    "low": 1,

    "medium": 2,

    "high": 3

}


# ==========================================================
# DATABASE SETTINGS
# ==========================================================

DATABASE_TIMEOUT = 30


DATABASE_FOREIGN_KEYS = True


# ==========================================================
# WEB APPLICATION SETTINGS
# ==========================================================

WEB_TITLE = "CNC Speeds & Feeds Calculator"


DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


# ==========================================================
# DEBUG SETTINGS
# ==========================================================

DEBUG_MODE = True


# ==========================================================
# FILE INITIALIZATION
# ==========================================================

def initialize_directories():

    """
    Creates required application directories
    if they do not exist.
    """

    directories = [

        UPLOAD_DIR,

        LOG_DIR

    ]


    for directory in directories:

        directory.mkdir(
            parents=True,
            exist_ok=True
        )


# Automatically create folders
initialize_directories()

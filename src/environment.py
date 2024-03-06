"""
Exposes environment as module level variables.
"""

import os

POSTGRES_URI = os.environ["POSTGRES_URI"]
LOG_LEVEL = os.environ["LOG_LEVEL"]

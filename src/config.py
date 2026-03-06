import os
from dotenv import load_dotenv

load_dotenv()

TRACE_LEVEL = os.environ.get("TRACE_LEVEL", "INFO")
TRACE_FORMAT = os.environ.get("TRACE_FORMAT", "json")

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
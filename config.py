import os

from dotenv import load_dotenv

load_dotenv()


# TWILIO
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
TU_WHATSAPP = os.getenv("TU_WHATSAPP")


# AHORRO
ALIAS = os.getenv("ALIAS")


from twilio.rest import Client

from config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_WHATSAPP_NUMBER,
    TU_WHATSAPP
)


client = Client(
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN
)


def enviar_whatsapp(mensaje):

    message = client.messages.create(
        body=mensaje,
        from_=TWILIO_WHATSAPP_NUMBER,
        to=TU_WHATSAPP
    )

    print("📲 WhatsApp enviado")
    print(f"SID: {message.sid}")
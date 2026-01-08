import os
import smtplib
from email.message import EmailMessage

from app.config import (
    SMTP_SERVER,
    SMTP_PORT,
    EMAIL_SENDER,
    EMAIL_PASSWORD,
    EMAIL_RECEIVERS,
)


def send_email(attachments):
    msg = EmailMessage()
    msg["Subject"] = "📊 Rapport quotidien Grafana"
    msg["From"] = EMAIL_SENDER
    msg["To"] = ", ".join(EMAIL_RECEIVERS)

    msg.set_content(
        "Bonjour,\n\n"
        "Veuillez trouver ci-joint le rapport Grafana du jour.\n\n"
        "Cordialement."
    )

    # Pièces jointes
    for file_path in attachments:
        with open(file_path, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(file_path)

        msg.add_attachment(
            file_data,
            maintype="image",
            subtype="png",
            filename=file_name,
        )

    # Envoi SMTP
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)

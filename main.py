from app.capture import capture_dashboards
from app.mailer import send_report_email

if __name__ == "__main__":
    image_paths = capture_dashboards()
    send_report_email(image_paths)

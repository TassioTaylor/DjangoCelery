

from time import sleep
from django.core.mail import send_mail
from celery import shared_task

@shared_task()
def send_feedback_email_task(email_adress, message):
    """Sends an email when the feedback form has been submitted."""
    sleep(20)  # Simulate expensive operation that freezes Django
    send_mail(
        "Your Feedback",
        f"\t{message}\n\nThank you!",
        "support@example.com",
        [email_adress],
        fail_silently=False,
    )

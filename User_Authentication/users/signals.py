from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User  


@receiver(post_save, sender=User)
def send_confirmation_email(sender, instance, created, **kwargs):
    if created:
        token = default_token_generator.make_token(instance)
        uid = urlsafe_base64_encode(force_bytes(instance.pk))  # Encode the user's ID

        # Generate confirmation email
        subject = 'Confirm your registration  in my Django app by Federico Guakinchay '
        confirmation_link = f"http://127.0.0.1:8000/accounts/confirm/{uid}/{token}"  # Replace with your actual domain
        html_message = render_to_string('confirmation_email.html', {'confirmation_link': confirmation_link})
        plain_message = strip_tags(html_message)
        from_email = settings.DEFAULT_FROM_EMAIL
        to = instance.email

        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
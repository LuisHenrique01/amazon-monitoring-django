from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_mail(to: list, product_name: str, user_name: str, product_url: str, price: float, title: str = 'Alerta de preço!'):
    html_content = render_to_string('template_email.html', {'title': title,
                                                            "product_name": product_name,
                                                            "user_name": user_name,
                                                            "product_url": product_url,
                                                            "price": price})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        # Subject
        title,
        # Content
        text_content,
        # From email
        settings.EMAIL_HOST_USER,
        to)
    email.attach_alternative(html_content, 'text/html')
    email.send()

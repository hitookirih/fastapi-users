from textwrap import dedent

from core.models import User
from mailing.send_email import send_email


async def send_verification_email(
    user: User,
    verification_link: str,
    verification_token: str,
):
    recipient = user.email
    subject = "Confirm your email"
    plain_content = dedent(
        f"""
    Dear {recipient},
    
    Please follow the link to verify your email:
    {verification_link}
    
    Use this code to verify your email 
    """,
    )
    html_content = ...
    await send_email(
        recipient=recipient,
        subject=subject,
        plain_content=plain_content,
        html_content="",
    )

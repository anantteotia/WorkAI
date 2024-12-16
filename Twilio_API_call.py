from twilio.rest import Client

# Twilio account credentials
account_sid = 'Replace with your actual Twilio Account SID'
auth_token = 'Replace with your actual Twilio Auth Token'
client = Client(account_sid, auth_token)

# List of recipient phone numbers for WhatsApp
phone_numbers = [
    'whatsapp:+Your_Phone_Number',
    'whatsapp:+Your_Phone_Number_2',
]

# Message content
message_body = """
    Hi,\n
Work AI got a job for you! 🎉
A Restaurant is looking for a waiter. They’re offering $24/hour + tips.\n
Are you interested? Reply YES or NO to let us know.\n
If you say YES, we’ll share your name and contact info with the employer so they can reach out to you.\n
Let us know soon! 😊\n
Work AI Team
"""

# Sending WhatsApp messages
for number in phone_numbers:
    message = client.messages.create(
        body=message_body,
        #content_sid = "HX165be760285b69c984a211ec968bdd7d",
        from_='whatsapp:+Twilio's WhatsApp Sandbox Number',  # 
        to=number,

    )
    print(f"WhatsApp message sent to {number}, SID: {message.sid}")

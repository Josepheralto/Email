# File name: domain_email_generator.py

# Import and use it:
from domain_email_generator import generate_domain_email

# Create your email parameters
email_params = {
    'domain_name': 'yourdomain.com',
    'sender_name': 'Your Name',
    'sender_company': 'Your Company',
    'recipient_name': 'Recipient Name',
    'recipient_company': 'Their Company',
    'industry': 'their industry',
    'estimated_value': '$XXXX' # optional
}

# Generate the email
email = generate_domain_email(email_params)
print(email)

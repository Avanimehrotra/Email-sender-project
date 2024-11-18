import openai
import requests
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure to set this in your environment

def generate_email_content(prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=150  # Adjust tokens as needed
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating content: {e}")
        return None


import requests

def send_email(recipient, subject, body):
    url = "https://api.sendinblue.com/v3/smtp/email"
    headers = {
        "Content-Type": "application/json",
        "api-key": os.getenv("SENDINBLUE_API_KEY")  # Securely retrieve the API key
    }
    payload = {
        "sender": {"email": "avanimehrotra2004@gmail.com"},
        "to": [{"email": recipient}],
        "subject": subject,
        "htmlContent": body
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"Response: {response.text}")
        response.raise_for_status()  # Check for HTTP errors
        print("Email sent successfully!")
        return response.json()  # Return response JSON for verification
    except requests.exceptions.RequestException as e:
        print(f"Error sending email: {e}")
        return None
    #except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    #except Exception as err:
        print(f"Other error occurred: {err}")
        return None
import json
from twilio.rest import Client

# Function to read JSON file
def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to send SMS
def send_sms(phone_number, message):
    # Replace with your Twilio Account SID, Auth Token, and Twilio phone number
    account_sid = 'ACed274781e7c0e01756f7ffa3539000b2'
    auth_token = 'dc2dc323fa94fe9d501971fd0ab0fdca'
    from_number = '+447488891405'

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=from_number,
        to=phone_number
    )

    print(f"SMS sent successfully to {phone_number}. SID: {message.sid}")

# Function to initiate chat with SMS
def initiate_chat(data):
    for entry in data:
        message = f"Hello, {entry['name']} from {entry['country']}"
        send_sms(entry['celphone'], message)

# Example usage
file_path = './contact.json'
data = read_json(file_path)
initiate_chat(data)

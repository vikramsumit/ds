import pywhatkit as kit

phone_number = "+91 8986256596"  # Replace with the recipient's phone number
message = "Hello, this is a test message!"  # Replace with your messaged

# kit.sendwhatmsg(phone_number, message, 15, 0)  # Sends the message at 15:00 (3 PM)
kit.sendwhatmsg_instantly(phone_number, message)  # Sends the message instantly
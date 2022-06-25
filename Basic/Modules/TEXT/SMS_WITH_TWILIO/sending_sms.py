#pip install twilio
#pip install gtts
from twilio.rest import Client
from gtts import gTTS
from pprint import pprint
import os


def sending_sms(sending_to, message):
    try:
        account_sid = os.environ.get("ACCOUNT_SID")
        auth_token = os.environ.get("AUTH_TOKEN")
        twilio_number = os.environ.get("TWILIO_NUM")
        
        client = Client(account_sid, auth_token)
        call = client.messages.create(
            to = sending_to,
            from_=twilio_number,
            body = message
        )
        print(call.sid)
    except Exception as e:
        print(e)
    return None
# calling Sending Sms from another function that
# def calling_function():
#     try:
#         message = input("please what is ur message")
#         sending_to = input("please enter phone number")
#         sending_sms(sending_to, message)
#     except Exception as e:
#         print(e)
        
def robbort (message):
    mytext = message
    language = "en"
    vioce = gTTS(
        text= mytext,
        lang =language,
        slow = False
    )
    vioce.save("audior_translate/welcome.mp3")
    return None


message = input("what  whould you like to say")
robbort(message)
        
if __name__ == "__main__":
    pass

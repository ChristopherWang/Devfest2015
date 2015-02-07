
from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC0eedf00fd1e7df73452215804a74af87"
auth_token  = "20ea898c9fd20d0cca3fac6a0e3e8d03"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Jenny please?! I love you <3",
    to="+17134437253",    # Replace with your phone number
    from_="+12819730838") # Replace with your Twilio number
print(message.sid)


from twilio.rest import TwilioRestClient 
ACCOUNT_SID = "AC0eedf00fd1e7df73452215804a74af87"
AUTH_TOKEN  = "20ea898c9fd20d0cca3fac6a0e3e8d03"
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
call = client.calls.create( 
	from_="+12819730838",
        to="+17134437253",
	url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient",
        method="GET",  
	fallback_method="GET",  
	status_callback_method="GET",    
	record="false"
) 
 
print(call.sid)

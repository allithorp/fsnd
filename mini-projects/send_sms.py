from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC586a3486165b86760a84d71d9f5e86b5"
auth_token = "0f1ee0646fa825503df721fb0ada6a68"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+18176007942", from_="+18086003884",
                                     body="Hello there! This is a test of my Python program")

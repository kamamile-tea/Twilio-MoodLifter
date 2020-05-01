# from twilio.rest import Client

# client = Client(
#   'AC2e09228d2523437f440652da9f17dec5', '8256fba14769bd1cbc3224769abb0279')
# #9173535383
# #giving error when call probaly due to url
# call = client.calls.create(
#   to='+13479937535',
#   from_='+16812424500',
#   url='http://demo.twilio.com/docs/voice.xml')

# print(call.sid)



# Start-up instructions

# do: pip install flask
# do: pip install twilio
# do: pip install pyngrok
# do: pip install axju-jokes
# run "python MoodLifter.py"
# call (347) 252-8864




from flask import Flask
from joke.jokes import *
from random import choice
from pyngrok import ngrok
from twilio.twiml.voice_response import VoiceResponse, Gather

public_url = ngrok.connect(5000)
print(public_url)

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():

  joke = (choice([geek, icanhazdad, icndb])())
  print(joke)

  resp = VoiceResponse()
  

  resp.say(joke)

  return str(resp)

if __name__ == "__main__":
  app.run(debug=True)

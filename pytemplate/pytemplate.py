import requests

def i_do_things():
  print requests.get('https://google.co.uk/').status_code

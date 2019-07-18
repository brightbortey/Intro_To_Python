import requests

r = requests.get("https://maker.ifttt.com/trigger/button_pressed/with/key/ezMm1vHtyNTfqUCEG_HNvwVQkXW1e8sB-HPqxeXhXQ0")
#p = requests.post("https://maker.ifttt.com/trigger/button_pressed/with/key/ezMm1vHtyNTfqUCEG_HNvwVQkXW1e8sB-HPqxeXhXQ0")
def button_pressed(r):
	print ("hey, we're testing here")

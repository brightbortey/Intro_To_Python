from gpiozero import Button
from signal import pause
from subprocess import call
import requests

r = requests.get("https://maker.ifttt.com/trigger/button_pressed/with/key/ezMm1vHtyNTfqUCEG_HNvwVQkXW1e8sB-HPqxeXhXQ0")

button = Button(2)

button.when_pressed = r #requests.get("https://maker.ifttt.com/trigger/button_pressed/with/key/ezMm1$$/ezMm1vHtyNTfqUCEG_HNvwVQkXW1e8sB-HPqxeXhXQ0")
button.when_released = r


from gpiozero import Button, DistanceSensor

class Platine:
    def __init__(self, pin_trigger=17, pin_echo=12, pin_start=26, pin_mesure=21):
        self.capteur = DistanceSensor(trigger=pin_trigger, echo=pin_echo, max_distance=2)
        self.start = Button(pin_start, pull_up=True)
        self.btnMesure = Button(pin_mesure, pull_up=True)

    def siStart(self, fonction):
        self.start.when_pressed = fonction
import os
import json
import time
from modele.mesure import Mesure
from datetime import datetime
from vue.vue import LCDVue
from modele.platine import Platine

class Controleur:
    def __init__(self):
        self.platine = Platine()
        self.vue = LCDVue()
        self.systeme_actif = False 

        self.platine.siStart(self.changeEtat)
        self.platine.siMesure(self.prendre_mesure)

    def changeEtat(self):
        self.systeme_actif = not self.systeme_actif
        if self.systeme_actif:
            self.vue.afficher("Systeme actif", "Mesure auto")
        else:
            self.vue.afficher("Systeme stop")
            time.sleep(2)
            self.vue.effacer()

    
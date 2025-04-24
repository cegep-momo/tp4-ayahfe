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

    def prendre_mesure(self):
        if not self.systeme_actif:
            return
        valeur = self.platine.lire_distance()
        if valeur == -1.0:
            self.vue.afficher("Erreur capteur", "Pas de retour")
            return
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mesure = Mesure(date, f"{valeur} cm")
        self.vue.afficher("Mesure prise", f"{valeur} cm")
        print(f"[MESURE] {valeur} cm")
        self.sauvegarder(mesure)

    def sauvegarder(self, mesure):
        dossier = "sauvegarde"
        fichier = os.path.join(dossier, "mesures.json")
        if not os.path.exists(dossier):
            os.makedirs(dossier)
        if not os.path.exists(fichier):
            with open(fichier, "w") as f:
                pass  


        with open(fichier, "a") as f:
            json.dump(mesure.__dict__, f)
            f.write("\n")

    

    def demarrer(self):
        self.vue.afficher("Appuyez pour", "démarrer")
        try:
            while True:
                if self.systeme_actif:
                    self.prendre_mesure()
                    time.sleep(5)
                else:
                    time.sleep(0.1)  
        except KeyboardInterrupt:
            self.arreter()
            
            
    def arreter(self):
        self.vue.afficher("Fin du programme.")
        time.sleep(1)
        self.vue.effacer()
        self.platine.cleanup()

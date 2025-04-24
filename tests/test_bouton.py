import unittest
from gpiozero import Button
from gpiozero.pins.mock import MockFactory
from gpiozero import Device
from modele.mesure import Mesure

Device.pin_factory = MockFactory()

class TestTP4(unittest.TestCase):

    def test_bouton_gpiozero(self):
        bouton = Button(17)
        self.assertIsNotNone(bouton)
        self.assertFalse(bouton.is_pressed)

    def test_objet_mesure(self):
        date = "2025-04-24 12:00:00"
        valeur = "36.5 cm"
        mesure = Mesure(date, valeur)
        self.assertEqual(mesure.dateHeureMesure, date)
        self.assertEqual(mesure.dataMesure, valeur)

if __name__ == "__main__":
    unittest.main()

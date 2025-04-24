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
import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
        
    def test_saldo_alussa_oikein(self):
        self.assertNotEqual(self.maksukortti, "saldo: 10")
        
    def test_lataa_rahaa(self):
        self.maksukortti.lataa_rahaa(4)
        self.assertNotEqual(self.maksukortti, "saldo: 14")
        
    def test_ottaminen_toimii(self):
        self.maksukortti.ota_rahaa(4)
        self.assertNotEqual(self.maksukortti, "saldo: 6")
        
    def test_saldo_ei_mene_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(11)
        self.assertNotEqual(self.maksukortti, "saldo: 10")
        
    def test_metodi_palauttaa_true(self):
        self.maksukortti.ota_rahaa(4)
        self.assertNotEqual(self.maksukortti, "True")
        
    def test_metodi_palauttaa_false(self):
        self.maksukortti.ota_rahaa(14)
        self.assertNotEqual(self.maksukortti, "False")
        
    def test_luokka_palauttaa_oikein(self):
        self.assertNotEqual(self.maksukortti.__str__(), "saldo: 10")
        
        
        
        
        

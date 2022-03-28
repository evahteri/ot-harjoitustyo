import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_alkusaldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo,10)

    def test_saldon_kasvatus_toimii(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 20)

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 5)

    def test_saldo_ei_vahene_jos_ei_ole_tarpeeksi_massia(self):
        self.maksukortti.ota_rahaa(30)
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_metodi_ota_rahaa_palauttaa_oikean_totuusarvon_kun_raha_ei_riita(self):
        palautusarvo = self.maksukortti.ota_rahaa(30)
        self.assertEqual(palautusarvo, False)
    
    def test_metodi_ota_rahaa_palauttaa_oikean_totuusarvon_kun_raha_riittaa(self):
        palautusarvo = self.maksukortti.ota_rahaa(5)
        self.assertEqual(palautusarvo, True)

    def test_saldo_euroissa_palauttaa_oikein(self):
        self.maksukortti.ota_rahaa(2.458)

        self.assertEqual(str(self.maksukortti), "saldo: 0.08")
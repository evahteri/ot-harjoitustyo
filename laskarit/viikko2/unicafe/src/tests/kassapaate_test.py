import unittest

from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_rahaa_oikea_maara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullisia_myyty_oikea_maara(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukkaita_myyty_oikea_maara(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateinen_edullisesti_lisaa_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_kateinen_edullisesti_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)

    def test_kateinen_maukkaasti_lisaa_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_kateinen_maukkaasti_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
    
    def test_kateinen_maukkaasti_raha_ei_riita_raha_palautuu(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)
    
    def test_kateinen_edulllisesti_raha_ei_riita_raha_palautuu(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)
    
    def test_maukas_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(400)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_maukas_maara_ei_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_maara_ei_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

#korttiostot
    def test_kortilla_tarpeeksi_rahaa_palauttaa_True_maukas(self):
        totuus = self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(500))
        self.assertEqual(totuus, True)

    def test_kortilla_tarpeeksi_rahaa_palauttaa_True_edullinen(self):
        totuus = self.kassapaate.syo_edullisesti_kortilla(Maksukortti(500))
        self.assertEqual(totuus, True)
    
    def test_veloitus_oikein_maukas(self):
        maksukortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 100)
    
    def test_veloitus_oikein_edullinen(self):
        maksukortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 260)
    
    def test_korttimaksu_saldo_kasvaa_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(500))
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttimaksu_saldo_kasvaa_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(500))
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_veloitus_oikein_maukas_rahat_ei_riita(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 200)

    def test_veloitus_oikein_edullinen_rahat_ei_riita(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 200)
    
    def test_korttimaksu_saldo_ei_kasva_kasvaa_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(100))
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_korttimaksu_saldo_ei_kasva_kasvaa_edullinen(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(100))
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kortilla_ei_tarpeeksi_rahaa_palauttaa_False_maukas(self):
        totuus = self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(100))
        self.assertEqual(totuus, False)

    def test_kortilla_ei_tarpeeksi_rahaa_palauttaa_False_edullinen(self):
        totuus = self.kassapaate.syo_edullisesti_kortilla(Maksukortti(100))
        self.assertEqual(totuus, False)

    def test_kassan_rahamaara_ei_muutu_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(500))
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_rahamaara_ei_muutu_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(500))
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kortin_lataus_kortin_saldo_muuttuu(self):
        maksukortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(maksukortti,100)
        self.assertEqual(maksukortti.saldo, 600)
    
    def test_kortin_lataus_kassan_saldo_muuttuu(self):
        maksukortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(maksukortti,100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
    
    def test_kortin_lataus_jos_summa_on_nolla(self):
        maksukortti = Maksukortti(100)
        paluu = self.kassapaate.lataa_rahaa_kortille(maksukortti, -200)
        self.assertEqual(paluu, None)


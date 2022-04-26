# Viikko 3

- Projektin aloitus
- Hakemistorakennetta muodostettu
- Käyttäjätietojen tallentamiseen käytettävän database tiedoston voi luoda ja alustaa sen initialize_database.py käskyllä
- invoke -käskyt start, test ja coverage_report luotu
- Käyttäjä voi käynnistää create user näkymän index.py tiedoston suorittamalla tai invoke käskyllä
- Luotu testi, joka testaa, luoko initialize_database.py oikeanlaisen tiedoston

# Viikko 4

- Käyttäjän luominen graafisen käyttöliittymän kautta onnistuu
- Ensimmäinen testi toimii; voidaan testata, toimiiko käyttäjän luominen
- Pylint asennettu 
- Autopep8 asennettu
- Task "format" formatoi koodin
- Task "lint" tarkistaa koodin laadun
- Task "build" alustaa nyt tietokannan oikein, että muut moduulit löytävät users.db:n
- Ui:ssa on nyt vaihtoehto roolille
- Roolin valinta toimii ja tallentuu databaseen
- Task coverage report luotu

# Viikko 5
- Lisätty olio "Shift" entities kansioon
- Build -task alustaa nyt myös shift.db tiedoston onnistuneesti
- Luotu toiminnallisuutta vuoron luomiseksi
- Vuoron luominen onnistuu komentorivin kautta, testi tätä varten luotu
- UI rakennettu uudelleen näkymien vaihtamiseksi
- Create user näkymä ilmoittaa uuden käyttäjän luomisesta
- Create user näkymästä voi palata login näkymään

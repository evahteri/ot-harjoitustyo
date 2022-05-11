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
- Employee näkymä luotu ja siihen siirrytään sisäänkirjautumalla
- Virheilmoitus näkyy kun väärillä tunnuksilla yritetään kirjautua
- Virheilmoitus näkyy kun yritetään luoda käyttäjä liian heikolla salasanalla
- Testi sisäänkirjautumista varten luotu

# Viikko 6
- Docstring dokumentaatio aloitettu
- Logout button lisätty employee näkymään
- Näkymä vuorojen tarkastelulle luotu
- Käyttäjä näkee nyt omat vuorot sekä vapaat vuorot eri nappien kautta
- Näkymien välillä voi siirtyä
- Lisätty testit työntekijän vuorojen löytämiselle ja vapaiden vuorojen löytämiselle
- Alustava käyttöohje tehty

# Viikko 7
- Employer näkymä luotu
- Create shift näkymä luotu
- Vuoron luominen graafisen käyttöliittymän kautta onnistuu
- Työnantaja näkee kaikki vuorot
- Kahta samannimistä käyttäjää ei pysty enää luoda
- Shift näkymän choose -button näkyy nyt vain relevantissa näkymässä
- Shift näkymän back -button toiminto palaa nyt oikeaan näkymään
- Vuorojen taulukkoon lisätty "shift id" jonka mukaan tunnistaa uniikit vuorot
- Choose shift toimii nyt
- Ilmoituksia lisätty vuoron valintaan liittyen
- Tallennuksen konfiguraatio uusittu ketterämmäksi
- Testit käyttävät nyt testitietokantoja
- Uusia testejä luotu
- Testit testaavat nyt ohjelmaa laajasti
- Uusi virheviesti sille, jos käyttäjä valitsee liian monta vuoroa itselleen kerralla
- Docstring dokumentaation viimeistely



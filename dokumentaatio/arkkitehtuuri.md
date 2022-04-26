# Käyttäjän kirjautuminen

Käyttäjä näkee näkymässä kentät käyttäjätunnukselle ja salasanalle. Nämä syötettyään käyttäjän painaessa login nappia, seuraavat asiat tapahtuvat:

![Sekvenssikaavio](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sekvenssikaavio.png)

UI käyttää ShiftAppServicen login-funktiota, joka taas käyttää user repositoryn login -funktiota, joka hakee tietokannasta käyttäjän. Tässä vaiheessa nostetaan error jos käyttäjää ei löydy tai salasana ei täsmää. User repository palauttaa user -olion ShiftAppServicelle, joka edelleen palauttaa sen UI:lle ja UI:n näkymä siirtyy roolin mukaiseen näkymään.



# Pakkauskaavio
![Arkkitehtuurikaavio](https://github.com/evahteri/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/arkkitehtuurikaavio_shift_app.drawio(1).svg)

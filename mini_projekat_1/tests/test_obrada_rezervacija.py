from obrada_rezervacija import (
    ObradaRezervacija,
    Rezervacija,
    CsvIzvorRezervacija,
)


class LazniIzvor:
    """Zamjenski izvor podataka za testove."""

    def __init__(self, rezervacije):
        self.rezervacije = rezervacije

    def ucitaj(self):
        return list(self.rezervacije)


class LazniIzvjestaj:
    """Bilježi šta je servis poslao izvještaju."""

    def __init__(self):
        self.sacuvani_iznosi = None

    def sacuvaj(self, iznosi):
        self.sacuvani_iznosi = list(iznosi)


def test_obracunava_iznose_i_salje_ih_izvjestaju():
    izvor = LazniIzvor([
        Rezervacija("Ana", 2, 100.0),
        Rezervacija("Marko", 3, 50.0),
    ])
    izvjestaj = LazniIzvjestaj()
    servis = ObradaRezervacija(izvor, izvjestaj)

    rezultat = servis.izvrsi()

    assert rezultat == [200.0, 150.0]
    assert izvjestaj.sacuvani_iznosi == [200.0, 150.0]


def test_prazan_izvor_vraca_praznu_listu():
    izvjestaj = LazniIzvjestaj()
    servis = ObradaRezervacija(LazniIzvor([]), izvjestaj)

    assert servis.izvrsi() == []
    assert izvjestaj.sacuvani_iznosi == []


def test_servis_ne_zavisi_od_konkretne_implementacije_izvora():
    # Drugi izvor može se ubaciti bez izmjene klase ObradaRezervacija.
    izvor = LazniIzvor([Rezervacija("Ivana", 1, 75.5)])
    izvjestaj = LazniIzvjestaj()

    rezultat = ObradaRezervacija(izvor, izvjestaj).izvrsi()

    assert rezultat == [75.5]
    assert izvjestaj.sacuvani_iznosi == [75.5]


def test_csv_izvor_ucitava_podatke(tmp_path):
    csv_fajl = tmp_path / "rezervacije.csv"
    csv_fajl.write_text(
        "gost,noci,cijena_noci\nAna,2,40\n",
        encoding="utf-8",
    )

    rezervacije = CsvIzvorRezervacija(csv_fajl).ucitaj()

    assert rezervacije == [Rezervacija("Ana", 2, 40.0)]

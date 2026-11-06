"""Obrada rezervacija uz razdvojene odgovornosti i injekciju zavisnosti."""

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol
import csv


@dataclass(frozen=True)
class Rezervacija:
    gost: str
    noci: int
    cijena_noci: float

    @property
    def iznos(self) -> float:
        return self.noci * self.cijena_noci


class IzvorRezervacija(Protocol):
    """Ugovor za svaki izvor podataka o rezervacijama."""

    def ucitaj(self) -> list[Rezervacija]:
        ...


class Izvjestaj(Protocol):
    """Ugovor za svaki način čuvanja/prikaza izvještaja."""

    def sacuvaj(self, iznosi: list[float]) -> None:
        ...


class CsvIzvorRezervacija:
    """Učitava rezervacije iz CSV fajla."""

    def __init__(self, putanja: str | Path) -> None:
        self.putanja = Path(putanja)

    def ucitaj(self) -> list[Rezervacija]:
        rezervacije: list[Rezervacija] = []
        with self.putanja.open("r", newline="", encoding="utf-8") as fajl:
            citac = csv.DictReader(fajl)
            obavezne_kolone = {"gost", "noci", "cijena_noci"}
            if not obavezne_kolone.issubset(set(citac.fieldnames or [])):
                raise ValueError("CSV mora sadržati kolone: gost, noci, cijena_noci")

            for red in citac:
                noci = int(red["noci"])
                cijena = float(red["cijena_noci"])
                if noci <= 0 or cijena < 0:
                    raise ValueError("Noćenja moraju biti pozitivna, a cijena nenegativna")
                rezervacije.append(Rezervacija(red["gost"], noci, cijena))
        return rezervacije


class MemorijskiIzvorRezervacija:
    """Primjer drugog izvora; koristan za testiranje i demonstraciju proširenja."""

    def __init__(self, rezervacije: list[Rezervacija]) -> None:
        self.rezervacije = rezervacije

    def ucitaj(self) -> list[Rezervacija]:
        return list(self.rezervacije)


class TekstualniIzvjestaj:
    """Čuva obračunate iznose u tekstualni fajl."""

    def __init__(self, putanja: str | Path) -> None:
        self.putanja = Path(putanja)

    def sacuvaj(self, iznosi: list[float]) -> None:
        ukupno = sum(iznosi)
        sadrzaj = (
            "Iznosi rezervacija:\n"
            + "\n".join(f"{iznos:.2f}" for iznos in iznosi)
            + f"\nUkupno: {ukupno:.2f}\n"
        )
        self.putanja.write_text(sadrzaj, encoding="utf-8")


class KonzolniIzvjestaj:
    """Alternativni izvještaj koji ispisuje rezultat u konzolu."""

    def sacuvaj(self, iznosi: list[float]) -> None:
        print("Iznosi:", iznosi)
        print(f"Ukupno: {sum(iznosi):.2f}")


class ObradaRezervacija:
    """Koordinira učitavanje, obračun i predaju izvještaja."""

    def __init__(self, izvor: IzvorRezervacija, izvjestaj: Izvjestaj) -> None:
        self.izvor = izvor
        self.izvjestaj = izvjestaj

    def izvrsi(self) -> list[float]:
        rezervacije = self.izvor.ucitaj()
        iznosi = [rezervacija.iznos for rezervacija in rezervacije]
        self.izvjestaj.sacuvaj(iznosi)
        return iznosi


if __name__ == "__main__":
    izvor = CsvIzvorRezervacija("rezervacije.csv")
    izvjestaj = TekstualniIzvjestaj("izvjestaj.txt")
    obrada = ObradaRezervacija(izvor, izvjestaj)
    print("Obračunati iznosi:", obrada.izvrsi())

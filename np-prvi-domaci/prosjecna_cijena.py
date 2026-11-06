import csv
from pathlib import Path


def prosjecna_cijena(putanja: Path) -> float:
    """Vraca ponderisanu prosjecnu cijenu jednog nocenja iz CSV datoteke.

    CSV mora imati kolone: gost, noci, cijena_noci.
    """
    ukupna_vrijednost = 0.0
    ukupno_nocenja = 0

    try:
        with putanja.open(newline="", encoding="utf-8") as datoteka:
            citac = csv.DictReader(datoteka)

            potrebne_kolone = {"gost", "noci", "cijena_noci"}
            if citac.fieldnames is None or not potrebne_kolone.issubset(citac.fieldnames):
                raise ValueError("CSV mora imati kolone: gost, noci, cijena_noci.")

            for broj_reda, red in enumerate(citac, start=2):
                try:
                    noci = int(red["noci"])
                    cijena = float(red["cijena_noci"])
                except (TypeError, ValueError) as greska:
                    raise ValueError(
                        f"Neispravni podaci u redu {broj_reda}."
                    ) from greska

                if noci < 0 or cijena < 0:
                    raise ValueError(
                        f"Broj nocenja i cijena ne mogu biti negativni (red {broj_reda})."
                    )

                ukupna_vrijednost += noci * cijena
                ukupno_nocenja += noci

    except FileNotFoundError as greska:
        raise FileNotFoundError(f"Datoteka nije pronadjena: {putanja}") from greska

    if ukupno_nocenja == 0:
        raise ValueError("Nema ostvarenih nocenja za izracunavanje prosjeka.")

    return ukupna_vrijednost / ukupno_nocenja

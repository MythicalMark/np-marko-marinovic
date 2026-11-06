# Prvi domaci – Napredno programiranje

## Opis projekta

Program racuna ponderisanu prosjecnu cijenu jednog nocenja na osnovu podataka iz CSV datoteke.

Ponderisani prosjek se racuna tako sto se ukupna vrijednost svih nocenja podijeli ukupnim brojem nocenja:

`zbir(noci * cijena_noci) / zbir(noci)`

CSV datoteka mora imati kolone `gost`, `noci` i `cijena_noci`.

## Potrebni alati

- Python 3.12 ili noviji
- Git i GitHub
- VS Code
- Ruff
- Pytest

## Pokretanje projekta

1. Napraviti i aktivirati virtuelno okruzenje.
2. Instalirati razvojne alate komandom:

   `python -m pip install -e ".[dev]"`

3. Pokrenuti testove:

   `pytest -q`

4. Provjeriti stil koda:

   `ruff check .`

5. Formatirati kod:

   `ruff format .`

## AI upit (prompt)

Kontekst: Koristim Python 3.12. Podaci o hotelskim rezervacijama nalaze se u CSV datoteci sa kolonama: gost, noci i cijena_noci.

Zadatak: Napisi Python funkciju `prosjecna_cijena(putanja: Path) -> float` koja racuna ponderisanu prosjecnu cijenu nocenja. Ukupnu vrijednost racunaj kao zbir proizvoda broja nocenja i cijene po noci, a zatim podijeli ukupnim brojem nocenja.

Ogranicenja: Koristi samo standardnu Python biblioteku, type hints, `csv.DictReader` i `pathlib.Path`. Datoteku otvaraj pomocu `with`. Obradi slucaj nepostojece datoteke, prazne datoteke, nedostajuce kolone i neispravne ili negativne vrijednosti. Ako nema nijednog ostvarenog nocenja, podigni `ValueError`.

Format odgovora: Prikazi kod funkcije, najmanje tri pytest testa i kratko objasnjenje rjesenja.

## Nedostaci koje treba provjeriti kod AI-generisanog koda

Prva, jednostavna verzija funkcije moze imati sljedece nedostatke:

1. Ne provjerava da li CSV ima sve potrebne kolone.
2. Ne obradjuje neispravne vrijednosti u kolonama `noci` i `cijena_noci`.
3. Ne provjerava negativan broj nocenja ili negativnu cijenu.
4. Ne daje dovoljno jasnu poruku kada datoteka ne postoji.
5. Testira samo jedan primjer, a ne i prazne/neispravne podatke.

U ovom projektu su dodate provjere i testovi za navedene slucajeve.

## Testiranje

Testovi provjeravaju:
- tacan ponderisani prosjek;
- slucaj bez ostvarenih nocenja;
- neispravan broj nocenja;
- nedostajuce kolone;
- datoteku koja ne postoji.



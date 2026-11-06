# Mini projekat 1 – Refaktoring obrade rezervacija

## Opis zadatka

Monolitna klasa iz prezentacije obavljala je više poslova: učitavanje podataka,
obračun iznosa, čuvanje izvještaja i obavještavanje. Rješenje je refaktorisano
tako da svaka komponenta ima jasnu odgovornost.

## Struktura

- `Rezervacija` – predstavlja jednu rezervaciju i računa njen iznos.
- `IzvorRezervacija` – Protocol koji definiše ugovor za učitavanje podataka.
- `Izvjestaj` – Protocol koji definiše ugovor za čuvanje/prikaz izvještaja.
- `CsvIzvorRezervacija` – učitava podatke iz CSV fajla.
- `MemorijskiIzvorRezervacija` – drugi izvor podataka.
- `TekstualniIzvjestaj` i `KonzolniIzvjestaj` – dvije implementacije izvještavanja.
- `ObradaRezervacija` – koordinira obradu, bez poznavanja konkretnih implementacija.

## Primijenjeni principi

### Single Responsibility (S)

Učitavanje, predstavljanje rezervacije, obrada i izvještavanje razdvojeni su
u zasebne klase. Promjena CSV formata ne zahtijeva izmjenu klase za obračun.

### Dependency Inversion (D)

`ObradaRezervacija` zavisi od Protocol ugovora `IzvorRezervacija` i `Izvjestaj`,
a ne od konkretnih CSV ili tekstualnih klasa. Zavisnosti se prosljeđuju
kroz konstruktor.

### Open / Closed (O)

Novi izvor ili način izvještavanja može se dodati implementacijom postojećeg
Protocol-a, bez izmjene klase `ObradaRezervacija`.

## Pokretanje

Potrebno je imati Python 3.12 ili noviji.

Iz ovog foldera pokrenuti:

```bash
python -m pip install pytest ruff
pytest -q
ruff check .
python obrada_rezervacija.py
```

Testovi koriste zamjenski izvor i zamjenski izvještaj, tako da ne zavise od
stvarne baze, fajla izvještaja ili mreže.

## Testiranje

Testovi provjeravaju:
1. obračun više rezervacija i predaju iznosa izvještaju;
2. ponašanje kada nema rezervacija;
3. zamjenu izvora podataka bez izmjene servisa;
4. učitavanje podataka iz CSV fajla.

## Upiti korišćeni AI asistentu

1. „Refaktoriši klasu koja učitava rezervacije, računa iznose i čuva izvještaj
   primjenom Single Responsibility principa.“
2. „Uvedi typing.Protocol za izvor podataka i izvještaj i primijeni injekciju
   zavisnosti kroz konstruktor.“
3. „Dodaj najmanje tri pytest testa koji koriste zamjenski izvor podataka.“
4. „Provjeri da li novi izvor podataka može da se doda bez izmjene klase servisa.“

## Ispravke i kritička provjera AI koda

- Provjereno je da servis ne pravi sam konkretan CSV izvor ili izvještaj,
  već ih prima kroz konstruktor.
- Testovi koriste lažne (zamjenske) objekte, pa se ponašanje servisa može
  provjeriti bez spoljnih zavisnosti.
- Dodata je provjera obaveznih CSV kolona i osnovna validacija broja noćenja
  i cijene.
- AI prijedloge treba provjeriti pokretanjem testova; generisani kod nije
  prihvaćen bez provjere.



# Mini projekat 3 — Testiran i obezbijeđen API

## Opis
FastAPI servis za obračun cijene hotelske rezervacije, prema primjeru iz prezentacije Nedjelja 5. API demonstrira validaciju zahtjeva, automatizovano testiranje, CI i osnovne bezbjednosne kontrole iz Nedjelje 6.

## Endpointi
- `GET /health` — status servisa
- `GET /info` — naziv i verzija
- `POST /cijena` — izračun cijene sa brojem noći, cijenom noći i popustom

Validacija ograničava broj noći na 1–30, cijenu na pozitivnu vrijednost do 10.000 i popust na interval 0–1. Neispravan zahtjev FastAPI/Pydantic odbija HTTP statusom 422.

## Testiranje
Testovi koriste `pytest` i FastAPI `TestClient`, pa server nije potrebno ručno pokretati. `fixture` priprema standardni zahtjev, a `pytest.mark.parametrize` pokreće isti test nad više skupova ulaza. Pokriveni su uspješan obračun, popusti, granične vrijednosti, nevalidni podaci, health/info i nepostojeća ruta. Testovi provjeravaju ponašanje i pragove/statusne kodove, ne zavise od mreže ili plaćenog API-ja.

U Colab-u pokrenuti ćelije redom. Testna ćelija izvršava `pytest -q`.

## Kontinuirana integracija
`.github/workflows/ci.yml` automatski pokreće provjere na `push` i `pull_request`:
1. `ruff check` — stil i česte greške
2. `mypy` — provjera tipova
3. `pytest` — testovi
4. `bandit` — bezbjednosni pregled Python koda
5. `pip-audit` — provjera poznatih ranjivosti zavisnosti

## Bezbjednosni rizici i mjere
1. **Nevalidiran korisnički unos:** ograničenja Pydantic modela odbacuju neispravne vrijednosti.
2. **Tajne u kodu:** projekat ne sadrži API ključeve; u stvarnoj aplikaciji tajne čuvati u environment varijablama ili secret manager-u.
3. **Ranjive zavisnosti:** `pip-audit` provjerava instalirane pakete; održavati zavisnosti ažurnim.
4. **SQL/komandna injekcija:** trenutni API ne izvršava SQL ni shell komande. Ako se uvedu, koristiti parametrizovane upite i izbjegavati `shell=True` sa korisničkim unosom.
5. **Nesigurna deserijalizacija:** ne učitavati nepouzdane datoteke pomoću `pickle`; koristiti JSON za razmjenu podataka.
6. **Osjetljivi podaci u logovima:** ne zapisivati lozinke, tokene ili lične podatke.



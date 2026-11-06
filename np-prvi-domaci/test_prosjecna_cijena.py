import pytest

from prosjecna_cijena import prosjecna_cijena


def test_ponderisani_prosjek(tmp_path):
    putanja = tmp_path / "rezervacije.csv"
    putanja.write_text(
        "gost,noci,cijena_noci\nAna,2,100\nMarko,2,50\nIvana,1,80\n",
        encoding="utf-8",
    )

    assert prosjecna_cijena(putanja) == 76.0


def test_prazna_datoteka_bez_nocenja(tmp_path):
    putanja = tmp_path / "prazna.csv"
    putanja.write_text("gost,noci,cijena_noci\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Nema ostvarenih nocenja"):
        prosjecna_cijena(putanja)


def test_neispravni_broj_nocenja(tmp_path):
    putanja = tmp_path / "greska.csv"
    putanja.write_text(
        "gost,noci,cijena_noci\nAna,dva,100\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Neispravni podaci"):
        prosjecna_cijena(putanja)


def test_nedostajuce_kolone(tmp_path):
    putanja = tmp_path / "kolone.csv"
    putanja.write_text("gost,noci\nAna,2\n", encoding="utf-8")

    with pytest.raises(ValueError, match="CSV mora imati kolone"):
        prosjecna_cijena(putanja)


def test_datoteka_ne_postoji(tmp_path):
    putanja = tmp_path / "ne_postoji.csv"

    with pytest.raises(FileNotFoundError):
        prosjecna_cijena(putanja)

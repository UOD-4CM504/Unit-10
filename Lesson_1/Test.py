import pytest
from main import Plumber, Roomba


@pytest.fixture
def plumber_merio():
    return Plumber("Merio")


@pytest.fixture
def plumber_luegi():
    return Plumber("Luegi")


@pytest.fixture
def roomba_hetti():
    return Roomba("Hetti")


@pytest.fixture
def roomba_olga():
    return Roomba("Olga")


def test_plumber_creation(plumber_merio, plumber_luegi):
    assert plumber_merio.name == "Merio"
    assert plumber_luegi.name == "Luegi"


def test_roomba_creation(roomba_hetti, roomba_olga):
    assert roomba_hetti.name == "Hetti"
    assert roomba_hetti._squashed == False
    assert roomba_olga.name == "Olga"
    assert roomba_olga._squashed == False


def test_plumber_squash_roomba(plumber_merio, plumber_luegi, roomba_hetti, roomba_olga):
    assert roomba_hetti._squashed == False
    plumber_merio.squash(roomba_hetti)
    assert roomba_hetti._squashed == True

    assert roomba_olga._squashed == False
    plumber_luegi.squash(roomba_olga)
    assert roomba_olga._squashed == True


@pytest.mark.parametrize("roomba_name", ["Hetti", "Olga"])
def test_roomba_initial_state(roomba_name):
    r = Roomba(roomba_name)
    assert r.name == roomba_name
    assert r._squashed == False

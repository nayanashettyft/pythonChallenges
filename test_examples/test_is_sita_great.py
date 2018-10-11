import pytest

from GreatPersonTruth import GreatPersonTruth

@pytest.fixture
def get_truth_obj():
    return GreatPersonTruth()

def test_Sita_is_great(get_truth_obj):
    assert get_truth_obj.is_person_great('Sita') == "great"

def test_sita_is_not_great(get_truth_obj):
    assert get_truth_obj.is_person_great('sita') == None

def test_Rita_is_not_great(get_truth_obj):
    assert get_truth_obj.is_person_great('Rita') == None
import pytest
from workout_planner import calculate_bmi, get_plan, gym_or_home

def test_calculate_bmi():
    assert calculate_bmi(70, 175) == 22.86
    with pytest.raises(ValueError):
        calculate_bmi(-60, 170)

def test_get_plan():
    assert get_plan(17)[0] == "Underweight"
    assert get_plan(24)[0] == "Normal"
    assert get_plan(27)[0] == "Overweight"
    assert get_plan(32)[0] == "Obese"

def test_gym_or_home():
    assert gym_or_home(23) == "Home"
    assert gym_or_home(27) == "Gym"

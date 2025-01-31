#library
import python_tuorial as p
import pytest

def test_addition():
    assert (5+7) == 12

@pytest.mark.parametrize("weight, unit, con_weight", 
[(69, "L", (69*2.205)), (69, "l", (69*2.205)), (69, "k", (69/2.205)),
(69, "K", (69/2.205))])
def test_weight_conversion(weight, unit, con_weight):
    assert p.Weight_Conversion(weight,unit) == con_weight

@pytest.mark.parametrize("weight, unit", [("aaa", "K"), (-10, "L"), (80, "aaa")])
def test_weight_conversion_ValueError(weight, unit): 
    with pytest.raises(ValueError):
        p.Weight_Conversion(weight, unit)


@pytest.mark.parametrize ("Temp, rainfall, event_happening", [(20, True, False), (-10, False, False), 
                        (40, False, False), (25, False, True), (25, True, False), (35, False, True)])
def test_outdoor_event_check(Temp, rainfall, event_happening):
    assert p.outdoor_event_check(Temp, rainfall) == event_happening


@pytest.mark.parametrize ("base, height", [ (2.65788,1), (1000,4.5)])
def test_area_triangle(base, height):
    assert p.area_triangle(base,height) == (0.5*base*height)

@pytest.mark.parametrize("base, height", [(0,1), (-1000, 200)])
def test_area_triangle_ValueError(base, height):
    with pytest.raises(ValueError): 
        p.area_triangle(base, height)

@pytest.mark.parametrize("base, height", [("Boy", 1), (True, False)])
def test_area_triangle_TypeError(base, height):
    with pytest.raises(TypeError):
        p.area_triangle(base, height)


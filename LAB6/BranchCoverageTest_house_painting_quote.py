"""Lab 6: tests that execute every application statement."""
import pytest
from house_painting_quote import painting_quote, paint_litres, crew_days


def test_exterior_enamel():
    assert painting_quote("enamel", 500, 2, True) == 32500


def test_unknown_paint():
    with pytest.raises(ValueError, match="^unknown paint$"):
        painting_quote("acrylic", 500, 1, False)


def test_invalid_area():
    with pytest.raises(ValueError, match="^invalid job$"):
        painting_quote("emulsion", 0, 1, False)


def test_exterior_distemper_rejected():
    with pytest.raises(ValueError, match="^distemper is for interiors only$"):
        painting_quote("distemper", 500, 1, True)


def test_large_job_discount():
    # 3000 * 20 = 60000; ten percent discount = 6000.
    assert painting_quote("emulsion", 3000, 1, False) == 54000


def test_minimum_charge():
    assert painting_quote("distemper", 100, 1, False) == 5000


def test_smooth_litres():
    assert paint_litres(200, 1, "smooth") == 2


def test_rough_litres_rounded_up():
    assert paint_litres(100, 1, "rough") == 2


def test_unknown_surface():
    with pytest.raises(ValueError, match="^unknown surface$"):
        paint_litres(100, 1, "metal")


def test_no_painters():
    with pytest.raises(ValueError, match="^need at least one painter$"):
        crew_days(800, 0, False)


def test_crew_rounding_and_wallpaper():
    # Two painters cover 800 sqft/day: round 801/800 up to 2, add 2.
    assert crew_days(801, 2, True) == 4


@pytest.mark.parametrize("area,coats", [(100, 0), (100, -1), (-1, 1)])
def test_other_invalid_jobs(area, coats):
    with pytest.raises(ValueError, match="^invalid job$"):
        painting_quote("emulsion", area, coats, False)


@pytest.mark.parametrize("area,expected", [(1999, 39980), (2000, 40000), (2001, 36018)])
def test_discount_boundary(area, expected):
    assert painting_quote("emulsion", area, 1, False) == expected


@pytest.mark.parametrize("area,expected", [(249, 5000), (250, 5000), (251, 5020)])
def test_minimum_charge_boundary(area, expected):
    assert painting_quote("emulsion", area, 1, False) == expected


def test_exterior_emulsion():
    assert painting_quote("emulsion", 500, 1, True) == 12500


def test_exterior_discount_includes_surcharge():
    assert painting_quote("enamel", 3000, 2, True) == 175500


@pytest.mark.parametrize("area,coats,surface,expected", [
    (100, 1, "smooth", 1), (101, 1, "smooth", 2),
    (60, 1, "rough", 1), (61, 1, "rough", 2),
    (100, 2, "rough", 4),
])
def test_litre_boundaries(area, coats, surface, expected):
    assert paint_litres(area, coats, surface) == expected


@pytest.mark.parametrize("area,painters,wallpaper,expected", [
    (800, 2, False, 1), (801, 2, False, 2),
    (800, 2, True, 3), (400, 1, False, 1),
])
def test_crew_decisions(area, painters, wallpaper, expected):
    assert crew_days(area, painters, wallpaper) == expected

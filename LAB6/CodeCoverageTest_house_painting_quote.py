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

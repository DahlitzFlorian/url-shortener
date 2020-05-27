from app.services import shortener


def test_true_ord_digit():
    """Test true_ord function with digit"""
    assert shortener.true_ord("1") == 1


def test_true_ord_lower():
    """Test true_ord function with lower-case character"""
    assert shortener.true_ord("a") == 36


def test_true_ord_upper():
    """Test true_ord function with upper-case character"""
    assert shortener.true_ord("A") == 10


def test_true_chr_digit():
    """Test true_chr function with digit"""
    assert shortener.true_chr(1) == "1"


def test_true_chr_lower():
    """Test true_chr function with lower-case character"""
    assert shortener.true_chr(36) == "a"


def test_true_chr_upper():
    """Test true_chr function with upper-case character"""
    assert shortener.true_chr(10) == "A"


def test_dehydrate_small_number():
    """Test dehydrate function with small number"""
    assert shortener.dehydrate(5) == "5"


def test_dehydrate_large_number():
    """Test dehydrate function with large number"""
    assert shortener.dehydrate(10_000) == "2SG"


def test_saturate_short_string():
    """Test saturate function with short string"""
    assert shortener.saturate("Q5e") == 106856


def test_saturate_long_string():
    """Test saturate function with long string"""
    assert shortener.saturate("3ej16Ypa7d8d") == 268288747256799982119

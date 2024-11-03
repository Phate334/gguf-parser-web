from app.utils import abbreviate_number, human_readable_size


def test_human_readable_size():
    assert human_readable_size(500) == "500.00 B"
    assert human_readable_size(1023) == "1023.00 B"
    assert human_readable_size(1024) == "1.00 KB"
    assert human_readable_size(1048576) == "1.00 MB"
    assert human_readable_size(1073741824) == "1.00 GB"


def test_abbreviate_number():
    assert abbreviate_number(500) == "500"
    assert abbreviate_number(999) == "999"
    assert abbreviate_number(1000) == "1.00 K"
    assert abbreviate_number(1500000) == "1.50 M"
    assert abbreviate_number(2000000000) == "2.00 B"

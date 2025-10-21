import functions

def test_get_page_books():
    # Invalid Index
    assert functions.get_page_books(-1).empty
    # Valid Index
    assert not functions.get_page_books(1).empty
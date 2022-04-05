from _lib.runescape_fetcher import RunscapeFetcher

def test_fetcher():
    fetcher = RunscapeFetcher()
    assert fetcher.get_text()

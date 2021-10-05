import pytest

@pytest.director
class Director:
    def test_get_code(self):
        pass

    def test_start_game(self):
        pass


@pytest.code
class Code():
    def test_generate_code():
        pass

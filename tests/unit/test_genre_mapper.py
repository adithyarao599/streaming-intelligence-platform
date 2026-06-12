from app.silver.genre_mapper import GenreMapper


def test_genre_mapping():

    result = GenreMapper.normalize("Hip-Hop")

    assert result == "HIP_HOP"

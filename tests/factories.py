import factory

from models import Anime


class AnimeFactory(factory.Factory):
    class Meta:
        model = Anime

    anime_id = 11
    name = 'anime_default'
    genre = 'Action'
    type = 'TV'
    episodes = '27'
    rating = 8.0
    members = 123456

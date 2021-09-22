from enum import Enum


class Choice(Enum):
    @classmethod
    def choice(cls):
        return [(c.value, c.name) for c in cls]

    @classmethod
    def repr(cls):
        return {c.name: {'id': c.value, 'name': c.name} for c in cls}

    @classmethod
    def list(cls):
        return [c.value for c in cls]

    def __str__(self):
        return self.value


class GenModeratorChoice(str, Choice):
    USER1 = 'User1'
    Moderator = "Moderator"
    Admin = "Admin"


class Likes(str, Choice):
    LIKE = 'Like'
    DISLAKE = 'Dislake'


class ViewChoise(str, Choice):
    BLOG = 'Blog'
    NEWS = 'News'
    ADVERTISING = 'Advertising'

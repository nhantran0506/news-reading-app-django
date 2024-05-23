from enum import Enum

class Category(Enum):
    SPORTS = 'Sports'
    TECHNOLOGY = 'Technology'
    ENTERTAINMENT = 'Entertainment'
    POLITICS = 'Politics'
    HEALTH = 'Health'
    EDUCATION = 'Education'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

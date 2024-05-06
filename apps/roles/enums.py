from enum import Enum

class Roles(Enum):
  Publisher = 'Publisher'
  Author = 'Author'
  Reader = 'Reader'

  @classmethod
  def choices(cls):
    return [(role.value, role.name) for role in cls]

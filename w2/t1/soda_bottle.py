class SodaBottle:
  __brand: str
  __volume: float
  __separator: str = ';'

  def __init__ (self, brand: str, volume: float):
    self.__brand = brand
    self.__volume = volume

  @property
  def serialize(self) -> str:
    param_list = []
    for key, value in vars(self).items():
      param_list.append(value)
    return self.__separator.join(param_list)
      
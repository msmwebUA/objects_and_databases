class SodaBottle:
  brand: str
  volume: float
  separator: str = ';'

  def __init__ (self, brand: str, volume: float):
    self.brand = brand
    self.volume = volume

  @property
  def serialize(self) -> str:
    param_list = []
    for key, value in vars(self).items():
      param_list.append(value)
    return self.separator.join(param_list)

  @staticmethod
  def deserialize(serialised_str: str) -> 'SodaBottle':
    values = serialised_str.split(';')
    return SodaBottle(brand = values[0], volume = values[1])
      
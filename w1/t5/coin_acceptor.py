class CoinAcceptor:
  __amount: int
  __value: float

  def __init__(self) -> None:
    self.__amount = 0
    self.__value = 0.0
    return None

  def insertCoin(self, value: float) -> None:
    self.__amount += 1
    self.__value += value
    return None

  def getAmount(self) -> tuple[int, float]:
    return (self.__amount, self.__value)

  def returnCoins(self) -> tuple[int, float]:
    current_coins = self.__amount
    current_value = self.__value
    self.__amount = 0
    self.__value = 0
    return (current_coins, current_value)
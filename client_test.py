import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  
  
  def test_getDataPoint_calculatePrice(self):
    """This test simply calculates the bid price and the ask price"""
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      actualStock = quote["stock"]
      actualBidPrice = quote["top_bid"]["price"]
      actualAskPrice = quote["top_ask"]["price"]
      actualPrice = (actualBidPrice + actualAskPrice) / 2 
      self.assertEqual(getDataPoint(quote), (actualStock, actualBidPrice, actualAskPrice, actualPrice))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
     """This test covers the scenario where the bid price is greater than the ask price."""
     quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
     for quote in quotes:
      actualStock = quote["stock"]
      actualBidPrice = quote["top_bid"]["price"]
      actualAskPrice = quote["top_ask"]["price"]
      actualPrice = (actualBidPrice + actualAskPrice) / 2 
      self.assertEqual(getDataPoint(quote), (actualStock, actualBidPrice, actualAskPrice, actualPrice))
  
  def test_priceBZero(self):
    """This test covers the rare scenario where price_b is 0."""
    self.assertIsNone(getRatio(100, 0))


if __name__ == '__main__':
    unittest.main()

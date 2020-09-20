import converters
from converters import emoji_picker
from utils import find_max
import ecommerce.shipping
from ecommerce.shipping import calc_shipping
from ecommerce import shipping

print(converters.kg_to_lbs(119))

print(emoji_picker("Aha nice :) good function"))

numbers = [2, 4, 10, 13, 8, 20, 17]

print(find_max(numbers))
ecommerce.shipping.calc_shipping()
calc_shipping()

shipping.calc_shipping()

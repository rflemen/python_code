class Playing_Card:
	"""A simple attempt to represent a playing card."""

	def __init__(self, name, suit, value):
		"""Initialize attributes to describe card."""
		self.name = name
		self.suit = suit
		self.value = value

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name of the card."""
		return f"{self.name} of {self.suit}"

	def get_name(self):
		"""Return the simple name of the card"""
		playing_card_name = self.name
		return self.name

	def get_suit(self):
		"""Return the suit of the card."""
		return self.suit

	def get_value(self):
		"""Return the value of the card."""
		return self.value

my_playing_card = Playing_Card('ace','hearts', 11)
print(my_playing_card.get_descriptive_name())
print(my_playing_card.get_name())
print(my_playing_card.get_suit())
print(my_playing_card.get_value())
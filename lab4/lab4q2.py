#lab4q2.py
# House Management System
# Room class
class Room:
    """Represents a room in the house."""

    def __init__(self, room_type: str, size: int):
        self._type = room_type
        self._size = size

    # Getter and Setter for type
    @property
    def type(self):
        """Returns the room type (e.g., Bedroom, Kitchen)."""
        return self._type

    @type.setter
    def type(self, value):
        """Updates the room type."""
        self._type = value

    # Getter and Setter for size
    @property
    def size(self):
        """Returns the size of the room in square feet."""
        return self._size

    @size.setter
    def size(self, value):
        """Updates the size of the room in square feet."""
        self._size = value

    def __eq__(self, other):
        return isinstance(other, Room) and self._type == other._type and self._size == other._size

    def __repr__(self):
        return f"Room(type='{self._type}', size={self._size})"

    def __str__(self):
        return f"{self._type} ({self._size} sqft)"


# Garage class
class Garage:
    """Represents a garage in the house."""

    def __init__(self, garage_type: str, size: int, door_type: str):
        self._type = garage_type
        self._size = size
        self._door_type = door_type

    @property
    def type(self):
        """Returns the garage type (single/double)."""
        return self._type

    @type.setter
    def type(self, value):
        """Updates the garage type."""
        self._type = value

    @property
    def size(self):
        """Returns the garage size in square feet."""
        return self._size

    @size.setter
    def size(self, value):
        """Updates the garage size."""
        self._size = value

    @property
    def door_type(self):
        """Returns the garage door type (manual/auto)."""
        return self._door_type

    @door_type.setter
    def door_type(self, value):
        """Updates the garage door type."""
        self._door_type = value

    def __eq__(self, other):
        return isinstance(other, Garage) and self._type == other._type and self._size == other._size

    def __repr__(self):
        return f"Garage(type='{self._type}', size={self._size}, door='{self._door_type}')"

    def __str__(self):
        return f"{self._type} Garage ({self._size} sqft, Door: {self._door_type})"


# Television class
class Television:
    """Represents a television in the house."""

    def __init__(self, screen_type: str, screen_size: int, resolution: str, price: float):
        self._screen_type = screen_type
        self._screen_size = screen_size
        self._resolution = resolution
        self._price = price

    @property
    def screen_type(self):
        """Returns the screen type (LCD, OLED, etc.)."""
        return self._screen_type

    @screen_type.setter
    def screen_type(self, value):
        """Updates the screen type."""
        self._screen_type = value

    @property
    def screen_size(self):
        """Returns the screen size in inches."""
        return self._screen_size

    @screen_size.setter
    def screen_size(self, value):
        """Updates the screen size."""
        self._screen_size = value

    @property
    def resolution(self):
        """Returns the screen resolution (1080p, 4K, etc.)."""
        return self._resolution

    @resolution.setter
    def resolution(self, value):
        """Updates the screen resolution."""
        self._resolution = value

    @property
    def price(self):
        """Returns the TV price."""
        return self._price

    @price.setter
    def price(self, value):
        """Updates the TV price."""
        self._price = value

    def __eq__(self, other):
        return isinstance(other, Television) and self._screen_type == other._screen_type and self._screen_size == other._screen_size

    def __repr__(self):
        return f"Television(type='{self._screen_type}', size={self._screen_size}, res='{self._resolution}', price={self._price})"

    def __str__(self):
        return f"{self._screen_size}\" {self._screen_type} ({self._resolution}) - ${self._price}"

# House class
class House:
    """Represents a house with rooms, a garage, and televisions."""

    def __init__(self, address: str, square_feet: int, rooms: list, garage: Garage, televisions: list):
        self._address = address
        self._square_feet = square_feet
        self._rooms = rooms
        self._garage = garage
        self._televisions = televisions

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def square_feet(self):
        return self._square_feet

    @square_feet.setter
    def square_feet(self, value):
        self._square_feet = value

    @property
    def rooms(self):
        return self._rooms

    @property
    def garage(self):
        return self._garage

    @garage.setter
    def garage(self, value):
        self._garage = value

    @property
    def televisions(self):
        return self._televisions

    def add_television(self, tv: Television):
        """Adds a television to the house."""
        self._televisions.append(tv)

    def remove_television(self, tv: Television):
        """Removes a television from the house."""
        self._televisions = [t for t in self._televisions if t != tv]

    def get_biggest_room(self):
        """Returns the largest room by size."""
        return max(self._rooms, key=lambda r: r.size, default=None)

    def get_oled_televisions(self):
        """Returns a list of televisions with OLED display."""
        return [tv for tv in self._televisions if tv.screen_type.lower() == "oled"]

    def is_similar_house(self, other):
        """Two houses are similar if they have same square footage and number of rooms."""
        return self._square_feet == other._square_feet and len(self._rooms) == len(other._rooms)

    def __eq__(self, other):
        return isinstance(other, House) and self._address == other._address

    def __repr__(self):
        return f"House(address='{self._address}', size={self._square_feet}, rooms={len(self._rooms)})"

    def __str__(self):
        rooms_str = "\n".join(str(r) for r in self._rooms)
        tvs_str = "\n".join(str(tv) for tv in self._televisions)
        return f"House at {self._address}\nSize: {self._square_feet} sqft\nGarage: {self._garage}\nRooms:\n{rooms_str}\nTelevisions:\n{tvs_str}"


# Main method with example
if __name__ == "__main__":
    # Create rooms
    room1 = Room("Bedroom", 200)
    room2 = Room("Living Room", 400)
    room3 = Room("Kitchen", 180)

    # Create garage
    garage = Garage("Double", 300, "Auto")

    # Create televisions
    tv1 = Television("OLED", 65, "4K", 1200)
    tv2 = Television("LCD", 55, "1080p", 500)
    tv3 = Television("OLED", 75, "8K", 3000)

    # Create house
    house1 = House("123 NY St", 2000, [room1, room2, room3], garage, [tv1, tv2])

    print(house1)

    # Add a new TV
    house1.add_television(tv3)
    print("\nAfter adding a new TV:")
    print(house1)

    # Biggest room
    print("\nBiggest room:", house1.get_biggest_room())

    # OLED TVs
    print("\nOLED TVs:", house1.get_oled_televisions())

    # Compare with another house
    house2 = House("456 SF St", 2000, [room1, room2, room3], garage, [])
    print("\nAre the houses similar?", house1.is_similar_house(house2))
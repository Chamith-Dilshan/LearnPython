class HashTable:
    def __init__(self):
        """Initialize HashTable with an empty collection dictionary"""
        self.collection = {}

    def hash(self, key):
        """
        Compute hash value as a sum of Unicode values of characters in the key.

        Args:
            key (str): The string key to hash

        Returns:
            int: Sum of ord() values for each character in the key
        """
        return sum(ord(char) for char in key)

    def add(self, key, value):
        """
        Add a key-value pair to the hash table.

        If multiple keys produce the same hash, they're stored in the same
        nested dictionary under different keys.

        Args:
            key (str): The key to store
            value: The value to associate with the key
        """
        hashed_key = self.hash(key)
        # Create nested dictionary if this hash value doesn't exist yet
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}

        # Store the key-value pair in the nested dictionary
        self.collection[hashed_key][key] = value

    def remove(self, key):
        """
        Remove a key-value pair from the hash table.

        Args:
            key (str): The key to remove
        """
        hashed_key = self.hash(key)

        # Check if hash exists and key exists in nested dictionary
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            del self.collection[hashed_key][key]
            # Clean up empty nested dictionaries
            if not self.collection[hashed_key]:
                del self.collection[hashed_key]

    def lookup(self, key):
        """
        Retrieve the value associated with a key.

        Args:
            key (str): The key to look up

        Returns:
            The value associated with the key, or None if not found
        """
        hashed_key = self.hash(key)
        # Check if hash exists and key exists in nested dictionary
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]
        return None


def main():
    # Create hash table
    ht = HashTable()

    # Add items
    ht.add("name", "Alice")
    ht.add("age", 30)

    # Lookup values
    print(ht.lookup("name"))  # Output: Alice
    print(ht.lookup("age"))  # Output: 30

    # Remove an item
    ht.remove("age")
    print(ht.lookup("age"))  # Output: None

    # Handle collisions (different keys, same hash)
    ht.add("abc", "value1")
    ht.add("bac", "value2")  # May have same hash as "abc"
    print(ht.lookup("abc"))  # Output: value1
    print(ht.lookup("bac"))  # Output: value2


if __name__ == "__main__":
    main()

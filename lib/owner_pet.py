class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []  

    def add_pet(self, pet):
        """Adds a pet to the owner's list of pets."""
        if isinstance(pet, Pet):  
            self.pets.append(pet)
            pet.owner = self  
        else:
            raise TypeError("Only Pet instances can be added.")

    def get_sorted_pets(self):
        """Returns a sorted list of pet objects by name."""
        return sorted(self.pets, key=lambda pet: pet.name)  


class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"{pet_type} is not a valid pet type")

        self.name = name
        self.pet_type = pet_type
        self._owner = None  
        self.owner = owner  

        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        """Sets the pet's owner and ensures it's an Owner instance."""
        if new_owner is not None:
            if isinstance(new_owner, Owner):
                self._owner = new_owner
                if self not in new_owner.pets:  
                    new_owner.add_pet(self)
            else:
                raise TypeError("Owner must be an instance of Owner")

class Frame:
    def __init__(self):
        self.slots = {}

    def fill_slot(self, slot, value):
        self.slots[slot] = value

    def get_slot(self, slot):
        return self.slots.get(slot, None)

    def is_filled(self):
        return all(value is not None for value in self.slots.values())

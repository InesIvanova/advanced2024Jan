class Glass:
    """
    This class produces glasses
    """
    capacity = 250

    def __init__(self):
        """
        This is the init to create instances of this class
        """
        self.content = 0

    def fill(self, ml):
        """
        If there is enough capacity we fill the glass
        :param ml: fload
        :return: string - the output of the action
        """
        if Glass.capacity >= (self.content + ml):
            self.content += ml
            return f"Glass filled with {ml} ml"
        return f"Cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        diff = Glass.capacity - self.content
        return f"{diff} ml left"



print(Glass.__doc__)
print(Glass.fill.__doc__)
glass = Glass()
print(Glass.__dict__)
print(glass.__dict__)

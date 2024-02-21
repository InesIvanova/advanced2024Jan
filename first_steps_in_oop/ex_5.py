class Engine:
    def __init__(self):
        pass


class Car:
    def __init__(self, engine):
        self.engine = engine


class Music(object):
    def __init__(self, length: int, name: str):
        self.length = length


song = Music(30)
song.asd = "Test"

song2 = Music(30)

print(song.asd)
print(song2.asd)



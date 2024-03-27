from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def writeData(self, data):
        pass

    @abstractmethod
    def readData(self) -> str:
        pass


class FileDataSource(DataSource):
    def __init__(self, filename):
        self._file = filename

    def writeData(self, data):
        # write data to file.
        with open(self._file, "a") as f:
            f.write(data)

    def readData(self) -> str:
        # read data from file.
        with open(self._file, "r") as f:
            return f.read()


class EncryptionDecorator(DataSource):
    def writeData(self, data):
        # encrypt the data
        # pass encrypted data to wrapper
        return ''.join([str(ord(c) for c in data)])

    def readData(self) -> str:
        # get encrypted data
        # decrypt it
        # return it
        data = ""
        return ''.join([str(chr(c) for c in data)])


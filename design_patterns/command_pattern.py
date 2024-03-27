# check size
# check headers (column names, missing?)
# check data in column Age (all rows should be with values)


from abc import ABC, abstractmethod
class Invoker:
    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()


class Command(ABC):
    def __init__(self, receiver):
        self._receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class CheckSizeCommand(Command):
    def execute(self):
        if len(self._receiver) < 3:
            raise ValueError("File is below certain size")


class HeaderCheckerFile(Command):
    def execute(self):
        if self._receiver.columns != ["name", "age"]:
            raise ValueError("Headers are invalid")


class AgeColumnCheckerFile(Command):
    def execute(self):
        if len(self._receiver['age']) != len([el for el in self._receiver['age'] if el is not None]):
            raise ValueError("Headers are invalid")


class Receiver:
    def action(self):
        pass



def main():
    receiver = Receiver()
    concrete_command = HeaderCheckerFile(receiver)
    cc2 = CheckSizeCommand(receiver)
    cc3 = AgeColumnCheckerFile(receiver)
    invoker = Invoker()
    invoker.store_command(concrete_command)
    invoker.store_command(cc2)
    invoker.store_command(cc3)

    invoker.execute_commands()

if __name__ == "__main__":
    main()


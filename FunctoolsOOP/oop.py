from abc import ABC, abstractmethod


class Developer(ABC):
    @abstractmethod
    def fix_bug(self):
        pass


class Senior(Developer):
    def fix_bug(self):
        print("I don't fix bugs, I debug features.")


class Mid(Developer):
    def fix_bug(self):
        print("I can fix that bug, but I need a coffee first.")


class Junior(Developer):
    def fix_bug(self):
        print("I'm on it! *types furiously*")


# Example usage
senior = Senior()
mid = Mid()
junior = Junior()

developers: list[Developer] = [senior, mid, junior]

for dev in developers:
    dev.fix_bug()

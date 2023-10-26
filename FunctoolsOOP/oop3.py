from typing import Protocol, runtime_checkable


@runtime_checkable
class Developer(Protocol):
    def fix_bug(self):
        pass


class Senior:
    def fix_bug(self):
        print("I don't fix bugs, I debug features.")


class Mid:
    def fix_bug(self):
        print("I can fix that bug, but I need a coffee first.")


class Junior:
    def fix_bug(self):
        print("I'm on it! *types furiously*")


class HR:
    def fix_human(self):
        print("I'm fixing humans")


# Example usage
senior = Senior()
mid = Mid()
junior = Junior()
hr = HR()

developers: list[Developer] = [senior, mid, junior, hr]

for dev in developers:
    dev.fix_bug()

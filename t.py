from collections import UserDict


class BaseDict(UserDict):

    def __getattr__(self, item):
        try:
            return self.data.__getitem__(item)
        except KeyError as e:
            raise AttributeError(e) from None

    def kv_join(self, sep: str = ':', endswith: str = '\n') -> str:
        return ''.join(f'{k}{sep}{v}{endswith}' for k, v in self.items())

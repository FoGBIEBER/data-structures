from SequentialMap import *


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str("{}:{}".format(self.key, self.value))


class HashLinearMap:
    def __init__(self, M):
        self.table = [None] * M
        self.M = M

    def hashFn(self, key):
        sum = 0
        for c in key:
            sum = sum + ord(c)
        return sum % self.M

    def insert(self, key, value):
        p = False
        for entry in self.table:
            if entry == None or entry == '.':
                p = True
                break
        idx = self.hashFn(key)
        entry = Entry(key, value)
        while p is True:
            if self.table[idx] == None or self.table[idx] == '.':
                self.table[idx] = entry
                return
            idx = (idx + 1 + self.M) % self.M
        return

    def delete(self, key):
        p = False
        for entry in self.table:
            if entry != None and entry != '.':
                p = True
                break
        idx = self.hashFn(key)
        while p is True:
            if self.table[idx] == None:
                return
            elif self.table[idx] == '.':
                idx = (idx + 1 + self.M) % self.M
            elif self.table[idx].key == key:
                self.table[idx] = '.'
                return
            else:
                idx = (idx + 1 + self.M) % self.M
        return

    def display(self, msg):
        print(msg)
        for idx in range(len(self.table)):
            entry = self.table[idx]
            if entry is not None and entry != '.':
                print("[{:2d}] ".format(idx), end='')
                print(entry)

    def search(self, key):
        p = False
        for entry in self.table:
            if entry != None:
                p = True
                break
        idx = self.hashFn(key)
        while p is True:
            if self.table[idx] == None:
                return None
            elif self.table[idx] == '.':
                idx = (idx + 1 + self.M) % self.M
            elif self.table[idx].key == key:
                return self.table[idx].value
            else:
                idx = (idx + 1 + self.M) % self.M
        return


if __name__ == '__main__':
    map = HashLinearMap(13)
    map.insert('data', '??????')
    map.insert('structure', '??????')
    map.insert('sequential search', '????????????')
    map.insert('game', '??????')
    map.insert('binary search', '????????????')
    map.display("?????? ?????????:")
    print()
    print("?????? game ->", map.search('game'))
    print("?????? over ->", map.search('over'))
    print("?????? data ->", map.search('data'))
    print()
    map.delete('game')
    map.display('game ????????? ?????? ?????????:')
    print()
    map.delete('over')
    map.display('over ????????? ?????? ?????????:')

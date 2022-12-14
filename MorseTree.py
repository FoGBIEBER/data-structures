from Tree import *

table = [('A', '.-'), ('B', '-...'), ('C', '-.-.'),
         ('D', '-..'), ('E', '.'), ('F', '..-.'),
         ('G', '--.'), ('H', '....'), ('I', '..'),
         ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
         ('M', '--'), ('N', '-.'), ('O', '---'),
         ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),
         ('S', '...'), ('T', '-'), ('U', '..-'),
         ('V', '...-'), ('W', '.--'), ('X', '-..-'),
         ('Y', '-.--'), ('Z', '--..')]


def make_morse_tree():
    root = TNode(None, None, None)

    for tp in table:
        code = tp[1]
        node = root
        for c in code:
            if c == '.':
                if node.left == None:
                    node.left = TNode(None, None, None)
                node = node.left
            elif c == '-':
                if node.right == None:
                    node.right = TNode(None, None, None)
                node = node.right

        node.data = tp[0]
    return root


def encode(ch):
    idx = ord(ch) - ord('A')
    return table[idx][1]


def decode(root, code):
    node = root
    for ch in code:
        if ch == '.':
            node = node.left
        elif ch == '-':
            node = node.right
    return node.data


if __name__ == '__main__':
    morseCodeTree = make_morse_tree()
    str = input('입력 문장 : ')
    mlist = []
    for ch in str:
        code = encode(ch)
        mlist.append(code)
    print("Morse Code : ", mlist)
    print("Decoding : ", end='')
    for code in mlist:
        ch = decode(morseCodeTree, code)
        print(ch, end='')
    print()

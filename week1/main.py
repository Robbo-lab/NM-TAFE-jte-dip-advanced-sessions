from stack import Stack


class Reverser:
    def __init__(self, input_string):
        self.__input_string = input_string

    def reverse(self):
        stack = Stack()
        for s in self.__input_string.split(" "):
            stack.push(s)

        r = ""
        while not stack.is_empty():
            r += stack.pop() + " "

        return r.strip()


if __name__ == "__main__":
    while True:
        sentence = input("Enter a string: ")
        if sentence == "":
            break

        reverser = Reverser(sentence)
        print(reverser.reverse())

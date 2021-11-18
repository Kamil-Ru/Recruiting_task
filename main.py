

# TODO 10: Delete "print"
# TODO 10: Delete "print"

# TODO 9: Make descriptions of what you are doing!!
class Move:
    def __init__(self):
        self.position = [1, 1]
        # TODO 1: make matrix

        # TODO 9: Make descriptions of what you are doing!!

        self.matrix_2 = []

        start_number = 0
        row = 3
        column = 3

        for a in range(row):
            row = []

            for a in range(column):
                start_number += 1
                row.append(start_number)

            print(row)
            self.matrix_2.append(row)

        print(self.matrix_2)

    # TODO 9: Make descriptions of what you are doing!!
    def boundary_condition(function):
        def boundary_condition_wrapper(self):
            # print(f"1. Position before run function: {test.position}")
            # TODO 8: What is wrong??
            function(self)
            # print(f"2. Position after run function: {test.position}")
            print(self.position)



            for self.xy in self.position:

                if self.xy >= 3:
                    self.position[self.position.index(self.xy)] = 2

                elif self.xy <= 0:
                    self.position[self.position.index(self.xy)] = 0

            # print(f"3. Position after all function: {test.position}")

            return self.position

        return boundary_condition_wrapper

    # TODO 9: Make descriptions of what you are doing!!
    def number_in_matrix(self):
        return self.matrix_2[self.position[0]][self.position[1]]

    # TODO 9: Make descriptions of what you are doing!!
    @boundary_condition
    def up(self):
        self.position[0] -= 1

    @boundary_condition
    def down(self):
        self.position[0] += 1

    @boundary_condition
    def right(self):
        self.position[1] += 1

    @boundary_condition
    def left(self):
        self.position[1] -= 1

    def move(self, input_move=None):
        if input_move == "U":
            self.up()
        elif input_move == "D":
            self.down()
        elif input_move == "R":
            self.right()
        elif input_move == "L":
            self.left()




# TODO 9: Make descriptions of what you are doing!!

# TODO 8: Input (test)

# TODO 4: Write function what reads input and translates it (ease one)

# TODO 11: Write function what reads input and translates it (HARD ONE)

# TODO 5: Use all function to create working program.

from_user_instrukction = input("Instruction are:\n")

instructions_1 = """LLLLLLLLLDDDDDRRRRRRR"""

instructions_ = """RUU
DDDL
URLLL"""

instructions ="""RLRLLLULULULUUDUULULRDDLURURDDLDUUDDLRDDUUUDD
LDLRLDDDLUDRDRRUDUURLRULLUDDRLURLUULDLLRLLUDLRLRUDLULRLRRL
LLRRDURRDLDULRDUDLRDRDRURULDU
DULRRDRLRLUDLLURURLLRLRDLLDLLDRDUURL
DUULULUUDUDLLRLRURULLDLRRLURDLLDUDUDDRURRLUDULULD"""

test = Move()
pin = ""


instructions = instructions.split("\n")
for row in instructions:
    for letter in row:
        # print(f"Actual letter: {letter},\nPosition: {test.position},\nNumber: {test.number_in_matrix()}")
        test.move(input_move=letter)
        # print(f"Actual letter: {letter},\nPosition: {test.position},\nNumber: {test.number_in_matrix()}")

    pin += str(test.number_in_matrix())
    test.starting_position = test.position


print(pin)


print(f"4. Ending position: {test.position}")


test.number_in_matrix()

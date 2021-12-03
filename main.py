TESTING_INSTRUCTION = """RUU
DDDL
URLLL"""

LUNAR_INSTRUCTION = """RLRLLLULULULUUDUULULRDDLURURDDLDUUDDLRDDUUUDD
LDLRLDDDLUDRDRRUDUURLRULLUDDRLURLUULDLLRLLUDLRLRUDLULRLRRL
LLRRDURRDLDULRDUDLRDRDRURULDU
DULRRDRLRLUDLLURURLLRLRDLLDLLDRDUURL
DUULULUUDUDLLRLRURULLDLRRLURDLLDUDUDDRURRLUDULULD"""


class PinPAD:
    def __init__(self):
        # Starting position on PIN pad
        self.position = [1, 1]

        # Generating matrix - PIN pad
        self.matrix = []

        number = 0
        number_of_rows = 3
        number_of_column = 3

        for row in range(number_of_rows):
            x = []

            for column in range(number_of_column):
                number += 1
                x.append(number)

            self.matrix.append(x)

    # Decoration making boundary condition
    def boundary_conditions(function):
        def boundary_condition_wrapper(self):
            function(self)
            for self.xy in self.position:
                if self.xy >= 3:
                    self.position[self.position.index(self.xy)] = 2
                elif self.xy <= 0:
                    self.position[self.position.index(self.xy)] = 0
            return self.position

        return boundary_condition_wrapper

    # Getting number from Pin PAD/matrix
    def number_on_pin_pad(self):
        return self.matrix[self.position[0]][self.position[1]]

    # Functions of movements on Pin PAD
    @boundary_conditions
    def up(self):
        self.position[0] -= 1

    @boundary_conditions
    def down(self):
        self.position[0] += 1

    @boundary_conditions
    def right(self):
        self.position[1] += 1

    @boundary_conditions
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


pin_pad = PinPAD()
pin = ""

instructions = TESTING_INSTRUCTION.split("\n")
for row in instructions:
    for letter in row:
        pin_pad.move(input_move=letter)
    pin += str(pin_pad.number_on_pin_pad())
    pin_pad.starting_position = pin_pad.position

print(f"PIN: {pin}")


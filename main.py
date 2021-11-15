from_user = input()

class Move:
    def __init__(self):
        self.starting_position = [1, 1]
        self.position = [1, 1]
        self.matrix = [[x+1 for x in range(3)] for x in range(3)]

        self.matrix_2 = []
        start_number = 1
        row = 3
        column = 3
        for a in range(column):
            one_row = []
            for a in range(row):
                one_row.append(start_number)
                start_number += 1
            self.matrix_2.append(one_row)


    def border_condition(function):
        def border_condition_wrapper(self):
            print(f"1. Position before run function: {test.position}")
            function(self)
            print(f"2. Position after run function: {test.position}")

            for self.xy in self.position:

                if self.xy > 1:
                    self.position[self.position.index(self.xy)] = 2

                elif self.xy < 1:
                    self.position[self.position.index(self.xy)] = 0

            print(f"3. Position after all function: {test.position}")

            return self.position
        return border_condition_wrapper

    @border_condition
    def Up(self):
        self.position[0] += 1

    @border_condition
    def Down(self):
        self.position[0] -= 1

    @border_condition
    def Right(self):
        self.position[1] += 1

    @border_condition
    def Left(self):
        self.position[1] -= 1




test = Move()

print(test.matrix_2)

test.Up()
test.Up()
test.Up()
test.Up()

test.Down()
test.Down()
test.Down()

test.Left()
test.Left()
test.Left()
test.Left()


print(f"4. Ending position: {test.position}")


test.Right()
test.Right()
test.Right()
test.Right()

print(f"4. Ending position: {test.position}")
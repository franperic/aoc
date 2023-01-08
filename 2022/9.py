with open("2022/input/9.txt") as f:
    instructions = [instruction.rstrip() for instruction in f]


class Rope:
    def __init__(self, knots):
        self.knots = knots
        self.rope_xy = {}
        for i in range(knots+1):
            self.rope_xy[i] = [0, 0]
        self.tail_history = [tuple((self.rope_xy[knots]))]


    def perform_move(self, instruction):
        direction = instruction[0]
        steps = int(instruction[1])

        for _ in range(steps):
            if direction == "R":
                self.rope_xy[0][0] += 1
                for i in range(1, self.knots+1):
                    self.tails_reaction(i)

            if direction == "L":
                self.rope_xy[0][0] -= 1
                for i in range(1, self.knots+1):
                    self.tails_reaction(i)

            if direction == "U":
                self.rope_xy[0][1] += 1
                for i in range(1, self.knots+1):
                    self.tails_reaction(i)

            if direction == "D":
                self.rope_xy[0][1] -= 1
                for i in range(1, self.knots+1):
                    self.tails_reaction(i)

    def tails_reaction(self, knot):
        prior_knot = self.rope_xy[knot-1]
        adjacent = self.get_adjacent_range(knot)

        if prior_knot in adjacent:
            return 0
        
        else:
            self.move_knot(knot)
            if knot == self.knots:
                self.tail_history.append(tuple(self.rope_xy[knot]))
    
    def move_knot(self, knot):
        prior_xy = self.rope_xy[knot-1]
        knot_xy = self.rope_xy[knot]

        if prior_xy[0] == knot_xy[0]:
            if (prior_xy[1] - knot_xy[1]) < 0:
                knot_xy[1] -= 1
            else:
                knot_xy[1] += 1
        elif prior_xy[1] == knot_xy[1]:
            if (prior_xy[0] - knot_xy[0]) < 0:
                knot_xy[0] -= 1
            else:
                knot_xy[0] += 1
        else:
            if prior_xy[0] > knot_xy[0]:
                if prior_xy[1] > knot_xy[1]:
                    knot_xy[0] += 1
                    knot_xy[1] += 1
                else:
                    knot_xy[0] += 1
                    knot_xy[1] -= 1
            else:
                if prior_xy[1] > knot_xy[1]:
                    knot_xy[0] -= 1
                    knot_xy[1] += 1
                else:
                    knot_xy[0] -= 1
                    knot_xy[1] -= 1
        
        self.rope_xy[knot-1] = prior_xy
        self.rope_xy[knot] = knot_xy
            
    def get_adjacent_range(self, knot):
        min_x = self.rope_xy[knot][0] - 1
        max_x = self.rope_xy[knot][0] + 1
        min_y = self.rope_xy[knot][1] - 1
        max_y = self.rope_xy[knot][1] + 1

        adjacent = []
        for i in [min_y, self.rope_xy[knot][1], max_y]:
            adjacent.append([min_x, i])
            adjacent.append([self.rope_xy[knot][0], i])
            adjacent.append([max_x, i])
        
        return adjacent

# Part 1 
rope = Rope(1)
[rope.perform_move(instruction.split()) for instruction in instructions]
print(len(set(rope.tail_history)))


# Part 2
rope = Rope(9)
[rope.perform_move(instruction.split()) for instruction in instructions]
print(len(set(rope.tail_history)))

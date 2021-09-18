import numpy as np

table = np.array(
    [
        [
            [[], 0]
        ]*6
    ]*5
)

things = np.array([
    ('water', 3, 10),
    ('book', 1, 3),
    ('food', 2, 9),
    ('clothes', 2, 5),
    ('camera', 1, 6),
])

for i_row, row in enumerate(table):
    for j_column, column in enumerate(row):
        prev_max = [[], 0]

        if i_row - 1 >= 0:
            prev_max = table[i_row - 1][j_column]

        current_element_cost = [[], 0]
        thing_name = things[i_row][0]
        thing_weight = int(things[i_row][1])
        thing_cost = int(things[i_row][2])

        if thing_weight <= (j_column + 1):
            if (
                thing_weight < (j_column + 1) and
                i_row - 1 >= 0 and
                (j_column - thing_weight) >= 0
            ):
                current_element_cost[0] += \
                    [thing_name] + table[i_row - 1][j_column - thing_weight][0]
                current_element_cost[1] = \
                    thing_cost + \
                    table[i_row - 1][j_column - thing_weight][1]
            else:
                current_element_cost[0].append(thing_name)
                current_element_cost[1] = thing_cost

        table[i_row][j_column] = max(
            [prev_max, current_element_cost], key=lambda x: x[1]
        )

print(table[len(table) - 1][len(table[0]) - 1][0])

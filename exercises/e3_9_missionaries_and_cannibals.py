from search import Problem, breadth_first_graph_search


class MissionariesAndCannibals(Problem):
    """"""
    def __init__(self, initial, goal=(3, 3, 0, 0, 0)):
        """ Define goal state and initialize a problem
        (3, 3, 0, 0, 0)
        (M, C, M, C, B)
        """

        self.goal = goal
        Problem.__init__(self, initial, goal)

    def actions(self, state):
        possible_actions = ['ML', 'MR', 'CL', 'CR', 'MML', 'MMR', 'CCL', 'CCR', 'MCL', 'MCR']
        is_right_side = (state[-1] == 1)
        if is_right_side:
            possible_actions.remove('ML')
            possible_actions.remove('CL')
            possible_actions.remove('MML')
            possible_actions.remove('CCL')
            possible_actions.remove('MCL')

            # MR
            if (state[2] - 1 < 0) or (0 < state[2] - 1 < state[3]) or (0 < state[0] + 1 < state[1]):
                possible_actions.remove('MR')

            # MMR
            if (state[2] - 2 < 0) or (0 < state[2] - 2 < state[3]) or (0 < state[0] + 2 < state[1]):
                possible_actions.remove('MMR')

            # MCR
            if (state[2] - 1 < 0) or (state[3] - 1 < 0) or (0 < state[0] + 1 < state[1] + 1):
                possible_actions.remove('MCR')

            # CR
            if (state[3] - 1 < 0) or (0 < state[0] < state[1] + 1):
                possible_actions.remove('CR')

            # CCR
            if (state[3] - 2 < 0) or (0 < state[0] < state[1] + 2):
                possible_actions.remove('CCR')

        else:
            possible_actions.remove('MR')
            possible_actions.remove('CR')
            possible_actions.remove('MMR')
            possible_actions.remove('CCR')
            possible_actions.remove('MCR')

            # ML
            if (state[0] - 1 < 0) or (0 < state[0] - 1 < state[1]) or (0 < state[2] + 1 < state[3]):
                possible_actions.remove('ML')

            # MML
            if (state[0] - 2 < 0) or (0 < state[0] - 2 < state[1]) or (0 < state[2] + 2 < state[3]):
                possible_actions.remove('MML')

            # MCL
            if (state[0] - 1 < 0) or (state[1] - 1 < 0) or (0 < state[2] + 1 < state[3] + 1):
                possible_actions.remove('MCL')

            # CL
            if (state[1] - 1 < 0) or (0 < state[2] < state[3] + 1):
                possible_actions.remove('CL')

            # CCL
            if (state[1] - 2 < 0) or (0 < state[2] < state[3] + 2):
                possible_actions.remove('CCL')

        return possible_actions

    def result(self, state, action):
        new_state = list(state)

        if action == 'ML':
            new_state[0] = new_state[0] - 1
            new_state[2] = new_state[2] + 1

        elif action == 'MML':
            new_state[0] = new_state[0] - 2
            new_state[2] = new_state[2] + 2

        elif action == 'MCL':
            new_state[0] = new_state[0] - 1
            new_state[1] = new_state[1] - 1
            new_state[2] = new_state[2] + 1
            new_state[3] = new_state[3] + 1

        elif action == 'CL':
            new_state[1] = new_state[1] - 1
            new_state[3] = new_state[3] + 1

        elif action == 'CCL':
            new_state[1] = new_state[1] - 2
            new_state[3] = new_state[3] + 2

        elif action == 'MR':
            new_state[0] = new_state[0] + 1
            new_state[2] = new_state[2] - 1

        elif action == 'MMR':
            new_state[0] = new_state[0] + 2
            new_state[2] = new_state[2] - 2

        elif action == 'MCR':
            new_state[0] = new_state[0] + 1
            new_state[1] = new_state[1] + 1
            new_state[2] = new_state[2] - 1
            new_state[3] = new_state[3] - 1

        elif action == 'CR':
            new_state[1] = new_state[1] + 1
            new_state[3] = new_state[3] - 1

        elif action == 'CCR':
            new_state[1] = new_state[1] + 2
            new_state[3] = new_state[3] - 2

        new_state[4] = 1 - new_state[4]

        return tuple(new_state)

    def value(self, state):
        pass

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal


def solve():
    missionaries_and_cannibals = MissionariesAndCannibals((0, 0, 3, 3, 1))
    return breadth_first_graph_search(missionaries_and_cannibals).solution()


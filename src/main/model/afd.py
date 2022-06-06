class AFD:
    alphabet = []
    states = []
    transitions = {}
    initial_state = None
    final_states = []

    def __init__(self, alphabet, states, transitions, initial_state, final_states):
        self.alphabet = alphabet
        self.states = states
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def this_string_is_valid(self, string):
        current_state = self.initial_state

        for character in string:
            if character in self.transitions[current_state]:
                current_state = self.transitions[current_state][character]
            else:
                return False
        return current_state in self.final_states

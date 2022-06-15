import re
import string

from src.main.model.afd import AFD
from src.main.util import strings
from src.main.util.validation import validate_afd


def __str__(self):
    return self.main


alphabet: string = re.split(' ', input())

states: string = re.split(' ', input())

transitions_size: int = int(input())
transition_list = []
for i in range(transitions_size):
    transition_list.append(re.split(' ', input()))

initial_state: string = input()

final_states: string = re.split(' ', input())

afd = AFD(alphabet, states, initial_state, final_states)

for transition in transition_list:
    afd.add_transition(transition[0], (transition[1], transition[2]))

validate_afd(afd)

string_size: int = int(input())
for i in range(string_size):
    print(strings.accept if afd.this_string_is_valid(input()) else strings.refuse)

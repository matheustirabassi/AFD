from src.main.model.afd import AFD
from src.main.util import strings


def validate_afd(afd: AFD):
    if afd.alphabet().__len__() > 5 :
        raise(Exception(strings.alphabet_error))

    if afd.states().__len__() > 10:
      raise(Exception(strings.states_error))

    if afd.transitions_size() > 100:
      raise(Exception(strings.bigger_than_100_transitions_error))

    if afd.transitions_size() < 1 :
      raise(Exception(strings.less_than_1_transitions_error))

    if afd.initial_state() not in afd.states() :
      raise(Exception(strings.initial_state_error))

    if afd.final_states().__len__() > 10 :
      raise(Exception(strings.final_state_error))

    return True

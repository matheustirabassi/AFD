from src.main.model.afd import AFD
from src.main.util import strings


def validate_afd(afd: AFD):
    if(len(afd.alphabet()) > 5):
        raise(Exception(strings.alphabet_error))

    if(len(afd.states()) > 10):
      raise(Exception(strings.states_error))

    if(len(afd.transitions()) > 100):
      raise(Exception(strings.bigger_than_100_transitions_error))

    if (len(afd.transitions()) < 1):
      raise(Exception(strings.less_than_1_transitions_error))

    if(afd.initial_state() not in afd.states()):
      raise(Exception(strings.initial_state_error))

    if(len(afd.final_states()) > 10):
      raise(Exception(strings.final_state_error))

    return True

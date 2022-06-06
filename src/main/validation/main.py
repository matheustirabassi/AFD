from src.main.afd.afd import AFD
import strings

def validate_afn(alphabet=[], states=[], transitions={}, initial_state=None, final_states=[]):
    if(len(alphabet) > 5):
        raise(Exception(strings.alphabet_error))

    if(len(states) > 10):
      raise(Exception(strings.states_error))

    if(len(transitions) > 100 or len(transitions) < 1):
      raise(Exception(strings.transitions_error))

    if(initial_state not in states):
      raise(Exception(strings.initial_state_error))

    if(len(final_states) > 10):
      raise(Exception(strings.final_state_error))

    return AFD(alphabet, states, transitions,
              initial_state, final_states)

# afd = insert_afd()
# while(True):
#     string = input()

#     if(afd.this_string_is_valid(string)):
#         print("Aceita.")
#     else:
#         print("Rejeita.")

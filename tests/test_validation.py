import pytest
from src.main.model.afd import AFD
from src.main.util import strings
from src.main.util.validation import validate_afd

def test_validate_afd_all_valid_sucess():
    alphabet = ['a', 'b', 'c']
    states = ['q0', ' q1']
    transitions = {'q0': {'a': 'q1'}, 'q1': {'b': 'q1'}}
    initial_state = 'q0'
    final_state = ['q1']

    assert validate_afd(AFD(alphabet, states, transitions,
                        initial_state, final_state)) == True


def test_validate_afd_alphet_bigger_5_error():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f']
    with pytest.raises(Exception) as exception_info:
        validate_afd(AFD(alphabet, [], [], None, []))

    expected_error = strings.alphabet_error
    assert exception_info.value.args[0] == expected_error


def test_validate_afd_states_bigger_10_error():
    states = ['q0', 'q1', 'q2', 'q3', 'q4',
              'q5', 'q6', 'q7', 'q8', 'q9', 'q10']

    with pytest.raises(Exception) as exception_info:
        validate_afd(AFD([], states, [], None, []))

    expected_error = strings.states_error
    assert exception_info.value.args[0] == expected_error


def test_validate_afd_transitions_bigger_100_error():
    transitions = {'q0': {'a': 'q1'}, 'q1': {'a': 'q1'}}
    for i in range(101):
        transitions.update({'q' + str(i): {'a': 'q3'}})

    with pytest.raises(Exception) as exception_info:
        validate_afd(AFD([], [], transitions, None, []))

    expected_error = strings.bigger_than_100_transitions_error
    assert exception_info.value.args[0] == expected_error


def test_validate_afd_transitions_less_than_1_error():
    transitions = {}

    with pytest.raises(Exception) as exception_info:
        validate_afd(AFD([], [], transitions, None, []))

    expected_error = strings.less_than_1_transitions_error
    assert exception_info.value.args[0] == expected_error


def test_validate_afd_initial_state_not_in_states_error():
    alphabet = ['a', 'b']
    states = ['q0', 'q1']
    transitions = {'q0': {'a': 'q1'}}
    initial_state = 'q2'

    with pytest.raises(Exception) as exception_info:
        validate_afd(AFD(alphabet=alphabet, states=states, transitions=transitions,
                     initial_state=initial_state, final_states=[]))

    expected_error = strings.initial_state_error
    assert exception_info.value.args[0] == expected_error


def test_validate_afd_final_states_bigger_10_error():
    states = ['q0']
    transitions = {'q0': {'a': 'q1'}}
    initial_state = 'q0'
    final_states = ['q0', 'q1', 'q2', 'q3', 'q4',
                    'q5', 'q6', 'q7', 'q8', 'q9', 'q10']
    with pytest.raises(Exception) as exception_info:
        validate_afd(AFD(final_states=final_states, states=states, transitions=transitions,
                     initial_state=initial_state, alphabet=[]))

    expected_error = strings.final_state_error
    assert exception_info.value.args[0] == expected_error

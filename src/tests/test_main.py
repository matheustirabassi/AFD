import strings
import pytest
from src.main.validation.main import validate_afn


def test_insert_afd_alphet_bigger_5_error():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f']

    with pytest.raises(Exception) as exception_info:
        validate_afn(alphabet = alphabet)
    expected_error = strings.alphabet_error
    assert exception_info.value.args[0] == expected_error


def test_insert_afd_states_bigger_10_error():
    states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']

    with pytest.raises(Exception) as exception_info:
        validate_afn(states = states)
    expected_error = strings.states_error
    assert exception_info.value.args[0] == expected_error

def test_insert_afd_transitions_bigger_100_error():
    transitions = {'q0': {'a': 'q1'}, 'q1': {'a': 'q1'}}
    for i in range(101):
        transitions.update({'q' + str(i): {'a': 'q3'}})

    with pytest.raises(Exception) as exception_info:
        validate_afn(transitions = transitions)
    expected_error = strings.transitions_error
    assert exception_info.value.args[0] == expected_error

def test_insert_afd_transitions_less_than_1_error():
    transitions = {}

    with pytest.raises(Exception) as exception_info:
        validate_afn(transitions = transitions)
    expected_error = strings.transitions_error
    assert exception_info.value.args[0] == expected_error

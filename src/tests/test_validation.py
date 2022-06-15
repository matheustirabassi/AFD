import pytest
from src.main.model.afd import AFD
from src.main.util import strings
from src.main.util.validation import validate_afd

def test_validate_afd_all_valid_sucess():
    alphabet = ['a', 'b', 'c']
    states = ['q0', 'q1']
    initial_state = 'q0'
    final_state = ['q1']

    afd = AFD(alphabet, states,
              initial_state, final_state)
    afd.add_transition('q0', ('a', 'q1'))
    afd.add_transition('q1', ('b', 'q1'))

    assert validate_afd(afd) == True

def test_validate_afd_alphet_bigger_5_error():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f']
    with pytest.raises(Exception) as exception_info:
        validate_afd(AFD(alphabet, [], None, []))

    expected_error = strings.alphabet_error
    assert exception_info.value.args[0] == expected_error


def test_validate_afd_states_bigger_10_error():
    states = ['q0', 'q1', 'q2', 'q3', 'q4',
              'q5', 'q6', 'q7', 'q8', 'q9', 'q10']

    with pytest.raises(Exception) as exception_info:
        validate_afd(AFD([], states, None, []))

    expected_error = strings.states_error
    assert exception_info.value.args[0] == expected_error


def test_validate_afd_transitions_bigger_100_error():

    afd = AFD(alphabet=['a'], states=['q0', 'q3'],
              initial_state='q0', final_states=['q3'])

    for i in range(101):
        afd.add_transition('q0', ('a', 'q3'))

    with pytest.raises(Exception) as exception_info:
        validate_afd(afd)

    expected_error = strings.bigger_than_100_transitions_error
    assert exception_info.value.args[0] == expected_error


def test_validate_afd_transitions_less_than_1_error():
    with pytest.raises(Exception) as exception_info:
        afd = AFD([], [], None, [])
        validate_afd(afd)

    expected_error = strings.less_than_1_transitions_error
    assert exception_info.value.args[0] == expected_error


def test_validate_afd_initial_state_not_in_states_error():
    alphabet = ['a', 'b']
    states = ['q0', 'q1']
    initial_state = 'q2'

    with pytest.raises(Exception) as exception_info:
        afd = AFD(alphabet=alphabet, states=states,
                  initial_state=initial_state, final_states=[])
        afd.add_transition('q0', ('a', 'q1'))

        validate_afd(afd)

    expected_error = strings.initial_state_error
    assert exception_info.value.args[0] == expected_error


def test_validate_afd_final_states_bigger_10_error():
    states = ['q0', 'q1']
    initial_state = 'q0'
    final_states = ['q0', 'q1', 'q2', 'q3', 'q4',
                    'q5', 'q6', 'q7', 'q8', 'q9', 'q10']
    with pytest.raises(Exception) as exception_info:
        afd = AFD(final_states=final_states, states=states,
                  initial_state=initial_state, alphabet=['a'])
        afd.add_transition('q0', ('a', 'q1'))

        validate_afd(afd)

        expected_error = strings.final_state_error
        assert exception_info.value.args[0] == expected_error

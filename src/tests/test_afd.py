from venv import create
import pytest
from src.main.model.afd import AFD
from src.main.util import strings

# region construct afd test


def test_create_afd():
    afd = AFD([], [], None, [])

    assert afd.states() == []
    assert afd.alphabet() == []
    assert afd.transitions() == {}
    assert afd.initial_state() == None
    assert afd.final_states() == []


def test_create_afd_with_args():
    expected_alphabet = ['a', 'b']
    expected_states = ['q0', 'q1']
    expected_transitions = {'q0': [('a', 'q1')], 'q1': [('a', 'q1')]}
    expected_initial_state = 'q0'
    expected_final_state = ['q1']

    afd = AFD(expected_alphabet, expected_states,
              expected_initial_state, expected_final_state)
    afd.add_transition('q0', ('a', 'q1'))
    afd.add_transition('q1', ('a', 'q1'))

    assert afd.states() == expected_states
    assert afd.alphabet() == expected_alphabet
    assert afd.transitions() == expected_transitions
    assert afd.initial_state() == expected_initial_state
    assert afd.final_states() == expected_final_state

# endregion

# region this_string_is_valid


def create_mock_afd():
    alphabet = ['a', 'b']
    states = ['q0', 'q1']
    initial_state = 'q0'
    final_state = ['q1']

    afd = AFD(alphabet, states, initial_state, final_state)
    afd.add_transition('q0', ('a', 'q1'))
    afd.add_transition('q1', ('a', 'q1'))

    return afd


def test_string_a_accept():
    afd = create_mock_afd()
    expected_result = True

    assert afd.this_string_is_valid('a') == expected_result


def test_string_aa_accept():
    afd = create_mock_afd()
    expected_result = True

    assert afd.this_string_is_valid('aa') == expected_result


def test_string_b_refuse():
    afd = create_mock_afd()
    expected_result = False

    assert afd.this_string_is_valid('b') == expected_result


def test_all_valid_accept():
    alphabet = ['a', 'b']
    states = ['q0', 'q1', 'q2']
    initial_state = 'q0'
    final_state = ['q2']

    afd = AFD(alphabet, states, initial_state, final_state)

    afd.add_transition('q0', ('a', 'q1'))
    afd.add_transition('q0', ('b', 'q1'))
    afd.add_transition('q1', ('a', 'q2'))

    string_0 = 'aa'
    string_1 = 'ba'
    string_2 = 'bb'

    assert afd.this_string_is_valid(string_0) == True
    assert afd.this_string_is_valid(string_1) == True
    assert afd.this_string_is_valid(string_2) == False


def test_1_all_valid_success():
    alphabet = ['a', 'b']
    states = ['q0', 'q1', 'q2', 'qf']
    initial_state = 'q0'
    final_state = ['qf']

    afd = AFD(alphabet, states, initial_state, final_state)

    afd.add_transition('q0', ('a', 'q1'))
    afd.add_transition('q0', ('b', 'q2'))
    afd.add_transition('q1', ('a', 'qf'))
    afd.add_transition('q1', ('b', 'q2'))
    afd.add_transition('q2', ('a', 'q1'))
    afd.add_transition('q2', ('b', 'qf'))
    afd.add_transition('qf', ('a', 'qf'))
    afd.add_transition('qf', ('b', 'q1'))

    string_0 = 'aa'
    string_1 = 'abb'
    string_2 = 'abab'
    string_3 = 'baba'

    assert afd.this_string_is_valid(string_0) == True
    assert afd.this_string_is_valid(string_1) == True
    assert afd.this_string_is_valid(string_2) == False
    assert afd.this_string_is_valid(string_3) == False


def test_2_all_valid_success():
    alphabet = ['a', 'b']
    states = ['q0', 'q1', 'q2', 'q3']
    initial_state = 'q0'
    final_state = ['q1', 'q2']

    afd = AFD(alphabet, states, initial_state, final_state)

    afd.add_transition('q0', ('a', 'q1'))
    afd.add_transition('q0', ('b', 'q2'))
    afd.add_transition('q1', ('a', 'q0'))
    afd.add_transition('q1', ('b', 'q3'))
    afd.add_transition('q2', ('a', 'q3'))
    afd.add_transition('q2', ('b', 'q0'))
    afd.add_transition('q3', ('a', 'q2'))
    afd.add_transition('q3', ('b', 'q1'))

    string_0 = 'aab'
    string_1 = 'abab'
    string_2 = 'bbba'

    assert afd.this_string_is_valid(string_0) == True
    assert afd.this_string_is_valid(string_1) == False
    assert afd.this_string_is_valid(string_2) == False

# endregion

# region add_transition tests


def test_add_transition_state_not_in_states_error():
    afd = create_mock_afd()

    with pytest.raises(Exception) as exception_info:
        unknow_state = 'q3'
        afd.add_transition(unknow_state, ('a', 'q1'))

    expected_error = strings.state_isnt_states
    assert exception_info.value.args[0] == expected_error


def test_add_transition_next_state_not_in_states_error():
    afd = create_mock_afd()

    with pytest.raises(Exception) as exception_info:
        unknow_state = 'q5'
        afd.add_transition('q0', ('a', unknow_state))

    expected_error = strings.state_isnt_states
    assert exception_info.value.args[0] == expected_error


def test_add_transition_symbol_not_in_alphabet_error():
    afd = create_mock_afd()

    with pytest.raises(Exception) as exception_info:
        unknow_symbol = 'batata'
        afd.add_transition('q0', (unknow_symbol, 'q0'))

    expected_error = strings.symbol_isnt_alphabet
    assert exception_info.value.args[0] == expected_error


def test_add_transition_all_valid_success():
    alphabet = ['a', 'b']
    states = ['q0', 'q1']
    initial_state = 'q0'
    final_state = ['q1']

    afd = AFD(alphabet, states, initial_state, final_state)
    afd.add_transition('q0', ('a', 'q1'))
    afd.add_transition('q1', ('b', 'q1'))

    expected_transitions = {'q0': [('a', 'q1')], 'q1': [('b', 'q1')]}
    assert afd.transitions() == expected_transitions

# endregion

# region transitions_size tests


def test_transitions_size_2_transitions_return_size_2():
    afd = create_mock_afd()

    expected_size = 2

    assert afd.transitions_size() == expected_size
# endregion

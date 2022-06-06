from src.main.afd.afd import AFD

# region construct afd test


def test_create_afd():
    afd = AFD([], [], {}, None, [])

    assert afd.states == []
    assert afd.alphabet == []
    assert afd.transition == {}
    assert afd.initial_state == None
    assert afd.final_states == []


def test_create_afd_with_args():
    expected_alphabet = ['a', 'b']
    expected_states = ['q0', 'q1']
    expected_transitions = {'q0': {'a': 'q1'}, 'q1': {'a': 'q1'}}

    expected_initial_state = 'q0'
    expected_final_state = ['q1']
    afd = AFD(expected_alphabet, expected_states, expected_transitions,
              expected_initial_state, expected_final_state)

    assert afd.states == expected_states
    assert afd.alphabet == expected_alphabet
    assert afd.transition == expected_transitions
    assert afd.initial_state == expected_initial_state
    assert afd.final_states == expected_final_state

# endregion

## region this_string_is_valid

def create_mock_afd():
    expected_alphabet = ['a', 'b']
    expected_states = ['q0', 'q1']
    expected_transitions = {'q0': {'a': 'q1'}, 'q1': {'a': 'q1'}}

    expected_initial_state = 'q0'
    expected_final_state = ['q1']
    return AFD(expected_alphabet, expected_states, expected_transitions, expected_initial_state, expected_final_state)

def test_string_a_accept():
    afd = create_mock_afd()
    expected_result = True

    assert afd.this_string_is_valid('a') == expected_result

def test_string_aa_acept():
    afd = create_mock_afd()
    expected_result = False

    assert afd.this_string_is_valid('ab') == expected_result

def test_string_b_refuse():
    afd = create_mock_afd()
    expected_result = False

    assert afd.this_string_is_valid('b') == expected_result

def test_string_ab_refuse():
    afd = create_mock_afd()
    expected_result = False

    assert afd.this_string_is_valid('ab') == expected_result

## endregion
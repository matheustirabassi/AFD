from src.main.model.afd import AFD

# region construct afd test

def test_create_afd():
    afd = AFD([], [], {}, None, [])

    assert afd.states == []
    assert afd.alphabet == []
    assert afd.transitions == {}
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
    assert afd.transitions == expected_transitions
    assert afd.initial_state == expected_initial_state
    assert afd.final_states == expected_final_state

# endregion

# region this_string_is_valid


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


def test_string_aa_accept():
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


def test_all_valid_accept():
    alphabet = ['a', 'b']
    states = ['q0', 'q1', 'q2', 'qf']
    transitions = {
        states[0]: {alphabet[0]: states[1]},
        states[0]: {alphabet[1]: states[2]},
        states[1]: {alphabet[0]: states[3]},
        states[1]: {alphabet[1]: states[2]},
        states[2]: {alphabet[0]: states[1]},
        states[2]: {alphabet[1]: states[3]},
        states[3]: {alphabet[0]: states[3]},
        states[3]: {alphabet[1]: states[3]}
    }
    initial_state = states[0]
    final_state = [states[3]]

    afd = AFD(alphabet, states, transitions, initial_state, final_state)

    string_0 = 'aa'
    string_1 = 'abb'
    string_2 = 'abab'
    string_3 = 'baba'
    assert afd.this_string_is_valid(string_0) == True
    assert afd.this_string_is_valid(string_1) == True
    assert afd.this_string_is_valid(string_2) == False
    assert afd.this_string_is_valid(string_3) == False

# endregion

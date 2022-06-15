from dataclasses import dataclass
import string

from src.main.util import strings

class AFD:
    """
    classe que representa um Autômato finito determinístico.
    """

    __alphabet : list = []
    '''
    o alfabeto de simbolos do AFD.
    '''

    __states : list = []
    '''
    a lista de estados do AFD.
    '''

    __transitions : dict = {}
    '''
    o dicionário ou mapa de transições do AFD. Cada chave representa um estado e os valores serão
    uma lista de tuplas, cada tupla deverá ter um simbolo e o próximo estado.
    '''

    __initial_state = None
    '''
    O estado inicial do AFD.
    '''

    __final_states : list = []
    '''
    A lista de estados finais.
    '''


    def __init__(self, alphabet: list, states: list, initial_state: string,
                 final_states: list):
        """
        construtor da classe, também faz a função de limpar os atributos do objeto.
        """

        self.__alphabet = alphabet
        self.__states = states
        self.__initial_state = initial_state
        self.__final_states = final_states
        self.__transitions = {}

    def alphabet(self):
        return self.__alphabet

    def states(self):
        return self.__states

    def transitions(self):
        return self.__transitions

    def transitions_size(self):
        '''
        Retorna a quantidade de transiçòes.
        '''

        transitions_size = 0
        for transition in self.__transitions:
         transitions_size += self.__transitions[transition].__len__()

        return transitions_size

    def initial_state(self):
        return self.__initial_state

    def final_states(self):
        return self.__final_states


    def add_transition(self, state: string, transition: tuple):
        """
        Adiciona um novo estado na lista de estados do AFD.

        Parameters
        ----------
        state: string
            O estado que representa a chave do dicionário de transições.

        transition: tuple
            A transição em si a ser inserida no estado.
    
        >>> add_transition('q1', ('a', 'q2'))
        """

        if not state in self.__states:
             raise(Exception(strings.state_isnt_states))

        if not transition[1] in self.__states:
             raise(Exception(strings.state_isnt_states))

        if not transition[0] in self.__alphabet:
            raise(Exception(strings.symbol_isnt_alphabet))

        if not self.__transitions.__contains__(state):
            self.__transitions[state] = []

        self.__transitions[state].append(transition)

    def this_string_is_valid(self, string: string):
        """
        Verifica se a cadeia é valida.

        Parameters
        ----------
        string : string
            A cadeia de caracteres a ser verificada no AFD.

        Returns
        ----------
        true
            caso a cadeia seja válida nesse AFD.

        false
            caso a cadeia de caracteres seja inválida.

        >>> this_string_is_valid("aaa")
        true 
        """

        current_state = self.__initial_state

        for character in string:
            for transition in self.__transitions[current_state]:
                if character in transition[0]:
                    current_state = transition[1]

        return current_state in self.__final_states
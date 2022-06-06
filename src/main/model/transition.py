import string


class Transition:
  current_state: string = None
  next_states: list = []

  def __init__(self, current_state, next_states: NextStates):
    self.current_state = current_state
    self.next_states = next_states

class NextStates:
  symbol:string = None
  state: string = None

  def __init__(self, symbol, state):
    self.symbol = symbol
    self.state = state
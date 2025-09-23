from __future__ import annotations # allows us to avoid namespace errors since some classes need to be defined before others using them. Ex: AudioPlayer needs to use State interface, but it hasnt't been defined yet. 
from abc import ABC, abstractmethod

class AudioPlayer:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """
    _currentState = None # A reference to the current state of the Context. Protected variable

    def __init__(self, state: State) -> None: # returns nothing. 
        self.transition_to(state)

    def transition_to(self, state: State):
        '''The context allows changing the state object at runtime.'''

        print(f"***** Context: Transition to {type(state).__name__}") # checks the type of the state object by grabbing name of it's class.
        self._currentState = state # Ready state object is set as current state
        self._currentState.context = self # the current audioplayer object is then set to the attribute given by the interface class. 

    """
    The Context delegates(passes) part of its behavior to the current State object.
    """
    # context methods that call interface methods belonging to concrete state objects. 
    # Works because _currentState houses a Ready or Playing state object.  
    def request1(self): # Which both types of state objects inherit from the interface.
        self._currentState.handle1()

    def request2(self):
        self._currentState.handle2()



class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. 
    This backreference can be used by States to transition the Context to another State.
    """

    @property 
    def context(self) -> AudioPlayer:
        '''
        Returns an audioplayer object as an attribute so that different State objects may have access for using the context(AudioPlayer) methods. 
        The method, that allows us to transition the context to another state, transition_to(different State).
        '''
        return self._context
    
    @context.setter
    def context(self, context: AudioPlayer) -> None:
        self._context = context
    
    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass

"""
Concrete States implement various behaviors, associated with a state of the
Context.
"""


class Ready(State):
    '''Ready state ( or ConcreteStateA) implements abstract methods with the behavior we wish to see in a ready state for an audioplayer. '''
    def handle1(self) -> None:
        print('ConcreteStateA handles request1.')
        print('ConcreteStateA wants to change the state of the context.')

        # Current Ready object uses the context attribute it inherited from State to call method from context class. 
        # Passes a Playing state object as an argument. 
        self.context.transition_to(Playing())

    def handle2(self) -> None:
        print('ConcreteStateA handles request2.')
    

class Playing(State):
    '''Playing state ( or ConcreteStateB) implements abstract methods with the behavior we wish to see in a playing state for an audioplayer. '''
    def handle1(self) -> None:
        print('ConcreteStateB handles request1.')

    def handle2(self)-> None:
        print('ConcreteStateB handles request2.')
        print('ConcreteStateB wants to change the state of the context.')
        self.context.transition_to(Ready())



if __name__ == "__main__":
    
    context = AudioPlayer(Ready()) # Passing in concrete state object as argument. After this line, Context class starts with the ready state instance. 
    context.request1() # After this function call, context is now in the Playing state. 
    context.request2() 


    # TODO: Works, but I want to separate the module into separate packages. 



    # OUTPUT:
    # ***** Context: Transition to ConcreteStateA
    # ConcreteStateA handles request1.
    # ConcreteStateA wants to change the state of the context.
    # ***** Context: Transition to ConcreteStateB
    # ConcreteStateB handles request2.
    # ConcreteStateB wants to change the state of the context.
    # ***** Context: Transition to ConcreteStateA




from state_informal_interface import State
from ready_state import ReadyState
from playing_state import PlayingState


class LockedState(State):
    ''' Concrete class that extends the informal interface. '''

    def __init__(self):
        '''Connects player here. '''
    
    def clickLock(self): 
        '''Overrides State.clickLock(). UNLOCKS the phone'''
        
        if self.player.playing:
            self.player.changeState(PlayingState(self.player))
        else:
            self.player.chanegState(ReadyState(self.player))

    def clickPlay(self): 
        '''Overrides State.clickPlay(). Plays the song'''
        # Locked, so do nothing

    def clickNext(self): 
        '''Overrides State.clickNext(). Goes to the next song'''
        # Locked, so do nothing
    
    def clickPrevious(self):
        '''Overrides State.clickPrevious(). Goes to previous song'''
        # Locked, so do nothing








# Just to confirm we had a connection to that interface. Must return false, not true since true violates the definition of an interface.
# print(issubclass(LockedState, State)) 

# # "dunder method" that helps us see superclass we use for this subclass.
# print(LockedState.__mro__) 

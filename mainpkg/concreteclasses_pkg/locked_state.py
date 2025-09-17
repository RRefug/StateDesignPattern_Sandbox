from interface_pkg.state_informal_interface import State


import context_pkg.audio_player
import concreteclasses_pkg.playing_state
import concreteclasses_pkg.ready_state




class LockedState(State):
    ''' Concrete class that extends the informal interface. '''

    _audio_player = context_pkg.audio_player.AudioPlayer()

    def __init__(self, audioPlayer):
        '''Connects player here. '''
        self._audio_player = audioPlayer

    
    def clickLock(self): 
        '''Overrides State.clickLock(). UNLOCKS the phone'''
        
        if self._audio_player.playing:
            self._audio_player.changeState(concreteclasses_pkg.playing_state.PlayingState(self._audio_player))
        else:
            self._audio_player.changeState(concreteclasses_pkg.ready_state.ReadyState(self._audio_player))

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

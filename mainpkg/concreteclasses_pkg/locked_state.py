from mainpkg.subpkg import State
# from ready_state import ReadyState
# from playing_state import PlayingState
from mainpkg.subpkg import AudioPlayer
from mainpkg.subpkg import ReadyState
from mainpkg.subpkg import PlayingState




class LockedState(State):
    ''' Concrete class that extends the informal interface. '''

    _audio_player = AudioPlayer()

    def __init__(self, audioPlayer):
        '''Connects player here. '''
        self._audio_player = audioPlayer

    
    def clickLock(self): 
        '''Overrides State.clickLock(). UNLOCKS the phone'''
        
        if self._audio_player.playing:
            self._audio_player.changeState(PlayingState(self._audio_player))
        else:
            self._audio_player.changeState(ReadyState(self._audio_player))

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

from mainpkg.subpkg import State
from mainpkg.subpkg import LockedState
from mainpkg.subpkg import PlayingState
from mainpkg.subpkg import AudioPlayer

class ReadyState(State):
    ''' Concrete class that extends the informal interface. 
        Methods are inherited from state informal interface, here to be implemented.

        They can also trigger state transitions("lemme lock my phone after play my song") in the context.
    '''

    _audio_player = AudioPlayer()

    def __init__(self, audioplayer):
        ''' Argument is an audioplayer object'''
        self._audio_player = audioplayer
        

    '''Overrides State.clickLock(). Locks the phone'''
    def clickLock(self): 
        self._audio_player.changeState(LockedState(self._audio_player))

    '''Overrides State.clickPlay(). Plays the song'''
    def clickPlay(self): 
        self._audio_player.startPlayback()
        self._audio_player.changeState(PlayingState(self._audio_player))

    '''Overrides State.clickNext(). Goes to the next song'''
    def clickNext(self): 
        self._audio_player.nextSong()
    
    '''Overrides State.clickPrevious(). Goes to previous song'''
    def clickPrevious(self):
        self._audio_player.previousSong()
    
    
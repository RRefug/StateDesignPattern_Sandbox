from mainpkg.interface_pkg.state_informal_interface import State
import mainpkg.context_pkg.audio_player
import mainpkg.concreteclasses_pkg.locked_state
import mainpkg.concreteclasses_pkg.ready_state
class PlayingState(State):
    ''' Concrete class that extends the informal interface. '''

    _audio_player = mainpkg.context_pkg.audio_player.AudioPlayer()

    def __init__(self, audioPlayer):
        self._audio_player = audioPlayer

    def clickLock(self): 
        '''Overrides State.clickLock(). Unlocks the phone'''
        self._audio_player.setState(mainpkg.concreteclasses_pkg.locked_state.LockedState(self._audio_player))

    def clickPlay(self): 
        '''Overrides State.clickPlay(). 
        Pauses the song and 
        the audioplayer is waiting for you to play or lock the phone by being ready.'''
        self._audio_player.stopPlayback()
        self._audio_player.setState(mainpkg.concreteclasses_pkg.ready_state.ReadyState(self._audio_player))

    def clickNext(self): 
        '''Overrides State.clickNext(). Goes to the next song OR keeps playing the current song until done.'''
        if self.event.doubleclick:
            self._audio_player.nextSong()
        else:
            self.playerfastForward(5)

    
    def clickPrevious(self):
        '''Overrides State.clickPrevious(). Goes to previous song'''
        if self.event.doubleclick:
            self._audio_player.previous()
        else:
            self._audio_player.rewind(5)
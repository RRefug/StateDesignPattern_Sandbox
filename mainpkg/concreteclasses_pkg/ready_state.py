from mainpkg.interface_pkg.state_informal_interface import State
import mainpkg.context_pkg.audio_player
import mainpkg.concreteclasses_pkg.locked_state
import mainpkg.concreteclasses_pkg.playing_state

class ReadyState(State):
    ''' Concrete class that extends the informal interface. 
        Methods are inherited from state informal interface, here to be implemented.
        They can also trigger state transitions("lemme lock my phone after play my song") in the context.
    '''
    # protected variable, only want context to use. 
    _audio_player = mainpkg.context_pkg.audio_player.AudioPlayer()

    def __init__(self, audioplayer):
        ''' Argument is an audioplayer object'''
        self._audio_player = audioplayer
        
    # 4 inherited overwritten methods!
    def clickLock(self): 
        '''Overrides State.clickLock(). Locks the phone'''
        self._audio_player.setState(mainpkg.concreteclasses_pkg.locked_state.LockedState(self._audio_player))

    def clickPlay(self): 
        '''Overrides State.clickPlay(). Plays the song'''
        print('PUSHED PLAY: PLAYING CURRENT SONG')
        self._audio_player.startPlayback()
        self._audio_player.setState(mainpkg.concreteclasses_pkg.playing_state.PlayingState(self._audio_player))
    
    def clickNext(self): 
        '''Overrides State.clickNext(). Goes to the next song'''
        self._audio_player.nextSong()
    
    def clickPrevious(self):
        '''Overrides State.clickPrevious(). Goes to previous song'''
        self._audio_player.previousSong()
    
    
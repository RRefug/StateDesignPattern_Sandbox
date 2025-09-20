import mainpkg.interface_pkg.state_informal_interface
# USING import mainpkg.concreteclasses_pkg.ready_state
import mainpkg.concreteclasses_pkg.locked_state
# USING import mainpkg.concreteclasses_pkg.playing_state
class AudioPlayer:
    '''
        The AudioPlayer class acts as a context. It also maintains a
        reference to an instance of one of the state classes that
        represents the current state of the audio player.
    '''
    # Interface variable instances
    _readyState = mainpkg.interface_pkg.state_informal_interface.State()
    _lockedState = mainpkg.interface_pkg.state_informal_interface.State()
    _playingState = mainpkg.interface_pkg.state_informal_interface.State()

    _currentState = mainpkg.interface_pkg.state_informal_interface.State() # initial state is idle state 
    # UI = None
    
    # Constuctor 
    def __init__(self):

        # Audio player attributes
        self.player_name = 'Spotify'
        self.playlist = ['Atlast Genius, Stockholm', 'Go Wild, Friedberg', 'Surfin, Boy Amor', 'The Cracks, Another Sky']
        self.currentSong = self.playlist[0]
        self.volume = 50
        self.playlist_name = 'Motion'
        self.playing = False

        # Audio player states
        self._lockedState = mainpkg.concreteclasses_pkg.locked_state.LockedState(self._lockedState)
        #USING self._readyState = mainpkg.concreteclasses_pkg.ready_state.ReadyState(self._readyState)
        #USING self._playingState = mainpkg.concreteclasses_pkg.playing_state.PlayingState(self._playingState)
    
        # set initial state, locked state, to audio players current state
        self._currentState = self._lockedState

        # Can test without UI for now :)
        # UI = UserInterface()

        # UI.lockButton(self.clickLock)
        # UI.playButton(self.clickPlay)
        # UI.nextButton(self.clickNext)
        # UI.prevButton(self.clickPrevious)


# Other objects must be able to switch the audio player's active state.
    def setState(self, audioPlayerState):
        self._currentState = audioPlayerState

    
# # These are the methods from the abstract interface State
# # UI methods delegate execution to the active state. 
    def clickLock(self):
        self._currentState.clickLock()

    def clickPlay(self):
        self._currentState.clickPlay()

    def clickNext(self):
        self._currentState.clickNext()
    
    def clickPrevious(self):
        self._currentState.clickPrevious()


    # Audioplayer getters
    def get_audio_player_name(self):
        return self.player_name
    
    def get_playlist_name(self):
        return self.playlist_name    
    
    def get_current_state(self):
        return self._currentState
    

    # Audioplayer functions
    def startPlayback(self):
        print('Playing = ', self.playing)
        print(self._currentState.get_name())
        if self._currentState == self._lockedState:
            print('Phone is locked. Unlock the phone first! ')
        else:
            print(self._currentState)
            print('Playing = ', self.playing)
            print('Playing current song... : ', self.currentSong)

    def stopPlayback(self):
        pass

    def nextSong(self):
        pass

    def previousSong(self):
        pass

    def fastForward(self):
        pass

    def rewind(self):
        pass
from state_informal_interface import State
from ready_state import ReadyState

class AudioPlayer:

    '''
    The AudioPlayer class acts as a context. It also maintains a
    reference to an instance of one of the state classes that
    represents the current state of the audio player.
    '''
    player_name = 'Spotify'
    state = State()
    # UI = None
    volume = 50
    playlist_name = 'Motion'
    playlist = ['Atlast Genius, Stockholm', 'Go Wild, Friedberg', 'Surfin, Boy Amor', 'The Cracks, Another Sky']
    currentSong = None

    def __init__(self):
        # state = get_interface_import()
        self.state = ReadyState()

        # Can test without UI :)
        # UI = UserInterface()
        
        # UI.lockButton(self.clickLock)
        # UI.playButton(self.clickPlay)
        # UI.nextButton(self.clickNext)
        # UI.prevButton(self.clickPrevious)

    # Other objects must be able to switch the audio player's active state.
    def changeState(self, stateObject):
        self.state = stateObject 

    
# These are the methods from the abstract interface State
# UI methods delegate execution to the active state. 
    def clickLock(self):
        self.state.clickLock()

    def clickPlay(self):
        self.state.clickPlay()

    def clickNext(self):
        self.state.clickNext()
    
    def clickPrevious(self):
        self.state.clickPrevious()


    def get_audio_player_name(self):
        return self.player_name
    
    def get_interface_import(self):
        from state_informal_interface import State
        

    def startPlayback():
        pass

    def stopPlayback():
        pass

    def nextSong():
        pass

    def previousSong():
        pass

    def fastForward():
        pass

    def rewind():
        pass
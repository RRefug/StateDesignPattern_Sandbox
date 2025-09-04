
from state_informal_interface import State
from locked_state import LockedState
from ready_state import ReadyState

class PlayingState(State):
    ''' Concrete class that extends the informal interface. '''

    def clickLock(self): 
        '''Overrides State.clickLock(). Unlocks the phone'''
        self.player.changeState(LockedState(self.player))

    def clickPlay(self): 
        '''Overrides State.clickPlay(). 
        Pauses the song and 
        the audioplayer is waiting for you to play or lock the phone by being ready.'''
        self.player.stopPlayback()
        self.player.changeState(ReadyState(self.player))

    def clickNext(self): 
        '''Overrides State.clickNext(). Goes to the next song OR keeps playing the current song until done.'''
        if self.event.doubleclick:
            self.player.nextSong()
        else:
            self.playerfastForward(5)

    
    def clickPrevious(self):
        '''Overrides State.clickPrevious(). Goes to previous song'''
        if self.event.doubleclick:
            self.player.previous()
        else:
            self.player.rewind(5)
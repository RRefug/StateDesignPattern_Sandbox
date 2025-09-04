from state_informal_interface import State
from locked_state import LockedState
from playing_state import PlayingState

class ReadyState(State):
    ''' Concrete class that extends the informal interface. 
        Methods are inherited from state informal interface, here to be implemented.

        They can also trigger state transitions("lemme lock my phone after play my song") in the context.
    '''

    def clickLock(self): 
        '''Overrides State.clickLock(). Locks the phone'''
        self.player.changeState(LockedState(self.player))

    def clickPlay(self): 
        '''Overrides State.clickPlay(). Plays the song'''
        self.player.startPlayback()
        self.player.changeState(PlayingState(self.player))

    def clickNext(self): 
        '''Overrides State.clickNext(). Goes to the next song'''
        self.player.nextSong()
    
    def clickPrevious(self):
        '''Overrides State.clickPrevious(). Goes to previous song'''
        self.player.previousSong()
    
    
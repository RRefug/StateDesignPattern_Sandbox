import mainpkg.interface_pkg.state_informal_interface
import mainpkg.core
# TODO: Commented out classes not using yet. Want to see name of locked state first. 
# USING import mainpkg.concreteclasses_pkg.playing_state
# USING import mainpkg.concreteclasses_pkg.ready_state
class LockedState(mainpkg.interface_pkg.state_informal_interface.State):
    ''' Concrete class that extends the informal interface. '''
    # uses core import instead. Dang it so closeeeee
    # TODO: Where we stopped last time.
    _audio_player = mainpkg.core.AudioPlayer()

    # constructor, audio player is passed in and reassigned to a new audioplayer object instance,
    # to gain access to the audio player functions within our state functions.
    # state functions all act differently depending in what state they are in. 
    def __init__(self, audioPlayer):
        '''Connects player here. '''
        self.name = ':)'

        self._audio_player = audioPlayer

    # locked state getters
    def get_name(self):
        return self.name
    
    
    # locked state, state functions
    def clickLock(self): 
        '''Overrides State.clickLock(). UNLOCKS the phone'''
        
        print('Unlocked the phone.')
        if self._audio_player.playing:
            self._audio_player.setState(mainpkg.concreteclasses_pkg.playing_state.PlayingState(self._audio_player))
            print('Phone is in the playing state.')
        else:
            self._audio_player.setState(mainpkg.concreteclasses_pkg.ready_state.ReadyState(self._audio_player))
            print('Phone is in the ready state.')


    def clickPlay(self): 
        '''Overrides State.clickPlay(). Plays the song'''
        # Locked, so do nothing
        print("Phone is locked, can't play a song")

    def clickNext(self): 
        '''Overrides State.clickNext(). Goes to the next song'''
        # Locked, so do nothing
        print("Phone is locked, can't go to next song")
    
    def clickPrevious(self):
        '''Overrides State.clickPrevious(). Goes to previous song'''
        # Locked, so do nothing
        print("Phone is locked, can't go back to previous song")







# Just to confirm we had a connection to that interface. Must return false, not true since true violates the definition of an interface.
# print(issubclass(LockedState, State)) 

# # "dunder method" that helps us see superclass we use for this subclass.
# print(LockedState.__mro__) 

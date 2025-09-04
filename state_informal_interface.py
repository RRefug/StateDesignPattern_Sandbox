''' THIS IS OUR ABSTRACT <<INTERACE>>>
    However, in python no need for them... :( handles multiple inheritance)
'''
from audio_player import AudioPlayer


# You rely on Duck typing to inform users that this is an interface!!! If it quacks and walks like a duck, then it will be treated like a duck! '''
class State:
    ''' Informal interface that acts like a real interface.
    Defines the methods that will be in AudioPlayer concrete class. '''    
    
    _protected_player = AudioPlayer()

    def __init__(self):
        self.player = self._protected_player

    # 4 Abstract methods, implementation needs to be added in derived concrete classes.
    def clickLock(self): 
        '''Unlocks the phone'''

    def clickPlay(self): 
        '''Plays the song'''

    def clickNext(self): 
        '''Goes to the next song'''
    
    def clickPrevious(self):
        '''Goes to previous song'''
    
    



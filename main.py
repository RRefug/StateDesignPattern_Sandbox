''' Helpful Notes about relative andn absolute paths:
Relative import notation:
-   from . import module_name (imports a module in the same directory)
-   from .. import module_name (imports a module from the parent directory)
-   from .subpackage import module_name (iclmports a module from a subpackage within the same directory)
Better to use absolute imports. Looks a little clunky, but better for sure in being certain.
'''

''' 
NOTE:
WE Bookmarked two tutorials we used on this so far:
1. State Design Pattern: Easy Guide for Beginners
2. How to fix circular imports in Python | 2MinutesPy

It works for now because I kept it simple commenting out imports. 
Started from main's import and followed it myself, no breakpoints. We smarterrrr!!
We even understand __init__ files more. We were able to mess around with order do to them :)
You got everything in it's own packages.
Review co pilot notes if needed.
Need to refactor AudioPlayer in SOME way, State is imported not even 2 lines in there.

WE DID ITTTTTTT SOLUTION was to just do: 

import moduleName

code example:
    moduleName.moduleClass.class_method
'''
#from mainpkg.context_pkg.audio_player import AudioPlayer
import mainpkg.context_pkg.audio_player

def main():
    # Audio player access checks
    player = mainpkg.context_pkg.audio_player.AudioPlayer()
    print('Audio Player name:', player.get_audio_player_name())
    print(f'Playlist name: {player.get_playlist_name()}')


    # Locked state checks (Initial state of audio player)
    print('Current State: ', player._currentState.get_name())

    # player.startPlayback() # Fails, since locked. 
    #player.clickLock() # Unlock audio player


    # Ready state checks (After unlocked)

    # Playing state checks
    # player.clickPlay() # user plays the song
    # player.clickNext() # user plays next song
    # player.clickPrevious() # user wants to go back to the previous song
    # player.clickPlay() # user replays favorite song

    # Lock state checks

if __name__ == "__main__":
    print("Main working...")
    main()

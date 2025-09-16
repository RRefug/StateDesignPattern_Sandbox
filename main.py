# import sys
# from pathlib import Path

# sys.path.append(str(Path(__file__).parent))


'''
These are relative imports
from . import module_name (imports a module in the same directory)
from .. import module_name (imports a module from the parent directory)
from .subpackage import module_name (iclmports a module from a subpackage within the same directory)

Better to use absolute imports. Looks a little clunky, but better for sure in being certain.
'''
from mainpkg.context_pkg.audio_player import AudioPlayer


print("Main working...")

def main():
    player = AudioPlayer()

# player.clickLock() # user unlocks the phone
# player.clickPlay() # user plays the song
# player.clickNext() # user plays next song
# player.clickPrevious() # user wants to go back to the previous song
# player.clickPlay() # user replays favorite song

    print(player.get_audio_player_name())


if __name__ == "__main__":
    main()


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
'''

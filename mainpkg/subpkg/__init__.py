
'''
    Centralizing imports at a package level.
    allows internal modules to import from a single source. 
    Reducing need for cross imports. 
    Meaning no more circular imports in your project.
'''

# from mainpkg.context_pkg.audioplayer import AudioPlayer

# from mainpkg.concreteclasses_pkg.locked_state import LockedState
# from mainpkg.concreteclasses_pkg.playing_state import PlayingState
# from mainpkg.concreteclasses_pkg.ready_state import ReadyState


# from mainpkg.interface_pkg.state_informal_interface import State
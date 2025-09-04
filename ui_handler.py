# class UserInterface:
#     ''' This is not using a real GUI. I just use a simple pretend one. '''
#     def __init__(self):
#         self.UIstate = 'Locked'
#         self.menu = {1: 'clickLock', 2: 'clickPlay', 3: 'clickNext', 4: 'clickPrevious'}
    
#     def lockButton(self, clickLock):
#         print('PUSHED UNLOCK PLAYER....')
        
#         if clickLock == '1':
#             self.UIstate = 'Unlocked'
    
#     def playButton(self, clickPlay):
#         if clickPlay == '2' and self.UIstate == 'Unlocked':
#             print('PUSHED PLAY SONG....')
#         else:
#             print('Unlock the phone first....')

#     def nextButton(self, clickNext):
#         if clickNext == '3' and self.UIstate == 'Unlocked':
#             print('PUSHED NEXT SONG')
#         else:
#             print('Unlock the phone first....')

#     def prevButton(self, clickPrevious):
#         if clickPrevious == '4' and self.UIstate == 'Unlocked':
#             print('PUSHED PREVIOUS SONG')
#         else:
#             print('Unlock the phone first....')

#     def printMenu(self):
#         print('\n##########################')
#         for menuKey, menuValue in self.menu.items():
#             print(f'{menuKey} {menuValue}')
#         print('##########################\n')


# userInput = ''
# ui = UserInterface()
# out = True


# while out:
#     key = ''
    
#     ui.printMenu()

#     key = input('Enter your choice of the menu below: ')
#     if key != '1' and key != '2' and key != '3' and key != '4':
#         out = False

#     if key == '1':
#         ui.lockButton(key)
#     if key == '2':
#         ui.playButton(key)
#     if key == '3':
#         ui.nextButton(key)
#     if key == '4':
#         ui.prevButton(key)

# print('Thank you for using the audio player! \n Have a good day.')
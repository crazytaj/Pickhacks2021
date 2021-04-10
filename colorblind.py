def setColorMode(state, filterType = None, recursive = False):
    filterTypes = {
        0: "grayscale",
        1: "inverted",
        2: "grayscale inverted",
        3: "deuteranopia",
        4: "protanopia",
        5: "tritanopia"
    }

    #imports
    import winreg as wreg
    from elevate import elevate
    import sys
    from pynput.keyboard import Key, Controller
    import time

    #rerouting console logs to files to account for shadow window when elevating program
    if recursive == False:
        sys.stderr = open('colorblindError.log', 'a')
        sys.stdout = open('colorblindPrint.log', 'a')

    #elavate the program to admin to edit registry
    elevate()

    editKey = wreg.OpenKey(wreg.HKEY_CURRENT_USER, r'Software\Microsoft\ColorFiltering', 0, wreg.KEY_SET_VALUE)
    viewKey = wreg.OpenKey(wreg.HKEY_CURRENT_USER, r'Software\Microsoft\ColorFiltering', 0, wreg.KEY_QUERY_VALUE)

    #get the current state of the colorblind filter
    currentState = wreg.QueryValueEx(viewKey, "Active")[0]
    #print('colorFilter state was: '+str(currentState)+' prior to script')
    
    #initialize keyboard object to use hotkey
    keyboard = Controller()

    j = 0

    #if color filters are already active turn off so that it can be reupdated
    if currentState == state:
        print('start of recursive')
        setColorMode(abs(state-1), None)
        print('stop of recursive')
        currentState = wreg.QueryValueEx(viewKey, "Active")[0]
        #print('colorFilter state was: '+str(currentState)+' after conditional if')

    #enable the hotkey to update registry
    wreg.SetValueEx(editKey, "HotkeyEnabled", 1, wreg.REG_DWORD, 1)

    i = 0
    while currentState != state:
        i += 1
        print('state changed on try '+str(i))
        keyboard.press(Key.cmd)
        keyboard.press(Key.ctrl)
        keyboard.press('c')
        keyboard.release(Key.cmd)
        keyboard.release(Key.ctrl)
        keyboard.release('c')

        

        currentState = wreg.QueryValueEx(viewKey, "Active")[0]
    print('state was: '+str(currentState)+' at the end of script')
    
    #swap to correct color filter setting
    wreg.SetValueEx(editKey, "HotkeyEnabled", 1, wreg.REG_DWORD, 0)
    currentFilter = wreg.QueryValueEx(viewKey, "FilterType")[0]
    if filterType != None and currentFilter != filterType:
        while currentFilter != filterType:
            j+=1
            print('filter changed in '+str(j))
            wreg.SetValueEx(editKey, "FilterType", 1, wreg.REG_DWORD, filterType)
            currentFilter = wreg.QueryValueEx(viewKey, "FilterType")[0]
        print('filter ended as '+str(currentFilter))

    #disable the hotkey to prevent accidentle activation
    

    currentFilter = wreg.QueryValueEx(viewKey, "FilterType")[0]
    print('filter ended ended at '+str(currentFilter))

    #close the log files
    sys.stdout.write('----------------------------')
    sys.stderr.write('----------------------------')
    if recursive == False:
        sys.stdout.close()
        sys.stderr.close()

setColorMode(0, 4)
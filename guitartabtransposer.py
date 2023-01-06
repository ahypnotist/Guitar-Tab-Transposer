#guitar tab transposer
#up and down


#where do i start
#ok so you take 1 tab and turn it into another

#beautiful tune

tab = "E|-------| \nB|-------| \nG|0-3-5--| \nD|0-3-5--| \nA|-------| \nE|-------|"
print(tab)

chromatic_circle = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

E_standard = ["E2", "A2", "D3", "G3", "B3", "E4"]
semitone_down_estandard = ["D#2", "G#2", "C#3", "F#3", "A#3", "D#4"]
tone_down_estandard = ["D2", "G2", "C3", "F3", "A3", "D4"]
open_g_banjo = ["G4", "D3", "G3", "B3", "D4"]

#i need to idenitfy each of the parts of the tab
base = E_standard
goto = semitone_down_estandard

guitar_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']

new_tab = []

for i in tab:
    if base == E_standard and goto == semitone_down_estandard:    
        if i in guitar_numbers:
            l = int(i) + 1
            new_tab.append(str(l))
        elif i in chromatic_circle:
            #NOT FINISIHED
            #USE THE ev FUNCTION FOR SOMETHING
            # I WILL REMEBER
            new_tab.append(i)            
        else:
            new_tab.append(i)
        
print(("".join(new_tab)))


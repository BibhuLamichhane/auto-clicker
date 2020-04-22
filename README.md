# Auto Typer/Clicker

1. Run the command "pip install -r requirements.txt" in your CLI
2. Open auto.py for the program to run with a console or run auto.pyw without console

## With this app you can schedule keyboard and mouse events at your will.
# For mouse events:<br>
    1. Choose the action that you want to do
        There are 2 choices:
            a. Left Click
            b. Right Click
            
    2. After you choose the action you need to enter the coordinates for where the event needs to occur.
    
    3. To get the coordinates click the button labeled "Locate X & Y" and move your mouse to the point
       that you want the coordinates of.
       
    4. Now write the displayed coordinates in the input boxes.
    
    5. Next enter the pause time between the events in the input box you can also enter decimal values 
       so set the delay as small as you want but the shortest delay between events depends on the processing 
       power of your computer.
       
    6. Keep in mind the delay doesnot apply to the first event
    
    7. To apply the delay to the first event add a dummy event such as typing the letter "a".
    
    8. After you're done adding the delay, coordinates and choosing the action click the button "add command"
# For Keyboard events:<br>
## Choose the tab according to which keyboard event you want to simulate

    Alphabets includes alphabets a to z (actions in this tab are equivalent to physically pressing keys on your keyboard)
    
    Numbers includes number 0 to 1
    
    Symbols includes all of the symbols in your keyboard
    
    Custom text tab is useful while scheduling typing long texts
        It has two options:
            1. Type Letter By Letter
              - This is also equivalent to physically pressing keys on your keyboard so each letter is displayed one at 
                a time so the delay you apply to this event will occur after each letter is typed.
                For example:
                    If you typed the text "Hello World" with delay 0.2 and added the command then at first 'H' is typed 
                    without delay than before 'e' is typed there is a delay of 0.2 seconds and and there is another delay
                    of 0.2 seconds before 'l' and so on with rest of the text.
            2. Type at once
              - This is equivalent to using Ctrl + v which means the letters in the text aren't pressed in your keyboard.
    Other Keys tab includes keys such as Backspace, Space, Enter, etc.
## Deleting a command
After you've added a command and later want to delete a command, select the command you want to remove and click
the button "Delete Command"
 ## Running the commands
 Cycles refers to the number of times you want to run the commands you have added.
 After your're done adding commands and entering the number of cycles click the "Start" button to run the commands
 

import random
import string
from termcolor import colored
import os

def generate_password(length):
    # Generate a password of the specified length using only alphanumeric characters
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == '__main__':
    # Print an ASCII art banner
    banner = r"""                                                                              
,-.----.                                                                      
\    /  \                                                                     
|   :    \                                                                    
|   |  .\ :                                                            ,---,  
.   :  |: |             .--.--.    .--.--.     ,----._,.           ,-+-. /  | 
|   |   \ : ,--.--.    /  /    '  /  /    '   /   /  ' /   ,---.  ,--.'|'   | 
|   : .   //       \  |  :  /`./ |  :  /`./  |   :     |  /     \|   |  ,"' | 
;   | |`-'.--.  .-. | |  :  ;_   |  :  ;_    |   | .\  . /    /  |   | /  | | 
|   | ;    \__\/: . .  \  \    `. \  \    `. .   ; ';  |.    ' / |   | |  | | 
:   ' |    ," .--.; |   `----.   \ `----.   \'   .   . |'   ;   /|   | |  |/  
:   : :   /  /  ,.  |  /  /`--'  //  /`--'  / `---`-'| |'   |  / |   | |--'   
|   | :  ;  :   .'   \'--'.     /'--'.     /  .'__/\_: ||   :    |   |/       
`---'.|  |  ,     .-./  `--'---'   `--'---'   |   :    : \   \  /'---'        
  `---`   `--`---'                             \   \  /   `----'              
                                                `--`-'                        """
    os.system("clear")
    print(colored(banner, 'green'))

    # Prompt the user to enter the password length
    while True:
        try:
            length = int(input('Enter the desired password length: '))
            if length <= 0:
                raise ValueError('Password length must be positive')
            break
        except ValueError:
            print('Invalid input. Please enter a positive integer.')

    # Generate the password and print it with a banner
    password = generate_password(length)
    passgen_banner = colored('PassWord: ', 'red')
    print(f'{passgen_banner}: {password}')


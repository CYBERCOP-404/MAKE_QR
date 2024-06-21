# banner section 
banner = '''\033[0;32m \033[1m
    .------------- -.         .----------------. 
   | .------------ . |       | .--------------. |
   | |    ___      | |       | |  _______     | |
   | |  .'   '.    | |       | | |_   __ \    | |
   | | /  .-.  \   | |       | |   | |__) |   | |
   | | | |   | |   | |       | |   |  __ /    | |
   | | \  `-'  \_  | |       | |  _| |  \ \_  | |
   | |  `.___.\__| | |       | | |____| |___| | |
   | '------------ ' |       | '--------------' |
    '------------- -'         '----------------' 
   ____________\033[0;34m CYBER CRIME RAJSHAHI\033[0;32m ____________
   
   [1] YOU CAN USE OUR FIRE TOOL  
'''
import os
import qrcode as qr
from random2 import randint
os.system('clear')
print(banner)
USER = input('  [+] ENTER YOUR TEXT HERE : ')
if USER=='1':
    os.chdir('..')
    os.system('rm -rf CYBER-404')
    os.system('git clone https://github.com/cybercop-404/cyber-404.git')
    os.chdir('CYBER-404')
    os.system('python main.py')
else:# Generate QR code
    qr_code = qr.make(USER)
    num = randint(0,999)
    file =f'qr_code{num}.png'
    # Save QR code to file
    qr_code.save(file)
    print(f"QR code saved as '{file}'")
    # Display QR code
    os.system('clear')

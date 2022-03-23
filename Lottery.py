import time

options = ['integretion', 'shoresh', 'kiruvim', 'linear']
input = int(input("Please enter ****:"))
random = (((time.localtime().tm_hour+time.localtime().tm_min)*time.localtime().tm_sec)//13) + input
print(options[random % len(options)])








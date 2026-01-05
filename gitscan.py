import os

os.system('sudo apt install epel-release')
os.system('sudo apt install pip3')
os.system('pip3 install truffleHog3')

file = open('GitRepoList.txt', 'r')
count = 0

# Using for loop
for line in file:
    count += 1
    tag = (line.strip().split("/"))
    name = tag[-1].split(".")
    print(name)
    path = line.strip()
    print("--------------------------- Scanning GitHub Repo:  " +name[0]+ " -----------------------------------")
    os.system('trufflehog3 -vv --no-entropy --no-history -r regex.txt '+path+' -f html -o ./Reports/mosip'+name[0]+'.html')
# Closing files 
file.close()

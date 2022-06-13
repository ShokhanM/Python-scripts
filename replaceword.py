# Read file where need replace word
with open('breplace.txt', 'r', encoding='utf-8') as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('6', 'б')

# Write the file out again
with open('breplace.txt', 'w', encoding='utf-8') as file:
    file.write(filedata)

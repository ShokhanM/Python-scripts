# Read file where need replace word
with open('file.txt', 'r', encoding='utf-8') as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('letter', 'letter')

# Write the file out again
with open('file.txt', 'w', encoding='utf-8') as file:
    file.write(filedata)

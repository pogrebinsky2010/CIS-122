#Talaba lab 4h
import urllib.request

names_url='http://www.cs.uoregon.edu/Classes/15W/cis122/data/yob1994.txt'
print("Data from cis class at U of O")
data = []

def read_file(fname):
    data = []
    with open(fname, 'r') as f:
        for line in f:
            line = line.strip("\n")
            temp = line.split(',')
            data.append(temp)
    return data
def search(name, data):
    name = name.capitalize()
    found = 0
    output = []
    for value in data:
        if name == value[0].capitalize():
            found += 1
            output.append(value)
            print(value[0], value[1], value[2])
    if found == 0:
        print(name,'not found!!')

    return output

def contain(substr, data):
    substr = substr.lower()
    found = 0
    output=[]
    for value in data:
        if substr in value[0].lower():
            found+=1
            output.append(value)
            print(value[0], value[1], value[2])
    if found == 0:
        print(substr, 'is not contained')
    else:
        print(found, 'occurences found')

        return output

def endswith(substr, data):
    substr = substr.lower()
    found = 0
    for value in data:
        if value[0].lower().endswith(substr):
            found+=1
            output.append(value)
            print(value[0], value[1], value[2])
    if found == 0:
        print('no name found with: ', substr)
    else:
        print(found, 'occurences found')

        return output

def write_values(output, fname):
    with open(fname, 'w') as f:
        for value in output:
            line = ','.join(value)
            f.write(line)
            f.write('\n')

        return output
def startswith(substr, data):
    substr = substr.lower()
    found = 0
    for value in data:
        if value[0].lower().startswith(substr):
            found+=1
            output.append(value)
            print(value[0], value[1], value[2])
    if found == 0:
        print('no name found with: ', substr)
    else:
        print(found, 'occurences found')


        return output


url =('http://www.cs.uoregon.edu/Classes/15W/cis122/data/yob1994.txt', 'r')
with urllib.request.urlopen('http://www.cs.uoregon.edu/Classes/15W/cis122/data/yob1994.txt') as webpage:
      for line in webpage:
          line = line.strip()
          line = line.decode('utf-8')
          name = line.split(',')
          data.append(name)

     
          
          


decider = input(' Would you like to search for names?(y/n) ')

while(decider == 'Y' or decider == 'y'):
    print('1. Name search')
    print('2. End search')
    print('3. Search by entering the end of a name ')
    print('4. Search by entering a containing letter ')
    print('5. Search by entering the beginning letter ')
  
    choice = input(' enter choice 1-3): ')
    output = []
    if choice == '1':
        name = input('Enter name: ')
        output = search(name, data)
        print()
    elif choice == '2':
        print('thanks for searching!')
        break
    elif choice == '3':
        substr = input('enter end string: ')
        output = endswith(substr, data)
        print()
    elif choice == '4':
        substr = input('Enter a letter that is in the name: ')
        output = contain(substr, data)
        print()
    elif choice == '5':
        substr = input('Enter a beginning of a name')
        output = startswith(substr, data)
        print()
    else:
       decider = input('that choice is not in the directory.... Would you like to search again?(y/n)')

    write = input('write to file y/n: ')
    if write.lower() == 'y':
         fname = input('Enter filename: ')
         write_values(output, fname + '.txt')
         decider = input("file saved! \n Would you like to search for more names? ")
    else:    
        decider = input('would you like to search for more names? ')
        
    

        
        
            

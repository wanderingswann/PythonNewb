word = input("Pick a fruit. ")

if word == 'banana' or 'Banana':
    print ('All right, bananas. ')

if word < 'banana' or 'Banana' :
    print('Your word,' + word + ', comes before banana.' )
elif word > 'banana' or 'Banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right bananas!')
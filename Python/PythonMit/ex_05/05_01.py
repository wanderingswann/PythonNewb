val = 0
tot = 0

while True:
    num = input("Enter a number: ")
    if num == 'done' :
        break
    try:
        fn = float(num)
    except:
        print("Error, please enter a numerical number.")
        continue
    print(num)
    val = val + 1
    tot = tot + val

print('All Done')
print(tot,val,tot/val)

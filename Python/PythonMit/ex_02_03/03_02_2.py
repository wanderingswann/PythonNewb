hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
    sh = float(hrs)
    sr = float(rate)
except:
    print("Error, please enter numberic input.")
    quit()

    print(sh, sr)
if sh > 40 :
    reg = sr * sh
    otp = (sh - 40.0) * (sr * 0.5)
    xp = reg + otp
else:
    xp = sh * sr
print("Pay:",xp)

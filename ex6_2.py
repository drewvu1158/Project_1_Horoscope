#Student: Andrew Vu
#Programing Excercise: 6_2

import InputBox
from tkinter import *
from selenium import web

url_aries = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=1"
url_Tarus = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=2"



ans_2 = ""
ans_3 = ""
horo = ""
s = ""

def CheckLeapYear(y):
 max = 0
 if (y % 4) == 0:
  if (y % 100) == 0:
   if (y % 400) == 0:
    max = 29
   else:
    max = 28
  else:
   max = 29
 else:
  max = 28
 return max

def GetTradHoro(m, d):
 horo = ""
 if (m == 1):
   if (d >= 20) :
    horo = "Aquarius"
   else: horo = "Capricorn"
 if (m == 2):
   if (d >= 12) :
    horo = "Pisces"
   else: horo = "Aquarius"

 if (m == 3):
     if (d >= 21):
        horo = "Aries"  
     else: horo = "Pisces"

 if (m == 4):
   if (d >= 20): 
    horo = "Taurus"
   else: horo = "Aries"

 if (m == 5):
   if (d >= 21) : 
    horo = "Gemini"
   else: horo = "Taurus"

 if (m == 6):
   if (d >= 21) :
    horo = "Cancer"
   else: horo = "Gemini"

 if (m == 7):
   if(d >= 23) : 
    horo = "Leo"
   else: horo = "Cancer"

 if (m == 8):
   if(d >= 23) : 
    horo = "Virgo"
   else: horo = "Leo"

 if (m == 9):
   if(d >= 23) : 
    horo = "Libra"
   else: horo = "Virgo"

 if (m == 10):
   if (d >= 23) : 
    horo = "Scorpio"
   else: horo = "Libra"

 if (m == 11):
   if (d >= 22) : 
    horo = "Sagittarius"
   else: horo = "Scorpio"

 if (m == 12):
   if (d >= 22) : 
    horo = "Capricorn"
   else: horo = "Sagittarius"

 return horo

def GetAdjHoro(m, d):
 horo = ""

 if (m == 1) :
   if (d > 20) : 
    horo = "Capricorn"
   elif (d == 20) : 
    horo = "Half-Sagittarius-Half-Capricorn"
   else: 
    horo = "Sagittarius"

 if (m == 2) :
   if (d > 16) : 
    horo = "Aquarius"
   elif (d == 16) : 
    horo = "Half-Capricorn-Half-Aquarius"
   else: horo = "Capricorn"

 if (m == 3) :
   if (d > 11) : 
    horo = "Pisces"
   elif (d == 11) :
    horo = "Half-Aquarius-Half-Pisces"
   else: 
    horo = "Aquarius"

 if (m == 4) :
   if (d > 18) : 
    horo = "Aries"
   elif (d == 18) : 
    horo = "Half-Pisces-Half-Aries"
   else: horo = "Pisces"

 if (m == 5) :
   if (d > 13) : 
    horo = "Taurus"
   elif (d == 13) : 
    horo = "Half-Aries-Half-Taurus"
   else: horo = "Aries"

 if (m == 6) :
   if (d > 21) : 
    horo = "Gemini"
   elif (d == 21) : 
    horo = "Half-Taurus-Half-Gemini"
   else: 
    horo = "Taurus"

 if (m == 7) :
   if (d > 20) : 
    horo = "Cancer"
   elif (d == 20) : 
    horo = "Half-Gemini-Half-Cancer"
   else: horo = "Gemini"

 if (m == 8) :
   if (d > 10) : 
    horo = "Leo"
   elif (d == 10) : 
    horo = "Half-Cancer-Half-Leo"
   else: horo = "Cancer"

 if (m == 9) :
   if (d > 16) : 
    horo = "Virgo"
   elif (d == 16) : 
    horo = "Half-Leo-Half-Virgo"
   else: 
    horo = "Leo"

 if (m == 10) :
   if (d > 30) : 
    horo = "Libra"
   elif (d == 30) : 
    horo = "Half-Virgo-Half-Libra"
   else: 
    horo = "Virgo"

 if (m == 11) :
   if (d > 23 and d < 29) : 
    horo = "Scorpio"
   elif (d == 23) : 
    horo = "Half-Libra-Half-Scorpio"
   elif (d > 29) : 
    horo = "Ophiuchus"
   elif (d == 29) : 
    horo = "Half-Scorpio-Half-Ophiuchus"
   else: horo = "Libra"

 if (m == 12) :
   if (d > 17) : 
    horo = "Sagittarius"
   elif (d == 17) : 
    horo = "Half-Ophiuchus-Half-Sagittarius"
   else: 
    horo = "Ophiuchus"

 return horo

InputBox.ShowDialog("Enter your Birthyear:")
y = int(InputBox.GetInput())

InputBox.ShowDialog("Enter the Month of your birth:")
m = int(InputBox.GetInput())

InputBox.ShowDialog("Enter the day:")
d = int(InputBox.GetInput())

if (m <1 or m > 12):
 print("Month value must be 1 ~ 12")
elif (d < 1 or d > 31):
  print("Day value must be 1 ~ 31")
elif ( (m == 4 or m==6 or m==9 or m==11) and d > 30):
  print("Maximum is 30.")
elif ( m == 2 and d > CheckLeapYear(y)):
  print("Maximum is 28 for regular year or 29 for leap year.")
else:
 InputBox.ShowDialog("Woould you like Traditional or Adjusted? \n (T/A)")
 ans = str(InputBox.GetInput())
 ans = ans.upper()
 ans = ans[0]

 if (ans == 'T'):
   print("Your traditional horoscope:", GetTradHoro(m, d))
 elif (ans == 'A'):
   print("Your adjusted horoscope:", GetAdjHoro(m, d))
 else:
   print(ans, " is an invalid option.")

if ans == "T":
    ans_2 = "Traditional"
else:
    ans_2 = "Adjusted"


if ans == "T":
    ans_3 = GetTradHoro(m, d)
else:
    ans_3 = GetAdjHoro(m, d)

s += "Your " + ans_2 + " horoscope is: " + " " + ans_3

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text = s).grid()
root.mainloop()
import smtplib
import requests
import json
from datetime import date
import tkinter 

from tkinter import *
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("surajtest12@gmail.com","9853266936r")
user={"value":"12345678"}
main=Tk()
lbl1 = Label(main, text="Covid19 Vaccine Finder App!", bg="orange red", fg="white", font="none 20 bold")
lbl1.config(anchor=CENTER)
lbl1.pack()


lbl2=Label(main,text="This app will mail you the details of your nearby Vaccine centers based on pincode",bg="white")
lbl2.config(anchor=CENTER, pady=10)
lbl2.pack()

lbl3=Label(main,text="Enter your email here!",height=3)
lbl3.pack()

ent1=Entry(main,width=25)
ent1.pack()

lbl4=Label(main,text="Enter your pincode")
lbl4.pack()

ent2=Entry(main)
ent2.pack()

def finder():
  server=smtplib.SMTP_SSL("smtp.gmail.com",465)
  server.login("surajtest12@gmail.com","9853266936r")
  email=ent1.get()
  pincode=ent2.get()
  todaydate=date.today()
  finaldate=todaydate.strftime("%m"+"-"+"/%d"+"-"+"/%y")
  api=("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=751001&date=05-05-2021")
  response=requests.post(api,headers=user)
  print(response)
  load_data=json.loads(response.text)
  Data = load_data['sessions'][0]
  name=Data['name']
  print(name)
  capacity=Data['available_capacity']
  print(capacity)
  slots=Data['slots']
  lbl5.configure(text="Done. Check your email",bg="black",fg="green")
  message=("Found a Vacination Spot at "+str(name)+". This has a capacity of "+str(capacity)+"  The slots are: ",slots)
  email_text='Subject: {}\n\n{}'.format("Vaccine Alert!",message)
  server.sendmail("surajtest12@gmail.com",email,email_text)
  server.quit()
  


  

but1=Button(text="Send me!",command=finder)
but1.pack()


lbl5=Label(main,text="Status appears here!")
lbl5.pack()






print("Done")


main.geometry('600x600')

main.mainloop()

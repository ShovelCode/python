from Tkinter import *
import smtplib
import fileinput
import openpyxl

root = Tk()

#smtp.mail.yahoo.com with port 465 or 587
#Create an object passing the domain name and port number.
smtpObj = smtplib.SMTP('smtp.mail.yahoo.com', 587)
type(smtpObj)

#Sending a helo to the smtp server
smtpObj.ehlo()
#starting TLS encryption (necessary)
smtpObj.starttls()
#logging in to the server with your email

#decalres global variables for login usage
global username 
global password

#Global variables used to grab the names, adresses, and actually send the files. 
global name
global address
global txtfile
global excelFile
names = "BOB"




#Sends a dummy email currently
def sendMail():
		smtpObj.login(userEntry.get(), passEntry.get())
		#actually sending mail using 3 arguements: your email, recipient, email body
		excelFile = namesEntry.get()
		wb = openpyxl.load_workbook(excelFile)
		sheet = wb.get_sheet_by_name('Sheet1')
		
		for row in range(1, sheet.max_row + 1):
			name = sheet['A' + str(row)].value
			address = sheet['B' + str(row)].value
			with open(textEntry.get(), 'r') as file :
				filedata = file.read()
			# Replace the target string
			filedata = filedata.replace("PLACEHOLDER", name)
			# Write the file out again
			with open(textEntry.get(), 'w') as file:
				file.write(filedata)
			txtfile = textEntry.get()
			smtpObj.sendmail('based_n8@yahoo.com', address, txtfile)
			
		
		
		smtpObj.quit()
	
	#Currently this function is not in use. Used for earlier testing.
def uploadTxt():
	uploadedFile = open(textEntry.get())
	print (uploadedFile.read())

	#Currently this function is not in use. Used for earlier testing.
def uploadNames():
	print "boob"
	
	#Currently this function is not in use. Used for earlier testing.
def replaceNames():
	# Read in the file
	with open(textEntry.get(), 'r') as file :
		filedata = file.read()
	# Replace the target string
	filedata = filedata.replace("PLACEHOLDER", 'bob')
	# Write the file out again
	with open(textEntry.get(), 'w') as file:
		file.write(filedata)


	
	

#Creating Widgets
userLabel = Label(root, text="Username")
passLabel = Label(root, text="Password")
userEntry = Entry(root)
passEntry= Entry(root)
textEntry = Entry(root)
namesEntry = Entry(root)
textButton = Label(root, text="Upload Text")
namesButton = Label(root, text="Upload Names")
sendButton = Button(root, text="Send", fg="Blue", command=sendMail)
check = Checkbutton(root, text="Remember Login Info")


#Placing the widgets with a grid layout. 
userLabel.grid(row=0, sticky=W)
passLabel.grid(row=1, sticky=W)
userEntry.grid(row=0, column=1)
passEntry.grid(row=1, column=1)
textEntry.grid(row=2, column=1)
namesEntry.grid(row=3, column=1)
textButton.grid(row=2, sticky=W)
namesButton.grid(row=3, sticky=W)
sendButton.grid(columnspan=2)
check.grid(columnspan=2)

#Grabbing the username and password for email sending use. 


#Causes the password entry box to only show "*" when typed in. 
passEntry.config(show="*")



root.mainloop()
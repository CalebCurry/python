# we're going to use a module called requests to handle our API
import requests

# we're going to use the API from randomfox.ca which gives us an image
dictionary = requests.get("https://randomfox.ca/floof/").json()  # gives us a dictionary with two parts, the one we want is called: image, and is the url to the fox's image (example - ./image.png)
imageurl = dictionary["image"]

# now we can use Tkinter to display this image
import tkinter
myWindow = tkinter.Tk()

# we want to get the data from our imageurl
alldata = requests.get(imageurl)

# .content gives our data in a byte array
bytearray = alldata.content

# we're going to use BytesIO to convert our array into a photo
from io import BytesIO
from PIL import Image
photo = Image.open(BytesIO(bytearray))

# we're going to use ImageTK to add an image to a Tkinter label
from PIL import ImageTk
TkinterImage = ImageTk.PhotoImage(photo)

myLabel = tkinter.Label(image=TkinterImage)
myLabel.pack()  # "pack" (add) the label to the window

# we now just add a mainloop() to the window to stop it closing
myWindow.mainloop()
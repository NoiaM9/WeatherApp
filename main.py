from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import filedialog
from geopy.geocoders import Photon
from timezonefinder import TimezoneFinder
from datetime import *
from geopy import location
import geopy.location
from geopy import distance
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather App")
root.geometry("890x490+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)


def getWeather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="Weather App")
    location = geolocator.geocode(city)

    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    timezone.config(text=result)

    long_lat.config(text=f"{round(location.latitude, 4)}°N, {round(location.longitude, 1)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    api = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(location.latitude) + "&lon=" + str(
        location.longitude) + "&appid=PUT HERE THE ID API"
    json_data = requests.get(api).json()

    # Extract and print current weather data
    temp = json_data['main']['temp']
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    wind = json_data['wind']['speed']
    description = json_data['weather'][0]['description']


    t.config(text=(temp, "K"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s"))
    d.config(text=(description))

    print(temp)
    print(humidity)
    print(pressure)
    print(wind)
    print(description)


# Icon
image_icon = ImageTk.PhotoImage(file="Images/logo.png")
root.iconphoto(False, image_icon)

Round_box = ImageTk.PhotoImage(file="Images/RoundedTest1.png")
Label(root, image=Round_box, bg="#203243").place(x=30, y=110)

# labels

label1 = Label(root, text="Temperature", font=("Helvetica", 11), fg="white", bg="#203243")
label1.place(x=50, y=120)

label2 = Label(root, text="Humidity", font=("Helvetica", 11), fg="white", bg="#203243")
label2.place(x=50, y=140)

label3 = Label(root, text="Pressure", font=("Helvetica", 11), fg="white", bg="#203243")
label3.place(x=50, y=160)

label4 = Label(root, text="Wind Speed", font=("Helvetica", 11), fg="white", bg="#203243")
label4.place(x=50, y=180)

label5 = Label(root, text="Description", font=("Helvetica", 11), fg="white", bg="#203243")
label5.place(x=50, y=200)

# search_box

# Search_image = ImageTk.PhotoImage(file="Images/Rounded2.png")
# myimage = Label(image=Search_image, bg="white")
# myimage.place(x=270, y=120)

weat_image = ImageTk.PhotoImage(file="Images/Layer1.png")
weather_image = Label(root, image=weat_image, bg="#203243")
weather_image.place(x=352, y=110)

textfield = Entry(root, justify="center", width=15, font=("poppins", 25, "bold"), bg="#203243", border=0, fg="white")
textfield.place(x=390, y=110)
textfield.focus()

Search_icon = ImageTk.PhotoImage(file="Images/Layer2.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather)
myimage_icon.place(x=630, y=120)

# bottom_boxes

frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

firstbox = ImageTk.PhotoImage(file="Images/Rounded4.png")
secondbox = ImageTk.PhotoImage(file="Images/Rounded5.png")

Label(frame, image=firstbox, bg="#212120").place(x=30, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=300, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=400, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=500, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=600, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=700, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=800, y=30)

# clock(here we will place time)

clock = Label(root, font=("Helvetica", 30, 'bold'), fg="white", bg="#57adff")
clock.place(x=30, y=20)

# timezone
timezone = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
timezone.place(x=700, y=20)

long_lat = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
long_lat.place(x=700, y=50)

t = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
t.place(x=150, y=120)


h = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
h.place(x=150, y=140)

p = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
p.place(x=150, y=160)

w = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
w.place(x=150, y=180)

d = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
d.place(x=150, y=200)

mainloop()

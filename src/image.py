import requests
import os

# URL of the galaxy wallpaper image
url = 'https://source.unsplash.com/1920x1080/?galaxy'

# Send a GET request to download the image
response = requests.get(url)

# Save the image to a file
with open('galaxy_wallpaper.jpg', 'wb') as f:
    f.write(response.content)

# Set the image as your wallpaper using gsettings
os.system('gsettings set org.gnome.desktop.background picture-uri file://' + os.path.abspath('galaxy_wallpaper.jpg'))

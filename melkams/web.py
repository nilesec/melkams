import webbrowser
from os import system
import subprocess
system(
     f" sudo chmod +x banner && sudo ./banner"
 )
def get_to_website(website_url):
  webbrowser.open(website_url)

if __name__ == "__main__":
  website_url = "https://courses.Nilesecurity.free.nf/"
  get_to_website(website_url)

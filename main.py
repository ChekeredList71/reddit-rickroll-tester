from bs4 import BeautifulSoup
from urllib.request import urlopen


url = "https://www.reddit.com/r/discordapp/comments/1b179if/comment/kscnr2t/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button"
html = urlopen(url).read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

soup.find("")

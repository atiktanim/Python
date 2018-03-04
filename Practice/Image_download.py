import random
import urllib.request
def download_web_image(url):
    name=random.randrange(1,1000)
    full_name=str(name)+".jpg"
    urllib.request.urlretrieve(url,full_name)
download_web_image("https://scontent.fmaa1-1.fna.fbcdn.net/v/t1.0-0/p526x296/23621524_2023860471230579_7560748806437641794_n.jpg?oh=c28aa25778e652b72510729b5cc81ded&oe=5AF08E9D")
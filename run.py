from pathlib import Path
from App import InstagramBot


if __name__ == "__main__":
    InstagramBot.driverpath = "./Driver/chromedriver.exe"
    insta = InstagramBot()
    insta.login()
    insta.do_like()
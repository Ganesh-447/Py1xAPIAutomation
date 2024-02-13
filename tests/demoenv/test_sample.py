from dotenv import load_dotenv
import os
def test():
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(username,password)
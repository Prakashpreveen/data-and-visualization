from dotenv import load_dotenv
import os
load_dotenv()

username = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
database = os.getenv('DATABASE')
port = os.getenv('PORT')
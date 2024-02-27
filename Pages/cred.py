import pickle
from pathlib import path 
import streamlit_authenticator as stauth
import os

names = ["Moses Jones","Quintor Ochieng"]
usernames = ["Mjones", "qochieng"]
passwords = ["abc123", "def123"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
  pickle.dump(hashed_passwords,file)




# credentials:
#   usernames:
#     jsmith:
#       email: jsmith@gmail.com
#       name: John Smith
#       password: abc # To be replaced with hashed password
#     rbriggs:
#       email: rbriggs@gmail.com
#       name: Rebecca Briggs
#       password: def # To be replaced with hashed password
# cookie:
#   expiry_days: 30
#   key: random_signature_key # Must be string
#   name: random_cookie_name
# preauthorized:
#   emails:
#   - qochieng88@gmail.com


#   hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
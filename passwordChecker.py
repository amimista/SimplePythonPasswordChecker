import requests
import time
import random

class passwordChecker:
  def __init__(self, password):
    self.password = password
    self.recommendedLength = 12
    self.recommendations = set()

  def checkAgainstCommonPasswords(self):
    # Check against the NordPass list of common passwords
    url = "https://nordpass.com/next/worst-passwords-list/2024/b2c/all.json"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
      # Get the list of common passwords
      commonPasswords = response.json()

      # Check if the user's password is in the list of common passwords
      for entry in commonPasswords:
        if self.password == entry["Password"]:
          self.recommendations.add("Your password is too common. Please choose a different password.")
          break
    else:
      print("Unable to retrieve common passwords. Please try again later.")

    # Check against the SecLists list of common passwords
    url = "https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
      # Get the list of common passwords
      commonPasswords = response.text.split("\n")

      # Check if the user's password is in the list of common passwords
      for entry in commonPasswords:
        if self.password == entry:
          self.recommendations.add("Your password is too common. Please choose a different password.")
          break
    # If the request was not successful, print an error message
    else:
      print("Unable to retrieve common passwords. Please try again later.")
  
  def checkFullPatterns(self):
    if self.password.isalpha():
      self.recommendations.add("Your password is only letters. Please include numbers and special characters.")
    if self.password.isdigit():
      self.recommendations.add("Your password is only numbers. Please include letters and special characters.")
    if self.password.isalnum():
      self.recommendations.add("Your password is only letters and numbers. Please include special characters.")
    if self.password.islower():
      self.recommendations.add("Your password is only lowercase. Please include uppercase letters.")
    if self.password.isupper():
      self.recommendations.add("Your password is only uppercase. Please include lowercase letters.")

  def printRecommendations(self):
    sort = sorted(self.recommendations)
    count = 1
    for recommendation in sort:
      print(str(count) + ". " + recommendation)
      count += 1
    if count == 0:
      print("Your password is secure.")
    else:
      print("Please update your password to be more secure.")

def createPassword():
  print("---------------------------------------- \n")
  print("Great! Let's get started.")
  print("Passwords are more secure when they are personal, long, and unique...")
  time.sleep(2)
  print("Here are some tips for creating a secure password:")
  print("1. Include a mix of letters, numbers, and special characters.")
  print("2. Avoid using common words or phrases.")
  print("3. Make it at least 12 characters long.")
  print("4. Use a passphrase or acronym to help you remember it.")
  print("5. Consider using a password manager to generate and store your passwords.\n")
  time.sleep(2)
  print("So why don't you try creating a new password now?")

  pet = input("What is the name of your first pet? ")
  number = input("What is your favorite number? This could be as simple as the number 12 (but it has to be two digits). ")
  special = ["*", "#", "@", "!", "&", "%", "$", "?", "+", "-"]
  print("Here! I've made a password for you: \n\n" + pet + number + special[random.randint(0, 9)])

    
  def checkPassword(self):
    if len(self.password) < self.recommendedLength:
      self.recommendations.add("Your password is too short. Please make it at least " + str(self.recommendedLength) + " characters.")
    
    self.checkAgainstCommonPasswords()
    self.checkFullPatterns()
    response = input("Do you want some recommendations for creating a secure password? (yes/no) ")
    if (response == "yes"): 
      self.createPassword()
    else:
      print("Please consider creating a more secure password in the future.")

if __name__ == "__main__":
    password = input("Please enter a password: ")
    checker = passwordChecker(password)
    checker.checkPassword()
    checker.printRecommendations()

    print ("As a reminder, all your passwords should be unique between accounts.")
    print("Thank you for using the password checker.")
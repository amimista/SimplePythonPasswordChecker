import requests

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
  

  def checkPassword(self):
    if len(self.password) < self.recommendendLength:
      self.recommendations.add("Your password is too short. Please make it at least " + str(self.recommendedLength) + " characters.")
    
    self.checkAgainstCommonPasswords()

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
    count = 0
    for recommendation in self.recommendations:
      print(count + ". " + recommendation)
      count += 1
    if count == 0:
      print("Your password is secure.")
    else:
      print("Please update your password to be more secure.")

    print ("As a reminder, all your passwords should be unique between accounts.")
    print("Thank you for using the password checker.")
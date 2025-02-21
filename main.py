# Author: Marcus Walker
# Date: 02/20/2025
# Description: This is the main file for the program. It will run the program and call the functions from the other files.

from passwordChecker import passwordChecker

def main():
  password = input("Please enter a password: ")
  checker = passwordChecker(password)
  checker.checkAgainstCommonPasswords()

main()
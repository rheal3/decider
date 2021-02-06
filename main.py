import inquirer
import random
import os
from termcolor import colored

def add_option(options_list:list):
    question = inquirer.prompt([inquirer.Text(name="option", message="Enter an option")])
    options_list.append(question["option"])
    os.system("clear")
    return options_list

options = []

os.system("clear")
print(f"Welcome Human. I am {colored('The Decider', 'red')}. \nEnter your options and I will decide.")

option = add_option(options)

print(f"Current options: {options}")

question = inquirer.prompt([inquirer.List(name="choice", choices=["ADD OPTION", "CHOOSE"])])


while question["choice"] != "CHOOSE":
    os.system("clear")
    print(f"Current options: {options}")
    option = add_option(options)
    print(f"Current options: {options}")
    question = inquirer.prompt([inquirer.List(name="choice", choices=["ADD OPTION", "CHOOSE"])])

os.system("clear")
print(f"It has been chosen: {colored(random.choice(options), 'red')}")
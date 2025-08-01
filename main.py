import os
import time
import requests
import colorama
from colorama import Fore, Style

# Initialize colorama for colored output
colorama.init()

# Project information
owner_name = "natrix"
github_url = "https://github.com/natrixdev"
requirements_url = "https://github.com/natrixdev/instagram-botter/blob/main/reqs.txt"
owner_repos = "https://github.com/natrixdev?tab=repositories"
howto_use = "https://github.com/natrixdev/instagram-botter/blob/main/README.md"
code_url = "https://github.com/natrixdev/instagram-botter/blob/main/main.py"

def set_console_title():
    """Set console title"""
    try:
        if os.name == 'nt':  # Windows
            os.system("title Instagram followers, likes and views botter.")
        else:  # Linux/Mac
            print("\033]0;Instagram followers, likes and views botter.\007", end='')
    except:
        pass

def check_account_exists(account_name):
    """Check if Instagram account exists"""
    try:
        url = f"https://www.instagram.com/{account_name}/"
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except:
        return False

def check_url_exists(url):
    """Check if URL exists"""
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except:
        return False

def likes_botter():
    """Handle likes botting functionality"""
    print(f"{Fore.CYAN}Likes Botter{Style.RESET_ALL}")
    url = input('Paste your instagram post url (your account needs to be public): ')
    
    if not check_url_exists(url):
        print(f"{Fore.RED}Cannot find the post{Style.RESET_ALL}")
        return
    
    print(f"{Fore.YELLOW}Note: This is a simulation. Actual botting may violate Instagram's terms of service.{Style.RESET_ALL}")
    likes_count = 0
    
    # Simulate likes (in reality, this would need proper Instagram API or automation)
    for i in range(10):  # Simulate 10 likes
        likes_count += 1
        print(f"{Fore.GREEN}{likes_count} likes processed{Style.RESET_ALL}")
        time.sleep(1)  # Simulate processing time

def views_botter():
    """Handle views botting functionality"""
    print(f"{Fore.CYAN}Views Botter{Style.RESET_ALL}")
    story_url = input("Please input your story URL (needs to be public and accessible): ")
    
    if not check_url_exists(story_url):
        print(f"{Fore.RED}Cannot find the story/account{Style.RESET_ALL}")
        return
    
    print(f"{Fore.YELLOW}Note: This is a simulation. Actual botting may violate Instagram's terms of service.{Style.RESET_ALL}")
    views_count = 0
    
    # Simulate views
    for i in range(15):  # Simulate 15 views
        views_count += 1
        print(f"{Fore.GREEN}{views_count} views processed{Style.RESET_ALL}")
        time.sleep(0.5)

def followers_botter():
    """Handle followers botting functionality"""
    print(f"{Fore.CYAN}Followers Botter{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Welcome to the followers botter for Instagram{Style.RESET_ALL}")
    print()
    print(f"{Fore.RED}Note: This feature is not available in this demo version.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Follower botting may violate Instagram's terms of service.{Style.RESET_ALL}")

def main():
    """Main function"""
    set_console_title()
    
    print(f"{Fore.MAGENTA}=== Instagram Botter ==={Style.RESET_ALL}")
    print(f"By: {owner_name}")
    print(f"GitHub: {github_url}")
    print()
    
    account_name = input("Account name? ")
    
    if account_name == "":
        print(f"{Fore.RED}Please input a real name{Style.RESET_ALL}")
        return
    
    if not check_account_exists(account_name):
        print(f"{Fore.RED}I didn't find your Instagram account{Style.RESET_ALL}")
        return
    
    print(f"{Fore.GREEN}Account found: {account_name}{Style.RESET_ALL}")
    print()
    print("Please choose a botter category:")
    print()
    print("[1] - Likes")
    print()
    print("[2] - Views")
    print()
    print("[3] - Followers")
    print()
    
    choice = input('> ')
    
    if choice == "1":
        likes_botter()
    elif choice == "2":
        views_botter()
    elif choice == "3":
        followers_botter()
    else:
        print(f"{Fore.RED}Invalid choice. Please select 1, 2, or 3.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
 

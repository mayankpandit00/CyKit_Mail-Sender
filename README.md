# CyKit Series  
## 9) Send Mails
A pthon program in cybersecurity kit series that send mail on your behalf without showing your password using OAUTH2.

### Requirements :
Python 3, cmd/terminal or any IDE (vscode or pycharm)

### Introduction : 

### Setup : 
1. Download Python 3 and IDE:
   1. https://www.python.org/downloads/ (python 3)
   2. https://www.jetbrains.com/pycharm/download/#section=windows (pycharm)
   3. https://code.visualstudio.com/download (vscode)

2. Set up OAUTH2: 
   1. Go to the Google Developers Console.
   2. Create a new project (or select an existing one).
   3. In the sidebar, navigate to APIs & Services -> Dashboard.
   4. Click on Enable APIs and Services.
   5. Search for "Gmail API" and click on it.
   6. Click the Enable button.
   7. Navigate to APIs & Services -> Credentials.
   8. Set up your OAuth consent screen with necessary information like application name, user support email, etc.
   9. Ensure that you've granted the the "https://www.googleapis.com/auth/gmail.send" scope in the OAuth consent screen for sending emails.
   10. Click on Create Credentials and select OAuth client ID.
   11. Choose the application type (typically "Desktop app" for this use case).
   12. Set a name for your OAuth client ID.
   13. Click Create.
   14. Download the credentials.json file.
   15. When you run your Python script for the first time, it will prompt you to authorize access to your Gmail account.
   16. Follow the authorization flow and grant the necessary permissions.

3. Download repository :
   1. On GitHub, navigate to the main page of the repository.
   2. Under the repository name, click Clone or Download.
   3. In the Clone with HTTPs section, click to copy the clone URL for the repository.
   4. Open Git Bash.
   5. Change the current working directory to the location where you want the cloned directory to be made.
   6. Alternatively, you can download its .zip file and store it to your desired location on the system.
   7. Fill all the [VALUE] sections of the code(s).

4. Run requirements.txt (if any): 
   1. Open terminal/Command Prompt
   2. Type the following code : pip install -r requirements.txt (Python 2) or pip3 install -r requirements.txt (Python 3)

5. Usage : 
   1. python send_mails.py
   2. Double click the .exe file (Social Engineering/Trojan)

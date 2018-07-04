This is a bot used by a large activist organization.

A few things are needed to start using the bot:
1. install the python libraries needed (sorry, still need to compile a list of what those are)
2. Save your voters as a csv to the project directory with columns/headers as follows:
    - Name
    - Street_Address
    - Apt_Number
    - Zip_Code
    - City
2. `cd <your-project-directory>`
3. `python3 setup.py`; follow the instructions that follow
4. Log into the subject email address and follow step 1 in the link below (no need to go past step 1).  Save the `client_secret.json` file to the secrets directory.
[gmail api instructions](https://developers.google.com/gmail/api/quickstart/python?authuser=3).
5. `python3 index.py` and follow the browser prompts that follow.
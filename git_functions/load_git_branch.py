import subprocess
import os
# Link to Branch List: https://github.com/CSUF-THETA/TrafficHelper/branches
ORIGIN = "https://github.com/Ramirez0245/Aurora_State_Web_App_Fast_API.git"  
BRANCH = input("Enter the branch you want to connect: ") # Set the branch you want to use/load.

def main():
    load_branch()

def load_branch():
    os.chdir(os.path.dirname(__file__))
    os.chdir('..')
    FETCH = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-m", '"Loading Branch"'],
        ["git", "remote", "add", "origin", ORIGIN],
        ["git", "fetch", "origin"],
        ]
    loop_actions(FETCH)
    
    MERGE = [
        ["git", "branch", BRANCH, f"origin/{BRANCH}", ],
        ["git", "checkout", BRANCH],
        ["git", "merge", f"origin/{BRANCH}"]
    ]
    loop_actions(MERGE)

def loop_actions(command):
    for actions in command:
        print(actions)
        result = subprocess.run(actions, shell=True, capture_output=True, text=True)
        print(result)
        print(type(result))
        print(result.stdout)    

if __name__ == '__main__':
    main()
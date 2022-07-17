import os
Folder = os.listdir("path")
 
list= []
for dosya in Folder:
        list.append(dosya)


path = os.getcwd()

for i in list:
    os.chdir("path+"+i)
    print(os.getcwd())
    os.system("""
                #!/bin/sh
                git filter-branch --env-filter '
                OLD_EMAIL=""
                CORRECT_NAME=""
                CORRECT_EMAIL=""
                if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
                then
                    export GIT_COMMITTER_NAME="$CORRECT_NAME"
                    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
                fi
                if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
                then
                    export GIT_AUTHOR_NAME="$CORRECT_NAME"
                    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
                fi
                ' --tag-name-filter cat -- --branches --tags
                """)
    os.system("git push --force --tags origin 'refs/heads/*'")
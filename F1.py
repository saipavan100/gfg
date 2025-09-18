# git rm --cached FILENAME (this removes file from stagged area ,go to untracking )

# git restore --staged FILENAME (this brings back the deleted file to stagging area from working directory)

# git rm FILENAME (this removes file in workspace as well as stagging area )
#         ----> git restore --staged FILENAME (this brings delted file to stagging )
#         ----> git restore FILENAME (this bring deleted file to working space but it need to be done after adding to staging)

# if file is deleted in stagging and commited as well then how ?
#         git rm FILENAME (this removed file from workingspace as well as stagging) and if we do 
#         commit it delete permentalty form stagging as well as local repo

#         Now if we want to restore , we need to do reset,Identify previous commit id
#         git reset commit_id -> (it brings back the deleted ones)
# heloo      
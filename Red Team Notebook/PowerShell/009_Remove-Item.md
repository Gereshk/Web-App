Remove-Item

Tuesday, October 24, 2023

8:49 PM

-   Aliases: del, rm, rmdir, erase, rd, ri

-   This would be the same as deleting a file or folder in your file explorer.

    -   Example: Remove-Item -Path \~/Desktop/emptyfile.txt

        -   This command will delete the file called emptyfile.txt from the current user\'s desktop

    -   Exmaple: Remove-Item -Path \~/Desktop/EmptyDirectory -Recurse

        -   This command will delete the directory EmptyDirectory from the current user\'s desktop

        -   We specify -Recurse to say if the directory has contents, delete everything within it.

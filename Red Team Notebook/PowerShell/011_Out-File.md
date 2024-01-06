Out-File

Sunday, October 29, 2023

9:10 PM

 

-   Example1: \'I want to add this string and overwrite everything\' \| Out-File \~/Desktop/myfile.txt

    -   You\'re seeing the first of example of a pipe \'\|\'

    -   We write the string and send the stdout down the pipe to the command.

    -   Out-File then receives the stdin and writes the contents to the file, overwriting everything.

        -   Note: Not all commands accept pipeline input.

-   Example2: \'I want to append this text to the end of the file\' \| Out-File \~/Desktop/myfile.txt -Append

    -   The stdout is passed down the pipeline to Out-File\'s stdin.

    -   Out-File \"appends\" the stdin to the end of the file in addition to existing content.

-   Example3: \'I want to overwrite everything in the file again\' \> \~/Desktop/myfile.txt

    -   Does the same thing as Example1

    -   The \> character means redirect stdout and overwrite everything with this text.

-   Example4: \'I want to add this text to the end of the file again\' \>\> \~/Desktop/myfile.txt

    -   Does the same thing as Example2

    -   The \>\> characters means redirect stdout to the end of the file in addition to existing content.

-   Example 5: cat \~/Desktop/File1.txt \> \~/Desktop/newfile.txt

    -   Recall, cat is an alias for Get-Content

    -   So, we\'re reading the file and redirecting stdout to newfile.txt

    -   So yes, you can combine commands together like this.

> * *

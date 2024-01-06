Find hidden files

Saturday, December 16, 2023

11:12 PM

 

-   cat a hidden file that shows blank

> ![](001_Find_hidden_files_000.png){width="5.0in" height="1.1666666666666667in"}

-   ls -il

-   find . -inum \[NUMBER\] -exec chmod 777 {} \\;

-   find . Inum \[NUMBER\] -exec cat {} \\;

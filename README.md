# Interactive Periodic Table using Python Tkinter and SQL
This program is an interactive periodic table made with pyhton tkinter. When you run the program a Graphical User Interface will pop up and show all the 118 elements in the periodic table and will be available for the user to click. When a certain button or tile is clicked, on the same screen the properties of that certain element will be displayed in a small frame. It also has a clear function if you want to go to the default look of the periodic table. The size of the GUI is not resizable and might be odd to some users who use a smaller screen. The program can be terminated using the exit button in the title bar.

## How to Use this Program
1. Download and install python.
2. Download the Interactive Periodic Table(IPT) folder from this repository.
3. Move it to a New Folder of your choice.
4. Run the Main.py file
5. Explore!

NOTE: The search function of this system uses a  mysql database as its source of data. The data for the periodic table and the search function needs to be separated because the order of elements that corresponds with the periodic table and the search function is different. If we insist on using the same list for both the periodic table and search function, the code would be redundant for each column of buttons made for the periodic table. To avoid redundancy inside the code and to make it more readable and shorter, we decided that an external database is necessary. To use an external database specifically the mysql database, your python bin should have a module for my sql connector to connect the python system and mysql. If you are using the latest version of python, my sql connector is pre installed in your system, if not then you can install it in your command prompt by typing the command "pip install mysql-connector-python". The uploaded version is connected to a database made with mysql benchwork, to be able to use it you need to recreate the mysql database, the sql script is provided along with the system file. Once you have recreated the database you need to change the password written in the code with the password of your sql installed. If you want to make it more easily accessible, you can use "phpMyAdmin" to create the database. Sqlite3 is also recommended.

## TEAM
    David, Jerson Noehl D.
    Gaite,Jhon Edward A.
    Hortal, Gian Carlo I.
    Pilapil, Brian Kenneth M.
    Quiroz, Charles Wayne M.

## Email us at
ilaogian000@gmail.com ||
lindowamamiya1412@gmail.com ||
jersonnoehldavid@yahoo.com

## References and tools
    https://www.rsc.org/periodic-table/ 
    https://www.w3schools.com/colors/colors_hexadecimal.asp
    https://www.python.org/
    https://www.youtube.com/watch?v=VMP1oQOxfM0&ab_channel=edureka%21
    https://code.visualstudio.com/
    https://www.mysql.com/
    https://www.w3schools.com/
    https://www.acs.org/
    https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&ab_channel=Codemy.com (Playlist)

## Other creations
Our team also created another periodic table using Procedural Programming be sure to check it out if you want. Here's the link to it.
Interactive_Periodic_TableV1: https://drive.google.com/drive/folders/1D2rxIA5uh1h1dHgrk0gAvEWz4Ftb6qLj?usp=share_link 


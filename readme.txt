This application is made for educational purposes.
The application is implemented using Python 3.8 and Docker-desktop.
The document-oriented MongoDB database is used

Requirements:
1. There are Docker-desktop (WindowsOS, WSL is also required) or Docker Compose (Linux OS).
2. Availability of ports 5000 and 27017 in a free state

Manual:
1. How to launch the solution
    1.1. First of all, you should clone the repository with this project to a local PC.
    1.2. You must open the project in any code editors (e.: VSCode, PyCharm or others).
    1.3. In the built-in terminal, run the "docker-compose.yml" and run the "docker-compose up" command in it.
    1.4. The "ihstask_mongodb" and "ihstask_web" images should be deployed and the "ihstask" container stack should start
2. How to fill the database
    2.1. At this stage, the database has already been formed and filled in, since it is filled in when the API is first launched.
    2.2. The database is filled completely randomly. The volume of the table to form by default is 100 records. This value can be changed in the file <settings.py>.
        2.2.1. The full name generator is used for the author's names. The number of authors is random (by default, in the range from 1 to 30, these parameters can be configured in the file <settings.py>
        2.2.2. The date is generated randomly according to the format: random year, random month, random day. The lower bound of the date (of the year) is the value from the file <settings.py >, upper - today
        2.2.3. The Lorem Ipsum random text generator is used to generate the paragraph texts.
        2.2.4. Each book is formed by a random author from the total number.
3. How to use the API
    3.1. You can view the result of the work at "http://localhost:5000". By default, the entire table of the created database will be unloaded on this page.
    3.2. At the address "http://localhost:5000/statistic" the results of the endpoint are displayed, statistics on the top 10 authors and a table for building a histogram (the number of books created by month) are uploaded
    3.3. For ease of reading, html templates were generated so that the data on the application page is uploaded to tables.
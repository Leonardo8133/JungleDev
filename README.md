# Jungle Dev Challenge

##### Article REST API built in django and django rest framework.


### [Link to the Documentation](https://documenter.getpostman.com/view/11867976/Tzz7Mx1M).

This API allows you to manage a set of articles and authors.
The title, category, summary, first paragraph and author are avaliable to public, but the full article body text required the user be authenticated to be accessed.

### Running the API

#### Requirements

• In order to run the API locally, you just need [Docker](https://docs.docker.com) installed.

#### Starting the server

> Once Docker is running, open a terminal and browse to the repository folder.

> Browse to the "/ArticlesApi" folder and run the command: ` docker compose up ` for build/start the database and server .

> If everything went fine, you should see This message: ` Your Server is Running `

> Access the API in "http://127.0.0.1:8000/" url while the server is running.

### Notes for testing the API.

> The .env file is available in the repository to simplify the testing process. 

> You can pre-populate the database (next Topic), avoiding manual data insertion.



### Pre populate the database

>  For Testing purpose, you can run a command for insert some data in your empty database.

>  While the servers are running, run the command in terminal:

>  ` docker compose exec app sh -c "python manage.py shell < ArticlesApi/utils/pre_populate_database.py"" `.

>  Once done, you can access the Django Admin with the (username: "admin", password: "admin") credentials.

>  Your database now have some articles and authors records automatcally created.





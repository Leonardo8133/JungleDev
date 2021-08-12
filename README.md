# Jungle Dev Challenge

### Article REST API built in django and django rest framework.


### [Link to the Documentation](https://documenter.getpostman.com/view/11867976/Tzz7Mx1M).

This API allows you to manage a set of articles and authors.
The title, category, summary, first paragraph and author are avaliable to public, but the full article body text required the user to be authenticated to be accessed.

### Running the API

> In order to run the API locally, you need [Docker](https://docs.docker.com) installed.

> Once Docker is running, clone the repository, open a terminal and browse to the repository folder.

> Browse to the "/ArticlesApi" folder and run the command ` docker compose up `.



### Pre populate the database

> For Testing purpose, you can run a command for insert some data in your empty database.

> In the terminal, run the command ` python manage.py shell < ArticlesApi/utils/pre_populate_database.py `

> Once done, you can access the Django Admin with the (username: "admin", password: "admin") credentials.

> Your database now have some articles and authors Records.




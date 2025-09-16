https://roadmap.sh/projects/broadcast-server

I used Django, Django Channels, Redis and Daphne in this project, so you will likely need to install them if you want to test it, all requirements needed included in requirements.txt which you can install by running the following command:
> pip install -r requirements.txt

I personally used Apidog to test it with the following url: ws://localhost:8000/ws/chat/

To run the server:
> daphne broadcast_server.asgi:application

To send a message you can send a JSON with a "message" field

You can run the following command in the terminal to notify the users that you are about to shut down the server:
> python manage.py utils

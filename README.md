# ShortLink

Clone a project and move to it:

    $ git clone https://github.com/Kouff/ShortLink.git
    $ cd ShortLink

Create a [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html#via-pip)
and [activate](https://virtualenv.pypa.io/en/latest/user_guide.html#activators) it and install the requirements:

    $ pip install -r requirements.txt

Create the file `.env` with virtual environments (see in `.env.example`):

    SECRET_KEY={secret}
    DEBUG={true|false}
    DB_NAME={name}
    DB_USER={user}
    DB_PASSWORD={password}
    DB_HOST={host}
    DB_PORT={port}

Migrate:

    $ python manage.py migrate

Run the server:

    $ python manage.py runserver

Create a short link: http://127.0.0.1:8000/

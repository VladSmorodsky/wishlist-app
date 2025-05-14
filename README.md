# wishlist-app

Wishlist App is a DRF application for storing and sharing wishes.
It's possible to:

- Login to the system
- Get wishes
- Get wish info
- Create a wish

## Setup

1. Clone the repo and go to the project root.
2. Create `.env` file from `.env.example` and set values:

- **`DJANGO_SECRET_KEY`**: Django secret key value
- **`DJANGO_DEBUG`**: Django Debug value. Can be True or False.
- **`ACCESS_TOKEN_TTL`**: JWT access token lifetime in number of minutes.
- **`REFRESH_TOKEN_TTL`**: JWT refresh token lifetime in number of days.
- **`DB_NAME`**: database name.
- **`DB_USER`**: database user.
- **`DB_PASSWORD`**: database user password.
- **`DB_HOST`**: database host.
- **`DB_PORT`**: database port.
- **`ALLOWED_HOST`**: list of available hosts. It should be string with comma separated values (e.g.
  `'test.com,test.domai.com'`).
- **`CELERY_BROKER_URL`**: Celery broker url.
- **`EMAIL_HOST`**: email host provider domain
- **`EMAIL_PORT`**: email port
- **`EMAIL_HOST_USER`**: host user's email
- **`EMAIL_HOST_PASSWORD`**: host user's password
- **`EMAIL_USE_TLS`**: use TLS connection (True or False)
- **`DEFAULT_FROM_MAIL`**: define from what email messages will be sent by default
- **`EMAIL_BACKEND`**: define django email backend to work with emails. Use next value for debug environment:
  `django.core.mail.backends.console.EmailBackend`

3. Run `docker-compose.yml` script:

```shell
docker compose up --build -d
```

4. To create a superuser for entering into django admin, run the next command:

```shell
docker compose run -it api make shell
```

And then run python commands for creating a superuser:

```python
from accounts.models import User

user = User(email="<superuser_email>", is_staff=True, is_superuser=True)
user.set_password("<superuser_password>")
user.save()
exit()
```

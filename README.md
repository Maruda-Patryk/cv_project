# CV_PROJECT

#### Run app:

```bash
docker-compose -f develop.docker-compouse up 
```

after build and run application you can go to swager for more infromation about the project: [swagger](http://0.0.0.0:8000/)

Project contain example data, which will load after first start with develop docker compose file

#### Envs:
- SQL_ENGINE: database engine (default django.db.backends.postgresql)
- SQL_NAME: database name (default: postgres)
- SQL_USER: database user (default: postgres)
- SQL_PASSWORD: database password (default: postgres)
- SQL_HOST: database host (default: db)
- SQL_PORT: database port (default: 5432)

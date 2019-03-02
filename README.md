# Bookstore

Bookstore is a simple application for buying books.
A user of application can create an account, and after login he has read access to books, and he is able to create an order.
The admin can manage of books and he can create another admin account.

This is a recruitment task.
The full task definition is available [here](doc/task.pdf)


# Pre installation

1. You need to install [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
1. You need to install [docker-compose](https://docs.docker.com/compose/install/)


# Build

1. Configure settings
    :information_source: You can skip this step. To simplify demo I added already configured `settings.json` file to repository.
    ```sh
    cp bookstore/config/settings_template.json bookstore/config/settings.json
    ```
    Open the `bookstore/config/settings.json` file and edit according to your needs.
    :warning: Edit this file only if you know what are you doing.

1. Configure settings
    :information_source: You can skip this step. To simplify demo I added already configured `secrets.json` file to repository.
    ```sh
    cp bookstore/config/secrets_template.json bookstore/config/secrets.json
    ```
    Open the `bookstore/config/secrets.json` file and fill all of the keys.
    :warning: If you don't know how to fill the file, please contact application creator @danielpiesik

1. Build docker image
    ```sh
    docker-compose -f local.yml build
    ```


# Run

1. Run container
    ```sh
    docker-compose -f local.yml up
    ```

1. The API is available on [http://localhost:8000](http://localhost:8000)

from initialize_database import CreateDatabases


def build():
    """Function to create databases from the invoke command
    """
    CreateDatabases().initialize_database()


if __name__ == "__main__":
    build()

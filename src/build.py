from initialize_database import CreateDatabases

def build():
    CreateDatabases().initialize_database()

if __name__ == "__main__":
    build()

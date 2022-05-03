class User:
    """Class for user object

    """

    def __init__(self, username, password, role):
        """Constructor that creates a user type object

        Args:
            username (string): username
            password (string): password
            role (string): role (employee/employer)
        """

        self.username = username
        self.password = password
        self.role = role

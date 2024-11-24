from database import Database  # Ensure this line is present


# user_model.py
class UserModel:
    """Represents a user in the system."""
    def __init__(self, user_id=None, username=None, name=None, password=None, email=None, contact_info=None, date_of_birth=None, gender=None):
        """
        Initializes a user_model instance.
        
        Args:
            user_id: Unique identifier for the user.
            username: Username of the user.
            name: Full name of the user.
            password: User's password (should be hashed).
            email: User's email address.
            contact_info: User's contact information.
        """
        self.user_id = user_id
        self.username = username  # Added username field
        self.name = name
        self.password = password  # Ensure this is stored securely
        self.email = email
        self.contact_info = contact_info
        self.date_of_birth = date_of_birth
        self.gender = gender
    def register(self):
        """Registers a new user in the database."""
        connection = Database.connect_db()
        if connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO USER (username, password, email, contact_info) VALUES (%s, %s, %s, %s)",
                           (self.name, 'default_password', f'{self.name}@example.com', self.contact_info))
            connection.commit()
            self.user_id = cursor.lastrowid
            cursor.close()
            connection.close()


    @staticmethod
    def fetch_user_by_username(username):
        """
    Fetches a user from the database by their username
    Args:
        username (str): The username of the user to be fetched.  
    Returns:
        UserModel or None: Returns a UserModel instance if found, otherwise None.
    """

        connection = Database.connect_db()
        user = None
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM USER WHERE username = %s", (username,))
            user_data = cursor.fetchone()
            if user_data:
                user = UserModel(
                    user_id=user_data[0],
                    username=user_data[1],
                    name=user_data[2],
                    password=user_data[3],  # Assuming password is stored in the database
                    email=user_data[4],
                    contact_info=user_data[5],
                    date_of_birth=user_data[6],
                    gender=user_data[7]
                )
            cursor.close()
            connection.close()
        return user
    
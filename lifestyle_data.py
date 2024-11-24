
class LifestyleData:
    """Represents lifestyle data collected from a user."""
    def __init__(self, lifestyle_data_id=None, user_id=None, collection_date=None, diet_info=None, exercise_info=None, sleep_info=None):
        """
        Initializes a lifestyle_data instance.
        
        Args:
            lifestyle_data_id: Unique identifier for the lifestyle data.
            user_id: ID of the user.
            diet_info: Information about the user's diet.
            exercise_info: Information about the user's exercise habits.
        """

        self.lifestyle_data_id = lifestyle_data_id
        self.user_id = user_id
        self.collection_date = collection_date
        self.diet_info = diet_info
        self.exercise_info = exercise_info
        self.sleep_info = sleep_info

    def collect_data(self):
        """Simulates collecting lifestyle data."""
        print("Collecting lifestyle data...")
        self.diet_info = "vegetarian"
        self.exercise_info = "daily running"
        self.sleep_info = "7 hours"
        print("Lifestyle data collected")

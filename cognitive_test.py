class CognitiveTest:
     """Represents a user in the system."""
     def __init__(self, test_id=None, user_id=None, test_type=None, score=None, date_taken=None):
         """
        Initializes a cognitive_test instance.
        
        Args:
            test_id: Unique identifier for the test.
            user_id: ID of the user taking the test.
            test_type: Type of cognitive test.
            score: Score obtained in the test.
        """

         self.test_id = test_id
         self.user_id = user_id
         self.test_type = test_type
         self.score = score
         self.date_taken = date_taken

     def administer_test(self):
        print("Administering cognitive test...")
        self.score = 95.0  # Placeholder score
        print("Cognitive test administered")

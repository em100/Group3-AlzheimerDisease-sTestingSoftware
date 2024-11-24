class GeneticData:
    """Represents genetic data collected from a user."""

    def __init__(self, genetic_data_id=None, user_id=None, collection_date=None, genetic_markers=None):
        """
        Initializes a genetic_data instance.
        
        Args:
            genetic_data_id: Unique identifier for the genetic data.
            user_id: ID of the user.
            genetic_markers: Genetic markers collected.
        """
        self.genetic_data_id = genetic_data_id
        self.user_id = user_id
        self.collection_date = collection_date
        self.genetic_markers = genetic_markers

    def collect_data(self):
        """Simulates collecting genetic data."""
        print("Collecting genetic data...")
        self.genetic_markers = "APOE4"
        print("Genetic data collected")

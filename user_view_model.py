
from user_model import UserModel
from cognitive_test import CognitiveTest
from genetic_data import GeneticData
from lifestyle_data import LifestyleData

# user_view_model.py
class UserViewModel:
    def __init__(self):
        self.user = None

    def register_user(self, name, date_of_birth, gender, contact_info):
        self.user = UserModel(name=name, date_of_birth=date_of_birth, gender=gender, contact_info=contact_info)
        self.user.register()

    def submit_cognitive_test(self, test_type, date_taken):
        if self.user:
            cognitive_test = CognitiveTest(test_type=test_type, date_taken=date_taken)
            cognitive_test.administer_test()
            self.user.submit_cognitive_test(cognitive_test)

    def submit_genetic_data(self, genetic_markers, collection_date):
        if self.user:
            genetic_data = GeneticData(genetic_markers=genetic_markers, collection_date=collection_date)
            genetic_data.collect_data()
            self.user.submit_genetic_data(genetic_data)

    def submit_lifestyle_data(self, diet_info, exercise_info, sleep_info, collection_date):
        if self.user:
            lifestyle_data = LifestyleData(diet_info=diet_info, exercise_info=exercise_info, sleep_info=sleep_info, collection_date=collection_date)
            lifestyle_data.collect_data()
            self.user.submit_lifestyle_data(lifestyle_data)

    def view_results(self):
        if self.user:
            return self.user.view_results()

    def get_all_users(self):
        return UserModel.fetch_all_users()
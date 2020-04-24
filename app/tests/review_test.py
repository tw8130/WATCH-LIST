import unittest
from app.models import Review
Review = review.Review

class TestReview(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Review class
    '''


    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_review = Review(12345,'Review for movies',"https://image.tmdb.org/t/p/w500/jdjdjdjn",'This movie is the best thing since sliced bread')


    def tearDown(self):
        Review.clear_reviews()

    def test_instance(self):
        '''
        test case that uses the isinstance() to check if object is an instance of review class
        '''
        self.assertTrue(isinstance(self.new_review,Review))


    def test_check_instance_variables(self):
        '''
        test that uses self.assertEqual to check for the expected  review results
        '''
        self.assertEquals(self.new_review.movie_id,12345)
        self.assertEquals(self.new_review.title,'Review for movies')
        self.assertEquals(self.new_review.imageurl,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_review.review,'This movie is the best thing since sliced bread')


    def test_save_review(self):
        '''
        test that calls save_review() method to save our review objects
        '''
        self.new_review.save_review()
        self.assertTrue(len(Review.all_reviews)>0)

# if __name__ == '__main__':
#     unittest.main()
class Review:
    '''
    Class that generates new instances of reviews
    '''
    #class variable
    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        '''
        helps us define properties for review objects
        '''

        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        '''
        appends review object to the class variable
        '''
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        '''
        clears all the items from list
        '''
        Review.all_reviews.clear()
    
    @classmethod
    def get_reviews(cls,id):
        '''
        method that displays all the reviews for a particular movie
        '''

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response
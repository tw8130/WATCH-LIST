from . import db
# from werkzeug.security import generate_password_hash,check_password_hash
class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count



class Review:

    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response

class User(db.Model):
    '''
    User class to create new users
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)#id column
    username = db.Column(db.String(255))#user column
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))#role column
    pass_secure = db.Column(db.String(255))#password column

    # @property#create a write only class property password
    # def password(self):
    #         raise AttributeError('You cannot read the password attribute')#block access to password property

    # @password.setter
    # def password(self, password):
    #         self.pass_secure = generate_password_hash(password)


    # def verify_password(self,password):
    #         return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'#make it easier to debug our application

class Role(db.Model):
    '''
    Role class to create roles for our users
    '''
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)#id column
    name = db.Column(db.String(255))#name column
    users = db.relationship('User',backref = 'role',lazy="dynamic")#create virtual column to connect with foreign key

    def __repr__(self):
        return f'User {self.name}'
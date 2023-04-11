"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


import os
from unittest import TestCase
from sqlalchemy import exc

from models import db, User, Message, Follows


# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        db.drop_all()
        db.create_all()

        user1 = User.signup("user1","user1@gmail.com", "user123", "","","","")
        user2 = User.signup("user2","user2@gmail.com", "user231",  "","","","")
       

        db.session.commit()
        user1 = db.session.query(User).filter(User.username=="user1").first()
        user2 = db.session.query(User).filter(User.username=="user2").first()
        
        self.user1 = user1
        self.user1_id = user1.id
        self.user2 = user2
        self.user2_id = user2.id
        
        
        self.client = app.test_client()
    
    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res

    def test_user_model(self):
        """Does basic model work?"""

        u = User.signup(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD",
            image_url="",
            header_image_url="",
            bio="",
            location=""
        )

        db.session.add(u)
        db.session.commit()

        # User should have no messages & no followers
        self.assertEqual(len(u.messages), 0)
        self.assertEqual(len(u.followers), 0)

       
    def test_userfollows(self):
        self.user1.following.append(self.user2)
        db.session.commit()
        # user 1 following user 2
        self.assertEqual(len(self.user2.following), 0)
        self.assertEqual(len(self.user2.followers), 1)
        self.assertEqual(len(self.user1.followers), 0)
        self.assertEqual(len(self.user1.following), 1)
        self.assertEqual(self.user2.followers[0].id, self.user1.id)
        self.assertEqual(self.user1.following[0].id, self.user2.id)
        

    def test_is_following(self):
        self.user1.following.append(self.user2)
        db.session.commit()

        self.assertTrue(self.user1.is_following(self.user2))
        self.assertFalse(self.user2.is_following(self.user1))
    
    def test_is_notfollowing(self):
        self.user2.following.append(self.user1)
        db.session.commit()

        self.assertTrue(self.user2.is_following(self.user1))
        self.assertFalse(self.user1.is_following(self.user2))

    def test_isfollowedby(self):
        self.user1.following.append(self.user2)
        db.session.commit()

        self.assertTrue(self.user2.is_followed_by(self.user1))
        self.assertFalse(self.user1.is_followed_by(self.user2))
    
    def test_is_notfollowedby(self):
        self.user2.following.append(self.user1)
        db.session.commit()

        self.assertTrue(self.user1.is_followed_by(self.user2))
        self.assertFalse(self.user2.is_followed_by(self.user1))

    def test_valid_signup(self):
        user = User.signup("usertest", "usertest@gmail.com", "usertest",  "","","","")
        db.session.commit()
        user = db.session.query(User).filter(User.username=="usertest").first()
        
        
        self.user = user
        self.user_id = user.id

        user = User.query.get(user.id)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "usertest")
        self.assertIsNotNone(user.username, "")
        self.assertIsNotNone(user.email, "")
        self.assertEqual(user.email, "usertest@gmail.com")
        self.assertNotEqual(user.password, "usertest")
        self.assertIsNotNone(user.password, "")

    def test_user_authentication(self):
        user = User.authenticate(self.user1.username, "password")
        self.assertIsNotNone(user)
       
    
    def test_invalid_username(self):
        self.assertFalse(User.authenticate("test1user", "password"))

    def test_wrong_password(self):
        self.assertFalse(User.authenticate(self.user1.username, "test1password"))


        
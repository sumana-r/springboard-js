"""Message View tests."""

# run these tests like:
#
#    FLASK_ENV=production python -m unittest test_message_views.py


import os
from unittest import TestCase
from bs4  import BeautifulSoup

from models import db, connect_db, Message, User, Likes, Follows

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app, CURR_USER_KEY

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


app.config['WTF_CSRF_ENABLED'] = False


class UserViewTestCase(TestCase):
    """Test views for users."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()

        self.client = app.test_client()

        self.testuser = User.signup(username="testuser",
                                    email="test@test.com",
                                    password="testuser",
                                    image_url=None,
                                    header_image_url=None,
                                    bio=None,
                                    location=None
                                    )
        user1 = User.signup("user1","user1@gmail.com", "user123", None,None,None,None)
        user2 = User.signup("user2","user2@gmail.com", "user231", None,None,None,None)
        user3 = User.signup("user3","user3@gmail.com", "user321",  None,None,None,None)
        user4 = User.signup("user4","user4@gmail.com", "user432",   None,None,None,None)
       
        user5 = User.signup("user5","user5@gmail.com", "user543",  None,None,None,None)
        user6 = User.signup("user6","user6@gmail.com", "user654",   None,None,None,None)
       
       

        db.session.commit()
        user1 = db.session.query(User).filter(User.username=="user1").first()
        testuser = db.session.query(User).filter(User.username=="testuser").first()
        user2 = db.session.query(User).filter(User.username=="user2").first()
        user1 = db.session.query(User).filter(User.username=="user1").first()
        testuser = db.session.query(User).filter(User.username=="testuser").first()
        user3 = db.session.query(User).filter(User.username=="user3").first()
        user4 = db.session.query(User).filter(User.username=="user4").first()
        user5 = db.session.query(User).filter(User.username=="user5").first()
        user6 = db.session.query(User).filter(User.username=="user6").first()
        
        self.user1 = user1
        self.user1_id = user1.id
        self.user2 = user2
        self.user2_id = user2.id
        self.testuser = testuser
        self.testuser_id = testuser.id
        self.user3 = user3
        self.user3_id = user3.id
        self.user4 = user4
        self.user4_id = user4.id
        self.user5 = user5
        self.user5_id = user5.id
        self.user6 = user6
        self.user6_id = user6.id

  
    def setup_follows(self):
        follower1 = Follows(user_being_followed_id=self.user1_id, user_following_id=self.testuser_id)
        follower2 = Follows(user_being_followed_id=self.user2_id, user_following_id=self.testuser_id)
        follower3 = Follows(user_being_followed_id=self.testuser_id, user_following_id=self.user1_id)

        db.session.add_all([follower1,follower2,follower3])
        db.session.commit()

    def test_loggeduser_follower(self):
        """user logged In and see follower page"""
       
        self.setup_follows()
        with self.client as c:
            resp = c.get(f"/users/{self.testuser_id}")
            parsed_data = BeautifulSoup(resp.data)  
            parsed_data.select("#following")         

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(parsed_data.select("#following")[0].text, '2')
            self.assertEqual(parsed_data.select("#follower")[0].text, '1')

            
    def test_logged_message_follower(self):
        """user logged In and see follower page"""
       
        self.setup_follows()
        with self.client as c:
            resp = c.post(f"/messages/new", data={"text": "Test Message"})
            self.assertEqual(resp.status_code, 302)

            msg = Message.query.one()
            self.assertEqual(msg.text, "Test Message") 



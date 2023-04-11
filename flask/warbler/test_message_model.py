import os
from unittest import TestCase
from sqlalchemy import exc

from models import db, User, Message, Follows, Likes


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
class MessageModelTestCase(TestCase):
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

    def test_message_model(self):
             
        msg = Message(
            text="user test message",
            user_id=self.user1.id
            
        )
        db.session.add(msg)
        db.session.commit()
        self.assertEqual(len(self.user1.messages), 1)
        self.assertEqual(self.user1.messages[0].text, "user test message")
        self.assertNotEqual(len(self.user1.messages), 0)
        self.assertNotEqual(self.user1.messages[0].text, "user1 test message")
    
    def test_message_likes(self):
        msg = Message(
            text="user test message",
            user_id=self.user1.id
        )

        mesg = Message(
            text="user test message2",
            user_id=self.user1.id
        )

        user = User.signup("test3", "test3@gmail.com", "test3psd", "", "", "", "")
        
        self.user = user
        self.user_id = user.id
        db.session.add_all([msg, mesg, user])
        db.session.commit()

        user.likes.append(msg)

        db.session.commit()

        like = Likes.query.filter(Likes.user_id == user.id).all()
        self.assertEqual(len(like), 1)
        self.assertEqual(like[0].message_id, msg.id)
        self.assertNotEqual(len(like), 0)
        self.assertNotEqual(like[0].message_id, mesg.id)
    
    
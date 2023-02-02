from unittest import TestCase
from app import app
from models import db, User, Post
from datetime import date

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sqla_intro_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()



class UserListTestCase(TestCase):
    """Tests for views for Pets."""

    def setUp(self):
        """Add sample pet."""

        User.query.delete()

        user = User(first_name='Nancy', last_name="John", image_url="https://www.pngfind.com/pngs/m/470-4703547_icon-user-icon-hd-png-download.png")
        db.session.add(user)
        db.session.commit()
        self.user_id = user.id
        self.client = app.test_client()
        app.config['TESTING'] = True
            

    def test_home_page(self):
         with  self.client :
            resp = self.client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code,200)
            self.assertIn('<h1> Users</h1>',html)
            self.assertIn('<a href = "/users/new" ><button type="button" name="adduser">Add user</button>',html)

    def test_adduser_page(self):
       
       with  self.client :
            resp = self.client.get('/users/new')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code,200)
            self.assertIn('<input name = "image" type = "url" placeholder="Provide an image of this user"/>',html)
            self.assertIn('<input name = "lname" type = "text" placeholder="Enter a last name"/>',html)

    def test_addeduser_page(self):
       
       with  self.client :
            sent = {"fname":"FTest1","lname":"LTest1","image":"https://www.pngfind.com/pngs/m/470-4703547_icon-user-icon-hd-png-download.png"}
            resp = self.client.post('/users/new',data = sent, follow_redirects=True)
            self.assertEqual(resp.status_code,200)

    def test_deleteuser_page(self):
       
       with  self.client :
            sent = {"fname":"FTest1","lname":"LTest1","image":"https://www.pngfind.com/pngs/m/470-4703547_icon-user-icon-hd-png-download.png"}
            resp = self.client.post(f"/users/{self.user_id}/delete",data = sent, follow_redirects=True)
            self.assertEqual(resp.status_code,200)


class PostTestCase(TestCase):
    """Tests for views for Pets."""

    def setUp(self):
        """Add sample pet."""

        Post.query.delete()

        post = Post(title='test title', content="test content", created_at = date.today(), user_id =100)
        db.session.add(post)
        db.session.commit()
        self.post_id = post.id
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_addedpost_page(self):
       
       with  self.client :
            sent = {"title":"test title", "content":"test content", "created_at" : date.today(), "user_id":101}
            resp = self.client.post(f'/users/{self.user_id}/posts/new',data = sent, follow_redirects=True)
            self.assertEqual(resp.status_code,200)
            
            
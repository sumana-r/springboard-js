from unittest import TestCase
from app import app



class BloglyTestCase(TestCase):
    def setUp(self):
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
            resp = self.client.post(f"/users/{18}/delete",data = sent, follow_redirects=True)
            self.assertEqual(resp.status_code,200)
            
            
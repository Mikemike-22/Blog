import unittest
from app.models import Blog,Comment
from app import db
from datetime import datetime

class CommentsTest(unittest.TestCase):
    def setUp(self):
        self.new_blog = Blog(id=40, title='New Blog', content='This is the content', category ='Travel', posted=datetime.now())
        self.new_comment = Comment(name='Test Comment', comment='This is my Test comment',blog=new_blog)

    def tearDown(self):
        db.session.delete(self.new_blog)
        db.session.commit()
        db.session.delete(self.new_comment)
        db.session.commit()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.name,'Test Comment')
        self.assertEquals(self.new_comment.comment,'This is my Test comment')
        self.assertEquals(self.new_comment.blog, new_blog)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(1000))
    name = db.Column(db.String)
    blog = db.Column(db.Integer,db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,blog):
        comments = Comment.query.filter_by(blogit = blog).all()
        return comments

    @classmethod
    def delete_comment(cls,id):
        comment = Comment.query.filter_by(id=id).first()
        db.session.delete(comment)
        db.session.commit()

    def __repr__(self):
        return f'Comment{self.comment}'

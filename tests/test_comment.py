import unittest
from app.models import Pitch, User, Comment
from app import db

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(pitch_content = "pitch one", pitch_category='Business')
        self.new_comment = Comment(comment_content = "One comment", pitch=self.new_pitch)
    
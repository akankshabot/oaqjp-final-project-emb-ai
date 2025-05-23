import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        response = emotion_detector("I am glad this happened")
        assert response['dominant_emotion'] == "joy"

    def test_anger(self):
        response = emotion_detector("I am really mad about this")
        assert response['dominant_emotion'] == "anger"
    
    def test_disguise(self):
        response = emotion_detector("I feel disgusted just hearing about this")
        assert response['dominant_emotion'] == "disgust"
    
    def test_sadness(self):
        response = emotion_detector("I am so sad about this")
        assert response['dominant_emotion'] == "sadness"

    def test_fear(self):
        response = emotion_detector("I am really afraid that this will happen")
        assert response['dominant_emotion'] == "fear"

unittest.main()
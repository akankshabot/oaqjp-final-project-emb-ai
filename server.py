''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask,render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows different kind of emotion score and the dominant_emotion 
        for the provided text.
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return f"For the given statement, the system response is 'anger' : {response['anger']} , \
        'disgust': {response['disgust']}, 'fear': {response['fear']},'joy':{response['joy']} and 'sadness': {response['sadness']}.\
         The dominant emotion is {response['dominant_emotion']} "

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

"""
This script runs emotion detection app
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detection App")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_det():
    """
    Detection emotion for given string.
    """
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is 'anger': {response['anger']}, " \
    f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} " \
    f"and 'sadness': {response['sadness']}. The dominant emotion is " \
    f"{response['dominant_emotion']}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import av
import cv2
import requests
from io import BytesIO
import time

st.set_page_config(page_title='Real-Time Emotion Detector', layout='centered')
st.markdown(
'''
<div style='text-align: center; font-size: 3em; font-weight: bold; margin: 0.1em 0'>Moodlens</div>
<p style='text-align: center;'>Moodlens knows your emotions based on your face</p>
''',
unsafe_allow_html=True,
)

API_URL = 'https://moodlens-qavb.onrender.com/detect'

# Initialize session state
if 'emotion' not in st.session_state:
    st.session_state.emotion = 'no face detected'
if 'score' not in st.session_state:
    st.session_state.score = 0.0

# Video processing class
class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.frame_count = 0
        self.latest_emotion = "no face detected"
        self.latest_score = 0.0

    def recv(self, frame):
        img = frame.to_ndarray(format='bgr24')
        
        # Process every 10th frame
        self.frame_count += 1
        if self.frame_count % 40 == 0:
            # Convert image to bytes
            _, buffer = cv2.imencode('.jpg', img)
            io_buf = BytesIO(buffer)
            io_buf.seek(0)
            
            # Send to API
            try:
                files = {'file': ('image.jpg', io_buf, 'image/jpeg')}
                response = requests.post(API_URL, files=files)
                
                if response.status_code == 200:
                    result = response.json()
                    print(f"Got result: {result}")
                    # Update session state
                    self.latest_emotion = result['emotion']
                    self.latest_score = result['score']
            except Exception as e:
                print(f"API Error: {e}")
        
        return av.VideoFrame.from_ndarray(img, format='bgr24')

# Create a container for the display
display_container = st.container()

# Display webcam stream
webrtc_ctx = webrtc_streamer(
    key='emotion-detector',
    video_processor_factory=VideoTransformer,
    rtc_configuration={'iceServers': [{'urls': ['stun:stun.l.google.com:19302']}]},
    media_stream_constraints={'video': True, 'audio': False},
)

# Display current emotion and score
with display_container:
    if webrtc_ctx.video_processor is not None:
        emotion = webrtc_ctx.video_processor.latest_emotion
        score = webrtc_ctx.video_processor.latest_score
        st.markdown(
            f"""
            <div style='text-align: center;'>
            <div style='font-size: 1.5em; margin:0; padding:0'>Current Emotion</div>
            <div style='font-size:2em; font-weight:bold; text-align: center;'>{emotion}</div>
            </div>
            """,
            unsafe_allow_html=True,
            )
    else:
        st.markdown(
            f"""
            <div style='text-align: center;'>
            <div style='font-size: 1.5em; margin:0; padding:0'>Current Emotion</div>
            <div style='font-size:2em; font-weight:bold; text-align: center;'>no face detected</div>
            </div>
            """,
            unsafe_allow_html=True,
            )

# Rerun the app periodically to update the UI
if webrtc_ctx.state.playing:
    time.sleep(2)  # Add a small delay to prevent too frequent updates
    st.rerun()

# Moodlens: Real-Time Facial Emotion Detection

Moodlens is a real-time facial emotion detection app built with Streamlit and Python. It uses your webcam to detect your current emotion and displays it live in the browser.

## Features

- Real-time emotion detection from your webcam
- Clean, centered UI
- No audio/microphone access required
- Easy to run locally

---

## Requirements

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- [Git](https://git-scm.com/)

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/moodlens.git
   cd moodlens
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install backend dependencies:**

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. **Install frontend dependencies:**

   ```bash
   cd ../frontend
   pip install -r requirements.txt
   ```

---

## Running the App

1. **Start the backend (FastAPI):**

   ```bash
   cd backend
   uvicorn main:app --reload
   ```

2. **Start the frontend (Streamlit):**

   Open a new terminal window/tab, then:

   ```bash
   cd frontend
   streamlit run app.py
   ```

3. **Open your browser and go to:**

   ```
   http://localhost:8501
   ```

---

## Usage

- Allow webcam access when prompted.
- Your current emotion will be displayed in real time.
- No audio is recorded or transmitted.

---

## Troubleshooting

- If you see "no face detected," make sure your webcam is working and you are well-lit.
- If you get errors about missing packages, make sure you've installed both backend and frontend dependencies.
- If you change the backend port, update `API_URL` in `frontend/app.py`.

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## License

[MIT](LICENSE)

---

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [streamlit-webrtc](https://github.com/whitphx/streamlit-webrtc)
- [OpenCV](https://opencv.org/)
- [FastAPI](https://fastapi.tiangolo.com/) 
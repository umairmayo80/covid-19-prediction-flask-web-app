# COVID-19 Prediction Web App

This is a web-based Flask application that utilizes machine learning to predict COVID-19 infection using chest X-ray images. The application is designed to help users quickly assess the likelihood of COVID-19 based on the X-ray image analysis.

## Getting Started

To run the Flask-based COVID-19 Prediction Web App, follow the instructions below:

### Prerequisites

- Python 3.7 or higher
- Anaconda environment (optional but recommended)

### Installation

1. Clone this GitHub repository to your local machine by running the following command in your terminal or command prompt:
   ```
   git clone https://github.com/your_username/COVID-19-Prediction-Web-App.git
   ```

2. (Optional but recommended) Create a virtual environment using Anaconda or venv to isolate the dependencies. Activate the virtual environment.

3. Create the conda environment with the required dependencies using the provided `environment.yml` file. Navigate to the project directory and run the following command:
   ```
   conda env create -f environment.yml
   ```

### Run the Web App

1. Activate the conda environment (if you created one) using the following command:
   ```
   conda activate your_env_name
   ```

2. Navigate to the project directory containing the Flask application.

3. Run the following command to start the Flask web app:
   ```
   python app.py
   ```

4. The COVID-19 Prediction Web App will be up and running at `http://localhost:5000/`.

### How to Use

1. Access the web app through your web browser at `http://localhost:5000/`.

2. Upload a chest X-ray image using the provided interface.

3. Click the "Predict" button to obtain the COVID-19 prediction for the uploaded image.

4. The web app will display the prediction result as "COVID-19 Positive" or "COVID-19 Negative".

### Note

- The COVID-19 prediction accuracy depends on the quality and quantity of the dataset used for training the machine learning model. The model's performance is subject to its training data and may not be entirely accurate in real-world scenarios. This application is intended for educational and experimental purposes and should not be used as a definitive diagnostic tool.

- Always consult with healthcare professionals for accurate COVID-19 diagnosis and follow appropriate testing and safety guidelines.

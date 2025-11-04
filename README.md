# NetworkSecurity – Phishing Detection & Batch‑Prediction Pipeline
_A batch inference & retraining system for phishing website detection_

## 📘 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Architecture & Design](#architecture--design)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Training & Inference Flow](#model-training--inference-flow)
- [Deployment](#deployment)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## About the Project
This project implements an end‑to‑end machine‑learning pipeline for detecting phishing websites. It provides:
- Automated **data ingestion** from a MongoDB collection.
- Preprocessing, model training and saving of artifacts (preprocessor + classifier).
- A batch prediction API where you upload a CSV of website features, and the system returns predictions for each row.
- Integration with a REST API (via FastAPI) and support for containerization via a `Dockerfile`.

The aim is to showcase how a real‑world phishing‑detection pipeline can be designed, packaged, and deployed — making it relevant for data science / ML engineering roles.

---

## Features
- ✅ Batch prediction: upload CSV → get output CSV + predictions.
- ✅ Model retraining endpoint: trigger full pipeline from data ingestion → train → save artifacts.
- ✅ Schema‑based validation: ensures input data conforms to expected columns & types via `data_schema/`.
- ✅ Modular codebase: separation of ingestion, transformation, training, inference for clarity and maintainability.
- ✅ Containerized setup: with `Dockerfile`, enabling reproducible deployment.

---

## Architecture & Design
```
[MongoDB]  ← data ingestion →  [data_ingestion collection]
                     ↓
           [data_schema] → validate → [data_transformation]
                     ↓
          [model_training] → save preprocessor.pkl & model.pkl
                     ↓
   [REST API (FastAPI)]  ← upload CSV → load artifacts → batch prediction → output
```

---

## Getting Started

### Prerequisites
- Python 3.8+ (recommended)
- MongoDB connection string (set in environment variable `MONGODB_URL_KEY`)
- `git` and optionally `docker` if you plan to containerize

### Installation
```bash
git clone https://github.com/Asad22Khan/networksecurity.git
cd networksecurity
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
# .venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### Add environment variables
Create a `.env` file at the root directory:
```
MONGODB_URL_KEY=your_mongo_connection_string
```

---

## Usage

### Train the model via API
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```
Then open in browser:
```
http://localhost:8000/train
```
This will trigger the training pipeline and save artifacts under `final_model/`.

### Run batch prediction via API
Upload a CSV file via the endpoint:
```
POST http://localhost:8000/predict
```
The response returns an HTML table of results and writes `prediction_output/output.csv`.

---

## Project Structure
```
networksecurity/
├── data_schema/                # JSON schemas for input validation
├── Network_Data/               # Raw or ingested data folder
├── final_model/                # Output folder: preprocessor.pkl + model.pkl
├── prediction_output/          # Inference output CSVs
├── templates/                  # Jinja2 templates for API response
├── valid_data/                 # Validated incoming data
├── app.py                      # FastAPI app: training + prediction endpoints
├── push_data.py                # Script to push new data (ingestion)
├── requirements.txt            # Dependencies
├── Dockerfile                  # For containerizing the application
├── setup.py                    # Package installation config
├── README.md                   # Project overview (you are here)
└── ...                         # Other modules (utils, pipeline, logging, exception)
```

---

## Model Training & Inference Flow
1. **Data Ingestion**: Reads from MongoDB collection.
2. **Data Validation & Preprocessing**: Ensures format and applies transformations.
3. **Model Training**: Trains and saves preprocessor & model.
4. **Serving / Inference**: Loads artifacts and performs batch predictions.
5. **Persistence & Output**: Saves predictions to `prediction_output/output.csv`.

---

## Deployment

### Containerization
```bash
docker build -t networksecurity-app .
docker run -p 8000:8000 --env MONGODB_URL_KEY="your_mongo_url" networksecurity-app
```

### Production Hosting
Deploy using any cloud service (AWS, GCP, Azure, Hugging Face Spaces).  
Ensure environment variables are configured.

---

## Future Enhancements
- [ ] Add real‑time prediction endpoint.
- [ ] Integrate model versioning and CI/CD pipeline.
- [ ] Front‑end UI with Streamlit.
- [ ] Automated feature engineering & monitoring.

---

## Contributing
Contributions are welcome!  
1. Fork the repo.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Submit a pull request.

---

## License
This project is licensed under the **MIT License**.


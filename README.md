# Insurance Premium Prediction

A machine learning-powered web application that predicts insurance premium categories based on user health and lifestyle data.

## Features

- **ML-based Prediction**: Uses a trained scikit-learn model to classify insurance premiums into categories (low, medium, high)
- **FastAPI Backend**: RESTful API with automatic validation and documentation
- **Streamlit Frontend**: Interactive web interface for easy predictions
- **Feature Engineering**: Automatic computation of BMI, lifestyle risk, age group, and city tier

## Project Structure

```
Insurance_Price_Prediction/
├── app.py                 # FastAPI application
├── frontend.py            # Streamlit web interface
├── insurance.csv          # Training dataset
├── ml_model.ipynb         # Model training notebook
├── req.txt                # Python dependencies
├── config/
│   └── city_list.py       # City tier classifications
├── model/
│   ├── model.pkl          # Trained ML model
│   └── predict.py         # Prediction logic
└── schema/
    ├── user_input.py      # Input validation schema
    └── prediction_response.py  # Response schema
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/saai07/Insurance_Price_Prediction.git
   cd Insurance_Price_Prediction
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     env\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source env/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r req.txt
   ```

## Usage

### Start the Backend Server

```bash
uvicorn app:app --reload
```

The API will be available at `http://127.0.0.1:8000`

### Start the Frontend

In a new terminal:

```bash
streamlit run frontend.py
```

The web interface will open at `http://localhost:8501`

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Welcome message |
| `/health` | GET | Health check and model status |
| `/predict` | POST | Predict insurance premium category |

### Prediction Request Example

```json
{
  "age": 30,
  "weight": 70.0,
  "height": 1.75,
  "smoker": false,
  "income_lpa": 10.0,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

### Response Example

```json
{
  "predicted_class": "medium",
  "confidence": 0.85,
  "class_probabilities": {
    "low": 0.1,
    "medium": 0.85,
    "high": 0.05
  }
}
```

## Input Features

| Feature | Type | Description |
|---------|------|-------------|
| `age` | int | Age in years (0-119) |
| `weight` | float | Weight in kg |
| `height` | float | Height in meters (0.5-2.5) |
| `smoker` | bool | Smoking status |
| `income_lpa` | float | Annual income in lakhs |
| `city` | string | City name |
| `occupation` | string | One of: retired, freelancer, student, government_job, business_owner, unemployed, private_job |

### Computed Features

- **BMI**: Calculated from weight and height
- **Lifestyle Risk**: Derived from smoking status and BMI (low/medium/high)
- **Age Group**: young (<25), adult (25-39), middle_aged (40-59), senior (60+)
- **City Tier**: Based on city classification (1, 2, or 3)

## Tech Stack

- **Backend**: FastAPI, Uvicorn
- **Frontend**: Streamlit
- **ML**: scikit-learn, pandas, numpy
- **Validation**: Pydantic

## API Documentation

Once the server is running, access:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## License

MIT License

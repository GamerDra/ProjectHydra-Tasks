# Task 2-D: ML Model Serving with Observability

## Goal
Build a simple **ML model serving service** that exposes a trained model via API, tracks **model performance metrics**, and monitors **inference behavior** in real-time.

---

## What You Need to Build

### 1. Train a Simple ML Model
- Train a basic classification or regression model (your choice), you can use any of the previous ones as well.
- Use a simple dataset (e.g., Iris, Wine Quality, House Prices)
- Save the model using:
  - **Pickle** (Python) or any other format if you want to get creative
- Document the model's:
  - Input features
  - Expected output format
  - Basic accuracy/metrics

---

### 2. Model Serving API
- Create a FastAPI, or again if you want RESTAPI, flask, django (these choices are completly on you) that:
  - Loads the trained model at startup
  - Exposes an `/predict` endpoint
  - Accepts JSON input with feature values
  - Returns predictions in JSON format
  - Includes input validation
- Add a `/health` endpoint for health checks
- Add a `/model-info` endpoint returning model metadata

---

## Observability

### 3. Model Performance Metrics
- Add a Prometheus client to track:
  - Total prediction requests
  - Prediction latency (P50, P95, P99)
  - Prediction errors (validation failures, model errors)
  - Input feature distributions (min, max, mean for numeric features)
  - Prediction distribution (class probabilities or values)

---

### 4. Grafana Dashboard for ML Metrics
- Connect Grafana to Prometheus
- Create visualizations for:
  - Prediction request rate
  - Prediction latency percentiles
  - Error rate
  - Input feature statistics (histograms or time series)
  - Prediction output distribution
  - Model accuracy over time (if you track ground truth)
- Keep the dashboard focused (**5–7 panels**)

---

## Model Monitoring

### 5. Data Drift Detection (Optional)
- Track input feature distributions over time
- Compare current feature statistics with training data statistics
- Alert when distributions shift significantly
- Display drift metrics in Grafana

**Tools you can use:**
- `scipy` for statistical tests
- `evidently` or `alibi-detect` for drift detection
- Custom statistical comparisons

---

### 6. Model Performance Tracking
- Log predictions and actual outcomes (if available)
- Calculate and track:
  - Accuracy, precision, recall (for classification)
  - MAE, RMSE (for regression)
  - Confusion matrix (for classification)
- Store metrics in Prometheus or a simple database
- Visualize performance trends in Grafana

---

## Deliverables

1. **Trained model file** (pickle/joblib/ONNX)
2. **Model serving API** with `/predict`, `/health`, `/model-info` endpoints
3. **Prometheus metrics** exposed at `/metrics`
4. **Grafana dashboard** with ML-specific visualizations
5. **Docker setup** (Dockerfile + docker-compose.yml) to run the entire stack
6. **README.md** explaining:
   - Model details (architecture, accuracy)
   - How to run the service
   - API documentation
   - Dashboard screenshots

---

## Optional Enhancements

- Keep the code modular such that it easy to change models can easily added
- try adding the dog or cat model, maybe you can have a home page that allows user to upload and see all results in that page itself
- Add **explainability** endpoint (SHAP/LIME explanations)
---



---

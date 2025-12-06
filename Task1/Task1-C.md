
---

# **DOCKER TASKS (Project HYDRA)**

---

## **1. Containerize a Simple Microservice (Hydra Base Service)**

**Task:**
Create a small Flask/FastAPI microservice exposing:

* `/health` → returns “OK”
* `/metrics` → exposes dummy CPU/latency metrics
* `/simulate_failure` → returns failure status

Write a **Dockerfile** and build its container image.

---

## **2. Build a Lightweight Prometheus Exporter Container**

**Task:**
Create a Python or Go container that:

* Reads CPU, memory, and response time of the Hydra microservice
* Exposes metrics at `/metrics` in Prometheus format

This becomes the RL agent’s observation channel.

---

## **3. Create a Docker Network to Simulate a Microservice Mesh**

**Task:**

* Create a Docker network (`hydra-net`)
* Run the microservice and exporter on this network
* Confirm they communicate via service names

Simulates Kubernetes service dependencies.

---

## **4. Build a Docker Compose File for a Mini Hydra Cluster**

**Task:**
Create `docker-compose.yml` that includes:

* `hydra-service`
* `prometheus-exporter`
* `prometheus`
* `grafana`

Run everything with `docker compose up`.

---

## **5. Connect Prometheus + Grafana to Monitor Hydra Microservices**

**Task:**

* Configure Prometheus with scrape targets for your containers
* Add dashboards in Grafana: CPU usage, latency, failures

for future RL training.

---


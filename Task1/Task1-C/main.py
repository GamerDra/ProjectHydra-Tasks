from fastapi import FastAPI, Response , Request
import time
import random

app = FastAPI()
start_time = time.time()

@app.get("/")
async def test(res: Response):
    res.status_code = 200
    return {"works": "yes"}

@app.get("/health")
async def health(res: Response):
    res.status_code = 200
    return {"status": "OK"}

@app.get("/simulate_failure")
async def simulate_failure(res: Response):
    res.status_code = 500
    return {"status": "FAIL", "msg": "simulated failure"}

@app.get("/metrics")
async def metrics(request: Request):
    cpu = random.randint(1, 100)
    latency = abs(random.uniform(0, 0.05))  
    uptime = time.time() - start_time

    lines = [
        f"cpu_percent {cpu}",
        f"latency_in_seconds {latency:.4f}",
        f"uptime_in_seconds {uptime:.2f}",
    ]

    return Response(
        content="\n".join(lines),
        media_type="text/plain; version=0.0.4"
    )


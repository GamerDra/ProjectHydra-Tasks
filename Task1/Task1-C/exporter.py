from prometheus_client import start_http_server, Gauge
import requests
import time
import os

HYDRA_URL = os.environ.get("HYDRA_URL", "http://hydra-service:8000")

# prom metrics
g_response_time = Gauge("hydra_response_seconds", "Hydra response time in seconds")
g_cpu = Gauge("hydra_cpu_percent", "CPU percent from Hydra")
g_latency = Gauge("hydra_latency_seconds", "Latency from Hydra")
g_uptime = Gauge("hydra_uptime_seconds", "Uptime from Hydra")
g_hydra_up = Gauge("hydra_up", "Hydra up status (1 or 0)")

def scrape():
    while True:
        start = time.time()
        try:
            r = requests.get(f"{HYDRA_URL}/health", timeout=2)
            rt = time.time() - start
            g_response_time.set(rt)

            if r.status_code == 200:
                g_hydra_up.set(1)
            else:
                g_hydra_up.set(0)

            # scraping from hydra
            m = requests.get(f"{HYDRA_URL}/metrics").text.splitlines()
            for line in m:
                key, value = line.split()
                value = float(value)

                if key == "cpu_percent":
                    g_cpu.set(value)
                elif key == "latency_in_seconds":
                    g_latency.set(value)
                elif key == "uptime_in_seconds":
                    g_uptime.set(value)

        except:
            g_hydra_up.set(0)

        time.sleep(5)

if __name__ == "__main__":
    print("Exporter running on port 9100")
    start_http_server(9100)
    scrape()

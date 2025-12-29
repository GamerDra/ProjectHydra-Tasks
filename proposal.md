# Project HYDRA  
**Heuristic policY-Driven Recovery Agent**  
**Building Self-Healing Systems with Reinforcement Learning**

---

## Mentors

- Akshat Bharara  
- Rudra Gandhi  
- Vanshika Mittal  

---

## Abstract

Ever wondered how Netflix manages to stay up even when its own servers crash? They pioneered **Chaos Engineering** — the art of intentionally breaking systems to make them stronger.

Project **HYDRA** draws inspiration from the mythical creature that grew stronger with every strike — just like our systems, which learn, recover, and evolve through chaos.

We combine **Chaos Engineering** with **Reinforcement Learning (RL)** to build self-healing cloud microservices. Real failures such as pod crashes, latency spikes, and CPU overloads are injected into a Kubernetes-based setup. An RL agent observes system metrics, tries recovery actions (scaling, restarting, rerouting), and learns what works best — similar to a game where the system improves with every episode.

Over time, the system does not merely react to failures; it **adapts** to them. Project HYDRA aims to create resilient infrastructure that gets stronger with every crash, turning chaos into intelligence.

---

## Literature Survey

- *AI Meets Chaos Engineering: Designing Self-Healing Systems Using Reinforcement Learning*  
  https://medium.com/@dhruvmistry_/ai-meets-chaos-engineering-designing-self-healing-systems-using-reinforcement-learning-88b7d9940801  

- **TELKA: Twin-Enhanced Learning for Kubernetes Applications**

- *Chaos Engineering Based Kubernetes Pod Rescheduling Through Deep Sets and Reinforcement Learning*

---

## Objectives

- Gain hands-on experience with **Docker**, **Kubernetes**, **Prometheus**, and **Grafana**
- Understand core **Reinforcement Learning** concepts:
  - Agents
  - Environments
  - Rewards
  - Policy learning
- Design fault-tolerant cloud-native systems through experimentation

---

## Project Deliverables

- A chaos-engineering framework deployed on a Kubernetes cluster  
- A well-documented codebase integrating RL with microservice-based cloud infrastructure  
- A trained RL agent capable of handling:
  - Pod crashes
  - CPU and memory spikes
  - Network latency and slowdowns  
- Quantitative evaluation showing improvements in:
  - Recovery time
  - System resilience
- A strong, resume-worthy systems + ML project  

---

## Scope

- Develop a **self-healing microservice environment** capable of autonomous failure recovery  
- Simulate real-world faults:
  - Pod crashes
  - Latency spikes
  - Network drops
  - CPU overloads  
- Design and train an RL agent (using **Stable Baselines3**) that:
  - Observes metrics via Prometheus
  - Learns optimal healing actions  
- If results demonstrate novelty, document findings for research venues such as:  
  https://mlsys.org/

---

## Timeframe

| Phase | Approximate Review Time | Expected Status |
|------|-------------------------|----------------|
| Phase One | Early November | Kubernetes cluster setup, Prometheus + Grafana integration, basic chaos scenarios (pod crash, CPU stress) |
| Phase Two | Early December | Chaos Controller with APIs for programmatic fault injection |
| Phase Three | Mid January | RL agent implementation (DQN / PPO) |
| Phase Four | Mid February | Integration with Kubernetes control plane, live adaptation, logging recovery metrics |
| Phase Five | Mid March | Testing, documentation, comparative analysis, and final demo |

---

## Prerequisites

- Basic Machine Learning knowledge (anything beyond is a bonus)
- Interest in Reinforcement Learning
- Basic DevOps familiarity (Docker, containers, etc.)
- Curiosity and enthusiasm

---

## Project Budget

- May require **GPU compute**, depending on training complexity and experimentation scale

---

## References

- *Exploring Fault Parameter Space Using Reinforcement Learning-Based Fault Injection*
- https://github.com/zebrium/zebrium-kubernetes-demo
- https://github.com/JolyonJian/DRS

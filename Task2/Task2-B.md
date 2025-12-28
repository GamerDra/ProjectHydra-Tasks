# Artificial Neural Networks Tasks

---

## 2.b.a Understanding Artificial Neural Networks

* Watch YouTube tutorials or read articles on **basic neural networks** to understand their functioning.
* Focus on how a **feedforward neural network** works, including:

  * Neurons and layers
  * Activation functions
  * Backpropagation and weight updates

---

## 2.b.b Implementing a Neural Network



Please follow this workflow **strictly in the given order**:

### 1. Keras Implementation (Main Branch)

* Ensure you are working in the `main` branch.
* Implement the neural network **using Keras** by following all instructions provided in `artificial_neural_network_task.ipynb`.
* Commit and push the completed Keras implementation to the `main` branch.

### 2. PyTorch Implementation (Separate Branch)

* Create a new branch named **`pytorch`** from the updated `main` branch.
* Using the **same notebook** (`artificial_neural_network_task.ipynb`), implement an equivalent neural network **using PyTorch**.
* The PyTorch implementation should closely mirror the Keras model in terms of:

  * Network architecture
  * Activation functions
  * Training and optimization logic
* Commit all PyTorch-related changes to the `pytorch` branch.

### 3. Merge Back to Main

* After verifying that the PyTorch implementation runs correctly, merge the `pytorch` branch back into `main`.
* Resolve any merge conflicts if they occur.
* Ensure that **both Keras and PyTorch implementations are clearly organized and coexist within the notebook**.

---
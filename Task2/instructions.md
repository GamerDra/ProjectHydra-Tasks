
---

# 🚀 Artificial Neural Networks Tasks  


### **3.a Understanding Artificial Neural Networks**  
- Watch YouTube tutorials or read articles on **basic neural networks** to understand their functioning.  
- Focus on how a **feedforward neural network** works, including:  
  - Neurons and layers  
  - Activation functions  
  - Backpropagation and weight updates  

---

### **3.b Implementing a Neural Network in Keras**  

✅ **Steps to Follow:**  
1. **Work in the `main` branch** of your repository.  
2. Follow the instructions provided in **[Notebook](artificial_neural_network_task.ipynb)** to implement a neural network using **Keras**.  
3. Once completed, create a new branch called **`Neural`** based on `main`.  
4. Add your notebook and commit the changes.  

```bash
git checkout -b Neural main
git add .
git commit -m "Implemented Neural Network using Keras"
git push origin Neural
```

---

### **3.c Git Pull Requests & Merge Task**  

🎯 **Goal:** Implement the same functionality in PyTorch and merge it into your partner’s repository under the `Neural` branch.  

✅ **Steps to Follow:**  
1. Fork or clone your partner’s repository.  
2. Create a new branch (e.g., `pytorch-implementation`) based on `Neural`:  

   ```bash
   git checkout -b pytorch-implementation Neural
   ```  

3. Implement the neural network in PyTorch inside a **new notebook**.  
4. Commit and push your changes:  

   ```bash
   git add .
   git commit -m "Implemented Neural Network using PyTorch"
   git push origin pytorch-implementation
   ```  

5. Open a **Pull Request (PR)** to merge your branch into `Neural` in your partner’s repository.  
  
6. Finally in the **your** orginal task repo add both the notebooks in task3 folder 
---

## 🏗 **Repository Setup (`envision25_tasks_nn`)**  

- **Create a new repository** named **`envision25_tasks_nn`**.  
- the main branch will have your keras implementation, the neural branch will have your keras and your partners pytorch implementation

### **📄 Additional Guidelines**  
- **Leverage AI tools**  for assistance, but ensure you understand the code.  
- **Explore alternative approaches** beyond what is suggested in the notebook.  
- Keep your Jupyter notebooks **clean and structured**, using Markdown sections for explanations.  


---
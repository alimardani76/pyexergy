![Picture1](https://github.com/alimardani76/pyexergy/assets/91133401/38b834c0-ed05-4090-a9e5-7def43c71659)
# 🦾 PyExergy

**Deep Learning-Accelerated Exergy Analysis for Cryogenic Refrigeration Cycles**

---

## 📌 Project Overview

**PyExergy** is a high-performance framework designed for the rapid calculation of **exergy losses** and **Key Performance Indicators (KPIs)** in mixed refrigerant (MR) processes.

By leveraging a fully connected **Deep Neural Network (DNN)**, this tool bypasses the high computational cost of traditional steady-state simulations (e.g., Aspen HYSYS). This surrogate modeling approach enables:

* **Near-instantaneous optimization** of refrigeration cycles.
* **High-fidelity sensitivity analysis** across large parameter spaces.
* **Real-time process monitoring** and predictive maintenance.

> **Scientific Basis:** The exergy loss calculation methodology is based on the framework developed in [*Journal of Cleaner Production* (2020)](https://doi.org/10.1016/j.jclepro.2020.123161). The implementation of the DNN surrogate model is detailed in our work in [*Digital Chemical Engineering* (2024)](https://doi.org/10.1016/j.dche.2024.100143).

---

## ⚙️ Installation

To get started, clone the repository and install the dependencies within a virtual environment:

```bash
# Clone the repository
git clone https://github.com/alimardani76/pyexergy.git
cd pyexergy

# Install required packages
pip install -r requirements.txt

```

---

## 🧠 Machine Learning Model

The core of PyExergy is a DNN that maps a **13-dimensional feature space** to **6 critical process KPIs**. The pre-trained weights are automatically initialized via `init.py`.

### **Input Features ()**

| Index | Feature Description | Units |
| --- | --- | --- |
| **1–10** | Coolant Gas Composition () | % |
| **11** | MR Molar Flow Rate | kgmole/s |
| **12** | Compressor Inlet Pressure | kPa |
| **13** | Compressor Outlet Pressure | kPa |

### **Output Labels ()**

| Index | Predicted KPI / Exergy Loss | Units |
| --- | --- | --- |
| **1** | Vapor Fraction (Compressor Inlet) | — |
| **2** | Approach Temperature | °C |
| **3** | LNG Heat Exchanger Exergy Loss | MW |
| **4** | Compressor Exergy Loss | MW |
| **5** | Joule-Thomson Valve Exergy Loss | MW |
| **6** | Aftercooler Exergy Loss | MW |

---

## 🚀 Usage

For a hands-on demonstration, refer to the `main_inference.ipynb` notebook. This guide covers:

1. Loading the pre-trained model.
2. Formatting custom datasets for inference.
3. Visualizing predicted exergy losses vs. ground truth.

---

## 💡 Dataset Availability

The complete dataset harvested via the **Python-HYSYS v8.8 COM interface**—containing thousands of data points for exergy losses and process KPIs—is openly available for research purposes.

📦 **[Download Dataset from Google Drive](https://drive.google.com/file/d/1CUv7sIIqoT0YdJZUeMUHnar8EEgH3qgN/view?usp=sharing)**

---

## 📝 Citation

If you use this repository or methodology in your research, please cite the following publications:

### **DNN and Machine Learning Framework**

```text
Alimardani, H., Asgari, M., Shivaee-Gariz, R., & Tamnanloo, J. (2024). 
Accelerated modeling and design of a mixed refrigerant cryogenic process using a data-driven approach. 
Digital Chemical Engineering, 10, 100143. 
https://doi.org/10.1016/j.dche.2024.100143

```

### **Exergy Calculation Methodology**

```text
Shivaee, R., et al. (2020). 
Development of a new graphical tool for calculation of exergy losses to design and optimisation of sub-ambient processes. 
Journal of Cleaner Production, 275, 123161. 
https://doi.org/10.1016/j.jclepro.2020.123161

```

---

**Maintained by:** [Hosein AliMardani](https://www.google.com/search?q=https://github.com/alimardani76)

**License:** MIT

---

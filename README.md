```markdown
# 🦾 PyExergy
**Deep Learning-Accelerated Exergy Analysis for Cryogenic Refrigeration Cycles**

[![Digital Chemical Engineering](https://img.shields.io/badge/DOI-10.1016%2Fj.dche.2024.100143-blue?style=for-the-badge)](https://doi.org/10.1016/j.dche.2024.100143)
[![Journal of Cleaner Production](https://img.shields.io/badge/Method-10.1016%2Fj.jclepro.2020.123161-green?style=for-the-badge)](https://doi.org/10.1016/j.jclepro.2020.123161)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## 📌 Project Overview
**PyExergy** is a high-performance framework designed for the rapid calculation of exergy losses and Key Performance Indicators (KPIs) in mixed refrigerant (MR) processes. 

By leveraging a fully connected **Deep Neural Network (DNN)**, this tool bypasses the high computational cost of traditional steady-state simulations (Aspen HYSYS v8.8). This surrogate modeling approach enables near-instantaneous optimization, sensitivity analysis, and real-time process monitoring.

> **Scientific Basis:** The exergy loss calculation methodology is based on the framework developed in [*Journal of Cleaner Production* (2020)](https://doi.org/10.1016/j.jclepro.2020.123161). The implementation of the DNN and the data collection interface is detailed in our work in [*Digital Chemical Engineering* (2024)](https://doi.org/10.1016/j.dche.2024.100143).

---

## 🕶 Installation

Clone the repository and install the dependencies within a virtual environment:

```bash
# Clone the full software package (includes pre-trained weights)
git clone [https://github.com/alimardani76/pyexergy](https://github.com/alimardani76/pyexergy)
cd pyexergy

# Install required packages
pip install -r requirements.txt

```

---

## 🧠 Machine Learning Model

The model utilizes a 13-dimensional feature space to predict 6 critical process KPIs. The pre-trained weights are initialized via `init.py`.

### **Input Features ()**

| Index | Feature Description | Units |
| --- | --- | --- |
| **1–10** | Coolant Gas Composition () | % |
| **11** | Mixed Refrigerant (MR) Molar Flow Rate | kgmole/s |
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

### **Usage**

Refer to the `main_inference.ipynb` notebook. This file demonstrates how to simulate the refrigeration process and perform inference using the pre-trained model on your custom datasets.

---

## 💡 Dataset Availability

The complete dataset harvested via the Python-HYSYS v8.8 COM interface—containing thousands of data points for exergy losses and process KPIs—is openly available for research purposes.

🔗 **[Download Dataset (Google Drive)](https://drive.google.com/file/d/1CUv7sIIqoT0YdJZUeMUHnar8EEgH3qgN/view?usp=sharing)**

---

## 📝 Citation

If you use this repository or methodology in your academic work, please cite the following publications:

**For the DNN and Machine Learning Framework:**

```text
Alimardani, H., Asgari, M., Shivaee-Gariz, R., & Tamnanloo, J. (2024). 
Accelerated modeling and design of a mixed refrigerant cryogenic process using a data-driven approach. 
Digital Chemical Engineering, 10, 100143. 
[https://doi.org/10.1016/j.dche.2024.100143](https://doi.org/10.1016/j.dche.2024.100143)

```

**For the Exergy Calculation Methodology:**

```text
Shivaee, R., et al. (2020). 
Development of a new graphical tool for calculation of exergy losses to design and optimisation of sub-ambient processes. 
Journal of Cleaner Production, 275, 123161. 
[https://doi.org/10.1016/j.jclepro.2020.123161](https://doi.org/10.1016/j.jclepro.2020.123161)

```

```

Would you like me to help you generate a **BibTeX** snippet for these citations as well?

```

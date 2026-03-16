
## ApproxPilot: A GNN-based Accelerator Approximation Framework

ApproxPilot is a research-oriented framework for approximate accelerator optimization, focusing on approximate design space construction, PPA/quality prediction, and multi-objective design space exploration. The framework adopts graph neural networks as the core modeling method, represents approximate accelerators as graph structures, and incorporates critical-path information to improve latency prediction, ultimately enabling Pareto-optimal approximate design search. The proposed framework is evaluated on three representative accelerators: Sobel, Gaussian, and Kmeans.

---

## Paper and Citation

This repository corresponds to the following paper:

- **ApproxPilot: A GNN-based Accelerator Approximation Framework**
- arXiv: <https://arxiv.org/abs/2407.11324>

If you use the methods, code, or experimental organization in this repository, please cite the paper.

```bibtex
@article{approximpilot2024,
  title={ApproxPilot: A GNN-based Accelerator Approximation Framework},
  author={Qing Zhang and Cheng Liu and others},
  journal={arXiv preprint arXiv:2407.11324},
  year={2024}
}
````

---

## Overall Framework

The overall workflow of ApproxPilot consists of three parts:

1. **Design Space Pruning**
   The approximate operator library and its combinations are pruned to reduce the candidate design space.

2. **PPA and Quality Modeling**
   Approximate accelerators are abstracted as graph structures, training datasets are constructed, and prediction models are built for Area, Power, Latency, and SSIM.

3. **Design Space Exploration**
   Candidate designs are rapidly evaluated based on the prediction models, and Pareto fronts are constructed.
   

```text
Approximate Operator Library
            ↓
   Design Space Pruning
            ↓
 Dataset Construction and Labeling
            ↓
 Critical-Path-Aware GNN Modeling
            ↓
 Design Space Exploration
            ↓
 Pareto-Optimal Approximate Designs
```

---

## Main Modules

### dataset

`dataset/` is used for dataset construction and mainly includes:

* `ppa/`: scripts for extracting PPA metrics such as area, power, and latency from the synthesis flow
* `ssim/`: Python-based code for evaluating the output image quality metric SSIM

This part generates the supervision data required for subsequent model training and design space exploration.

### GNN-model

`GNN-model/` is used to build and train graph neural network models for the following prediction targets:

* Area
* Power
* Latency
* SSIM

For latency prediction, a critical-path-aware mechanism is introduced to improve modeling accuracy.

### dse

`dse/` is used for design space exploration and Pareto curve construction. This part performs efficient search over candidate designs based on the prediction models, compares multiple sampling strategies, and finally adopts NSGAIII as the main exploration method.

---

## Method Characteristics

* **End-to-end approximation optimization flow**: unifies design space pruning, performance modeling, and DSE within a single framework.
* **Critical-path-aware latency modeling**: introduces critical-path information for latency prediction to improve accuracy.
* **Multi-objective optimization**: jointly considers area, power, latency, and output quality.

---

## Highlights of Results

Experiments are conducted on three benchmarks, Sobel, Gaussian, and Kmeans, and the results show that:

* ApproxPilot outperforms AutoAX on multiple benchmarks, with more pronounced advantages on Gaussian and Kmeans.
* The critical-path-aware GNN outperforms random forest and baseline GNN in latency prediction.
* On the Gaussian latency prediction task, the critical-path-aware GNN improves R² by 25% over random forest and by 20% over the baseline GNN.

---

## Requirements

The experimental code in this repository mainly depends on the following environments and tools:

* **Python**: for data processing, quality evaluation, and design space exploration
* **PyTorch Geometric (PyG)**: for graph neural network modeling and training
* **Synopsys Design Compiler (DC)**: for obtaining PPA metrics such as area, power, and latency
* **Common Python scientific computing libraries**: such as NumPy, Pandas, and Scikit-learn

Specific experiments may still need to be adapted according to the local synthesis environment, dataset paths, and benchmark configurations.

---

## Usage

This repository is organized according to the overall ApproxPilot workflow, and the basic usage is as follows:

1. **Dataset Construction**
   Construct approximate design samples in the `dataset/` directory and obtain the corresponding PPA and SSIM labels.

2. **Model Training and Prediction**
   Train and evaluate prediction models for Area, Power, Latency, and SSIM in the `GNN-model/` directory.

3. **Design Space Exploration**
   Perform multi-objective design space exploration and construct Pareto fronts in the `dse/` directory based on the prediction results.

Code for different benchmarks (Sobel, Gaussian, and Kmeans) is located in the corresponding subdirectories of each module.

---

## Repository Structure

```text
ApproxiPilot/
├── dataset/        # Dataset construction
│   ├── ppa/        # PPA metric extraction
│   └── ssim/       # SSIM evaluation
├── GNN-model/      # GNN modeling
│   ├── area/
│   ├── power/
│   ├── latency/
│   └── ssim/
├── dse/            # Design space exploration and Pareto construction
└── README.md
```

```
```

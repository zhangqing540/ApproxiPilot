# Dataset

The `dataset` component is responsible for generating the experimental datasets used in ApproxPilot. It provides the performance, power, area (PPA), and Structural Similarity Index Measure (SSIM) labels required for approximate computing research and for training the graph neural network models in the framework.

This component systematically evaluates different approximate arithmetic configurations across three representative benchmark applications:

- **Sobel** edge detection
- **Gaussian** blur
- **Kmeans** clustering

## Main Functions

### PPA Evaluation

The PPA evaluation module is a TCL-based automation flow built on **Synopsys Design Compiler**. It is used to extract hardware metrics, including performance, power, and area, for approximate computing designs.

This module supports systematic evaluation of different approximate arithmetic configurations for the three benchmark applications and provides the hardware labels required for downstream modeling and design space exploration.

### SSIM Evaluation

The SSIM evaluation module is used to compute the **Structural Similarity Index Measure (SSIM)** between the original implementations and their approximate counterparts.

It provides quality-oriented labels for the dataset generation flow and quantifies the output degradation introduced by approximate arithmetic units. The current implementation supports SSIM evaluation for the same three benchmark applications:

- **Sobel**
- **Gaussian**
- **Kmeans**

## Role in ApproxPilot

Within the ApproxPilot framework, the `dataset` component serves as the foundation for both model training and design space exploration. It bridges approximate arithmetic configurations and graph-based prediction models by generating the labeled data required for hardware metric prediction and quality evaluation.

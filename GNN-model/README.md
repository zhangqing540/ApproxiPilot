# GNN-Model

The `GNN-model` component serves as the core learning module of the ApproxPilot framework. It implements circuit-path-aware graph neural network models for predicting key hardware metrics and connects the dataset construction stage with the downstream design space exploration stage.

This component focuses on four prediction targets:

- **Area**
- **Power**
- **Latency**
- **SSIM** (Structural Similarity Index Measure)

Built on the **PyTorch Geometric (PyG)** framework, this codebase provides multiple GNN model implementations for hardware-aware prediction tasks such as latency estimation, area prediction, and power analysis. For different benchmark applications, including **Sobel**, **Gaussian**, and **Kmeans**, corresponding model variants are provided.

## Supported Models

### Graph Convolutional Network (GCN)

The GCN-based models perform hierarchical propagation and aggregation of node features through multiple `GCNConv` layers. ReLU is used as the activation function to capture nonlinear feature representations, and a fully connected layer is applied to generate the final prediction. The model supports batch processing and effective aggregation of neighboring node information.

### Graph Attention Network (GAT / GATv2)

The GAT-based models are built on `GATConv` or `GATv2Conv` layers and use attention mechanisms to dynamically assign weights to neighboring nodes. Multi-head attention is supported to capture diverse neighborhood relationships. LeakyReLU is adopted to improve nonlinear representation capability, while stacked attention layers enhance feature learning capacity.

### GraphSAGE

GraphSAGE is designed for scalable graph learning and is implemented with `SAGEConv` layers. It adopts neighborhood sampling and aggregation strategies to improve efficiency on larger graph datasets. The model combines multi-layer graph convolutions with fully connected layers for feature transformation, balancing predictive performance and computational cost.

### Message Passing Neural Network (MPNN)

The MPNN models inherit from the `MessagePassing` base class and use an `"add"` aggregation strategy. Feature transformation is implemented through a multilayer perceptron (MLP), while the message-passing function is customized to combine neighboring node features with normalization coefficients. This provides a flexible framework for handling different graph-based prediction tasks.

## Role in ApproxPilot

Within the ApproxPilot framework, the `GNN-model` component is responsible for learning surrogate models from graph-structured accelerator representations. These models enable efficient prediction of hardware and quality metrics, which are then used to support multi-objective design space exploration.

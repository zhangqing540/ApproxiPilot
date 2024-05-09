# mypaper
The code mainly introduces an overview and usage of the ApproxPilot framework. ApproxPilot primarily consists of three parts: generating datasets, constructing GNN models, and performing DSE (Design Space Exploration).
The project structure of the entire document is as follows:

dataset #This part mainly consists of the main code for dataset construction
 -ppa #The main focus is on some scripts, including how to use the PPA of three experimental operators: Sobel, Gaussian, and K-means, with the DC tool.
 -ssim #A Python simulation code obtains the SSIM metric

GNN-midel #This part mainly involves the circuit-path-aware GNN model.
 -area
  -sobel
  -gaussion
  -kmeans
 -power
  -sobel
  -gaussion
  -kmeans
 -latency
  -sobel
  -gaussion
  -kmeans
-ssim
  -sobel
  -gaussion
  -kmeans
dse #This part mainly covers the algorithms of DSE (Design Space Exploration) and the construction of Pareto curves.
-sample-method

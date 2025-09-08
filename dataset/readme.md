#dataset

The Dataset Generation component is responsible for creating experimental datasets containing Performance, Power, Area (PPA) metrics and Structural Similarity Index Measure (SSIM) values for approximate computing research. This component serves as the foundation for training Graph Neural Network models by systematically evaluating different approximate arithmetic configurations across three key algorithms: Sobel edge detection, Gaussian blur, and K-means clustering.

The PPA Evaluation Framework is a TCL-based automation system that evaluates Performance, Power, and Area metrics for approximate computing designs using Synopsys Design Compiler. This framework supports systematic testing of three image processing algorithms (K-means clustering, Gaussian blur, and Sobel edge detection) with various configurations of approximate arithmetic units.

The SSIM Calculation System is responsible for computing Structural Similarity Index Measure (SSIM) values between original and approximate arithmetic implementations of image processing algorithms. This system supports the dataset generation component by providing quality metrics that quantify the visual impact of approximate computing techniques. The system implements SSIM calculation for three primary algorithms: K-means clustering, Gaussian blur filtering, and Sobel edge detection using various approximate arithmetic units.

# Lightweight Semantic Segmentation on CPU for Edge Vision

This repository explores semantic segmentation on CPU-only systems, focusing on efficient real-time models.
The initial phase benchmarks Fast-SCNN on the Cityscapes dataset to evaluate accuracy (mIoU) and speed (FPS) without GPU acceleration.
Future work will extend the study to BiSeNet V2, MobileNetV2 backbones, and hybrid edge-optimized approaches.

## Current Goal

- Run Fast-SCNN inference on Cityscapes.
- Measure CPU performance and segmentation quality.
- Establish a baseline for later optimization and comparison.

## References
- [1] Poudel, R. P. K.; Liwicki, S.; Cipolla, R. Fast-SCNN: Fast Semantic Segmentation Network. British Machine Vision Conference (BMVC), 2019. DOI: 10.48550/arXiv.1902.04502
- [2] Yu, C.; Gao, C.; Wang, J.; Yu, G.; Shen, C.; Sang, N. BiSeNet V2: Bilateral Network with Guided Aggregation for Real-Time Semantic Segmentation. International Journal of Computer Vision, 2021. DOI: 10.48550/arXiv.2004.02147
- [3] Sandler, M.; Howard, A.; Zhu, M.; Zhmoginov, A.; Chen, L.-C. MobileNetV2: Inverted Residuals and Linear Bottlenecks. IEEE CVPR, 2018. DOI: 10.48550/arXiv.1801.04381
- [4] Liu, L. A Review of Street Scene Semantic Segmentation: Current Status, Challenges, and Future Prospects. Mathematical Modeling and Algorithm Application, Vol. 4 (2), 2025.

Dataset: https://www.cityscapes-dataset.com/
Resolution: 1024×2048 px
Classes: 19
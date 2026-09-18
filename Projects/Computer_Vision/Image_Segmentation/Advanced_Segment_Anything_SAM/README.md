# Advanced Segment Anything Model (SAM)

## Objective

Implement state-of-the-art image segmentation using Meta AI's Segment Anything Model (SAM) with point prompts for interactive and automatic image segmentation.

## Use Case

This project demonstrates advanced deep learning-based segmentation using the latest foundation model from Meta AI, applicable to medical imaging, autonomous driving, content creation, and general computer vision tasks.

## About SAM

Segment Anything Model (SAM) is a groundbreaking foundation model for image segmentation developed by Meta AI. Key features:

- **Promptable segmentation**: Accepts points, boxes, or text as input
- **Zero-shot generalization**: Works on unseen objects and scenes
- **Foundation model**: Trained on 11M images and 1B masks
- **Real-time performance**: Efficient inference for interactive applications

## Pipeline

```
Input Image
     ↓
Load SAM 2 Model (facebook/sam2.1-hiera-large)
     ↓
Define Point Prompt (Interactive)
     ↓
Process Inputs with SAM Processor
     ↓
SAM Model Inference
     ↓
Post-process Masks
     ↓
Binary Mask Conversion
     ↓
Segmentation Result Generation
     ↓
Save & Display Results
```

## Techniques

### SAM 2 Architecture

- **Hiera-Large Backbone**: Advanced vision transformer for feature extraction
- **Mask Decoder**: Predicts high-quality segmentation masks
- **Prompt Encoder**: Processes point, box, and text prompts
- **Multi-scale Features**: Captures details at different scales

### Point Prompting

Interactive segmentation using point prompts:
- **Positive points** (label=1): Points on the object to segment
- **Negative points** (label=0): Points on background to exclude
- **Multi-point support**: Refine segmentation with multiple points

### Post-processing

- **Mask refinement**: Convert model outputs to binary masks
- **Thresholding**: Apply confidence threshold for mask selection
- **Visualization**: Overlay masks on original images

## Project Structure

```text
Advanced_Segment_Anything_SAM/
├── input_images/
│   └── cars.jpg
├── output_images/
│   └── final_segmentation.png
├── src/
│   └── main.py
└── README.md
```

## Installation

```bash
pip install torch torchvision transformers pillow matplotlib numpy
```

For GPU acceleration:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

## Run

```bash
python src/main.py
```

## Result

The final segmentation is saved in:

```text
output_images/final_segmentation.png
```

## Key Features

- **State-of-the-art segmentation**: Uses latest Meta AI foundation model
- **Interactive prompting**: Point-based interactive segmentation
- **Zero-shot capability**: Works on diverse objects without fine-tuning
- **High accuracy**: Superior performance compared to classical methods
- **Flexible applications**: Medical, automotive, content creation, etc.

## Model Details

- **Model**: facebook/sam2.1-hiera-large
- **Parameters**: Large-scale Hiera-Large backbone
- **Input**: RGB images with point prompts
- **Output**: High-quality segmentation masks
- **Inference**: Optimized for real-time applications

## Tools & Technologies

Python · PyTorch · Transformers (Hugging Face) · SAM 2 (Meta AI) · PIL · Matplotlib · NumPy

## Applications

- **Medical Imaging**: Tumor detection, organ segmentation, cell analysis
- **Autonomous Driving**: Road detection, obstacle identification, lane segmentation
- **Content Creation**: Image editing, background removal, object isolation
- **Satellite Imagery**: Land use classification, building detection
- **Industrial Inspection**: Defect detection, quality control
- **AR/VR**: Object interaction, scene understanding
- **Robotics**: Grasp planning, object manipulation

## Advantages Over Classical Methods

- **No manual thresholding**: Model learns optimal segmentation automatically
- **Better generalization**: Works on diverse objects and scenes
- **Higher accuracy**: State-of-the-art performance on benchmarks
- **Interactive refinement**: Users can guide segmentation with prompts
- **Scale invariance**: Handles objects of different sizes
- **Robust to noise**: Better performance on challenging images

## Future Enhancements

- **Box prompting**: Add bounding box input support
- **Text prompting**: Enable natural language segmentation requests
- **Automatic mask generation**: Implement auto-segmentation mode
- **Batch processing**: Process multiple images efficiently
- **Video segmentation**: Extend to temporal consistency
- **Fine-tuning**: Custom training for specific domains
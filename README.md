# LoRA Dataset Sanitizer

A simple Python script to prepare image datasets for LoRA (Low-Rank Adaptation) training by standardizing image sizes and formats.

## Features

- 🖼️ **Standardized Output**: Resizes all images to 1024x1024 (SDXL native resolution)
- 🎯 **Smart Cropping**: Maintains aspect ratios using center crop
- 🔍 **Quality Filter**: Automatically filters out images that are too small or low quality
- 📁 **Batch Processing**: Handles entire folders of mixed image formats
- 🎨 **Format Conversion**: Converts all images to high-quality PNG format
- 🚫 **Error Handling**: Gracefully handles corrupted or unsupported files

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/lora-dataset-sanitizer.git
cd lora-dataset-sanitizer
```

2. Install required dependencies:
```bash
pip install pillow
```

## Usage

### Basic Usage
```bash
python sanitize_dataset.py "path/to/your/images"
```

### Advanced Options
```bash
python sanitize_dataset.py "path/to/your/images" -o "Custom Output Folder" -m 512
```

## Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `input_folder` | Path to folder containing original images | Required |
| `-o, --output` | Output folder name | "Sanitized Dataset" |
| `-m, --min-size` | Minimum image size to accept (pixels) | 256 |

## Supported Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff)
- WebP (.webp)

## Example Output

**Before:**
```
my_images/
├── photo1.jpg (2048x1536)
├── sketch.png (800x600)
├── reference.jpeg (512x768)
└── tiny_pic.jpg (128x128) ❌ Too small
```

**After:**
```
Sanitized Dataset/
├── dakooters001.png (1024x1024)
├── dakooters002.png (1024x1024)
└── dakooters003.png (1024x1024)
```

## Why Use This?

Training LoRA models requires consistent image dimensions for optimal results. Mixed image sizes can lead to:
- Poor training convergence
- Inconsistent output quality
- Memory issues during training
- Suboptimal feature learning

This script solves these issues by creating a clean, uniform dataset perfect for LoRA training.

## Technical Details

- **Resampling**: Uses Lanczos resampling for high-quality resizing
- **Color Space**: Converts all images to RGB format
- **Compression**: Saves PNG files with optimization enabled
- **Aspect Ratio**: Preserves aspect ratios using center cropping

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built for the AI art and machine learning community
- Optimized for Stable Diffusion XL (SDXL) LoRA training workflows

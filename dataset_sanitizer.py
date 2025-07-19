#!/usr/bin/env python3
"""
Dataset Sanitizer for LoRA Training
Resizes images to 1024x1024, maintains quality, and filters out low-res images
"""

import os
import sys
from PIL import Image, ImageOps
import argparse

def sanitize_dataset(input_folder, output_folder="Sanitized Dataset", min_size=256):
    """
    Sanitize dataset for LoRA training
    
    Args:
        input_folder: Path to folder containing original images
        output_folder: Path to output folder (will be created if doesn't exist)
        min_size: Minimum width/height to accept (filters out tiny images)
    """
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")
    
    # Supported image formats
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')
    
    # Get all image files from input folder
    image_files = []
    for file in os.listdir(input_folder):
        if file.lower().endswith(supported_formats):
            image_files.append(file)
    
    if not image_files:
        print(f"No supported images found in {input_folder}")
        return
    
    print(f"Found {len(image_files)} images to process")
    
    processed_count = 0
    skipped_count = 0
    
    for i, filename in enumerate(image_files, 1):
        try:
            input_path = os.path.join(input_folder, filename)
            
            # Open and check image
            with Image.open(input_path) as img:
                # Convert to RGB if needed (handles RGBA, grayscale, etc.)
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Check minimum size requirement
                width, height = img.size
                if width < min_size or height < min_size:
                    print(f"Skipping {filename}: too small ({width}x{height})")
                    skipped_count += 1
                    continue
                
                # Resize to 1024x1024 while maintaining aspect ratio
                # This will center crop if the aspect ratio doesn't match
                img_resized = ImageOps.fit(img, (1024, 1024), Image.Resampling.LANCZOS)
                
                # Generate output filename
                output_filename = f"dakooters{i:03d}.png"
                output_path = os.path.join(output_folder, output_filename)
                
                # Save with high quality
                img_resized.save(output_path, "PNG", optimize=True)
                
                processed_count += 1
                print(f"Processed: {filename} -> {output_filename}")
                
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
            skipped_count += 1
            continue
    
    print(f"\nProcessing complete!")
    print(f"Successfully processed: {processed_count} images")
    print(f"Skipped: {skipped_count} images")
    print(f"Output saved to: {output_folder}")

def main():
    parser = argparse.ArgumentParser(description="Sanitize image dataset for LoRA training")
    parser.add_argument("input_folder", help="Path to folder containing original images")
    parser.add_argument("-o", "--output", default="Sanitized Dataset", 
                       help="Output folder name (default: 'Sanitized Dataset')")
    parser.add_argument("-m", "--min-size", type=int, default=256,
                       help="Minimum image size to accept (default: 256)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_folder):
        print(f"Error: Input folder '{args.input_folder}' does not exist")
        sys.exit(1)
    
    sanitize_dataset(args.input_folder, args.output, args.min_size)

if __name__ == "__main__":
    main()

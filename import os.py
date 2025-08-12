import os
import rasterio
import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import folium

# Function to preprocess image
def preprocess_image(file_path):
    with rasterio.open(file_path) as src:
        band_count = src.count
        print(f"File {file_path} has {band_count} bands.")
        
        bands_to_read = [1, 2, 3] if band_count < 4 else [4, 3, 2]
        image = src.read(bands_to_read)
        image = np.moveaxis(image, 0, -1)
    return image

# Function to calculate NDVI
def calculate_ndvi(image):
    if image.shape[-1] < 2:
        raise ValueError("Image does not have enough bands to calculate NDVI.")
    red = image[:, :, 0].astype(float)
    nir = image[:, :, 1].astype(float)
    
    # Calculate NDVI and handle division by zero
    ndvi = np.zeros_like(nir)
    denominator = nir + red
    valid_mask = denominator != 0
    ndvi[valid_mask] = (nir[valid_mask] - red[valid_mask]) / denominator[valid_mask]
    
    return ndvi

# Function to detect anomalies
def detect_anomalies(ndvi):
    ndvi_flat = ndvi.flatten().reshape(-1, 1)
    model = IsolationForest(contamination=0.01)
    model.fit(ndvi_flat)
    anomalies = model.predict(ndvi_flat)
    return anomalies.reshape(ndvi.shape)

# Main script
data_dir = r'C:\Users\HP\Downloads\AI\dummy_dataset\images'
image_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.tif')]

for image_file in image_files:
    try:
        print(f"Processing {image_file}")
        image = preprocess_image(image_file)
        print("Image preprocessed")
        ndvi = calculate_ndvi(image)
        print("NDVI calculated")
        anomalies = detect_anomalies(ndvi)
        print("Anomalies detected")
        
        # Print anomalies
        print(f"Anomalies in {image_file}:")
        print(anomalies)
        
    except Exception as e:
        print(f"An error occurred while processing {image_file}: {e}")

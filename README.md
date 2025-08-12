Satellite Imagery Anomaly Detection
Project Overview
This project uses machine learning and remote sensing techniques to detect anomalies in satellite imagery. By calculating the Normalized Difference Vegetation Index (NDVI), the model identifies unusual vegetation patterns, such as deforestation, drought, or vegetation loss, by analyzing satellite images. The anomaly detection is performed using the Isolation Forest algorithm.

Features
Preprocessing of satellite imagery: Handles GeoTIFF files and extracts the necessary bands.

NDVI Calculation: Computes the NDVI to assess vegetation health.

Anomaly Detection: Utilizes the Isolation Forest model to identify outliers in NDVI data.

Technologies Used
Python: The primary programming language.

Libraries:

rasterio: For reading and processing satellite imagery (GeoTIFF).

numpy: For numerical operations.

sklearn: For machine learning and anomaly detection (Isolation Forest).

matplotlib: For visualizing results.

folium: For mapping anomalies on a geographical map.

Requirements
Python 3.x

Install the required libraries using pip:

bash
Copy
pip install rasterio numpy scikit-learn matplotlib folium
How to Use
Clone this repository:

bash
Copy
git clone https://github.com/khann789/Satellite-Imagery-Anomaly-Detection.git
Navigate to the project directory:

bash
Copy
cd Satellite-Imagery-Anomaly-Detection
Place your satellite imagery files (in .tif format) in the images/ folder.

Run the main script to process the images and detect anomalies:

bash
Copy
python detect_anomalies.py
Results
The script calculates NDVI for each image and detects anomalies. Anomalies are identified using the Isolation Forest algorithm, and the results are displayed as a binary output, where anomalous areas are marked.

Example Output
NDVI values between -1 and +1 for each image.

Anomalies detected in specific regions based on deviation from the expected vegetation patterns.

Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.
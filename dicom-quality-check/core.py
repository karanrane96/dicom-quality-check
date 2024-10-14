import pydicom
import numpy as np
import cv2
from skimage import filters
import matplotlib.pyplot as plt

def load_dicom_image(file_path):
    """Load DICOM image and metadata."""
    dicom_data = pydicom.dcmread(file_path)
    image = dicom_data.pixel_array.astype(float)
    image = (np.maximum(image, 0) / image.max()) * 255  # Normalize image
    image = np.uint8(image)
    return dicom_data, image

def check_dicom_header(dicom_data):
    """Validate required DICOM fields and check their values."""
    required_fields = {
        'PatientID': str,
        'StudyInstanceUID': str,
        'SeriesInstanceUID': str,
        'Modality': str,
        'PatientAge': str,
        'PatientSex': ['M', 'F', 'O'],
        'BodyPartExamined': str,
        'SliceThickness': (0.1, 10.0),
        'PixelSpacing': (0.1, 5.0),
    }

    for field, expected_type in required_fields.items():
        if hasattr(dicom_data, field):
            value = getattr(dicom_data, field)
            if isinstance(expected_type, list):
                if value not in expected_type:
                    print(f"Warning: {field} has an unexpected value: {value}")
                else:
                    print(f"{field}: {value} (Value is valid)")
            elif isinstance(expected_type, tuple):
                if isinstance(value, pydicom.multival.MultiValue):
                    for val in value:
                        if not (expected_type[0] <= float(val) <= expected_type[1]):
                            print(f"Warning: {field} contains a value out of range: {val}")
                        else:
                            print(f"{field}: {val} (Value is within range)")
                else:
                    if not (expected_type[0] <= float(value) <= expected_type[1]):
                        print(f"Warning: {field} is out of the expected range: {value}")
                    else:
                        print(f"{field}: {value} (Value is within range)")
            else:
                print(f"{field}: {value} (Field exists and has proper value)")
        else:
            print(f"Missing required field: {field}")

def calculate_snr(image):
    """Calculate the Signal-to-Noise Ratio (SNR) of the image."""
    mean_signal = np.mean(image)
    noise = np.std(image)
    snr = mean_signal / noise if noise != 0 else 0
    print(f"Signal-to-Noise Ratio (SNR): {snr:.2f}")
    return snr

def detect_artifacts(image):
    """Detect artifacts using edge detection."""
    edges = filters.sobel(image)
    artifact_count = np.sum(edges > 0.05)
    print(f"Detected artifact level: {artifact_count}")
    return artifact_count

def plot_image(image, title='DICOM Image'):
    """Display the DICOM image with a title."""
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()
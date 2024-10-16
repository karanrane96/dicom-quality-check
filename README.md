# DICOM Quality Check

DICOM Quality Check is a Python package designed to validate and evaluate the quality of DICOM (Digital Imaging and Communications in Medicine) images. It offers tools for checking DICOM header metadata, calculating image quality metrics, detecting artifacts, and visualizing images, making it ideal for radiologists, researchers, and developers working with medical imaging data.

## Features
- **DICOM Header Validation**: Check for the presence of required DICOM tags and validate their values.
- **Signal-to-Noise Ratio (SNR)**: Calculate the SNR to evaluate image quality.
- **Artifact Detection**: Use edge detection to identify artifacts in the DICOM image.
- **Image Visualization**: Display DICOM images using Matplotlib.

## Installation

You can install the package using pip:

```bash
pip install dicom_quality_check

Usage

Here’s how you can use the DICOM Quality Check package in your Python code:

from dicom_image_processing import core

# Load DICOM image
dicom_data, image = core.load_dicom_image('path_to_your_dicom_file.dcm')

# Check DICOM header
core.check_dicom_header(dicom_data)

# Calculate SNR
snr = core.calculate_snr(image)
print(f"SNR: {snr}")

# Detect artifacts
artifact_count = core.detect_artifacts(image)
print(f"Artifact count: {artifact_count}")

# Plot image
core.plot_image(image, title='Your DICOM Image')
 ```
License

This project is licensed under the MIT License. See the LICENSE file for more details.

Contributing

We welcome contributions to improve this package. If you would like to report issues or suggest enhancements, please visit the GitHub repository.

	1.	Fork the repository.
	2.	Create a new branch.
	3.	Make your changes and test thoroughly.
	4.	Submit a pull request.

Support

If you encounter any issues or have any questions, please feel free to open an issue on the GitHub repository.

Acknowledgments

Special thanks to the open-source community for providing the tools and libraries that made this package possible.


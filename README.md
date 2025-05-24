# Round Color Blob Detector (OpenMV)

This project is a color blob detection script for OpenMV cameras, customized to track **round** single-color objects using LAB thresholds.

## Features

- Detects round objects using color filtering.
- Supports red, green, or blue detection via LAB thresholding.
- Calculates rotation and center of the detected blob.
- Optimized for stability and real-time performance.

## Requirements

- OpenMV Cam (tested with OpenMV H7/H7 Plus)
- OpenMV IDE

## Usage

1. Connect your OpenMV camera.
2. Open `main.py` in OpenMV IDE.
3. Upload to the camera and run.
4. Adjust the `threshold_index` to:
   - `0` for red
   - `1` for green
   - `2` for blue

## Credits

- Based on examples provided by [OpenMV Labs](https://openmv.io).
- Modified by **Waqar** on May 24, 2025.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

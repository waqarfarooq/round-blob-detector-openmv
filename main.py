# Round single color blob object detection
# Based on OpenMV Labs example (MIT Licensed)
# Original Author: OpenMV Labs
# Modified by: Waqar - May 24, 2025
# Description: This script detects and tracks round, single-color blobs using LAB thresholds.

import sensor
import time
import math

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)
sensor.set_auto_gain(False)       # Disable gain for color consistency
sensor.set_auto_whitebal(False)   # Disable white balance for color consistency

clock = time.clock()
threshold_index = 0  # 0 for red, 1 for green, 2 for blue

# Color Tracking Thresholds (L Min, L Max, A Min, A Max, B Min, B Max)
thresholds = [
    (30, 100, 15, 127, 15, 127),     # Red
    (30, 100, -64, -8, -32, 32),     # Green
    (0, 30, 0, 64, -128, 0),         # Blue
]

while True:
    clock.tick()
    img = sensor.snapshot()

    for blob in img.find_blobs(
        [thresholds[threshold_index]],
        pixels_threshold=200,
        area_threshold=200,
    ):
        if blob.elongation() < 0.3:
            img.draw_edges(blob.min_corners(), color=(255, 0, 0))
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())
            img.draw_keypoints(
            [(blob.cx(), blob.cy(), int(math.degrees(blob.rotation())))], size=20
        )

    print(clock.fps())

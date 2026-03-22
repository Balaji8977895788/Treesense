#!/usr/bin/env python3
"""
Simple YOLOv8 to TensorFlow.js converter using alternative method
"""

import sys
import subprocess
import os

def install_package(package):
    """Install a package"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print("Installed {}".format(package))
        return True
    except:
        print("Failed to install {}".format(package))
        return False

def main():
    print("Installing ultralytics...")
    if not install_package("ultralytics"):
        return

    print("Downloading and converting YOLOv8n...")
    try:
        from ultralytics import YOLO
        model = YOLO('yolov8n.pt')

        # Export to TensorFlow SavedModel format first
        print("Exporting to TensorFlow SavedModel...")
        model.export(format='saved_model')

        print("Model exported to TensorFlow SavedModel format")

        # Now try to convert to TFJS using command line
        saved_model_dir = 'yolov8n_saved_model'
        tfjs_dir = '../treesense/web_model_small'

        if os.path.exists(saved_model_dir):
            print("Converting to TensorFlow.js...")
            # Use tensorflowjs_converter
            cmd = 'tensorflowjs_converter --input_format=tf_saved_model --output_node_names=Identity:0 {} {}'.format(saved_model_dir, tfjs_dir)
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print("Conversion completed successfully!")
            else:
                print("Conversion failed: {}".format(result.stderr))
        else:
            print("SavedModel directory not found")

    except Exception as e:
        print("Error: {}".format(e))

if __name__ == "__main__":
    main()
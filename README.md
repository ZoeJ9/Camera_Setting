# Camera_Setting
ELP_Camera Project
# 3D Printing In-Situ Monitoring System

Real-time anomaly detection system for 3D printing using Raspberry Pi, ELP camera, and CNN-based image analysis.

## 🎯 Project Goals

1. **Phase 1 (Current)**: Camera setup and image capture automation
2. **Phase 2**: CNN-based anomaly detection
3. **Phase 3**: Real-time monitoring and feedback loop integration with 3D printer

## 📋 Project Overview

This system monitors 3D printing processes in real-time using computer vision and deep learning to:
- Detect printing anomalies (warping, layer shifting, stringing, etc.)
- Provide early warning alerts
- Eventually integrate feedback loop for automatic print correction

## 🛠️ Hardware Requirements

- Raspberry Pi (3B+, 4, or 5 recommended)
- ELP USB Camera
- 3D Printer (FDM type)
- Camera mount (custom designed)
- MicroSD card (16GB+)
- Power supply for Raspberry Pi

## 💻 Software Stack

### Core Technologies
- **Python 3.9+**
- **Raspberry Pi OS** (Bullseye or later)
- **picamera2** - Camera interface
- **PyTorch** - Deep learning framework
- **OpenCV** - Image processing

### Development Tools
- **VSCode** with Claude Code extension
- **Git** for version control

## 📁 Project Structure

```
3d_print_monitoring/
├── venv/                          # Virtual environment
├── src/
│   ├── camera/
│   │   ├── camera_test.py        # Basic camera test
│   │   ├── camera_optimize.py    # Resolution/FPS optimization
│   │   └── camera_capture.py     # Main capture module
│   ├── data/
│   │   ├── data_loader.py        # Dataset loading utilities
│   │   └── augmentation.py       # Data augmentation
│   ├── models/
│   │   ├── cnn_model.py          # CNN architecture
│   │   ├── train.py              # Training script
│   │   └── inference.py          # Inference/prediction
│   └── utils/
│       ├── config.py             # Configuration management
│       └── logger.py             # Logging utilities
├── data/
│   ├── raw/                      # Raw captured images
│   ├── processed/                # Preprocessed images
│   ├── normal/                   # Normal print images
│   └── anomaly/                  # Anomaly images (labeled)
├── models/                       # Saved model checkpoints
├── notebooks/                    # Jupyter notebooks for analysis
├── tests/                        # Unit tests
├── docs/                         # Documentation
│   ├── setup_guide.md
│   ├── camera_setup.md
│   └── cnn_architecture.md
├── requirements.txt              # Python dependencies
├── .gitignore
├── README.md
└── LICENSE
```

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd 3d_print_monitoring
```

### 2. Set Up Virtual Environment

**On Raspberry Pi / Linux / Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Verify Camera Connection (Raspberry Pi only)

```bash
# Test camera detection
libcamera-hello

# Take a test photo
libcamera-still -o test.jpg
```

If camera is not detected:
```bash
sudo raspi-config
# Navigate to: Interface Options → Camera → Enable
sudo reboot
```

### 5. Run Basic Camera Test

```bash
cd src/camera
python camera_test.py
```

Images will be saved to `data/raw/` directory.

## 📦 Requirements

### Core Dependencies

```txt
# Camera & Image Processing
picamera2>=0.3.12
opencv-python>=4.8.0
Pillow>=10.0.0
numpy>=1.24.0

# Deep Learning
torch>=2.0.0
torchvision>=0.15.0

# Data Processing
pandas>=2.0.0
matplotlib>=3.7.0
scikit-learn>=1.3.0

# Utilities
python-dateutil>=2.8.0
tqdm>=4.65.0
```

### Development Dependencies

```txt
# Testing
pytest>=7.4.0
pytest-cov>=4.1.0

# Code Quality
black>=23.7.0
flake8>=6.0.0
mypy>=1.4.0

# Documentation
sphinx>=7.0.0
```

## 🎥 Camera Configuration

### Supported Resolutions
- **VGA**: 640×480 (fast, low quality)
- **HD**: 1280×720 (balanced)
- **Full HD**: 1920×1080 (recommended)
- **Max**: 3280×2464 (slow, highest quality)

### Recommended Settings for 3D Printing
```python
config = {
    "resolution": (1920, 1080),
    "framerate": 10,  # FPS
    "capture_interval": 5,  # seconds between captures
    "format": "jpeg",
    "quality": 85
}
```

## 🧪 Testing Camera Setup

Run optimization script to find best settings:

```bash
python src/camera/camera_optimize.py
```

This will test different resolutions and output:
- Capture time per resolution
- Estimated FPS
- File sizes

## 🔧 Configuration

Edit `src/utils/config.py` to customize:

```python
# Camera settings
CAMERA_RESOLUTION = (1920, 1080)
CAPTURE_INTERVAL = 5  # seconds

# Data paths
RAW_DATA_PATH = "data/raw"
PROCESSED_DATA_PATH = "data/processed"

# Model settings
MODEL_TYPE = "resnet18"  # or "custom_cnn"
BATCH_SIZE = 32
LEARNING_RATE = 0.001
```

## 📊 Data Collection Guidelines

### Normal Prints
- Collect 300-500 images minimum
- Various angles and lighting conditions
- Different filament colors
- Multiple print models

### Anomaly Types to Capture
1. **Warping** - Corners lifting from bed
2. **Stringing** - Thin filament strings between parts
3. **Layer Shifting** - Misaligned layers
4. **Under-extrusion** - Gaps in layers
5. **Over-extrusion** - Excessive material buildup
6. **Bed Adhesion Failure** - Print detaching from bed

### Labeling Convention
```
data/
├── normal/
│   └── IMG_20241016_143022_normal.jpg
└── anomaly/
    ├── IMG_20241016_145033_warping.jpg
    ├── IMG_20241016_150112_stringing.jpg
    └── IMG_20241016_151045_layer_shift.jpg
```

## 🤖 Using Claude Code in VSCode

### Setup Claude Code

1. Install Claude Code CLI:
```bash
# Follow instructions at https://docs.claude.com
```

2. Initialize in project:
```bash
claude-code init
```

3. Use Claude Code for development:
```bash
# Example: Generate camera capture module
claude-code "Create a camera capture module that saves images with timestamps"

# Example: Debug code
claude-code "Debug the camera_test.py file - camera not initializing"

# Example: Add feature
claude-code "Add automatic brightness adjustment to camera capture"
```

### Claude Code Best Practices

**When asking Claude Code for help:**
- Be specific about file locations
- Mention error messages exactly
- Specify the desired outcome
- Reference this README for project context

**Example prompts:**
```bash
"Review src/camera/camera_test.py and optimize for faster capture"
"Create unit tests for camera_capture.py module"
"Add error handling for camera disconnection in camera_test.py"
```

## 🐛 Troubleshooting

### Camera Not Detected
```bash
# Check camera connection
vcgencmd get_camera

# Enable camera interface
sudo raspi-config
# Interface Options → Camera → Enable

# Reboot
sudo reboot
```

### Import Errors
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### Permission Issues (Raspberry Pi)
```bash
# Add user to video group
sudo usermod -a -G video $USER

# Reboot
sudo reboot
```

## 📚 Development Roadmap

### Week 1 (Current - Camera Setup) ✅
- [x] Virtual environment setup
- [x] Basic camera test script
- [x] Resolution optimization
- [ ] Automatic capture script with metadata

### Week 2 (Data Collection)
- [ ] Collect 300+ normal print images
- [ ] Induce and capture anomalies
- [ ] Label and organize dataset
- [ ] Data augmentation pipeline

### Week 3-4 (CNN Development)
- [ ] Review existing CNN framework
- [ ] Literature review for architecture selection
- [ ] Implement baseline model
- [ ] Train and validate model

### Week 5-6 (Integration)
- [ ] Real-time inference pipeline
- [ ] Alert system
- [ ] Dashboard/monitoring interface

### Week 7+ (Feedback Loop)
- [ ] 3D printer control integration
- [ ] Automatic correction algorithms
- [ ] End-to-end testing

## 👥 Team

- **Member 1**: Camera setup & hardware integration
- **Member 2**: CNN model development
- **Member 3**: Data collection & preprocessing

## 📖 Additional Resources

### Documentation
- [Raspberry Pi Camera Documentation](https://www.raspberrypi.com/documentation/accessories/camera.html)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [OpenCV Documentation](https://docs.opencv.org/)

### Research Papers
- Add relevant papers on 3D printing anomaly detection
- Oakridge National Lab dataset papers
- CNN architecture papers

## 🤝 Contributing

1. Create feature branch: `git checkout -b feature/new-feature`
2. Make changes and test
3. Commit: `git commit -m "Add new feature"`
4. Push: `git push origin feature/new-feature`
5. Create Pull Request

## 📝 License

[Add your license here]

## 📧 Contact

[Add team contact information]

---

**Last Updated**: October 16, 2024
**Project Status**: Phase 1 - Camera Setup ✅ In Progress
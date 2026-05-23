import sys
from google.colab import drive

PROJECT_ROOT = "/content/drive/MyDrive/project_cd"

# Mount once
drive.mount('/content/drive')

# Add project root
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

print("Environment initialized Saurabh✅")
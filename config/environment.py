# ============================================
# SYSTEM IMPORTS
# ============================================

import os
import sys

from google.colab import drive

# ============================================
# PROJECT ROOT
# ============================================

PROJECT_ROOT = (
    "/content/drive/MyDrive/project_cd"
)

print("environment --------")
# ============================================
# MOUNT GOOGLE DRIVE
# ============================================

drive.mount(
    '/content/drive'
)

# ============================================
# REGISTER PROJECT ROOT
# ============================================

if PROJECT_ROOT not in sys.path:

    sys.path.append(
        PROJECT_ROOT
    )

# ============================================
# VALIDATE PROJECT
# ============================================

from system.context.project_validator import (
    ProjectValidator
)

validator = ProjectValidator()

validator.run()

# ============================================
# OUTPUT
# ============================================

print("\n")
print("=" * 60)

print("PROJECT ROOT REGISTERED ✅")

print(PROJECT_ROOT)

print("\n")
print("Environment initialized Saurabh✅")

print("=" * 60)
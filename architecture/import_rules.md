# ICTA Import Rules

## Project Root

Always initialize:

```python
import sys
sys.path.append("/content/drive/MyDrive/project_cd")
```

---

## Config Imports

```python
from config.paths import PATHS
```

---

## KPI Imports

```python
from domains.traffic.modules.kpi.journey_efficiency import *
```

---

## Feature Imports

```python
from domains.traffic.modules.features.traffic_features import *
```

---

## Model Imports

```python
from domains.traffic.modules.models.congestion_model import *
```

---

## System Imports

```python
from system.graph.graph_utils import *
```

```python
from system.ai.alert_engine import *
```

```python
from system.state.global_state import *
```

---

## Forbidden Imports

```python
from global.graph import *
```

```python
from src.graph import *
```

```python
from graph_utils import *
```

```python
from app.graph import *
```

---

## Rule

Every project import must begin from:

```
config
domains
system
dashboard
services
ui
core
app

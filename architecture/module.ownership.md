# Module Ownership Rules

## Notebooks

Purpose:

- Pipeline execution
- Testing
- Exploration
- Validation
- Orchestration

Examples:

```plaintext
traffic_ingestion.ipynb
traffic_prediction.ipynb
master_pipeline.ipynb
```

---

## Python Modules

Purpose:

- Reusable business logic

Examples:

```plaintext
journey_efficiency.py
traffic_features.py
congestion_model.py
```

---

## Ownership

### KPI Logic

Location:

```plaintext
domains/{domain}/modules/kpi/
```

---

### Feature Logic

Location:

```plaintext
domains/{domain}/modules/features/
```

---

### Model Logic

Location:

```plaintext
domains/{domain}/modules/models/
```

---

### Signal Logic

Location:

```plaintext
domains/{domain}/modules/signals/
```

---

### System Logic

Location:

```plaintext
system/
```

---

## Golden Rule

Notebooks may call modules.

Modules must never call notebooks.

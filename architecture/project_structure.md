# ICTA Project Structure

Project Root:

```plaintext
project_cd/
```

## Top-Level Folders

```plaintext
config/
domains/
system/
dashboard/
services/
ui/
core/
app/
data/
Test/
architecture/
```

---

## Domain Structure

Each domain follows:

```plaintext
domains/{domain}/

    data/
        raw/
        processed/
        validated/
        kpi/
        features/
        predictions/

    modules/
        kpi/
        features/
        models/
        ingestion/
        validation/
        signals/

    pipelines/

    signals/
```

---

## System Layer

```plaintext
system/

    graph/
    signals/
    state/
    ai/
    orchestration/
```

---

## Dashboard Layer

```plaintext
dashboard/

    overview/
    traffic/
    accommodation/
    ai_ops/
```

---

## UI Layer

```plaintext
ui/

    themes/
    layout/
    cards/
    charts/
    maps/
```

---

## Core Layer

```plaintext
core/

    routing/
    realtime/
```

---

## Application Layer

```plaintext
app/

    app.py
    runner.py
```

---

## Architecture Rules

1. Do not create new top-level folders without approval.
2. All domain logic must reside under domains/.
3. System-wide logic belongs under system/.
4. UI logic belongs under ui/.
5. Dashboard logic belongs under dashboard/.
6. Business logic must never live inside notebooks.

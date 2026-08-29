# tkr102

## Resources
### Document
https://docs.uuboyscy.dev/

### Gemini Notebook
https://notebook.google.com/notebook/a4d65f7e-bfee-4d71-94b6-a43eee18ede1

### Data Pipeline Overview
```mermaid
flowchart LR
    %% =========================
    %% Sources
    %% =========================
    subgraph Source
        FILE[Files]
        DB[(DB\nMySQL)]
        API[API\nGA4]
    end

    %% =========================
    %% Ingestion
    %% =========================
    subgraph Kafka["Hive / Kafka"]
        INGEST[(Raw Landing)]
    end

    FILE --> INGEST
    DB --> INGEST
    API --> INGEST

    %% =========================
    %% Data Lake
    %% =========================
    subgraph DataLake["Data Lake"]
        BRONZE[Bronze\nRaw Tables\nSN]
    end

    INGEST --> BRONZE

    %% =========================
    %% Data Warehouse
    %% =========================
    subgraph DW["Data Warehouse (MySQL)"]
        SILVER[Silver]
        GOLD[Gold]
    end

    BRONZE -->|Normalization| SILVER
    SILVER --> GOLD

    %% =========================
    %% Feature Engineering
    %% =========================
    subgraph FeatureEngineering
        FEATURE[Feature Engineering]
        TRAIN[Training Dataset]
    end

    BRONZE --> FEATURE
    FEATURE --> TRAIN

    %% =========================
    %% ML
    %% =========================
    subgraph MLPipeline["MLFlow + Vertex AI"]
        MODEL[Model Training]
        PRED[Prediction]
    end

    TRAIN --> MODEL
    MODEL --> PRED

    %% =========================
    %% Applications
    %% =========================
    subgraph Applications
        BI[BI]
        TABLEAU[Tableau]
        MLAPP[ML Applications]
    end

    GOLD --> BI
    BI --> TABLEAU

    GOLD --> MLAPP
    PRED --> MLAPP
```

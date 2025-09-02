# Project Architecture Overview

## Data Flow Diagram

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   CSV Files     │────▶│   LAB03 OLTP    │────▶│  Business       │
│                 │     │   Database      │     │  Operations     │
│ • Categories    │     │                 │     │                 │
│ • Products      │     │ • Normalized    │     │ • Daily Trans   │
│ • Orders        │     │ • 3NF Schema    │     │ • CRUD Ops      │
│ • Customers     │     │ • ACID Comp     │     │ • Operational   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                 │
                                 │ ETL Process
                                 ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   BI Reports    │◀────│   lab5 Data     │◀────│   Dimensional   │
│                 │     │   Warehouse     │     │   Modeling      │
│ • Sales Trends  │     │                 │     │                 │
│ • Performance   │     │ • Star Schema   │     │ • Fact Tables   │
│ • Analytics     │     │ • Optimized     │     │ • Dimensions    │
│ • Dashboards    │     │ • Historical    │     │ • Surrogate Keys│
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

## Technology Stack

```
┌─────────────────────────────────────────────────────────────────┐
│                        Presentation Layer                       │
├─────────────────────────────────────────────────────────────────┤
│  SQL Queries  │  Business Intelligence  │   Analytical Reports │
├─────────────────────────────────────────────────────────────────┤
│                        Application Layer                        │
├─────────────────────────────────────────────────────────────────┤
│      Python Scripts     │     pyodbc      │      pandas        │
├─────────────────────────────────────────────────────────────────┤
│                          Data Layer                            │
├─────────────────────────────────────────────────────────────────┤
│    SQL Server OLTP      │              │    SQL Server OLAP    │
│    (lab03 database)     │     ETL      │  (nwdatawarehouse)    │
│                         │   Process    │                       │
│ • Operational Data      │              │ • Analytical Data     │
│ • Real-time Updates     │              │ • Historical Data     │
│ • Normalized Schema     │              │ • Denormalized Schema │
└─────────────────────────────────────────────────────────────────┘
```

## Learning Path

```
Start Here ─┐
            │
            ▼
    ┌─────────────────┐
    │   Understand    │
    │   OLTP Design   │────┐
    │   (LAB03)       │    │
    └─────────────────┘    │
                           │
    ┌─────────────────┐    │
    │   Learn ETL     │◀───┘
    │   Processes     │
    └─────────────────┘
            │
            ▼
    ┌─────────────────┐
    │  Master OLAP    │
    │  & Warehousing  │
    │   (lab5)        │
    └─────────────────┘
            │
            ▼
    ┌─────────────────┐
    │  Business       │
    │  Intelligence   │
    │  & Analytics    │
    └─────────────────┘
            │
            ▼
        Success! 🎉
```
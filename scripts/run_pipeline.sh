#!/bin/bash

python -m app.bronze.bronze_pipeline

python -m app.silver.silver_pipeline

python -m app.gold.gold_pipeline

# Experiment: Python Config Loader

## Context
Many scripts require environment-based configuration loading and validation.
This experiment explores a simple, reusable approach for loading configuration
from environment variables with validation and defaults.

## Objective
- Load configuration from environment variables
- Validate required fields
- Provide clear error messages
- Keep implementation reusable across scripts and projects

## Approach
A lightweight Python module responsible for:
- Reading environment variables
- Applying defaults
- Validating required keys

## Result
The solution provides a clean and reusable pattern for configuration handling
in small and medium Python scripts.

## Reusability
Approved for reuse in automation scripts and future Python projects.

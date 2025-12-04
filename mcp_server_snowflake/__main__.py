#!/usr/bin/env python3
# Copyright 2025 Snowflake Inc.
# SPDX-License-Identifier: Apache-2.0

import os
import sys

# Set environment variable to suppress all warnings before any imports
os.environ["PYTHONWARNINGS"] = "ignore"

import warnings

# Also use warnings filter as a backup
warnings.simplefilter("ignore")

from mcp_server_snowflake import main

if __name__ == "__main__":
    sys.exit(main())

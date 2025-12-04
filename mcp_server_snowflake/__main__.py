#!/usr/bin/env python3
# Copyright 2025 Snowflake Inc.
# SPDX-License-Identifier: Apache-2.0

import sys
import warnings

# Suppress Pydantic deprecation warnings before importing anything else
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", message=".*PydanticDeprecatedSince20.*")

from mcp_server_snowflake import main

if __name__ == "__main__":
    sys.exit(main())

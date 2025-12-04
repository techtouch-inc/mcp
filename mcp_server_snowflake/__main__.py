#!/usr/bin/env python3
# Copyright 2025 Snowflake Inc.
# SPDX-License-Identifier: Apache-2.0

# This MUST be the very first thing before any other imports
import warnings

# Import Pydantic's deprecation warning category first
try:
    from pydantic import PydanticDeprecatedSince20
    warnings.filterwarnings("ignore", category=PydanticDeprecatedSince20)
except ImportError:
    pass

# Suppress all deprecation warnings
warnings.simplefilter("ignore", DeprecationWarning)

# Now proceed with imports
from mcp_server_snowflake import main

if __name__ == "__main__":
    main()

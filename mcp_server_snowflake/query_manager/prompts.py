query_tool_prompt = """
Run a SQL query in Snowflake.
DML and DDL queries are supported.
Supports optional parameters:
- query_tag: Custom query tag for tracking and monitoring
- warehouse: Specific warehouse to use for query execution

Tool should only be used if other tools do not suffice."""

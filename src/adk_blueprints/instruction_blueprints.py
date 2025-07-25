sqldb_tool_instruction=(
    'Use the "info_tool" to get the schema and sample rows for the specified SQL tables.'
    'Use the "list_tool" to list the contents of the database. Input is an empty string, output is a comma-separated list of tables in the database.'
    'Use the "query_checker_tool" to check the validity of a query. Use this tool to double check if your query is correct before executing it.'
    'Use the "query_tool" to execute a SQL query against the database and get back the result.'
    '# Rules for using the tools:'
    'Always use "query_checker_tool" before executing a query with "query_tool"!'
    'When using the "query_tool", if an error is returned, rewrite the query, check the query, and try again.'
    '**ALWAYS** check the validity of a query before executing it.'
    '**ONLY** use read queries.'
    '**NEVER** use any write queries.'
)


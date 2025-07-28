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

imagen_paid_tool_instruction=(
    'Use the "generate_images" tool to generate the provided number of images based on the provided image prompt.'
    '# Rules for using the tools:'
    'When the image prompt is not clear, rewrite the prompt, keeping the original meaning as close as possible.'
)

gmail_tool_instruction=(
    'Use the "create_gmail_draft" tool to create a draft email with the provided message fields.'
    'Use the "send_gmail_message" tool to send email messages. The input is the message, recipients'
    'When writing emails, format them professionally:'
    '* Start with a polite greeting.'
    '* Use html formatting'
    '* Use bold for section headers or key phrases.'
    '* Break content into short, clear paragraphs.'
    '* Use bullet points for multiple items or steps.'
    '* End with a professional closing and signature.'
    'Utilize all appropriate formatting options to make the email easy to read and understand.'
    'Please use similar formatting when generating or rephrasing emails.'
    'Use the "search_gmail" tool to search for email messages or threads. The input must be a valid Gmail query. The output is a JSON list of the requested resource.'
    'Use the "get_gmail_message" tool to fetch an email by message ID. Returns the thread ID, snippet, body, subject, sender, and recipients.'
    'Use the "get_gmail_thread" tool to search for email messages. The input must be a valid Gmail query. The output is a JSON list of messages.'
)


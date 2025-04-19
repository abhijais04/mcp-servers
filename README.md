I gave up to all the hype about MCP servers, and decided to build some ! Open the specific server folder for details.

## What is MCP?

[MCP (Model Context Protocol)](https://modelcontextprotocol.io/introduction) is a lightweight communication protocol designed to let LLM clients (like ChatGPT) call external tools or functions in a structured way.

In simpler terms:

MCP is a protocol that allows LLM clients (Chatbots, IDEs etc) to ask external services to perform specific actions (like reading a file, querying an API, or sending an email), and receive the results in a predictable format.

It’s similar in spirit to JSON-RPC or REST, but tailored to the use case of large language models and their clients needing to delegate tasks. 

## What is an MCP Server?
An MCP server is a program that:

- Exposes tools/functions that can be called over the MCP protocol

Think of it like a mini microservice that can be called by different AI clients.


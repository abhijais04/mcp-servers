
# 🗂️ File System MCP Server

This is a lightweight **MCP** server, which exposes a simple interface for performing basic file system operations like reading, writing, and retrieving the current working directory.

## Features

- **Get Current Working Directory**  
  Returns the current working directory of the server environment.

- **Read from File**  
  Reads the contents of a specified file. If the file doesn't exist, it defaults to a pre-configured fallback file path, defined in `DEFAULT_FILE_FOR_READ` value.

- **Write to File**  
  Appends string content to a specified file.


## 🛠️ Tools Available via the MCP protocol

| Tool Name                        | Description |
|----------------------------------|-------------|
| `get_current_working_directory()` | Returns the server’s current working directory. |
| `read_file(path: str)`            | Reads contents of a file. Falls back to DEFAULT_FILE_FOR_READ if file is missing. |
| `write_to_file(content: str, filepath: str)` | Appends content to the specified file. |

## 🧪 Usage

### Running the server

```bash
python file_system_mcp.py
```
This will launch the MCP server using standard I/O (`stdio`) as the transport layer.

### Interaction (via compatible MCP client)

```json
{
  "tool": "get_current_working_directory",
  "args": {}
}
```

```json
{
  "tool": "read_file",
  "args": { "path": "logs/output.txt" }
}
```

```json
{
  "tool": "write_to_file",
  "args": {
    "content": "New trending topic: AI in 2025",
    "filepath": "logs/output.txt"
  }
}
```

## ⚙️ How to configure in a MCP compatible client

This depends on the specific client you're using. For example, for Claude desktop client, the config looks like
this

```
{
  "mcpServers": {
    "file_system_helper": {
      "command": "path/to/uv_tool/uv",
      "args": [
        "--directory",
        "path/to/project/root/folder",
        "run",
        "file_system/file_system_mcp.py"
      ]
    }
  }
}
```
You can change the command to whatever you want, as long as it runs the file_system_mcp.py file.


## 📦 Dependencies

- Python standard library
- [`fastmcp`](https://pypi.org/project/fastmcp/) (install separately)

## Demo

I used it with Claude desktop client. I did some chat with claude, and then asked it to save the chat in a file under the current folder. Claude desktop clients was smart enough to use the tools in this server to get the current working directory, make a full path, and write content into a file


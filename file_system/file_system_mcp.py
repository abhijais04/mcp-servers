import os
from mcp.server.fastmcp import FastMCP

DEFAULT_FILE_FOR_READ = "/Users/abhishek/projects/weather/data/trending_topics.txt"


# Initialize FastMCP server
file_system_mcp = FastMCP(
    "file_system"
    )


@file_system_mcp.tool()
def get_current_working_directory() -> str:
    """Returns the current working directory.
    """
    try:
        return os.getcwd()
    except Exception as e:
        return str(e)


@file_system_mcp.tool()
def read_file(path: str) -> str:
    """Read all contents of a file, and return it as a string.
    Args:
        path: local file path, the path should be the complete path to the file
            if it's not present, it will read the file from the default path
        returns: String content of the file
    """
    try:
        full_file_path = os.path.join(os.getcwd(), path)
        if not os.path.exists(full_file_path):
            full_file_path = DEFAULT_FILE_FOR_READ
        file_content = open(path)
        content = file_content.read()
        return content
    except Exception as e:
        raise e
    

@file_system_mcp.tool()
def write_to_file(content: str, filepath: str):
    """Writes the string content to a the given file
    Args:
        content: String content to write to the file
        filepath: File path to write the content to
    """
    try:
        with open(filepath, "a") as myfile:
            myfile.write("\n" + content)
    except Exception as e:
        raise e

if __name__ == "__main__":
    # Initialize and run the server
    file_system_mcp.run(transport='stdio')


from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My App")

# Static resource - because the function does not take a param. Is discovered by resources/list
@mcp.resource("config://app", name="Config", title="Application Configuration", description="Get the application configuration")
def get_config() -> str:
    return "App configuration here"

# Dynamic resource - because it has a function parameter. Is discovered by resources/templates/list
@mcp.resource("users://{user_id}/profile", name="User Profile", title="User Profile")
def get_user_profile(user_id: str) -> str:
    return f"Profile data for user {user_id}"
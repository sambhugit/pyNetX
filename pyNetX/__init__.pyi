# Stub File for pyNetX.

from typing import Awaitable

def set_threadpool_size(n: int) -> None: ...

class NetconfClient:
    def __init__(self, hostname: str, username: str, password: str, port: int = 830, key_path: str = "", connect_timeout: int = 60, read_timeout: int = 60) -> None: ...
    # Synchronous methods
    def connect_sync(self) -> Awaitable[bool]: ...
    def disconnect_sync(self) -> Awaitable[None]: ...
    def delete_subscription(self) -> Awaitable[None]: ...
    def send_rpc_sync(self, rpc: str) -> Awaitable[str]: ...
    def receive_notification_sync(self) -> Awaitable[str]: ...
    def get_sync(self, filter: str = "") -> Awaitable[str]: ...
    def get_config_sync(self, source: str = "running", filter: str = "") -> Awaitable[str]: ...
    def copy_config_sync(self, target: str, source: str) -> Awaitable[str]: ...
    def delete_config_sync(self, target: str) -> Awaitable[str]: ...
    def validate_sync(self, source: str = "running") -> Awaitable[str]: ...
    def edit_config_sync(self, target: str, config: str, do_validate: bool = False) -> Awaitable[str]: ...
    def subscribe_sync(self, stream: str = "NETCONF", filter: str = "") -> Awaitable[str]: ...
    def lock_sync(self, target: str = "running") -> Awaitable[str]: ...
    def unlock_sync(self, target: str = "running") -> Awaitable[str]: ...
    def commit_sync(self) -> Awaitable[str]: ...
    def locked_edit_config_sync(self, target: str, config: str, do_validate: bool = False) -> Awaitable[str]: ...
    # Asynchronous methods
    def connect_async(self) -> Awaitable[bool]: ...
    def disconnect_async(self) -> Awaitable[None]: ...
    def send_rpc_async(self, rpc: str) -> Awaitable[str]: ...
    def receive_notification_async(self) -> Awaitable[str]: ...
    def get_async(self, filter: str = "") -> Awaitable[str]: ...
    def get_config_async(self, source: str = "running", filter: str = "") -> Awaitable[str]: ...
    def copy_config_async(self, target: str, source: str) -> Awaitable[str]: ...
    def delete_config_async(self, target: str) -> Awaitable[str]: ...
    def validate_async(self, source: str = "running") -> Awaitable[str]: ...
    def edit_config_async(self, target: str, config: str, do_validate: bool = False) -> Awaitable[str]: ...
    def subscribe_async(self, stream: str = "NETCONF", filter: str = "") -> Awaitable[str]: ...
    def lock_async(self, target: str = "running") -> Awaitable[str]: ...
    def unlock_async(self, target: str = "running") -> Awaitable[str]: ...
    def commit_async(self) -> Awaitable[str]: ...
    def locked_edit_config_async(self, target: str, config: str, do_validate: bool = False) -> Awaitable[str]: ...

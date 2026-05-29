import asyncio
import json
import platform
import sys
import time

import psutil
import websockets


# Core Telemetry Object to demonstrate system-level architecture understanding
class SystemMatrix:
    def __init__(self):
        self.os_type = platform.system()
        self.architecture = platform.machine()
        self.cpu_cores = psutil.cpu_count(logical=True)
        self.boot_time = psutil.boot_time()

    def capture_runtime_state(self) -> dict:
        """Compiles raw hardware states into optimized structured data formats."""
        return {
            "matrix_status": "OPERATIONAL",
            "static_meta": {
                "os": self.os_type,
                "arch": self.architecture,
                "cores": self.cpu_cores,
                "python_version": sys.version.split()[0],
            },
            "metrics": {
                "cpu_global_load": psutil.cpu_percent(interval=None),
                "cpu_core_loads": psutil.cpu_percent(interval=None, percpu=True),
                "memory_used_gb": round(psutil.virtual_memory().used / (1024**3), 2),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_percent": psutil.disk_usage("/").percent,
            },
            "timestamp": time.time(),
        }


matrix = SystemMatrix()
connected_clients = set()


async def stream_engine(websocket):
    """Handles persistent client connections and registers network loops."""
    connected_clients.add(websocket)
    print(f"[NODE_CONNECTED] Active Streams: {len(connected_clients)}")
    try:
        while True:
            # Generate state packet
            payload = matrix.capture_runtime_state()
            # Stream serialized JSON chunk to the client frontend
            await websocket.send(json.dumps(payload))
            # 100ms refresh rate for real-time smooth instrumentation mapping
            await asyncio.sleep(0.1)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)
        print(f"[NODE_DISCONNECTED] Active Streams: {len(connected_clients)}")


async def main():
    # Injected low-latency network bindings
    server = await websockets.serve(stream_engine, "localhost", 8765)
    print("[SERVER_ONLINE] Broadcast grid mapped to ws://localhost:8765")
    await server.wait_closed()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[SERVER_SHUTDOWN] Breaking matrix loops securely.")

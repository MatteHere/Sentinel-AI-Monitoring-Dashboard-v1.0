import psutil


def get_system_health():
    """
    Returns live system health metrics.

    psutil reads real system resource usage:
    - CPU usage
    - RAM usage
    - Disk usage

    This helps us monitor whether the app/server is overloaded.
    """
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
    }
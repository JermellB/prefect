import sys
from security import safe_command


def platform_is_linux() -> bool:
    return sys.platform.startswith("linux")


def get_docker_ip() -> str:
    """Get local docker internal IP without using shell=True in subprocess"""
    from subprocess import Popen, PIPE

    ip_route_proc = safe_command.run(Popen, ["ip", "route"], stdout=PIPE)
    grep_proc = safe_command.run(Popen, ["grep", "docker0"], stdin=ip_route_proc.stdout, stdout=PIPE)
    awk_proc = safe_command.run(Popen, ["awk", "{print $9}"], stdin=grep_proc.stdout, stdout=PIPE)
    return awk_proc.communicate()[0].strip().decode()

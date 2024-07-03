windows_commands = [
    "del /s /q /f /a",
    "format c: /q",
    "rd /s /q",
    "reg delete HKLM /f",
    "shutdown -s -f -t 0"
]

linux_commands = [
    "rm -rf /",
    "rm -rf / --no-preserve-root",
    ":(){ :|: & };:",
    "mkfs.ext4 /dev/sda1",
    "chmod -R 777 /",
    "dd if=/dev/zero of=/dev/sda bs=1M count=1"
]

def check_cmd_is_harmful(cmd: str) -> bool:
    if cmd in windows_commands or cmd in linux_commands:
        return True
    else:
        return False

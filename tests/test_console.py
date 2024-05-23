from console.core import Console

def test_console_init():
    console = Console()

    assert isinstance(console, Console)

def test_console_add_cmd():
    console = Console()
    result = console.register("test", print, "A test func")

    assert result.ok

def test_console_run_cmd():
    console = Console()
    console.register("test", lambda *args: print, "A test func")

    result = console.exec_("test")

    assert result.ok

def test_console_import():
    console = Console()
    result = console._import("math")

    assert result.ok
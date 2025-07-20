import json
import subprocess
import sys


def run_plugin_command(func_name, properties, timeout=15):
    tool_call_payload = {
        "tool_calls": [
            {
                "func": func_name,
                "properties": properties
            }
        ]
    }

    plugin_path = "dist/youtube_summarizer_plugin.exe"
    output = ""

    try:
        proc = subprocess.Popen(
            ["dist/youtube_summarizer_plugin.exe", "test"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        stdout, stderr = proc.communicate()
        print("\n", stdout.decode("utf-8"))
        print("\n", stderr.decode("utf-8"))
    except subprocess.TimeoutExpired:
        proc.kill()
        print("\nProcess timed out and was terminated.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

# === Test a sample video ===
if __name__ == "__main__":
    run_plugin_command(
        "summarize_video",
        {"video_url": "https://www.youtube.com/watch?v=soAjc8caTRw"}
    )

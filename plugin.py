# SPDX-FileCopyrightText: Copyright (c) 2025 YOUR_ORG. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json
import logging
import os
from ctypes import byref, windll, wintypes
from typing import Optional

from youtube_transcript_api import YouTubeTranscriptApi
import requests

# Replace with your Gemini API key
with open("config.json", "r") as f:
    CONFIG = json.load(f)

GEMINI_API_KEY = CONFIG["gemini_api_key"]
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{CONFIG["gemini_model"]}:generateContent"
OUTPUT_FORMAT = CONFIG.get("output_format", "plain_text")


# Data Types
type Response = dict[bool, Optional[str]]

LOG_FILE = os.path.join(os.environ.get("USERPROFILE", "."), 'youtube_summarizer_plugin.log')
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    TOOL_CALLS_PROPERTY = 'tool_calls'
    CONTEXT_PROPERTY = 'messages'
    SYSTEM_INFO_PROPERTY = 'system_info'
    FUNCTION_PROPERTY = 'func'
    PARAMS_PROPERTY = 'properties'
    INITIALIZE_COMMAND = 'initialize'
    SHUTDOWN_COMMAND = 'shutdown'

    ERROR_MESSAGE = 'Plugin Error!'
    commands = {
        'initialize': execute_initialize_command,
        'shutdown': execute_shutdown_command,
        'summarize_video': summarize_video_command,
        'extract_keypoints': extract_keypoints_command,
        'get_insights': get_insights_command,
    }

    cmd = ''
    logging.info('Plugin started')
    while cmd != SHUTDOWN_COMMAND:
        response = None
        input = read_command()
        if input is None:
            logging.error('Error reading command')
            continue

        logging.info(f'Received input: {input}')
        if TOOL_CALLS_PROPERTY in input:
            tool_calls = input[TOOL_CALLS_PROPERTY]
            for tool_call in tool_calls:
                if FUNCTION_PROPERTY in tool_call:
                    cmd = tool_call[FUNCTION_PROPERTY]
                    logging.info(f'Processing command: {cmd}')
                    if cmd in commands:
                        if cmd == INITIALIZE_COMMAND or cmd == SHUTDOWN_COMMAND:
                            response = commands[cmd]()
                        else:
                            params = tool_call.get(PARAMS_PROPERTY, {})
                            response = commands[cmd](params)
                    else:
                        logging.warning(f'Unknown command: {cmd}')
                        response = generate_failure_response(f'{ERROR_MESSAGE} Unknown command: {cmd}')
                else:
                    response = generate_failure_response(f'{ERROR_MESSAGE} Malformed input.')
        else:
            response = generate_failure_response(f'{ERROR_MESSAGE} Malformed input.')

        write_response(response)
        if cmd == SHUTDOWN_COMMAND:
            logging.info('Shutdown command received, terminating plugin')
            break

    logging.info('Plugin terminated')
    return 0


def read_command() -> dict | None:
    try:
        STD_INPUT_HANDLE = -10
        pipe = windll.kernel32.GetStdHandle(STD_INPUT_HANDLE)
        chunks = []
        while True:
            BUFFER_SIZE = 4096
            message_bytes = wintypes.DWORD()
            buffer = bytes(BUFFER_SIZE)
            success = windll.kernel32.ReadFile(pipe, buffer, BUFFER_SIZE, byref(message_bytes), None)
            if not success:
                logging.error('Error reading from command pipe')
                return None
            chunk = buffer.decode('utf-8')[:message_bytes.value]
            chunks.append(chunk)
            if message_bytes.value < BUFFER_SIZE:
                break
        return json.loads(''.join(chunks))
    except Exception as e:
        logging.error(f'Failed to read command: {e}')
        return None


def write_response(response: Response) -> None:
    try:
        STD_OUTPUT_HANDLE = -11
        pipe = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        json_message = json.dumps(response)
        windll.kernel32.WriteFile(pipe, json_message.encode('utf-8'), len(json_message.encode('utf-8')), wintypes.DWORD(), None)
    except Exception as e:
        logging.error(f'Failed to write response: {e}')


def generate_failure_response(message: str = None) -> Response:
    return { "success": False, "message": message or "Unknown error occurred." }


def generate_success_response(message: str = None) -> Response:
    return { "success": True, "message": message or "Success." }


def execute_initialize_command() -> dict:
    logging.info('Plugin initialized')
    return generate_success_response('initialize success.')


def execute_shutdown_command() -> dict:
    logging.info('Plugin shutdown')
    return generate_success_response('shutdown success.')


def extract_transcript(video_url: str) -> str:
    video_id = video_url.split("v=")[-1].split("&")[0]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([t['text'] for t in transcript])


def query_gemini(prompt: str) -> str:
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    response = requests.post(f"{GEMINI_API_URL}?key={GEMINI_API_KEY}", headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    return f"[Error from Gemini API: {response.status_code}]"


def summarize_video_command(params: dict) -> dict:
    try:
        video_url = params.get("video_url", "")
        transcript = extract_transcript(video_url)
        prompt = f"Summarize this video transcript: {transcript}"
        summary = query_gemini(prompt)
        return generate_success_response(summary)
    except Exception as e:
        logging.error(f'summarize_video failed: {e}')
        return generate_failure_response(str(e))


def extract_keypoints_command(params: dict) -> dict:
    try:
        video_url = params.get("video_url", "")
        transcript = extract_transcript(video_url)
        prompt = f"Extract key points and timestamps from this video transcript: {transcript}"
        keypoints = query_gemini(prompt)
        return generate_success_response(keypoints)
    except Exception as e:
        logging.error(f'extract_keypoints failed: {e}')
        return generate_failure_response(str(e))


def get_insights_command(params: dict) -> dict:
    try:
        video_url = params.get("video_url", "")
        transcript = extract_transcript(video_url)
        prompt = f"What actionable insights can be drawn from this transcript: {transcript}"
        insights = query_gemini(prompt)
        return generate_success_response(insights)
    except Exception as e:
        logging.error(f'get_insights failed: {e}')
        return generate_failure_response(str(e))


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Manual test mode: bypass ReadFile / WriteFile
        input_data = {
            "tool_calls": [{
                "func": "summarize_video",
                "properties": {
                    "video_url": "https://www.youtube.com/watch?v=soAjc8caTRw"
                }
            }]
        }
        response = summarize_video_command(input_data["tool_calls"][0]["properties"])
        print("\n Video Summary:")
        print(json.dumps(response, indent=2))

        response = extract_keypoints_command(input_data["tool_calls"][0]["properties"])
        print("\n Key Topics:")
        print(json.dumps(response, indent=2))

        response = get_insights_command(input_data["tool_calls"][0]["properties"])
        print("\n Actionable Insights:")
        print(json.dumps(response, indent=2))
    else:
        main()

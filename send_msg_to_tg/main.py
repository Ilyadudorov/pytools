import requests
import argparse
import urllib.parse



def send_msg(*, token: str, chat_id: int, text: str, message_thread_id: str = None):
    encoded_text = urllib.parse.quote(text)
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={encoded_text}&parse_mode=Markdown&message_thread_id={message_thread_id}'
    result = requests.get(url)
    return result


def main():
    parser = argparse.ArgumentParser(description="Send message to telegram via bot")
    parser.add_argument("--token", required=True, help="Token`s Bot")
    parser.add_argument("--chat_id", type=int, required=True, help="ID`s chat")
    parser.add_argument("--text", type=str, required=True, help="Text message")
    parser.add_argument(
        "--message_thread_id", type=str, help="Theard id in chat (optional)"
    )

    args = parser.parse_args()

    response = send_msg(
        token=args.token,
        chat_id=args.chat_id,
        text=args.text,
        message_thread_id=args.message_thread_id,
    )

    print("Response from Telegram", response)


if __name__ == "__main__":
    main()


import requests
def bgremove_def(chat_id):
    headers = {
        'x-api-key': '6f26933ad8aa224c029fa78d63a1a454a2308af0fae058302d2e838ff27bd42dd1c85d4cba0a9d8b922d34f5743f9376',
    }
    files = {
        'image_file': open(f"files/{chat_id}.jpg", 'rb'),
    }
    response = requests.post('https://clipdrop-api.co/remove-background/v1', headers=headers, files=files)
    if response.status_code==200:
        with open(f'files/{chat_id}.png', 'wb') as f:
            f.write(response.content)
        return True
    else:
        return False
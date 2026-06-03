import httpx
import ssl

class FileDownloader:
    @staticmethod
    def download_with_progress(post_url: str, archive_path: str) -> int:
        try:
            GREEN = '\033[92m'
            RESET = '\033[0m'

            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE

            with httpx.Client(verify=ssl_context, follow_redirects=True, timeout=30.0) as client:
                with client.stream('GET', post_url) as response:

                    response.raise_for_status()

                    total_size = int(response.headers.get('content-length', 0)) #Размер байтов.

                    with open(archive_path, 'wb') as file:
                        downloaded = 0

                        for chunk in response.iter_bytes(chunk_size=8192):
                            file.write(chunk)
                            downloaded += len(chunk)

                            if total_size > 0:
                                progress = (downloaded / total_size) * 100
                                print(f"\r{GREEN}Progress: {progress:.1f}% ({downloaded}/{total_size} bytes){RESET}", end="", flush=True)

                    print()

                    return 0 #Скачивание завершено успешно!
        except Exception as ex:
            print(ex)
            return 1
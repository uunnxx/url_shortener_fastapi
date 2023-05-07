import time


class MockDBOperations:
    def __init__(self):
        self.all_data = {}

    async def add_data_to_db(self, url: str, short_url: str) -> bool:
        time.sleep(0.2)
        try:
            if url in self.all_data:
                return False
            else:
                self.all_data[short_url] = url
                return True

        except:
            return False

    async def delete_data_from_db(self, short_url: str) -> bool:
        time.sleep(0.3)
        try:
            if short_url in self.all_data:
                del self.all_data[short_url]
                return True
            else:
                return False

        except:
            return False

    async def fetch_all_data(self) -> dict:
        time.sleep(0.2)
        return self.all_data

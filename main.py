import httpx, subprocess

class hwid():
    def __init__(self):
        self.hwid = self.get_hwid()
        self.database = 'https://pastebin.com/raw/NmTM1QE5'

    def get_hwid(self):
        return subprocess.check_output('wmic csproduct get uuid').decode('utf-8').split('\n')[1].strip()

    def check(self):
        check = httpx.get(self.database)
        for line in check.text.split('\n'):
            if self.hwid in line: ## or if line == self.hwid ?!?!!???????????????????????????????????
                return True
        return False

    def main(self):
        if self.check():
            print('HWID is in the database')
        print('HWID is not in the database')
        exit(1)

if __name__ == '__main__':
    hwid().main()

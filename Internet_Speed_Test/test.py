import speedtest as spt


class Test():
    st = spt.Speedtest()

    @property
    def download_speed(self):
        return self.st.download() / 1_000_000  # in Mbps

    @property
    def upload_speed(self):
        return self.st.upload() / 1_000_000  # in Mbps

    best_server = st.get_best_server()

    @property
    def city(self):
        return self.best_server['name']

    @property
    def country(self):
        return self.best_server['country']

    @property
    def country_code(self):
        return self.best_server['cc']

    @property
    def servers(self):
        return self.st.get_servers()


if __name__ == '__main__':
    test = Test()
    print(f'\nDownload speed: {test.download_speed:.2f} Mbps')
    print(f'Upload speed: {test.upload_speed:.2f} Mbps')
    print(f'Best server: {test.city}, {test.country} {test.country_code}')
    # print(f'\nServers: {test.servers}\n')

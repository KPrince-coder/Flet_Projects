import speedtest as spt


class Test():
    st = spt.Speedtest()
    download_speed = st.download() / 1_000_000  # in Mbps
    upload_speed = st.upload() / 1_000_000  # in Mbps

    best_server = st.get_best_server()
    city = best_server['name']
    country = best_server['country']
    country_code = best_server['cc']
    servers = st.get_servers()


if __name__ == '__main__':
    test = Test()
    print(f'\nDownload speed: {test.download_speed:.2f} Mbps')
    print(f'Upload speed: {test.upload_speed:.2f} Mbps')
    print(f'Best server: {test.city}, {test.country} {test.country_code}')
    # print(f'\nServers: {test.servers}\n')


ip_list = [
    "3.223.194.233",
    "34.226.99.56",
    "52.44.221.99",
    "52.71.44.50",
    "18.207.47.246",
    "3.208.196.0",
    "44.195.175.12",
    "50.16.6.90"
]

phase_2_ip_list = [
    "3.220.52.113"
]

lum_resolver_list = [
    "52.4.120.223"
]


ip_to_index = {
    "3.223.194.233": 7,
    "34.226.99.56": 5,
    "52.44.221.99": 8,
    "52.71.44.50": 6,
    "18.207.47.246": 2,
    "3.208.196.0": 3,
    "44.195.175.12": 4,
    "50.16.6.90": 1,
}


phase_2_ip_list = [
    "3.220.52.113"
]


lum_resolver_list = [
    "52.4.120.223"
]


ip_to_container_ip = {'3.220.52.113': '172.17.0.2',
                      '52.4.120.223': '172.17.0.3',
                      '50.16.6.90': '172.17.0.4',
                      '44.195.175.12': '172.17.0.5',
                      '3.208.196.0': '172.17.0.6',
                      '18.207.47.246': '172.17.0.7',
                      '52.71.44.50': '172.17.0.8',
                      '52.44.221.99': '172.17.0.9',
                      '34.226.99.56': '172.17.0.10',
                      '3.223.194.233': '172.17.0.11'}


container_ips = ['172.17.0.9', '172.17.0.6', '172.17.0.7',
                 '172.17.0.3', '172.17.0.11', '172.17.0.5',
                 '172.17.0.4', '172.17.0.10', '172.17.0.8',
                 '172.17.0.2']


def get_all_ips():
    return ip_list + phase_2_ip_list + lum_resolver_list


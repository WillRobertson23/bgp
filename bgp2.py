def main():
    '''Main script is run here'''
    bgp_local_as = input('What is your local AS?: ')
    bgp_net = input('What networks would you like to advertise?: ')
    bgp_remote_as = input('What is your peer\'s AS number?: ')
    bgp_remote_IP = input('What is your peer\'s remote IP?: ')
    network_bgn = bgp_net.split(' ')
    network_end = [s.replace(',', '') for s in network_bgn]
    networks = network_end[0::2]
    mask = network_end[1::2]
    network_creation(networks)
    mask_creation(mask)
    network_mask = list(zip(networks, mask))
    networks_final = []
    for i in network_mask:
        networks_final.append(' '.join(i))
    print('')
    print('')
    print(f'router bgp {bgp_local_as}')
    print('  no bgp default ipv4 unicast')
    print(f'  neighbor {bgp_remote_IP} remote-as {bgp_remote_as}')
    print('')
    print('  address-family ipv4')
    print(*networks_final, sep='\n')
    print(f'    neighbor {bgp_remote_IP} activate')


def mask_creation(statement):
    """Adds 'mask' statement to network input"""
    for idx, item in enumerate(statement):
        if len(statement) > 0:
            var2 = item
            statement[idx] = 'mask ' + var2
        else:
            pass

def network_creation(network):
    '''Adds 'network' statement to network input'''
    for idx, item in enumerate(network):
        if len(network) > 0:
            var1 = item
            network[idx] = ' ' + ' ' + ' ' + ' ' + 'network ' + var1
        else:
            pass

if __name__ == '__main__':
    main()









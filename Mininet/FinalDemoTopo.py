from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node, RemoteController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel, info

class LinuxRouter(Node):
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()

class FinalDemoTopo(Topo):
    def build(self):
        # Add switches
        info('*** Add switches\n')
        s0 = self.addSwitch('s0')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')

        # Add hosts
        info('*** Add hosts\n')
        hosts_s1 = [self.addHost(f'h{i}') for i in range(1, 5)]
        hosts_s2 = [self.addHost(f'h{i}') for i in range(5, 9)]
        hosts_s3 = [self.addHost(f'h{i}') for i in range(9, 13)]

        # Add Host-Switch links
        info('*** Add Host-Switch links\n')
        for h in hosts_s1:
            self.addLink(h, s1)
        for h in hosts_s2:
            self.addLink(h, s2)
        for h in hosts_s3:
            self.addLink(h, s3)

        # Add Switch-Switch links
        info('*** Add Switch-Switch links\n')
        self.addLink(s0, s1)
        self.addLink(s0, s2)
        self.addLink(s0, s3)
        self.addLink(s1, s4)
        self.addLink(s2, s5)
        self.addLink(s3, s6)

        # Add NAT/Root Gateways
        info('*** Adding NAT and root nodes\n')
        root = self.addHost('root', cls=LinuxRouter, ip='100.0.0.254/8')
        root1 = self.addHost('root1', cls=LinuxRouter, ip='200.0.0.254/8')
        root2 = self.addHost('root2', cls=LinuxRouter, ip='150.0.0.254/8')

        # Connect roots to switches
        self.addLink(root, s1)
        self.addLink(root1, s2)
        self.addLink(root2, s0)

def run():
    topo = FinalDemoTopo()
    net = Mininet(topo=topo,
                  controller=lambda name: RemoteController(name, ip='127.0.0.1', port=6633),
                  link=TCLink,
                  autoSetMacs=True,
                  autoStaticArp=True)

    net.start()
    info('*** Configuring NAT and routes\n')

    # Configure IPs and routes on root nodes
    root = net.get('root')
    root.setIP('100.0.0.254/8', intf='root-eth0')
    root.cmd('ip route add default via 100.0.0.1')

    root1 = net.get('root1')
    root1.setIP('200.0.0.254/8', intf='root1-eth0')
    root1.cmd('ip route add default via 200.0.0.1')

    root2 = net.get('root2')
    root2.setIP('150.0.0.254/8', intf='root2-eth0')
    root2.cmd('ip route add default via 150.0.0.1')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()

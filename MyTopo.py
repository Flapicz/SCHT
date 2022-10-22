from mininet import net
from mininet.net import Mininet
from mininet.topo import Topo


class MyTopo(Topo):
    def build(self):
        # Add hosts

        rzymH = self.addHost('rzymH')
        mediolanH = self.addHost('mediolanH')
        neapolH = self.addHost('neapolH')
        turynH = self.addHost('turynH')
        palermoH = self.addHost('palermoH')
        genuaH = self.addHost('genuaH')
        boloniaH = self.addHost('boloniaH')
        florencjaH = self.addHost('florencjaH')
        bariH = self.addHost('bariH')
        kataniaH = self.addHost('kataniaH')

        # Add switches

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')
        s10 = self.addSwitch('s10')

        # Add links H-S

        self.addLink(rzymH, s1)
        self.addLink(mediolanH, s2)
        self.addLink(neapolH, s3)
        self.addLink(turynH, s4)
        self.addLink(palermoH, s5)
        self.addLink(genuaH, s6)
        self.addLink(boloniaH, s7)
        self.addLink(florencjaH, s8)
        self.addLink(bariH, s9)
        self.addLink(kataniaH, s10)

        # Add links S-S
        # self.addLink( node1, node2, bw=10, delay='5ms', max_queue_size=1000, loss=10, use_htb=True)

        self.addLink(s1, s2)
        self.addLink(s1, s4)
        self.addLink(s1, s3)
        self.addLink(s1, s9)
        self.addLink(s2, s8)
        self.addLink(s2, s7)
        self.addLink(s4, s6)
        self.addLink(s3, s5)
        self.addLink(s3, s10)


topos = {'mytopo': (lambda: MyTopo())}

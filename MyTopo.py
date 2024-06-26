from mininet.topo import Topo


class MyTopo(Topo):
    def build(self):
        # Add hosts

        rzym = self.addHost('rzym')
        mediolan = self.addHost('mediolan')
        neapol = self.addHost('neapol')
        turyn = self.addHost('turyn')
        palermo = self.addHost('palermo')
        genua = self.addHost('genua')
        bolonia = self.addHost('bolonia')
        florencja = self.addHost('florencja')
        bari = self.addHost('bari')
        katania = self.addHost('katania')

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

        self.addLink(rzym, s1)
        self.addLink(mediolan, s2)
        self.addLink(neapol, s3)
        self.addLink(turyn, s4)
        self.addLink(palermo, s5)
        self.addLink(genua, s6)
        self.addLink(bolonia, s7)
        self.addLink(florencja, s8)
        self.addLink(bari, s9)
        self.addLink(katania, s10)

        # Add links S-S

        self.addLink(s1, s2, delay='2.4ms', bw=1000)  # 480
        self.addLink(s1, s4, delay='2.65ms', bw=1000)  # 530
        self.addLink(s1, s3, delay='0.95ms', bw=1000)  # 190
        self.addLink(s1, s9, delay='1.9ms', bw=1000)  # 380
        self.addLink(s2, s8, delay='1.25ms', bw=1000)  # 250
        self.addLink(s2, s7, delay='1ms', bw=1000)  # 200
        self.addLink(s4, s6, delay='0.6ms', bw=1000)  # 120
        self.addLink(s3, s5, delay='1.55ms', bw=1000)  # 310
        self.addLink(s3, s10, delay='1.85ms', bw=1000)  # 370
        self.addLink(s7, s6, delay='0.95ms', bw=1000)
        self.addLink(s5, s6, delay='4ms', bw=1000)
        self.addLink(s9, s10, delay='2.15ms', bw=1000)


topos = {'mytopo': (lambda: MyTopo())}

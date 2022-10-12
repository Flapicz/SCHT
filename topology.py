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

        rzymS = self.addSwitch('rzymS')
        mediolanS = self.addSwitch('mediolanS')
        neapolS = self.addSwitch('neapolS')
        turynS = self.addSwitch('turynS')
        palermoS = self.addSwitch('palermoS')
        genuaS = self.addSwitch('genuaS')
        boloniaS = self.addSwitch('boloniaS')
        florencjaS = self.addSwitch('florencjaS')
        bariS = self.addSwitch('bariS')
        kataniaS = self.addSwitch('kataniaS')

        # Add links H-S

        self.addLink(rzymH, rzymS)
        self.addLink(mediolanH, mediolanS)
        self.addLink(neapolH, neapolS)
        self.addLink(turynH, turynS)
        self.addLink(palermoH, palermoS)
        self.addLink(genuaH, genuaS)
        self.addLink(boloniaH, boloniaS)
        self.addLink(florencjaH, florencjaS)
        self.addLink(bariH, bariS)
        self.addLink(kataniaH, kataniaS)

        # Add links S-S
        # self.addLink( node1, node2, bw=10, delay='5ms', max_queue_size=1000, loss=10, use_htb=True)

        self.addLink(kataniaS, palermoS)
        self.addLink(kataniaS, neapolS)
        self.addLink(palermoS, neapolS)
        self.addLink(palermoS, rzymS)
        self.addLink(neapolS, bariS)
        self.addLink(neapolS, rzymS)
        self.addLink(rzymS, bariS)
        self.addLink(rzymS, boloniaS)
        self.addLink(rzymS, florencjaS)
        self.addLink(florencjaS, genuaS)
        self.addLink(florencjaS, mediolanS)
        self.addLink(genuaS, mediolanS)
        self.addLink(turynS, mediolanS)
        self.addLink(turynS, genuaS)
        self.addLink(turynS, boloniaS)
        self.addLink(mediolanS, boloniaS)


topos = {'mytopo': (lambda: MyTopo())}

from unittest import TestCase
from nose.plugins.skip import Skip, SkipTest
from pyhpeimc.tests.test_machine import *
from pyhpeimc.plat.termaccess import *

class TestGet_real_time_locate(TestCase):
    def test_get_real_time_locate_type(self):
        found_device = get_real_time_locate(term_access_host, auth.creds, auth.url)
        self.assertIs(type(found_device), list)
        self.assertIs(type(found_device[0]), dict)


    def test_get_real_time_locate_content(self):
        found_device = get_real_time_locate(term_access_host, auth.creds, auth.url)
        self.assertIs(len(found_device[0]), 5)
        self.assertIn('ifIndex', found_device[0])
        self.assertIn('ifDesc', found_device[0])
        self.assertIn('locateIp', found_device[0])
        self.assertIn('deviceIp', found_device[0])
        self.assertIn('deviceId', found_device[0])


    def test_get_real_time_locate_doesnt_exist(self):
        found_device = get_real_time_locate(DoesntExist, auth.creds, auth.url)
        self.assertIs(type(found_device), int)
        self.assertEqual(found_device, 403)







#Template for building Multiple Vendor Tests

"""============================================================================================="""

#####Test TEST_NAME_HERE for Multiple Vendor Devices

###Switches

#CW3_Switch
class TestGet_ip_mac_arp_list_CW3_Switch(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if CW3_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if CW3_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])

#CW5_Switch
class TestGet_ip_mac_arp_list_CW5_Switch(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if CW5_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if CW5_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


#CW7_Switch
class TestGet_ip_mac_arp_list_CW7_Switch(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if CW7_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if CW7_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


#Cisco_Switch
class TestGet_ip_mac_arp_list_Cisco_Switch(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if Cisco_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if Cisco_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


#Juniper_Switch
class TestGet_ip_mac_arp_list_Juniper_Switch(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if Juniper_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


#Arista_Switch
class TestGet_ip_mac_arp_list_Arista_Switch(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if Arista_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if Arista_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


#ArubaOS_Switch (Formerly Provision)
class TestGet_ip_mac_arp_list_ArubaOS_Switch(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


###Routers

#Cisco_Router
class TestGet_ip_mac_arp_list_Cisco_Router(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if Cisco_Router is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if Cisco_Router is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


#CW5_Router
class TestGet_ip_mac_arp_list_CW5_Router(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if CW5_Router is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if CW5_Router is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


#Juniper_Router (SRX)
class TestGet_ip_mac_arp_list_Juniper_Router(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if Juniper_Router is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if Juniper_Router is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


####Servers


#Windows_Server
class TestGet_ip_mac_arp_list_Windows_Server(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if Windows_Server is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if Windows_Server is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


#Linux_Server
class TestGet_ip_mac_arp_list_Linux_Server(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if Linux_Server is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if Linux_Server is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


###Hypervisors


#ESX
class TestGet_ip_mac_arp_list_ESX(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if ESX is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=ESX)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if ESX is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=ESX)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


#HyperV
class TestGet_ip_mac_arp_list_HyperV(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if HyperV is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=HyperV)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if HyperV is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=HyperV)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


#DoesntExist

class TestGet_ip_mac_arp_list_DoesntExist(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if DoesntExist is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=DoesntExist)
        self.assertIs(type(ip_mac_list), int)
        self.assertEqual(ip_mac_list, 403)



"""============================================================================================="""

#####Test for Terminal Access - IP Address Manager Functions


class TestGet_Get_ip_scope(TestCase):
    def test_get_ip_scope_type(self):
        delete_ip_scope('10.50.0.0/24', auth.creds, auth.url)
        new_scope = add_ip_scope('10.50.0.1', '10.50.0.254', 'cyoung', 'test group', auth.creds, auth.url)
        ip_scope_list = get_ip_scope(auth.creds, auth.url)
        self.assertIs(type(ip_scope_list), list)
        delete_ip_scope('10.50.0.0/24', auth.creds, auth.url)


    def test_get_ip_scope_content(self):
        delete_ip_scope('10.50.0.0/24', auth.creds, auth.url)
        new_scope = add_ip_scope('10.50.0.1', '10.50.0.254', 'cyoung', 'test group', auth.creds, auth.url)
        ip_scope_list = get_ip_scope(auth.creds, auth.url)
        self.assertIs(len(ip_scope_list[0]), 7)
        self.assertIn('name', ip_scope_list[0])
        self.assertIn('description', ip_scope_list[0])
        self.assertIn('id', ip_scope_list[0])
        self.assertIn('ip', ip_scope_list[0])
        self.assertIn('parentId', ip_scope_list[0])
        self.assertIn('percent', ip_scope_list[0])
        self.assertIn('percentStr', ip_scope_list[0])
        delete_ip_scope('10.50.0.0/24', auth.creds, auth.url)



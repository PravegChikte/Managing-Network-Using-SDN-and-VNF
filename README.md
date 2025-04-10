

---

```
 🚀 Managing Network Using SDN and NFV

![Project Banner](https://img.shields.io/badge/SDN--NFV-Network--Management-blue?style=flat-square)  
**Capstone Project | Final Year | Software Defined Networking + Network Function Virtualization**

---

 📌 About the Project

This project demonstrates a hybrid networking model by integrating **Software Defined Networking (SDN)** with **Network Function Virtualization (NFV)** to manage and optimize virtual ISP-level networks. It uses:

- 🛠️ **Mininet** for virtual topology
- 🌐 **OpenDaylight** as the SDN Controller
- ☁️ **OpenStack** for NFV services
- 🧠 **Custom Python Scripts** to enable NAT, routing, and service logic

---

## 🧱 Project Architecture

```bash
+--------------------+
|  OpenStack (NFV)   |
|   └── Virtual Instances (Web, File, VPN Servers)
+--------------------+
       ↑   ↓
   [ Internet Access ]
       ↑   ↓
+--------------------+
|  OpenDaylight SDN  |
|   └── Flow Rules + Controller Logic
+--------------------+
       ↑   ↓
+--------------------+
|   Mininet Topology |
|   └── Hosts + Switches (Core + Access) + NAT Gateways
+--------------------+
```

---

## ⚙️ Setup Instructions

### 🔧 Prerequisites
- Ubuntu 20.04 / 22.04 (Recommended)
- Git, Python3, Mininet, Open vSwitch
- POX or OpenDaylight Controller
- Optional: OpenStack for NFV

---

### 🛠️ Installation

```
# Clone this repository
git clone https://github.com/<your-username>/sdn-nfv-project.git
cd sdn-nfv-project

# Run your custom topology
sudo python3 finaltopo.py
```

Make sure your SDN controller (like POX) is already running:

```
# Example: Starting POX controller
cd pox
./pox.py forwarding.l2_learning
```

---

## 🌐 What This Project Includes

- 🔁 Custom Mininet Topology with 12 Hosts & 7 Switches
- 🌍 Internet Access via NAT for all subnets
- 📦 Subnet-based segmentation (100.0.0.0/8, 200.0.0.0/8, 150.0.0.0/8)
- 🛡️ Firewall, NAT, Routing, Load Balancer, VPN services via OpenStack
- 📊 Flow visualization using FlowGlance (custom tool)
- 🔄 Redundancy & Load Balancing via OpenDaylight flows

---

## 🧪 Testing

Inside Mininet CLI:

```
pingall                      # Check host connectivity
xterm h1 h2                  # Open terminals for hosts
h1 wget google.com           # Test external access
```

---

## 📚 Technologies Used

- 💻 Python
- ⚙️ Mininet
- 📡 OpenDaylight (Hydrogen)
- ☁️ OpenStack (Icehouse with DevStack)
- 🧠 POX Controller (Optional)
- 🔒 IPTables, NAT, VNC, GRE tunneling

---

## 🤝 Team Members

- Swarali Limaye 
- Saharsh Vaidya 
- Praveg Chikte 

---

## ⭐ Future Work

- 📈 Add Dockerized deployment
- 📊 Integrate AI/ML for adaptive flow rules
- 🔐 Enhance NFV functions with IDS/IPS logic
- 🌎 Multi-company, scalable NFV/SDN testbed

---

## 📄 License

MIT License – Feel free to use and modify this project!

---

Made with 💡, ☕, and a passion for networking innovation.

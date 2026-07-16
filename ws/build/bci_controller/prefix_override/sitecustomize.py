import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/abdelsalam/Hybrid-Adaptive-BCI-ROS2/ws/install/bci_controller'

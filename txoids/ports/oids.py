# -*- coding: utf-8 -*-


OIDS_MAP = {
    'D-Link DES-3200-28/C': {
        'medium_type': {
            'oid': '.1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.2',
            'values': {'1': 'copper', '2': 'fiber'}
        },
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.11.113.5.1.2.3.2.1.10',
            'values': {'1': 'auto', '2': 'normal', '3': 'cross'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.11.113.5.1.2.3.2.1.6',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_state': {
            'oid': '.1.3.6.1.4.1.171.11.113.5.1.2.3.2.1.5',
            'values': {
                '1': 'other', '2': 'nway-enabled', '3': 'nway-disabled-10Mbps-Half',
                '4': 'nway-disabled-10Mbps-Full', '5': 'nway-disabled-100Mbps-Half',
                '6': 'nway-disabled-100Mbps-Full', '7': 'nway-disabled-1Gigabps-Half',
                '8': 'nway-disabled-1Gigabps-Full', '9': 'nway-disabled-1Gigabps-Full-master',
                '10': 'nway-disabled-1Gigabps-Full-slave'
            }
        },
        'admin_state': {
            'oid': '.1.3.6.1.4.1.171.11.113.5.1.2.3.2.1.4',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_status': {
            'oid': '.1.3.6.1.4.1.171.11.113.5.1.2.3.1.1.6',
            'values': {
                '0': 'other', '1': 'empty', '2': 'link-down', '3': 'half-10Mbps',
                '4': 'full-10Mbps', '5': 'half-100Mbps', '6': 'full-100Mbps',
                '7': 'half-1Gigabps', '8': 'full-1Gigabps', '9': 'full-10Gigabps'
            }
        }
    },
    'D-Link DES-3200-18/C': {
        'medium_type': {
            'oid': '.1.3.6.1.4.1.171.11.113.3.1.2.3.1.1.2',
            'values': {'1': 'copper', '2': 'fiber'}
        },
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.11.113.3.1.2.3.2.1.10',
            'values': {'1': 'auto', '2': 'normal', '3': 'cross'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.11.113.3.1.2.3.2.1.6',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_state': {
            'oid': '.1.3.6.1.4.1.171.11.113.3.1.2.3.2.1.5',
            'values': {
                '1': 'other', '2': 'nway-enabled', '3': 'nway-disabled-10Mbps-Half',
                '4': 'nway-disabled-10Mbps-Full', '5': 'nway-disabled-100Mbps-Half',
                '6': 'nway-disabled-100Mbps-Full', '7': 'nway-disabled-1Gigabps-Half',
                '8': 'nway-disabled-1Gigabps-Full', '9': 'nway-disabled-1Gigabps-Full-master',
                '10': 'nway-disabled-1Gigabps-Full-slave'
            }
        },
        'admin_state': {
            'oid': '.1.3.6.1.4.1.171.11.113.3.1.2.3.2.1.4',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_status': {
            'oid': '.1.3.6.1.4.1.171.11.113.3.1.2.3.1.1.6',
            'values': {
                '0': 'other', '1': 'empty', '2': 'link-down', '3': 'half-10Mbps',
                '4': 'full-10Mbps', '5': 'half-100Mbps', '6': 'full-100Mbps',
                '7': 'half-1Gigabps', '8': 'full-1Gigabps', '9': 'full-10Gigabps'
            }
        }
    },
    'D-Link DES-3200-10/C': {
        'medium_type': {
            'oid': '.1.3.6.1.4.1.171.11.113.2.1.2.3.1.1.2',
            'values': {'1': 'copper', '2': 'fiber'}
        },
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.11.113.2.1.2.3.2.1.10',
            'values': {'1': 'auto', '2': 'normal', '3': 'cross'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.11.113.2.1.2.3.2.1.6',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_state': {
            'oid': '.1.3.6.1.4.1.171.11.113.2.1.2.3.2.1.5',
            'values': {
                '1': 'other', '2': 'nway-enabled', '3': 'nway-disabled-10Mbps-Half',
                '4': 'nway-disabled-10Mbps-Full', '5': 'nway-disabled-100Mbps-Half',
                '6': 'nway-disabled-100Mbps-Full', '7': 'nway-disabled-1Gigabps-Half',
                '8': 'nway-disabled-1Gigabps-Full', '9': 'nway-disabled-1Gigabps-Full-master',
                '10': 'nway-disabled-1Gigabps-Full-slave'
            }
        },
        'admin_state': {
            'oid': '.1.3.6.1.4.1.171.11.113.2.1.2.3.2.1.4',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_status': {
            'oid': '.1.3.6.1.4.1.171.11.113.2.1.2.3.1.1.6',
            'values': {
                '0': 'other', '1': 'empty', '2': 'link-down', '3': 'half-10Mbps',
                '4': 'full-10Mbps', '5': 'half-100Mbps', '6': 'full-100Mbps',
                '7': 'half-1Gigabps', '8': 'full-1Gigabps', '9': 'full-10Gigabps'
            }
        }
    },
    'D-Link DES-3200-28': {
        'medium_type': {
            'oid': '.1.3.6.1.4.1.171.11.113.1.3.2.2.1.1.2',
            'values': {'100': 'copper', '101': 'fiber'}
        },
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.10',
            'values': {'1': 'auto', '2': 'normal', '3': 'cross', '4': 'other'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.5',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_state': {
            'oid': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4',
            'values': {
                '1': 'nway-auto', '2': 'nway-disabled-10Mbps-Half',
                '3': 'nway-disabled-10Mbps-Full', '4': 'nway-disabled-100Mbps-Half',
                '5': 'nway-disabled-100Mbps-Full', '7': 'nway-disabled-1Gigabps-Full',
                '8': 'nway-disabled-1Gigabps-Full-Master', '9': 'nway-disabled-1Gigabps-Full-Slave'
            }
        },
        'admin_state': {
            'oid': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.3',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_status': {
            'oid': '.1.3.6.1.4.1.171.11.113.1.3.2.2.1.1.5',
            'values': {
                '1': 'auto', '2': 'half-10Mbps', '3': 'full-10Mbps',
                '4': 'half-100Mbps', '5': 'full-100Mbps', '7': 'full-1Gigabps'
            }
        }
    },
    'D-Link DES-3200-18': {
        'medium_type': {
            'oid': '.1.3.6.1.4.1.171.11.113.1.2.2.2.1.1.2',
            'values': {'100': 'copper', '101': 'fiber'}
        },
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.11.113.1.2.2.2.2.1.10',
            'values': {'1': 'auto', '2': 'normal', '3': 'cross', '4': 'other'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.11.113.1.2.2.2.2.1.5',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_state': {
            'oid': '.1.3.6.1.4.1.171.11.113.1.2.2.2.2.1.4',
            'values': {
                '1': 'nway-auto', '2': 'nway-disabled-10Mbps-Half',
                '3': 'nway-disabled-10Mbps-Full', '4': 'nway-disabled-100Mbps-Half',
                '5': 'nway-disabled-100Mbps-Full', '7': 'nway-disabled-1Gigabps-Full',
                '8': 'nway-disabled-1Gigabps-Full-Master', '9': 'nway-disabled-1Gigabps-Full-Slave'
            }
        },
        'admin_state': {
            'oid': '.1.3.6.1.4.1.171.11.113.1.2.2.2.2.1.3',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_status': {
            'oid': '.1.3.6.1.4.1.171.11.113.1.2.2.2.1.1.5',
            'values': {
                '1': 'auto', '2': 'half-10Mbps', '3': 'full-10Mbps',
                '4': 'half-100Mbps', '5': 'full-100Mbps', '7': 'full-1Gigabps'
            }
        }
    },
    'D-Link DES-3200-10': {
        'medium_type': {
            'oid': '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.2',
            'values': {'100': 'copper', '101': 'fiber'}
        },
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.10',
            'values': {'1': 'auto', '2': 'normal', '3': 'cross', '4': 'other'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.5',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_state': {
            'oid': '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4',
            'values': {
                '1': 'nway-auto', '2': 'nway-disabled-10Mbps-Half',
                '3': 'nway-disabled-10Mbps-Full', '4': 'nway-disabled-100Mbps-Half',
                '5': 'nway-disabled-100Mbps-Full', '7': 'nway-disabled-1Gigabps-Full',
                '8': 'nway-disabled-1Gigabps-Full-Master', '9': 'nway-disabled-1Gigabps-Full-Slave'
            }
        },
        'admin_state': {
            'oid': '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.3',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_status': {
            'oid': '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.5',
            'values': {
                '1': 'auto', '2': 'half-10Mbps', '3': 'full-10Mbps',
                '4': 'half-100Mbps', '5': 'full-100Mbps', '7': 'full-1Gigabps'
            }
        }
    },
    'D-Link DGS-3120-24SC': {
        'medium_type': {
            'oid': '.1.3.6.1.4.1.171.11.117.1.3.2.3.1.1.2',
            'values': {'1': 'copper', '2': 'fiber'}
        },
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.11.117.1.3.2.3.2.1.10',
            'values': {'1': 'auto', '2': 'normal', '3': 'cross'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.11.117.1.3.2.3.2.1.6',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_state': {
            'oid': '.1.3.6.1.4.1.171.11.117.1.3.2.3.2.1.5',
            'values': {
                '1': 'other', '2': 'nway-enabled',
                '3': 'nway-disabled-10Mbps-Half', '4': 'nway-disabled-10Mbps-Full',
                '5': 'nway-disabled-100Mbps-Half', '6': 'nway-disabled-100Mbps-Full',
                '7': 'nway-disabled-1Gigabps-Half',
                '8': 'nway-disabled-1Gigabps-Full', '9': 'nway-disabled-1Gigabps-Full-master',
                '10': 'nway-disabled-1Gigabps-Full-slave'
            }
        },

        'admin_state': {
            'oid': '.1.3.6.1.4.1.171.11.117.1.3.2.3.2.1.4',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_status': {
            'oid': '.1.3.6.1.4.1.171.11.117.1.3.2.3.1.1.6',
            'values': {
                '0': 'link-down', '1': 'full-10Mbps-8023x',
                '2': 'full-10Mbps-none', '3': 'half-10Mbps-backp',
                '4': 'half-10Mbps-none', '5': 'full-100Mbps-8023x',
                '6': 'full-100Mbps-none', '7': 'half-100Mbps-backp',
                '8': 'half-100Mbps-none', '9': 'full-1Gigabps-8023x',
                '10': 'full-1Gigabps-none', '11': 'half-1Gigabps-backp',
                '12': 'half-1Gigabps-none', '13': 'full-10Gigabps-8023x',
                '14': 'full-10Gigabps-none', '15': 'half-10Gigabps-8023x',
                '16': 'half-10Gigabps-none', '17': 'empty', '18': 'err-disabled'
            }
        }
    },

    'D-Link DGS-3120-24TC': {
        'medium_type': {
            'oid': '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.2',
            'values': {'1': 'copper', '2': 'fiber'}
        },
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.10',
            'values': {'1': 'auto', '2': 'normal', '3': 'cross'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.6',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_state': {
            'oid': '.1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.5',
            'values': {
                '1': 'other', '2': 'nway-enabled',
                '3': 'nway-disabled-10Mbps-Half', '4': 'nway-disabled-10Mbps-Full',
                '5': 'nway-disabled-100Mbps-Half', '6': 'nway-disabled-100Mbps-Full',
                '7': 'nway-disabled-1Gigabps-Half',
                '8': 'nway-disabled-1Gigabps-Full', '9': 'nway-disabled-1Gigabps-Full-master',
                '10': 'nway-disabled-1Gigabps-Full-slave'
            }
        },

        'admin_state': {
            'oid': '.1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.4',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_status': {
            'oid': '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.6',
            'values': {
                '0': 'link-down', '1': 'full-10Mbps-8023x',
                '2': 'full-10Mbps-none', '3': 'half-10Mbps-backp',
                '4': 'half-10Mbps-none', '5': 'full-100Mbps-8023x',
                '6': 'full-100Mbps-none', '7': 'half-100Mbps-backp',
                '8': 'half-100Mbps-none', '9': 'full-1Gigabps-8023x',
                '10': 'full-1Gigabps-none', '11': 'half-1Gigabps-backp',
                '12': 'half-1Gigabps-none', '13': 'full-10Gigabps-8023x',
                '14': 'full-10Gigabps-none', '15': 'half-10Gigabps-8023x',
                '16': 'half-10Gigabps-none', '17': 'empty', '18': 'err-disabled'
            }
        }
    },
    "D-Link DES-3028": {
        'medium_type': {
            'oid': '.1.3.6.1.4.1.171.11.63.6.2.2.1.1.2',
            'values': {'100': 'copper', '101': 'fiber'}
        },
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.11.63.6.2.2.2.1.10',
            'values': {'1': 'auto', '2': 'normal', '3': 'cross', '4': 'other'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.11.63.6.2.2.2.1.5',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_state': {
            'oid': '.1.3.6.1.4.1.171.11.63.6.2.2.2.1.4',
            'values': {
                '1': 'nway-auto', '2': 'nway-disabled-10Mbps-Half',
                '3': 'nway-disabled-10Mbps-Full', '4': 'nway-disabled-100Mbps-Half',
                '5': 'nway-disabled-100Mbps-Full', '7': 'nway-disabled-1Gigabps-Full',
                '8': 'nway-disabled-1Gigabps-Full-Master', '9': 'nway-disabled-1Gigabps-Full-Slave'
            }
        },
        'admin_state': {
            'oid': '.1.3.6.1.4.1.171.11.63.6.2.2.2.1.3',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_status': {
            'oid': '.1.3.6.1.4.1.171.11.63.6.2.2.1.1.5',
            'values': {
                '1': 'auto', '2': 'half-10Mbps', '3': 'full-10Mbps',
                '4': 'half-100Mbps', '5': 'full-100Mbps', '7': 'full-1Gigabps'
            }
        }
    },
    "D-Link DES-3028G": {
        'medium_type': {
            'oid': '.1.3.6.1.4.1.171.11.63.11.2.2.1.1.2',
            'values': {'100': 'copper', '101': 'fiber'}
        },
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.11.63.11.2.2.2.1.10',
            'values': {'1': 'auto', '2': 'normal', '3': 'cross', '4': 'other'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.11.63.11.2.2.2.1.5',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_state': {
            'oid': '.1.3.6.1.4.1.171.11.63.11.2.2.2.1.4',
            'values': {
                '1': 'nway-auto', '2': 'nway-disabled-10Mbps-Half',
                '3': 'nway-disabled-10Mbps-Full', '4': 'nway-disabled-100Mbps-Half',
                '5': 'nway-disabled-100Mbps-Full', '7': 'nway-disabled-1Gigabps-Full',
                '8': 'nway-disabled-1Gigabps-Full-Master', '9': 'nway-disabled-1Gigabps-Full-Slave'
            }
        },
        'admin_state': {
            'oid': '.1.3.6.1.4.1.171.11.63.11.2.2.2.1.3',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_status': {
            'oid': '.1.3.6.1.4.1.171.11.63.11.2.2.1.1.5',
            'values': {
                '1': 'auto', '2': 'half-10Mbps', '3': 'full-10Mbps',
                '4': 'half-100Mbps', '5': 'full-100Mbps', '7': 'full-1Gigabps'
            }
        }
    },
    "D-Link DES-3010G": {
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.11.63.1.2.2.2.2.1.10',
            'values': {'1': 'auto', '2': 'normal', '3': 'cross'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.11.63.1.2.2.2.2.1.4',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_state': {
            'oid': '.1.3.6.1.4.1.171.11.63.1.2.2.2.2.1.3',
            'values': {
                '1': 'nway-auto', '2': 'nway-disabled-10Mbps-Half',
                '3': 'nway-disabled-10Mbps-Full', '4': 'nway-disabled-100Mbps-Half',
                '5': 'nway-disabled-100Mbps-Full', '7': 'nway-disabled-1Gigabps-Full',
            }
        },
        'admin_state': {
            'oid': '.1.3.6.1.4.1.171.11.63.1.2.2.2.2.1.2',
            'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
        },
        'nway_status': {
            'oid': '.1.3.6.1.4.1.171.11.63.1.2.2.2.1.1.5',
            'values': {
                '1': 'auto', '2': 'full-10Mbps-8023x', '3': 'full-10Mbps-none',
                '4': 'half-10Mbps-backp', '5': 'half-10Mbps-none',
                '6': 'full-100Mbps-8023x', '7': 'full-100Mbps-none',
                '8': 'half-100Mbps-backp', '9': 'half-100Mbps-none',
                '10': 'full-1Gigabps-8023x', '11': 'full-1Gigabps-none',
                '12': 'half-1Gigabps-backp', '13': 'half-1Gigabps-none'
            }
        }
    },
    'D-Link DGS-3100-24': {
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.28',
            'values': {'1': 'cross', '2': 'normal', '3': 'auto'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.14',
            'values': {
                '1': 'on', '2': 'off', '3': 'autoNegotiation', '4': 'enabledRx',
                '5': 'enabledTx'
            }
        },
        'nway_state_duplex': {
            'oid': '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.3',
            'values': {
                '1': 'none', '2': 'half', '3': 'full',
            }
        },
        'nway_state_speed': {
            'oid': '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.15',
            'values': {
            }
        },
        'nway_status_duplex': {
            'oid': '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.4',
            'values': {
                '1': 'half', '2': 'full', '3': 'hybrid', '4': 'unknown'
            }
        },
        'nway_status_speed': {
            'oid': '.1.3.6.1.2.1.31.1.1.1.15',
            'values': {
            }
        }
    },
    "D-Link DGS-3100-24TG": {
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.28',
            'values': {'1': 'cross', '2': 'normal', '3': 'auto'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.14',
            'values': {
                '1': 'on', '2': 'off', '3': 'autoNegotiation', '4': 'enabledRx',
                '5': 'enabledTx'
            }
        },
        'nway_state_duplex': {
            'oid': '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.3',
            'values': {
                '1': 'none', '2': 'half', '3': 'full',
            }
        },
        'nway_state_speed': {
            'oid': '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.15',
            'values': {
            }
        },
        'nway_status_duplex': {
            'oid': '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.4',
            'values': {
                '1': 'half', '2': 'full', '3': 'hybrid', '4': 'unknown'
            }
        },
        'nway_status_speed': {
            'oid': '.1.3.6.1.2.1.31.1.1.1.15',
            'values': {
            }
        }
    },
    'D-Link DGS-1210-28ME': {
        'medium_type': {
            'oid': '.1.3.6.1.4.1.171.10.76.28.1.1.13.1.2',
            'values': {
                '1': 'copper', '2': 'fiber'
            }
        },
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.10.76.28.1.1.13.1.5',
            'values': {'1': 'auto', '2': 'mdi', '3': 'mdix'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.10.76.28.1.1.13.1.7',
            'values': {
                '1': 'enabled', '2': 'disabled'
            }
        },
        'nway_state': {
            'oid': '.1.3.6.1.4.1.171.10.76.28.1.1.13.1.3',
            'values': {
                '1': 'rate1000M-Full', '2': 'rate100M-Full',
                '3': 'rate100M-Half', '4': 'rate10M-Full', '5': 'rate10M-Half',
                '6': 'auto', '7': 'disable'
            }
        },
        'nway_status': {
            'oid': '.1.3.6.1.4.1.171.10.76.28.1.1.13.1.4',
            'values': {
                '1': 'down', '2': 'rate1000M-Full', '3': 'rate100M-Full',
                '4': 'rate100M-Half', '5': 'rate10M-Full', '6': 'rate10M-Half',
                '7': 'rate10G-Full'
            }
        }
    },
    "D-Link DGS-1210-12TS/ME": {
        'medium_type': {
            'oid': '.1.3.6.1.4.1.171.10.76.44.1.1.13.1.2',
            'values': {
                '1': 'copper', '2': 'fiber'
            }
        },
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.10.76.44.1.1.13.1.5',
            'values': {'1': 'auto', '2': 'mdi', '3': 'mdix'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.10.76.44.1.1.13.1.7',
            'values': {
                '1': 'enabled', '2': 'disabled'
            }
        },
        'nway_state': {
            'oid': '.1.3.6.1.4.1.171.10.76.44.1.1.13.1.3',
            'values': {
                '1': 'rate1000M-Full', '2': 'rate100M-Full',
                '3': 'rate100M-Half', '4': 'rate10M-Full', '5': 'rate10M-Half',
                '6': 'auto', '7': 'disable'
            }
        },
        'nway_status': {
            'oid': '.1.3.6.1.4.1.171.10.76.44.1.1.13.1.4',
            'values': {
                '1': 'down', '2': 'rate1000M-Full', '3': 'rate100M-Full',
                '4': 'rate100M-Half', '5': 'rate10M-Full', '6': 'rate10M-Half',
                '7': 'rate10G-Full'
            }
        }
    },
    "D-Link DGS-1210-28/ME": {
        'medium_type': {
            'oid': '.1.3.6.1.4.1.171.10.76.28.1.1.13.1.2',
            'values': {
                '1': 'copper', '2': 'fiber'
            }
        },
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.10.76.28.1.1.13.1.5',
            'values': {'1': 'auto', '2': 'mdi', '3': 'mdix'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.10.76.28.1.1.13.1.7',
            'values': {
                '1': 'enabled', '2': 'disabled'
            }
        },
        'nway_state': {
            'oid': '.1.3.6.1.4.1.171.10.76.28.1.1.13.1.3',
            'values': {
                '1': 'rate1000M-Full', '2': 'rate100M-Full',
                '3': 'rate100M-Half', '4': 'rate10M-Full', '5': 'rate10M-Half',
                '6': 'auto', '7': 'disable'
            }
        },
        'nway_status': {
            'oid': '.1.3.6.1.4.1.171.10.76.28.1.1.13.1.4',
            'values': {
                '1': 'down', '2': 'rate1000M-Full', '3': 'rate100M-Full',
                '4': 'rate100M-Half', '5': 'rate10M-Full', '6': 'rate10M-Half',
                '7': 'rate10G-Full'
            }
        }
    },
    "D-Link DGS-1210-10/ME": {
        'medium_type': {
            'oid': '.1.3.6.1.4.1.171.10.76.35.1.1.13.1.2',
            'values': {
                '1': 'copper', '2': 'fiber'
            }
        },
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.10.76.35.1.1.13.1.5',
            'values': {'1': 'auto', '2': 'mdi', '3': 'mdix'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.10.76.35.1.1.13.1.7',
            'values': {
                '1': 'enabled', '2': 'disabled'
            }
        },
        'nway_state': {
            'oid': '.1.3.6.1.4.1.171.10.76.35.1.1.13.1.3',
            'values': {
                '1': 'rate1000M-Full', '2': 'rate100M-Full',
                '3': 'rate100M-Half', '4': 'rate10M-Full', '5': 'rate10M-Half',
                '6': 'auto', '7': 'disable'
            }
        },
        'nway_status': {
            'oid': '.1.3.6.1.4.1.171.10.76.35.1.1.13.1.4',
            'values': {
                '1': 'down', '2': 'rate1000M-Full', '3': 'rate100M-Full',
                '4': 'rate100M-Half', '5': 'rate10M-Full', '6': 'rate10M-Half',
                '7': 'rate10G-Full'
            }
        }
    },
    "D-Link DGS-3000-28SC": {
        'medium_type': {
            'oid': '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.2',
            'values': {
                '1': 'copper', '2': 'fiber'
            }
        },
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.11.133.5.1.2.3.2.1.10',
            'values': {'1': 'auto', '2': 'normal', '3': 'cross'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.11.133.5.1.2.3.2.1.6',
            'values': {
                'values': {'1': 'other', '2': 'disabled', '3': 'enabled'}
            }
        },
        'nway_state': {
            'oid': '.1.3.6.1.4.1.171.11.133.5.1.2.3.2.1.5',
            'values': {
                '1': 'other', '2': 'nway-enabled', '3': 'nway-disabled-10Mbps-Half',
                '4': 'nway-disabled-10Mbps-Full', '5': 'nway-disabled-100Mbps-Half',
                '6': 'nway-disabled-100Mbps-Full', '7': 'nway-disabled-1Gigabps-Half',
                '8': 'nway-disabled-1Gigabps-Full', '9': 'nway-disabled-1Gigabps-Full-master',
                '10': 'nway-disabled-1Gigabps-Full-slave'
            }
        },
        'nway_status': {
            'oid': '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.6',
            'values': {
                '0': 'link-down', '1': 'full-10Mbps-8023x',
                '2': 'full-10Mbps-none', '3': 'half-10Mbps-backp',
                '4': 'half-10Mbps-none', '5': 'full-100Mbps-8023x',
                '6': 'full-100Mbps-none', '7': 'half-100Mbps-backp',
                '8': 'half-100Mbps-none', '9': 'full-1Gigabps-8023x',
                '10': 'full-1Gigabps-none', '11': 'half-1Gigabps-backp',
                '12': 'half-1Gigabps-none', '13': 'full-10Gigabps-8023x',
                '14': 'full-10Gigabps-none', '15': 'half-10Gigabps-8023x',
                '16': 'half-10Gigabps-none', '17': 'empty', '18': 'err-disabled'
            }
        }
    },
    "D-Link DGS-1210-20/ME": {
        'medium_type': {
            'oid': '.1.3.6.1.4.1.171.10.76.31.1.1.13.1.2',
            'values': {
                '1': 'copper', '2': 'fiber'
            }
        },
        'mdix': {
            'oid': '.1.3.6.1.4.1.171.10.76.31.1.1.13.1.5',
            'values': {'1': 'auto', '2': 'mdi', '3': 'mdix'}
        },
        'flow_control': {
            'oid': '.1.3.6.1.4.1.171.10.76.31.1.1.13.1.7',
            'values': {
                '1': 'enabled', '2': 'disabled'
            }
        },
        'nway_state': {
            'oid': '.1.3.6.1.4.1.171.10.76.31.1.1.13.1.3',
            'values': {
                '1': 'rate1000M-Full', '2': 'rate100M-Full',
                '3': 'rate100M-Half', '4': 'rate10M-Full', '5': 'rate10M-Half',
                '6': 'auto', '7': 'disable'
            }
        },
        'nway_status': {
            'oid': '.1.3.6.1.4.1.171.10.76.31.1.1.13.1.4',
            'values': {
                '1': 'down', '2': 'rate1000M-Full', '3': 'rate100M-Full',
                '4': 'rate100M-Half', '5': 'rate10M-Full', '6': 'rate10M-Half',
                '7': 'rate10G-Full'
            }
        }
    }
}

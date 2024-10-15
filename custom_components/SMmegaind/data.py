FULL_NAME="Industrial Automation"
LINK="https://sequentmicrosystems.com/products/industrial-raspberry-pi?variant=46030010810620"

import megaind
API = megaind
DOMAIN = "SMmegaind"
NAME_PREFIX = "smmi"
SM_MAP = {
    "button": {
        "opto_cnt_rst": {
            "chan_no": 4,
            "com": {
                "set": "rstOptoCount",
            },
        }
    },
    "sensor":  {
        "0_10_u_in": {
                "chan_no": 4,
                "uom": "V",
                "com": {
                    "get": "get0_10In",
                },
        },
        "pm10_u_in": {
                "chan_no": 4,
                "uom": "V",
                "com": {
                    "get": "getpmIn",
                },
        },
        "4_20_i_in": {
                "chan_no": 4,
                "uom": "mA",
                "com": {
                    "get": "get4_20In",
                },
        },
        "opto": {
                "chan_no": 4,
                "uom": "",
                "com": {
                    "get": "getOptoCh",
                },
                "icon": {
                    "on": "mdi:numeric-1",
                }
        },
        "opto_cnt": {
                "chan_no": 4,
                "uom": "",
                "com": {
                    "get": "getOptoCount",
                },
        },
        "owb_temp": {
                "chan_no": 16,
                "uom": "°C",
                "com": {
                    "get": "owdGetTemp",
                },
        },
    },
    "switch": {
        "led": {
                "chan_no": 4,
                "com": {
                    "get": "getLed",
                    "set": "setLed",
                },
        }
    },
    "number": {
        "0_10_u_out": {
                "chan_no": 4,
                "uom": "V",
                "min_value": 0.0,
                "max_value": 10.0,
                "step": 0.01,
                "com": {
                    "get": "get0_10Out",
                    "set": "set0_10Out",
                },
        },
        "4_20_i_out": {
                "chan_no": 4,
                "uom": "mA",
                "min_value": 4.0,
                "max_value": 20.0,
                "step": 0.01,
                "com": {
                    "get": "get4_20Out",
                    "set": "set4_20Out",
                },
        },
        "od": {
                "chan_no": 4,
                "uom": "%",
                "min_value": 0.0,
                "max_value": 100.0,
                "step": 0.01,
                "com": {
                    "get": "getOdPWM",
                    "set": "setOdPWM"
                },
                "icon": {
                    "on": "mdi:percent",
                    "off": "mdi:percent"
                }
        },
    },
}

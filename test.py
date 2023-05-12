

from pysondb.client import PysonDBClient

import uuid

HOST, PORT = "localhost", 9999

payload =   [{
      "type": "action.devices.types.SPRINKLER",
      "traits": [
        "action.devices.traits.StartStop",
        "action.devices.traits.Timer"
      ],
      "name": {
        "name": "Sprinkler1",
        "defaultNames": [
          "Sprinkler1"
        ],
        "nicknames": [
          "Sprinkler1"
        ]
      },
      "willReportState": True,
      "roomHint": "Playground",
      "attributes": {
        "pausable": True,
        "availableZones": [],
        "maxTimerLimitSec": 1200,
        "commandOnlyTimer": False
      },
      "states": {
        "online": True,
        "onlineStatusDetails": "STATE_UNSPECIFIED",
        "timerRemainingSec": 940,
        "timerPaused": False,
        "isPaused": False,
        "isRunning": True,
        "activeZones": [],
        "expectedStartStopCompletionUnixTimestampSec": 0
      },
      "suv": {
        "enabled": False,
        "challengeType": "pinNeeded",
        "pincode": "1234",
        "allowRetry": False,
        "rejectErrorCode": "pinIncorrect"
      }
    },
    {
      "type": "action.devices.types.LIGHT",
      "traits": [
        "action.devices.traits.OnOff",
        "action.devices.traits.Brightness",
        "action.devices.traits.ColorSetting",
        "action.devices.traits.LightEffects"
      ],
      "name": {
        "name": "light2",
        "nicknames": [
          "light2"
        ]
      },
      "willReportState": True,
      "roomHint": "Playground",
      "attributes": {
        "commandOnlyOnOff": False,
        "queryOnlyOnOff": False,
        "commandOnlyBrightness": False,
        "commandOnlyColorSetting": False,
        "colorModel": "rgb",
        "colorTemperatureRange": {
          "temperatureMinK": 2000,
          "temperatureMaxK": 9000
        },
        "defaultSleepDuration": 1800,
        "defaultWakeDuration": 1800,
        "supportedEffects": [
          "colorLoop",
          "wake",
          "sleep"
        ]
      },
      "states": {
        "online": True,
        "onlineStatusDetails": "STATE_UNSPECIFIED",
        "brightness": 100,
        "color": {
          "temperatureK": 7500
        },
        "activeLightEffect": "",
        "lightEffectEndUnixTimestampSec": 0,
        "id": "",
        "activeEmulatedLightEffect": "",
        "emulatedLightEffectEndUnixTimestampSec": 0,
        "expectedEmulatedEffectBrightness": {},
        "expectedEmulatedEffectColorSetting": {},
        "on": False
      },
      "suv": {
        "enabled": False,
        "challengeType": "pinNeeded",
        "pincode": "1234",
        "allowRetry": False,
        "rejectErrorCode": "pinIncorrect"
      }
    },
    {
      "type": "action.devices.types.OUTLET",
      "traits": [
        "action.devices.traits.OnOff"
      ],
      "name": {
        "name": "outlet1",
        "nicknames": [
          "outlet1"
        ]
      },
      "willReportState": True,
      "roomHint": "Playground",
      "attributes": {
        "commandOnlyOnOff": False,
        "queryOnlyOnOff": False
      },
      "states": {
        "online": True,
        "onlineStatusDetails": "STATE_UNSPECIFIED",
        "on": True,
        "brightness": 83
      },
      "suv": {
        "enabled": False,
        "challengeType": "pinNeeded",
        "pincode": "1234",
        "allowRetry": False,
        "rejectErrorCode": "pinIncorrect"
      }
    },
    {
      "type": "action.devices.types.OUTLET",
      "traits": [
        "action.devices.traits.OnOff"
      ],
      "name": {
        "name": "outlet1",
        "nicknames": [
          "outlet1"
        ]
      },
      "willReportState": True,
      "roomHint": "Playground",
      "attributes": {
        "commandOnlyOnOff": False,
        "queryOnlyOnOff": False
      },
      "states": {
        "online": True,
        "onlineStatusDetails": "STATE_UNSPECIFIED",
        "on": True,
        "brightness": 83
      },
      "suv": {
        "enabled": False,
        "challengeType": "pinNeeded",
        "pincode": "1234",
        "allowRetry": False,
        "rejectErrorCode": "pinIncorrect"
      }
    },
    {
      "type": "action.devices.types.OUTLET",
      "traits": [
        "action.devices.traits.OnOff"
      ],
      "name": {
        "name": "outlet1",
        "nicknames": [
          "outlet1"
        ]
      },
      "willReportState": True,
      "roomHint": "Playground",
      "attributes": {
        "commandOnlyOnOff": False,
        "queryOnlyOnOff": False
      },
      "states": {
        "online": True,
        "onlineStatusDetails": "STATE_UNSPECIFIED",
        "on": True,
        "brightness": 83
      },
      "suv": {
        "enabled": False,
        "challengeType": "pinNeeded",
        "pincode": "1234",
        "allowRetry": False,
        "rejectErrorCode": "pinIncorrect"
      }
    },
    {
      "type": "action.devices.types.OUTLET",
      "traits": [
        "action.devices.traits.OnOff"
      ],
      "name": {
        "name": "outlet1",
        "nicknames": [
          "outlet1"
        ]
      },
      "willReportState": True,
      "roomHint": "Playground",
      "attributes": {
        "commandOnlyOnOff": False,
        "queryOnlyOnOff": False
      },
      "states": {
        "online": True,
        "onlineStatusDetails": "STATE_UNSPECIFIED",
        "on": True,
        "brightness": 83
      },
      "suv": {
        "enabled": False,
        "challengeType": "pinNeeded",
        "pincode": "1234",
        "allowRetry": False,
        "rejectErrorCode": "pinIncorrect"
      }
    },
    {
      "type": "action.devices.types.OUTLET",
      "traits": [
        "action.devices.traits.OnOff"
      ],
      "name": {
        "name": "outlet1",
        "nicknames": [
          "outlet1"
        ]
      },
      "willReportState": True,
      "roomHint": "Playground",
      "attributes": {
        "commandOnlyOnOff": False,
        "queryOnlyOnOff": False
      },
      "states": {
        "online": True,
        "onlineStatusDetails": "STATE_UNSPECIFIED",
        "on": True,
        "brightness": 83
      },
      "suv": {
        "enabled": False,
        "challengeType": "pinNeeded",
        "pincode": "1234",
        "allowRetry": False,
        "rejectErrorCode": "pinIncorrect"
      }
    }
]


generator = "lambda: str(uuid.uuid4())"
#generator = "lambda: str(int(uuid.uuid4()))[:18]"

def main() -> int:
    s = PysonDBClient(HOST, PORT)
    ok = s.connect()
    while ok:
        print('?: ')
        data = input()
        if len(data) > 0:
            ok = data != "done"
            if ok:
                print (s.use_db("testfile3","google_devices"))
                print (s.set_id_generator(generator))
                ids = s.add_many(payload)
                for id in ids: 
                    print (s.get_by_id(id))
                print (s.get_all_by_section())
    s.close()

if __name__ == "__main__":
    main()



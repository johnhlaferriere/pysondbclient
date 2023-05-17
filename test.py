

from pysondb.client import PysonDBClient

import uuid

HOST, PORT = "localhost", 9999

payload =  [
  {
        "type": "action.devices.types.LIGHT",
    "traits": [
      "action.devices.traits.OnOff"
    ],
    "name": {
      "name": "Fence Lights",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
      "action.devices.traits.OnOff"
    ],
    "name": {
      "name": "Grape Vine Lights",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.SWITCH",
    "traits": [
      "action.devices.traits.OnOff"
    ],
    "name": {
      "name": "Yard Audio",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
      "action.devices.traits.OnOff"
    ],
    "name": {
      "name": "Box Lights (front)",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.SWITCH",
    "traits": [
      "action.devices.traits.OnOff"
    ],
    "name": {
      "name": "Cherry Tree Speakers",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
      "action.devices.traits.ColorSetting"
    ],
    "name": {
      "name": "Pool Lights",
      "defaultNames": [
        "Pool Lights"
      ],
      "nicknames": [
        "Pool Lights"
      ]
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False,
      "commandOnlyColorSetting": False,
      "colorModel": "rgb",
      "colorTemperatureRange": {
        "temperatureMinK": 2000,
        "temperatureMaxK": 5000
      }
    },
    "states": {
      "on": False,
      "color": {
        "spectrumRgb": 16711935
      },
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.SWITCH",
    "traits": [
      "action.devices.traits.OnOff"
    ],
    "name": {
      "name": "Pool Pump",
      "defaultNames": [
        "Pool Pump"
      ],
      "nicknames": [
        "Pool Pump"
      ]
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.SPRINKLER",
    "traits": [
      "action.devices.traits.StartStop"
    ],
    "name": {
      "name": "Back Yard Zone 2",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "pausable": False,
      "availableZones": [
        "kitchen",
        "bedroom",
        "living room"
      ]
    },
    "states": {
      "isPaused": False,
      "isRunning": False,
      "activeZones": [],
      "expectedStartStopCompletionUnixTimestampSec": 0,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.SWITCH",
    "traits": [
      "action.devices.traits.OnOff"
    ],
    "name": {
      "name": "Pool Oxidizer",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.SPRINKLER",
    "traits": [
      "action.devices.traits.StartStop"
    ],
    "name": {
      "name": "Garden Zone 4",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Garden Sprinklers",
    "attributes": {
      "pausable": False,
      "availableZones": [
        "kitchen",
        "bedroom",
        "living room"
      ]
    },
    "states": {
      "isPaused": False,
      "isRunning": False,
      "activeZones": [],
      "expectedStartStopCompletionUnixTimestampSec": 0,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
      "action.devices.traits.OnOff"
    ],
    "name": {
      "name": "Pump House Lights",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
      "name": "Waterfall Outlet",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.SWITCH",
    "traits": [
      "action.devices.traits.OnOff",
      "action.devices.traits.Toggles"
    ],
    "name": {
      "name": "Water Treatment",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False,
      "availableToggles": [
        {
          "name": "sterilization_toggle",
          "name_values": [
            {
              "name_synonym": [
                "Clean",
                "Bio clean"
              ],
              "lang": "en"
            }
          ]
        },
        {
          "name": "energysaving_toggle",
          "name_values": [
            {
              "name_synonym": [
                "Energy saving",
                "Eco"
              ],
              "lang": "en"
            }
          ]
        }
      ],
      "commandOnlyToggles": False,
      "queryOnlyToggles": False
    },
    "states": {
      "on": False,
      "currentToggleSettings": {
        "sterilization_toggle": True,
        "energysaving_toggle": False
      },
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.SPRINKLER",
    "traits": [
      "action.devices.traits.StartStop"
    ],
    "name": {
      "name": "Garden Raised Bed",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Garden Sprinkler",
    "attributes": {
      "pausable": False,
      "availableZones": [
        "kitchen",
        "bedroom",
        "living room"
      ]
    },
    "states": {
      "isPaused": False,
      "isRunning": False,
      "activeZones": [],
      "expectedStartStopCompletionUnixTimestampSec": 0,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
      "name": "Box Outlets",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.SWITCH",
    "traits": [
      "action.devices.traits.OnOff"
    ],
    "name": {
      "name": "Grape Vine Speakers",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
      "action.devices.traits.OnOff"
    ],
    "name": {
      "name": "Box Lights (back)",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
      "action.devices.traits.OnOff"
    ],
    "name": {
      "name": "Cabana Deck Lights",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.VALVE",
    "traits": [
      "action.devices.traits.OpenClose"
    ],
    "name": {
      "name": "Pool Water Supply",
      "defaultNames": [
        "Pool water Supply"
      ],
      "nicknames": [
        "Pool Water Supply"
      ]
    },
    "willReportState": True,
    "attributes": {
      "commandOnlyOpenClose": False,
      "discreteOnlyOpenClose": True,
      "openDirection": [
        "IN"
      ],
      "queryOnlyOpenClose": False
    },
    "states": {
      "openPercent": 0,
      "openDirection": "",
      "openState": [],
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.SWITCH",
    "traits": [
      "action.devices.traits.OnOff"
    ],
    "name": {
      "name": "Pool Deck Speakers",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
      "action.devices.traits.OnOff"
    ],
    "name": {
      "name": "Raised Box Lights",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.FAN",
    "traits": [
      "action.devices.traits.FanSpeed",
      "action.devices.traits.OnOff"
    ],
    "name": {
      "name": "Pump House Fan",
      "defaultNames": [
        "Pump House Fan"
      ],
      "nicknames": [
        "Pump House Fan"
      ]
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "reversible": False,
      "commandOnlyFanSpeed": False,
      "supportsFanSpeedPercent": False,
      "availableFanSpeeds": {
        "speeds": [
          {
            "speed_name": "speed_low",
            "speed_values": [
              {
                "speed_synonym": [
                  "low",
                  "slow"
                ],
                "lang": "en"
              }
            ]
          },
          {
            "speed_name": "speed_high",
            "speed_values": [
              {
                "speed_synonym": [
                  "high",
                  "fast"
                ],
                "lang": "en"
              }
            ]
          }
        ],
        "ordered": True
      },
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "currentFanSpeedSetting": "speed_low",
      "currentFanSpeedPercent": -1,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.SPRINKLER",
    "traits": [
      "action.devices.traits.StartStop"
    ],
    "name": {
      "name": "Back Yard Zone 3",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Yard Sprinklers ",
    "attributes": {
      "pausable": False,
      "availableZones": [
        "kitchen",
        "bedroom",
        "living room"
      ]
    },
    "states": {
      "isPaused": False,
      "isRunning": False,
      "activeZones": [],
      "expectedStartStopCompletionUnixTimestampSec": 0,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
      "action.devices.traits.OnOff"
    ],
    "name": {
      "name": "Cherry Tree Lights",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.SWITCH",
    "traits": [
      "action.devices.traits.OnOff"
    ],
    "name": {
      "name": "Pool Speakers",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
      "name": "Garden Outlet",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False
    },
    "states": {
      "on": False,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.SPRINKLER",
    "traits": [
      "action.devices.traits.StartStop"
    ],
    "name": {
      "name": "Garden Zone 2",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Garden Sprinklers",
    "attributes": {
      "pausable": False,
      "availableZones": [
        "kitchen",
        "bedroom",
        "living room"
      ]
    },
    "states": {
      "isPaused": False,
      "isRunning": False,
      "activeZones": [],
      "expectedStartStopCompletionUnixTimestampSec": 0,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.THERMOSTAT",
    "traits": [
      "action.devices.traits.TemperatureSetting"
    ],
    "name": {
      "name": "Pool Temperature",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "availableThermostatModes": [
        "auto"
      ],
      "thermostatTemperatureUnit": "F",
      "commandOnlyTemperatureSetting": False,
      "queryOnlyTemperatureSetting": True,
      "bufferRangeCelsius": 2,
      "thermostatTemperatureRange": {
        "minThresholdCelsius": 20,
        "maxThresholdCelsius": 30
      },
      "_lastThermostatMode": "auto"
    },
    "states": {
      "thermostatMode": "auto",
      "thermostatTemperatureSetpoint": 26,
      "thermostatTemperatureAmbient": 100,
      "thermostatTemperatureSetpointHigh": 0,
      "thermostatTemperatureSetpointLow": 0,
      "thermostatHumidityAmbient": 0,
      "activeThermostatMode": "none",
      "targetTempReachedEstimateUnixTimestampSec": 1680717206,
      "thermostatTemperaturePreset": "",
      "activeThermostatTemperatureHold": {},
      "thermostatActivityStatus": [],
      "activeThermostatTemperatureSensorIds": [],
      "thermostatAverageTemperatureAmbient": 0,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.SPRINKLER",
    "traits": [
      "action.devices.traits.StartStop"
    ],
    "name": {
      "name": "Garden Zone 1",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Garden Sprinklers",
    "attributes": {
      "pausable": False,
      "availableZones": [
        "kitchen",
        "bedroom",
        "living room"
      ]
    },
    "states": {
      "isPaused": False,
      "isRunning": False,
      "activeZones": [],
      "expectedStartStopCompletionUnixTimestampSec": 0,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.SPRINKLER",
    "traits": [
      "action.devices.traits.StartStop"
    ],
    "name": {
      "name": "Garden Zone 3",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Garden Sprinklers",
    "attributes": {
      "pausable": False,
      "availableZones": [
        "kitchen",
        "bedroom",
        "living room"
      ]
    },
    "states": {
      "isPaused": False,
      "isRunning": False,
      "activeZones": [],
      "expectedStartStopCompletionUnixTimestampSec": 0,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.SPRINKLER",
    "traits": [
      "action.devices.traits.StartStop"
    ],
    "name": {
      "name": "Back Yard Zone 1",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "pausable": False,
      "availableZones": [
        "kitchen",
        "bedroom",
        "living room"
      ]
    },
    "states": {
      "isPaused": False,
      "isRunning": False,
      "activeZones": [],
      "expectedStartStopCompletionUnixTimestampSec": 0,
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
        "type": "action.devices.types.SWITCH",
    "traits": [
      "action.devices.traits.OnOff",
      "action.devices.traits.Toggles"
    ],
    "name": {
      "name": "Pool Ionizer",
      "defaultNames": [],
      "nicknames": []
    },
    "willReportState": True,
    "roomHint": "Playground",
    "attributes": {
      "commandOnlyOnOff": False,
      "queryOnlyOnOff": False,
      "availableToggles": [
        {
          "name": "filter_toggle",
          "name_values": [
            {
              "name_synonym": [
                "filtered",
                "filter"
              ],
              "lang": "en"
            }
          ]
        }
      ],
      "commandOnlyToggles": False,
      "queryOnlyToggles": False
    },
    "states": {
      "on": False,
      "currentToggleSettings": {
        "filter_toggle": False
      },
      "online": True,
      "onlineStatusDetails": "STATE_UNSPECIFIED"
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
    ok = s.connect("test","password",False)
    
    #print (s.create_db("google"))
    #print (s.add_section("devices"))

    s.use_db('google','devices')
    while ok:
        print('?: ')
        data = input()
        if len(data) > 0:
            ok = data != "done"
            if ok:

                #print (s.create_db("google"))
                #print (s.add_section("devices"))
                print (s.set_id_generator(generator))
                ids = s.add_many(payload,True)
                for id in ids:
                    print (f"{id} -- {s.get_by_id(id)}")
                devices = s.get_all_by_section()
                for d in devices: 
                    print (devices[d])
    s.close()

if __name__ == "__main__":
    main()



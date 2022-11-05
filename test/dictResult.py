dictElizabeth = {
        "$type": "Tfl.Api.Presentation.Entities.Line, Tfl.Api.Presentation.Entities",
        "id": "elizabeth",
        "name": "Elizabeth line",
        "modeName": "elizabeth-line",
        "disruptions": [],
        "created": "2022-10-27T10:54:54.127Z",
        "modified": "2022-10-27T10:54:54.127Z",
        "lineStatuses": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineStatus, Tfl.Api.Presentation.Entities",
                "id": 0,
                "lineId": "elizabeth",
                "statusSeverity": 5,
                "statusSeverityDescription": "Part Closure",
                "reason": "ELIZABETH LINE: Saturday 29 and Sunday 30 October, no service between Paddington and Abbey Wood.",
                "created": "0001-01-01T00:00:00",
                "validityPeriods": [
                    {
                        "$type": "Tfl.Api.Presentation.Entities.ValidityPeriod, Tfl.Api.Presentation.Entities",
                        "fromDate": "2022-10-29T03:30:00Z",
                        "toDate": "2022-10-31T01:29:00Z",
                        "isNow": False
                    }
                ],
                "disruption": {
                    "$type": "Tfl.Api.Presentation.Entities.Disruption, Tfl.Api.Presentation.Entities",
                    "category": "PlannedWork",
                    "categoryDescription": "PlannedWork",
                    "description": "ELIZABETH LINE: Saturday 29 and Sunday 30 October, no service between Paddington and Abbey Wood.",
                    "created": "2022-06-06T07:36:00Z",
                    "affectedRoutes": [
                        {
                            "$type": "Tfl.Api.Presentation.Entities.DisruptedRoute, Tfl.Api.Presentation.Entities",
                            "id": "1183",
                            "name": "Paddington - Abbey Wood",
                            "direction": "inbound",
                            "originationName": "Paddington",
                            "destinationName": "Abbey Wood",
                            "isEntireRouteSection": True,
                            "routeSectionNaptanEntrySequence": [
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 0,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GPADTLL",
                                        "modes": [],
                                        "icsCode": "1001221",
                                        "stationNaptan": "910GPADTLL",
                                        "hubNaptanCode": "HUBPAD",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GPADTLL",
                                        "commonName": "Paddington",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                },
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 1,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GBONDST",
                                        "modes": [],
                                        "icsCode": "1000025",
                                        "stationNaptan": "910GBONDST",
                                        "hubNaptanCode": "HUBBDS",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GBONDST",
                                        "commonName": "Bond Street",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                },
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 2,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GTOTCTRD",
                                        "modes": [],
                                        "icsCode": "1000235",
                                        "stationNaptan": "910GTOTCTRD",
                                        "hubNaptanCode": "HUBTCR",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GTOTCTRD",
                                        "commonName": "Tottenham Court Road",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                },
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 3,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GFRNDXR",
                                        "modes": [],
                                        "icsCode": "1000080",
                                        "stationNaptan": "910GFRNDXR",
                                        "hubNaptanCode": "HUBZFD",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GFRNDXR",
                                        "commonName": "Farringdon",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                },
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 4,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GLIVSTLL",
                                        "modes": [],
                                        "icsCode": "1000138",
                                        "stationNaptan": "910GLIVSTLL",
                                        "hubNaptanCode": "HUBLST",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GLIVSTLL",
                                        "commonName": "Liverpool Street",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                },
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 5,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GWCHAPXR",
                                        "modes": [],
                                        "icsCode": "1000268",
                                        "stationNaptan": "910GWCHAPXR",
                                        "hubNaptanCode": "HUBZWL",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GWCHAPXR",
                                        "commonName": "Whitechapel",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                },
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 6,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GCANWHRF",
                                        "modes": [],
                                        "icsCode": "1002163",
                                        "stationNaptan": "910GCANWHRF",
                                        "hubNaptanCode": "HUBCAW",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GCANWHRF",
                                        "commonName": "Canary Wharf",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                },
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 7,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GCSTMHSXR",
                                        "modes": [],
                                        "icsCode": "1001079",
                                        "stationNaptan": "910GCSTMHSXR",
                                        "hubNaptanCode": "HUBCUS",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GCSTMHSXR",
                                        "commonName": "Custom House",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                },
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 8,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GWOLWXR",
                                        "modes": [],
                                        "icsCode": "1002162",
                                        "stationNaptan": "910GWOLWXR",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GWOLWXR",
                                        "commonName": "Woolwich",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                },
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 9,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GABWDXR",
                                        "modes": [],
                                        "icsCode": "1001001",
                                        "stationNaptan": "910GABWDXR",
                                        "hubNaptanCode": "HUBABW",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GABWDXR",
                                        "commonName": "Abbey Wood",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                }
                            ]
                        },
                        {
                            "$type": "Tfl.Api.Presentation.Entities.DisruptedRoute, Tfl.Api.Presentation.Entities",
                            "id": "1185",
                            "name": "Abbey Wood - Paddington",
                            "direction": "outbound",
                            "originationName": "Abbey Wood",
                            "destinationName": "Paddington",
                            "isEntireRouteSection": True,
                            "routeSectionNaptanEntrySequence": [
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 0,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GABWDXR",
                                        "modes": [],
                                        "icsCode": "1001001",
                                        "stationNaptan": "910GABWDXR",
                                        "hubNaptanCode": "HUBABW",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GABWDXR",
                                        "commonName": "Abbey Wood",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                },
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 1,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GWOLWXR",
                                        "modes": [],
                                        "icsCode": "1002162",
                                        "stationNaptan": "910GWOLWXR",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GWOLWXR",
                                        "commonName": "Woolwich",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                },
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 2,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GCSTMHSXR",
                                        "modes": [],
                                        "icsCode": "1001079",
                                        "stationNaptan": "910GCSTMHSXR",
                                        "hubNaptanCode": "HUBCUS",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GCSTMHSXR",
                                        "commonName": "Custom House",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                },
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 3,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GCANWHRF",
                                        "modes": [],
                                        "icsCode": "1002163",
                                        "stationNaptan": "910GCANWHRF",
                                        "hubNaptanCode": "HUBCAW",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GCANWHRF",
                                        "commonName": "Canary Wharf",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                },
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 4,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GWCHAPXR",
                                        "modes": [],
                                        "icsCode": "1000268",
                                        "stationNaptan": "910GWCHAPXR",
                                        "hubNaptanCode": "HUBZWL",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GWCHAPXR",
                                        "commonName": "Whitechapel",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                },
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 5,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GLIVSTLL",
                                        "modes": [],
                                        "icsCode": "1000138",
                                        "stationNaptan": "910GLIVSTLL",
                                        "hubNaptanCode": "HUBLST",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GLIVSTLL",
                                        "commonName": "Liverpool Street",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                },
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 6,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GFRNDXR",
                                        "modes": [],
                                        "icsCode": "1000080",
                                        "stationNaptan": "910GFRNDXR",
                                        "hubNaptanCode": "HUBZFD",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GFRNDXR",
                                        "commonName": "Farringdon",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                },
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 7,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GTOTCTRD",
                                        "modes": [],
                                        "icsCode": "1000235",
                                        "stationNaptan": "910GTOTCTRD",
                                        "hubNaptanCode": "HUBTCR",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GTOTCTRD",
                                        "commonName": "Tottenham Court Road",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                },
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 8,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GBONDST",
                                        "modes": [],
                                        "icsCode": "1000025",
                                        "stationNaptan": "910GBONDST",
                                        "hubNaptanCode": "HUBBDS",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GBONDST",
                                        "commonName": "Bond Street",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                },
                                {
                                    "$type": "Tfl.Api.Presentation.Entities.RouteSectionNaptanEntrySequence, Tfl.Api.Presentation.Entities",
                                    "ordinal": 9,
                                    "stopPoint": {
                                        "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                                        "naptanId": "910GPADTLL",
                                        "modes": [],
                                        "icsCode": "1001221",
                                        "stationNaptan": "910GPADTLL",
                                        "hubNaptanCode": "HUBPAD",
                                        "lines": [],
                                        "lineGroup": [],
                                        "lineModeGroups": [],
                                        "status": True,
                                        "id": "910GPADTLL",
                                        "commonName": "Paddington",
                                        "placeType": "StopPoint",
                                        "additionalProperties": [],
                                        "children": [],
                                        "lat": 0.0,
                                        "lon": 0.0
                                    }
                                }
                            ]
                        }
                    ],
                    "affectedStops": [
                        {
                            "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                            "naptanId": "910GPADTON",
                            "stationNaptan": "910GPADTON",
                            "status": True,
                            "id": "910GPADTON",
                            "commonName": "London Paddington Rail Station",
                            "lat": 0.0,
                            "lon": 0.0
                        },
                        {
                            "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                            "naptanId": "910GLIVST",
                            "stationNaptan": "910GLIVST",
                            "status": True,
                            "id": "910GLIVST",
                            "commonName": "London Liverpool Street Rail Station",
                            "lat": 0.0,
                            "lon": 0.0
                        },
                        {
                            "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                            "naptanId": "910GABWDXR",
                            "stationNaptan": "910GABWDXR",
                            "status": True,
                            "id": "910GABWDXR",
                            "commonName": "Abbey Wood",
                            "lat": 0.0,
                            "lon": 0.0
                        },
                        {
                            "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                            "naptanId": "910GBONDST",
                            "stationNaptan": "910GBONDST",
                            "status": True,
                            "id": "910GBONDST",
                            "commonName": "Bond Street",
                            "lat": 0.0,
                            "lon": 0.0
                        },
                        {
                            "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                            "naptanId": "910GCANWHRF",
                            "stationNaptan": "910GCANWHRF",
                            "status": True,
                            "id": "910GCANWHRF",
                            "commonName": "Canary Wharf",
                            "lat": 0.0,
                            "lon": 0.0
                        },
                        {
                            "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                            "naptanId": "910GCSTMHSXR",
                            "stationNaptan": "910GCSTMHSXR",
                            "status": True,
                            "id": "910GCSTMHSXR",
                            "commonName": "Custom House",
                            "lat": 0.0,
                            "lon": 0.0
                        },
                        {
                            "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                            "naptanId": "910GFRNDXR",
                            "stationNaptan": "910GFRNDXR",
                            "status": True,
                            "id": "910GFRNDXR",
                            "commonName": "Farringdon",
                            "lat": 0.0,
                            "lon": 0.0
                        },
                        {
                            "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                            "naptanId": "910GLIVSTLL",
                            "stationNaptan": "910GLIVSTLL",
                            "status": True,
                            "id": "910GLIVSTLL",
                            "commonName": "Liverpool Street",
                            "lat": 0.0,
                            "lon": 0.0
                        },
                        {
                            "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                            "naptanId": "910GPADTLL",
                            "stationNaptan": "910GPADTLL",
                            "status": True,
                            "id": "910GPADTLL",
                            "commonName": "Paddington",
                            "lat": 0.0,
                            "lon": 0.0
                        },
                        {
                            "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                            "naptanId": "910GTOTCTRD",
                            "stationNaptan": "910GTOTCTRD",
                            "status": True,
                            "id": "910GTOTCTRD",
                            "commonName": "Tottenham Court Road",
                            "lat": 0.0,
                            "lon": 0.0
                        },
                        {
                            "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                            "naptanId": "910GWCHAPXR",
                            "stationNaptan": "910GWCHAPXR",
                            "status": True,
                            "id": "910GWCHAPXR",
                            "commonName": "Whitechapel",
                            "lat": 0.0,
                            "lon": 0.0
                        },
                        {
                            "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                            "naptanId": "910GWOLWXR",
                            "stationNaptan": "910GWOLWXR",
                            "status": True,
                            "id": "910GWOLWXR",
                            "commonName": "Woolwich",
                            "lat": 0.0,
                            "lon": 0.0
                        }
                    ],
                    "closureText": "partClosure"
                }
            }
        ],
        "routeSections": [
            {
                "$type": "Tfl.Api.Presentation.Entities.MatchedRoute, Tfl.Api.Presentation.Entities",
                "name": "Reading Rail Station - London Paddington Rail Station",
                "direction": "inbound",
                "originationName": "Reading Rail Station",
                "destinationName": "London Paddington Rail Station",
                "originator": "910GRDNGSTN",
                "destination": "910GPADTON",
                "serviceType": "Regular",
                "validTo": "2022-12-31T00:00:00Z",
                "validFrom": "2022-10-08T00:00:00Z"
            },
            {
                "$type": "Tfl.Api.Presentation.Entities.MatchedRoute, Tfl.Api.Presentation.Entities",
                "name": "London Paddington Rail Station - Reading Rail Station",
                "direction": "outbound",
                "originationName": "London Paddington Rail Station",
                "destinationName": "Reading Rail Station",
                "originator": "910GPADTON",
                "destination": "910GRDNGSTN",
                "serviceType": "Regular",
                "validTo": "2022-12-31T00:00:00Z",
                "validFrom": "2022-10-08T00:00:00Z"
            },
            {
                "$type": "Tfl.Api.Presentation.Entities.MatchedRoute, Tfl.Api.Presentation.Entities",
                "name": "London Liverpool Street Rail Station - Shenfield Rail Station",
                "direction": "inbound",
                "originationName": "London Liverpool Street Rail Station",
                "destinationName": "Shenfield Rail Station",
                "originator": "910GLIVST",
                "destination": "910GSHENFLD",
                "serviceType": "Regular",
                "validTo": "2022-12-31T00:00:00Z",
                "validFrom": "2022-10-08T00:00:00Z"
            },
            {
                "$type": "Tfl.Api.Presentation.Entities.MatchedRoute, Tfl.Api.Presentation.Entities",
                "name": "Shenfield Rail Station - London Liverpool Street Rail Station",
                "direction": "outbound",
                "originationName": "Shenfield Rail Station",
                "destinationName": "London Liverpool Street Rail Station",
                "originator": "910GSHENFLD",
                "destination": "910GLIVST",
                "serviceType": "Regular",
                "validTo": "2022-12-31T00:00:00Z",
                "validFrom": "2022-10-08T00:00:00Z"
            },
            {
                "$type": "Tfl.Api.Presentation.Entities.MatchedRoute, Tfl.Api.Presentation.Entities",
                "name": "Paddington - Abbey Wood",
                "direction": "inbound",
                "originationName": "Paddington",
                "destinationName": "Abbey Wood",
                "originator": "910GPADTLL",
                "destination": "910GABWDXR",
                "serviceType": "Regular",
                "validTo": "2022-12-31T00:00:00Z",
                "validFrom": "2022-10-08T00:00:00Z"
            },
            {
                "$type": "Tfl.Api.Presentation.Entities.MatchedRoute, Tfl.Api.Presentation.Entities",
                "name": "Abbey Wood - Paddington",
                "direction": "outbound",
                "originationName": "Abbey Wood",
                "destinationName": "Paddington",
                "originator": "910GABWDXR",
                "destination": "910GPADTLL",
                "serviceType": "Regular",
                "validTo": "2022-12-31T00:00:00Z",
                "validFrom": "2022-10-08T00:00:00Z"
            },
            {
                "$type": "Tfl.Api.Presentation.Entities.MatchedRoute, Tfl.Api.Presentation.Entities",
                "name": "Heathrow Terminal 4 Rail Station - London Paddington Rail Station",
                "direction": "inbound",
                "originationName": "Heathrow Terminal 4 Rail Station",
                "destinationName": "London Paddington Rail Station",
                "originator": "910GHTRWTM4",
                "destination": "910GPADTON",
                "serviceType": "Regular",
                "validTo": "2022-12-31T00:00:00Z",
                "validFrom": "2022-10-08T00:00:00Z"
            },
            {
                "$type": "Tfl.Api.Presentation.Entities.MatchedRoute, Tfl.Api.Presentation.Entities",
                "name": "Heathrow Terminal 5 Rail Station - London Paddington Rail Station",
                "direction": "inbound",
                "originationName": "Heathrow Terminal 5 Rail Station",
                "destinationName": "London Paddington Rail Station",
                "originator": "910GHTRWTM5",
                "destination": "910GPADTON",
                "serviceType": "Regular",
                "validTo": "2022-12-31T00:00:00Z",
                "validFrom": "2022-10-08T00:00:00Z"
            },
            {
                "$type": "Tfl.Api.Presentation.Entities.MatchedRoute, Tfl.Api.Presentation.Entities",
                "name": "London Paddington Rail Station - Heathrow Terminal 4 Rail Station",
                "direction": "outbound",
                "originationName": "London Paddington Rail Station",
                "destinationName": "Heathrow Terminal 4 Rail Station",
                "originator": "910GPADTON",
                "destination": "910GHTRWTM4",
                "serviceType": "Regular",
                "validTo": "2022-12-31T00:00:00Z",
                "validFrom": "2022-10-08T00:00:00Z"
            },
            {
                "$type": "Tfl.Api.Presentation.Entities.MatchedRoute, Tfl.Api.Presentation.Entities",
                "name": "London Paddington Rail Station - Heathrow Terminal 5 Rail Station",
                "direction": "outbound",
                "originationName": "London Paddington Rail Station",
                "destinationName": "Heathrow Terminal 5 Rail Station",
                "originator": "910GPADTON",
                "destination": "910GHTRWTM5",
                "serviceType": "Regular",
                "validTo": "2022-12-31T00:00:00Z",
                "validFrom": "2022-10-08T00:00:00Z"
            }
        ],
        "serviceTypes": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities",
                "name": "Regular",
                "uri": "/Line/Route?ids=Elizabeth line&serviceTypes=Regular"
            }
        ],
        "crowding": {
            "$type": "Tfl.Api.Presentation.Entities.Crowding, Tfl.Api.Presentation.Entities"
        }
    }

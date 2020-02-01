# Device 9a:02:57:1e:8f:01, *** Make *** *** Model ***

## Test Roles

|  Role  |      Name              | Status |
|--------|------------------------|--------|
|Operator| *** Operator Name *** |        |
|Approver| *** Approver Name *** |        |

## Test Iteration

| Test             |                        |
|------------------|------------------------|
| Test report start date | 2019-10-22 09:34:33+00:00 |
| Test report end date   | 2019-10-22 09:41:18+00:00 |
| DAQ version      | 1.0.1 |
| Attempt number   | 1 |

## Device Identification

| Device            | Entry              |
|-------------------|--------------------|
| Name              | *** Name *** |
| GUID              | *** GUID *** |
| MAC addr          | 9a:02:57:1e:8f:01 |
| Hostname          | *** Network Hostname *** |
| Type              | *** Type *** |
| Make              | *** Make *** |
| Model             | *** Model *** |
| Serial Number     | *** Serial *** |
| Firmware Version  | *** Firmware Version *** |

## Device Description

![Image of device](*** Device Image URL ***)

*** Device Description ***


### Device documentation

[Device datasheets](*** Device Datasheets URL ***)
[Device manuals](*** Device Manuals URL ***)

## Report summary

Overall device result FAIL

|Category|Result|
|---|---|
|Security|PASS|
|Other|1/2|
|Connectivity|n/a|

|Expectation|pass|fail|skip|gone|
|---|---|---|---|---|
|Required|1|1|0|0|
|Recommended|1|0|0|0|
|Other|0|1|17|2|

|Result|Test|Category|Expectation|Notes|
|---|---|---|---|---|
|skip|base.switch.ping|Other|Other|No local IP has been set, check ext_loip in system.conf|
|pass|base.target.ping|Connectivity|Required|target reached|
|skip|cloud.udmi.pointset|Other|Other|No device id|
|fail|connection.mac_oui|Other|Other|Manufacturer prefix not found!|
|skip|connection.port_duplex|Other|Other|No local IP has been set, check ext_loip in system.conf|
|skip|connection.port_link|Other|Other|No local IP has been set, check ext_loip in system.conf|
|skip|connection.port_speed|Other|Other|No local IP has been set, check ext_loip in system.conf|
|fail|network.brute|Security|Required|Change the default password on the DUT|
|skip|poe.negotiation|Other|Other|No local IP has been set, check ext_loip in system.conf|
|skip|poe.power|Other|Other|No local IP has been set, check ext_loip in system.conf|
|skip|poe.support|Other|Other|No local IP has been set, check ext_loip in system.conf|
|skip|protocol.bacnet.pic|Other|Other|Bacnet device not found.|
|skip|protocol.bacnet.version|Other|Other|Bacnet device not found.|
|skip|security.firmware|Other|Other|Could not retrieve a firmware version with nmap. Check bacnet port.|
|skip|security.passwords.http|Other|Other|Could not lookup password info for mac-key 9a:02:57:1e:8f:01|
|skip|security.passwords.https|Other|Other|Could not lookup password info for mac-key 9a:02:57:1e:8f:01|
|skip|security.passwords.ssh|Other|Other|Could not lookup password info for mac-key 9a:02:57:1e:8f:01|
|skip|security.passwords.telnet|Other|Other|Could not lookup password info for mac-key 9a:02:57:1e:8f:01|
|pass|security.ports.nmap|Security|Recommended||
|skip|security.tls.v3|Other|Other||
|skip|security.x509|Other|Other||
|gone|unknown.fake.llama|Other|Other||
|gone|unknown.fake.monkey|Other|Other||
|pass|needless.nothing|Other|Other|Nothing happened|
|pass|needless.script.kiddie|Silly Python Scriptz|Other|The server is now down. hooray|


## Module ping

```
--------------------
Baseline ping test report
%% 61 packets captured.
LOCAL_IP not configured, assuming no network switch

Done with basic connectivity tests

--------------------
base.switch.ping
--------------------
Attempt to ping the OpenFlow compatible switch configured in system.conf
--------------------
See log above
--------------------
RESULT skip base.switch.ping No local IP has been set, check ext_loip in system.conf

--------------------
base.target.ping
--------------------
Attempt to ping the Device Under Test
--------------------
See log above
--------------------
RESULT pass base.target.ping target reached %% 10.20.70.164

```

## Module nmap

```
--------------------
security.ports.nmap
--------------------
Automatic TCP/UDP port scan using nmap
--------------------
Allowing 10000 open tcp snet-sensor-mgmt
No invalid ports found.
--------------------
RESULT pass security.ports.nmap 

```

## Module brute

```
--------------------
network.brute
--------------------
Educational test - not to be included in a production environment!
--------------------
Username:manager
Password:friend
Login success!
--------------------
RESULT fail network.brute Change the default password on the DUT

```

## Module discover

```
--------------------
security.firmware
--------------------
Automatic bacnet firmware scan using nmap
--------------------
PORT      STATE  SERVICE
47808/udp closed bacnet
MAC Address: 9A:02:57:1E:8F:01 (Unknown)
--------------------
RESULT skip security.firmware Could not retrieve a firmware version with nmap. Check bacnet port.

```

## Module switch

```
--------------------
connection.port_link
--------------------
Connect the device to the network switch. Check the device and the switch for the green connection light & no errors
--------------------
LOCAL_IP not configured, assuming no network switch.
--------------------
RESULT skip connection.port_link No local IP has been set, check ext_loip in system.conf

--------------------
connection.port_speed
--------------------
Verify the device auto-negotiates connection speed
--------------------
LOCAL_IP not configured, assuming no network switch.
--------------------
RESULT skip connection.port_speed No local IP has been set, check ext_loip in system.conf

--------------------
connection.port_duplex
--------------------
Verify the device supports full duplex
--------------------
LOCAL_IP not configured, assuming no network switch.
--------------------
RESULT skip connection.port_duplex No local IP has been set, check ext_loip in system.conf

--------------------
poe.power
--------------------
Verify that the device draws less than the maximum power allocated by the port. This is 15.4W for 802.3af and 30W for 802.3at
--------------------
LOCAL_IP not configured, assuming no network switch.
--------------------
RESULT skip poe.power No local IP has been set, check ext_loip in system.conf

--------------------
poe.negotiation
--------------------
Verify the device autonegotiates power requirements
--------------------
LOCAL_IP not configured, assuming no network switch.
--------------------
RESULT skip poe.negotiation No local IP has been set, check ext_loip in system.conf

--------------------
poe.support
--------------------
Verify if the device supports PoE
--------------------
LOCAL_IP not configured, assuming no network switch.
--------------------
RESULT skip poe.support No local IP has been set, check ext_loip in system.conf

```

## Module macoui

```
--------------------
connection.mac_oui
--------------------
Check Physical device address OUI against IEEE registration and verify it is registered with the correct manufacturer
--------------------
Using the host hardware address 9a:02:57:1e:8f:01
Mac OUI Test
--------------------
RESULT fail connection.mac_oui Manufacturer prefix not found!

```

## Module bacext

```
--------------------
protocol.bacnet.version
--------------------
Verify and record version of Bacnet used by the device
--------------------
 Bacnet device not found.
--------------------
RESULT skip protocol.bacnet.version Bacnet device not found.

--------------------
protocol.bacnet.pic
--------------------
Verify BACnet traffic is compliant to the PIC statement
--------------------
 Bacnet device not found... Pics check cannot be performed.
--------------------
RESULT skip protocol.bacnet.pic Bacnet device not found.

```

## Module tls

```
--------------------
Collecting TLS cert from target address %% 10.20.96.164
IOException unable to connect to server.

--------------------
security.tls.v3
--------------------
Verify the device supports TLS 1.2 or above (as a client)
--------------------
See log above
--------------------
RESULT skip security.tls.v3

--------------------
security.x509
--------------------
Verify the devices supports RFC 2459 - Internet X.509 Public Key Infrastructure Certificate and CRL Profile
--------------------
See log above
--------------------
RESULT skip security.x509

```

## Module password

```
--------------------
security.passwords.http
--------------------
Verify all default password have been updated. Ensure new Google provided passwords are set
--------------------
Redacted Log
--------------------
RESULT skip security.passwords.http Could not lookup password info for mac-key 9a:02:57:1e:8f:01

--------------------
security.passwords.https
--------------------
Verify all default password have been updated. Ensure new Google provided passwords are set
--------------------
Redacted Log
--------------------
RESULT skip security.passwords.https Could not lookup password info for mac-key 9a:02:57:1e:8f:01

--------------------
security.passwords.telnet
--------------------
Verify all default password have been updated. Ensure new Google provided passwords are set
--------------------
Redacted Log
--------------------
RESULT skip security.passwords.telnet Could not lookup password info for mac-key 9a:02:57:1e:8f:01

--------------------
security.passwords.ssh
--------------------
Verify all default password have been updated. Ensure new Google provided passwords are set
--------------------
Redacted Log
--------------------
RESULT skip security.passwords.ssh Could not lookup password info for mac-key 9a:02:57:1e:8f:01

```

## Module udmi

```
--------------------
cloud.udmi.pointset
--------------------
Validates device payload against the UDMI schema
--------------------
Device id is null, skipping.
--------------------
RESULT skip cloud.udmi.pointset No device id

```

## Module needless

```
--------------------
Running spurious DDoS script...
Sent 1 packet to 10.20.74.106 throught port:81
Sent 2 packet to 10.20.74.106 throught port:82
Sent 3 packet to 10.20.74.106 throught port:83
Sent 4 packet to 10.20.74.106 throught port:84
Sent 5 packet to 10.20.74.106 throught port:85
Sent 6 packet to 10.20.74.106 throught port:86
Sent 7 packet to 10.20.74.106 throught port:87
Sent 8 packet to 10.20.74.106 throught port:88
Sent 9 packet to 10.20.74.106 throught port:89
Sent 10 packet to 10.20.74.106 throught port:90
Sent 11 packet to 10.20.74.106 throught port:91
Sent 12 packet to 10.20.74.106 throught port:92
Sent 13 packet to 10.20.74.106 throught port:93
Sent 14 packet to 10.20.74.106 throught port:94
Sent 15 packet to 10.20.74.106 throught port:95
Sent 16 packet to 10.20.74.106 throught port:96
Sent 17 packet to 10.20.74.106 throught port:97
Sent 18 packet to 10.20.74.106 throught port:98
Sent 19 packet to 10.20.74.106 throught port:99
Sent 20 packet to 10.20.74.106 throught port:100
Sent 21 packet to 10.20.74.106 throught port:101
Sent 22 packet to 10.20.74.106 throught port:102
Sent 23 packet to 10.20.74.106 throught port:103
Sent 24 packet to 10.20.74.106 throught port:104
Sent 25 packet to 10.20.74.106 throught port:105
Sent 26 packet to 10.20.74.106 throught port:106
Sent 27 packet to 10.20.74.106 throught port:107
Sent 28 packet to 10.20.74.106 throught port:108
Sent 29 packet to 10.20.74.106 throught port:109
Sent 30 packet to 10.20.74.106 throught port:110
Sent 31 packet to 10.20.74.106 throught port:111
Sent 32 packet to 10.20.74.106 throught port:112
Sent 33 packet to 10.20.74.106 throught port:113
Sent 34 packet to 10.20.74.106 throught port:114
Sent 35 packet to 10.20.74.106 throught port:115
Sent 36 packet to 10.20.74.106 throught port:116
Sent 37 packet to 10.20.74.106 throught port:117
Sent 38 packet to 10.20.74.106 throught port:118
Sent 39 packet to 10.20.74.106 throught port:119
Sent 40 packet to 10.20.74.106 throught port:120
Sent 41 packet to 10.20.74.106 throught port:121
Sent 42 packet to 10.20.74.106 throught port:122
Sent 43 packet to 10.20.74.106 throught port:123
Sent 44 packet to 10.20.74.106 throught port:124
Sent 45 packet to 10.20.74.106 throught port:125
Sent 46 packet to 10.20.74.106 throught port:126
Sent 47 packet to 10.20.74.106 throught port:127
Sent 48 packet to 10.20.74.106 throught port:128
Sent 49 packet to 10.20.74.106 throught port:129
Sent 50 packet to 10.20.74.106 throught port:130
Sent 51 packet to 10.20.74.106 throught port:131
Sent 52 packet to 10.20.74.106 throught port:132
Sent 53 packet to 10.20.74.106 throught port:133
Sent 54 packet to 10.20.74.106 throught port:134
Sent 55 packet to 10.20.74.106 throught port:135
Sent 56 packet to 10.20.74.106 throught port:136
Sent 57 packet to 10.20.74.106 throught port:137
Sent 58 packet to 10.20.74.106 throught port:138
Sent 59 packet to 10.20.74.106 throught port:139
Sent 60 packet to 10.20.74.106 throught port:140
Sent 61 packet to 10.20.74.106 throught port:141
Sent 62 packet to 10.20.74.106 throught port:142
Sent 63 packet to 10.20.74.106 throught port:143
Sent 64 packet to 10.20.74.106 throught port:144
Sent 65 packet to 10.20.74.106 throught port:145
Sent 66 packet to 10.20.74.106 throught port:146
Sent 67 packet to 10.20.74.106 throught port:147
Sent 68 packet to 10.20.74.106 throught port:148
Sent 69 packet to 10.20.74.106 throught port:149
Sent 70 packet to 10.20.74.106 throught port:150
Sent 71 packet to 10.20.74.106 throught port:151
Sent 72 packet to 10.20.74.106 throught port:152
Sent 73 packet to 10.20.74.106 throught port:153
Sent 74 packet to 10.20.74.106 throught port:154
Sent 75 packet to 10.20.74.106 throught port:155
Sent 76 packet to 10.20.74.106 throught port:156
Sent 77 packet to 10.20.74.106 throught port:157
Sent 78 packet to 10.20.74.106 throught port:158
Sent 79 packet to 10.20.74.106 throught port:159
Sent 80 packet to 10.20.74.106 throught port:160
Sent 81 packet to 10.20.74.106 throught port:161
Sent 82 packet to 10.20.74.106 throught port:162
Sent 83 packet to 10.20.74.106 throught port:163
Sent 84 packet to 10.20.74.106 throught port:164
Sent 85 packet to 10.20.74.106 throught port:165
Sent 86 packet to 10.20.74.106 throught port:166
Sent 87 packet to 10.20.74.106 throught port:167
Sent 88 packet to 10.20.74.106 throught port:168
Sent 89 packet to 10.20.74.106 throught port:169
Sent 90 packet to 10.20.74.106 throught port:170
Sent 91 packet to 10.20.74.106 throught port:171
Sent 92 packet to 10.20.74.106 throught port:172
Sent 93 packet to 10.20.74.106 throught port:173
Sent 94 packet to 10.20.74.106 throught port:174
Sent 95 packet to 10.20.74.106 throught port:175
Sent 96 packet to 10.20.74.106 throught port:176
Sent 97 packet to 10.20.74.106 throught port:177
Sent 98 packet to 10.20.74.106 throught port:178
Sent 99 packet to 10.20.74.106 throught port:179
Sent 100 packet to 10.20.74.106 throught port:180
Sent 101 packet to 10.20.74.106 throught port:181
Sent 102 packet to 10.20.74.106 throught port:182
Sent 103 packet to 10.20.74.106 throught port:183
Sent 104 packet to 10.20.74.106 throught port:184
Sent 105 packet to 10.20.74.106 throught port:185
Sent 106 packet to 10.20.74.106 throught port:186
Sent 107 packet to 10.20.74.106 throught port:187
Sent 108 packet to 10.20.74.106 throught port:188
Sent 109 packet to 10.20.74.106 throught port:189
Sent 110 packet to 10.20.74.106 throught port:190
Sent 111 packet to 10.20.74.106 throught port:191
Sent 112 packet to 10.20.74.106 throught port:192
Sent 113 packet to 10.20.74.106 throught port:193
Sent 114 packet to 10.20.74.106 throught port:194
Sent 115 packet to 10.20.74.106 throught port:195
Sent 116 packet to 10.20.74.106 throught port:196
Sent 117 packet to 10.20.74.106 throught port:197
Sent 118 packet to 10.20.74.106 throught port:198
Sent 119 packet to 10.20.74.106 throught port:199
Sent 120 packet to 10.20.74.106 throught port:200
Sent 121 packet to 10.20.74.106 throught port:201
Sent 122 packet to 10.20.74.106 throught port:202
Sent 123 packet to 10.20.74.106 throught port:203
Sent 124 packet to 10.20.74.106 throught port:204
Sent 125 packet to 10.20.74.106 throught port:205
Sent 126 packet to 10.20.74.106 throught port:206
Sent 127 packet to 10.20.74.106 throught port:207
Sent 128 packet to 10.20.74.106 throught port:208
Sent 129 packet to 10.20.74.106 throught port:209
Sent 130 packet to 10.20.74.106 throught port:210
Sent 131 packet to 10.20.74.106 throught port:211
Sent 132 packet to 10.20.74.106 throught port:212
Sent 133 packet to 10.20.74.106 throught port:213
Sent 134 packet to 10.20.74.106 throught port:214
Sent 135 packet to 10.20.74.106 throught port:215
Sent 136 packet to 10.20.74.106 throught port:216
Sent 137 packet to 10.20.74.106 throught port:217
Sent 138 packet to 10.20.74.106 throught port:218
Sent 139 packet to 10.20.74.106 throught port:219
Sent 140 packet to 10.20.74.106 throught port:220
Sent 141 packet to 10.20.74.106 throught port:221
Sent 142 packet to 10.20.74.106 throught port:222
Sent 143 packet to 10.20.74.106 throught port:223
Sent 144 packet to 10.20.74.106 throught port:224
Sent 145 packet to 10.20.74.106 throught port:225
Sent 146 packet to 10.20.74.106 throught port:226
Sent 147 packet to 10.20.74.106 throught port:227
Sent 148 packet to 10.20.74.106 throught port:228
Sent 149 packet to 10.20.74.106 throught port:229
Sent 150 packet to 10.20.74.106 throught port:230
Sent 151 packet to 10.20.74.106 throught port:231
Sent 152 packet to 10.20.74.106 throught port:232
Sent 153 packet to 10.20.74.106 throught port:233
Sent 154 packet to 10.20.74.106 throught port:234
Sent 155 packet to 10.20.74.106 throught port:235
Sent 156 packet to 10.20.74.106 throught port:236
Sent 157 packet to 10.20.74.106 throught port:237
Sent 158 packet to 10.20.74.106 throught port:238
Sent 159 packet to 10.20.74.106 throught port:239
Sent 160 packet to 10.20.74.106 throught port:240
Sent 161 packet to 10.20.74.106 throught port:241
Sent 162 packet to 10.20.74.106 throught port:242
Sent 163 packet to 10.20.74.106 throught port:243
Sent 164 packet to 10.20.74.106 throught port:244
Sent 165 packet to 10.20.74.106 throught port:245
Sent 166 packet to 10.20.74.106 throught port:246
Sent 167 packet to 10.20.74.106 throught port:247
Sent 168 packet to 10.20.74.106 throught port:248
Sent 169 packet to 10.20.74.106 throught port:249
Sent 170 packet to 10.20.74.106 throught port:250
Sent 171 packet to 10.20.74.106 throught port:251
Sent 172 packet to 10.20.74.106 throught port:252
Sent 173 packet to 10.20.74.106 throught port:253
Sent 174 packet to 10.20.74.106 throught port:254
Sent 175 packet to 10.20.74.106 throught port:255
Sent 176 packet to 10.20.74.106 throught port:256
Sent 177 packet to 10.20.74.106 throught port:257
Sent 178 packet to 10.20.74.106 throught port:258
Sent 179 packet to 10.20.74.106 throught port:259
Sent 180 packet to 10.20.74.106 throught port:260
Sent 181 packet to 10.20.74.106 throught port:261
Sent 182 packet to 10.20.74.106 throught port:262
Sent 183 packet to 10.20.74.106 throught port:263
Sent 184 packet to 10.20.74.106 throught port:264
Sent 185 packet to 10.20.74.106 throught port:265
Sent 186 packet to 10.20.74.106 throught port:266
Sent 187 packet to 10.20.74.106 throught port:267
Sent 188 packet to 10.20.74.106 throught port:268
Sent 189 packet to 10.20.74.106 throught port:269
Sent 190 packet to 10.20.74.106 throught port:270
Sent 191 packet to 10.20.74.106 throught port:271
Sent 192 packet to 10.20.74.106 throught port:272
Sent 193 packet to 10.20.74.106 throught port:273
Sent 194 packet to 10.20.74.106 throught port:274
Sent 195 packet to 10.20.74.106 throught port:275
Sent 196 packet to 10.20.74.106 throught port:276
Sent 197 packet to 10.20.74.106 throught port:277
Sent 198 packet to 10.20.74.106 throught port:278
Sent 199 packet to 10.20.74.106 throught port:279
Sent 200 packet to 10.20.74.106 throught port:280
Sent 201 packet to 10.20.74.106 throught port:281
Sent 202 packet to 10.20.74.106 throught port:282
Sent 203 packet to 10.20.74.106 throught port:283
Sent 204 packet to 10.20.74.106 throught port:284
Sent 205 packet to 10.20.74.106 throught port:285
Sent 206 packet to 10.20.74.106 throught port:286
Sent 207 packet to 10.20.74.106 throught port:287
Sent 208 packet to 10.20.74.106 throught port:288
Sent 209 packet to 10.20.74.106 throught port:289
Sent 210 packet to 10.20.74.106 throught port:290
Sent 211 packet to 10.20.74.106 throught port:291
Sent 212 packet to 10.20.74.106 throught port:292
Sent 213 packet to 10.20.74.106 throught port:293
Sent 214 packet to 10.20.74.106 throught port:294
Sent 215 packet to 10.20.74.106 throught port:295
Sent 216 packet to 10.20.74.106 throught port:296
Sent 217 packet to 10.20.74.106 throught port:297
Sent 218 packet to 10.20.74.106 throught port:298
Sent 219 packet to 10.20.74.106 throught port:299
Sent 220 packet to 10.20.74.106 throught port:300
Sent 221 packet to 10.20.74.106 throught port:301
Sent 222 packet to 10.20.74.106 throught port:302
Sent 223 packet to 10.20.74.106 throught port:303
Sent 224 packet to 10.20.74.106 throught port:304
Sent 225 packet to 10.20.74.106 throught port:305
Sent 226 packet to 10.20.74.106 throught port:306
Sent 227 packet to 10.20.74.106 throught port:307
Sent 228 packet to 10.20.74.106 throught port:308
Sent 229 packet to 10.20.74.106 throught port:309
Sent 230 packet to 10.20.74.106 throught port:310
Sent 231 packet to 10.20.74.106 throught port:311
Sent 232 packet to 10.20.74.106 throught port:312
Sent 233 packet to 10.20.74.106 throught port:313
Sent 234 packet to 10.20.74.106 throught port:314
Sent 235 packet to 10.20.74.106 throught port:315
Sent 236 packet to 10.20.74.106 throught port:316
Sent 237 packet to 10.20.74.106 throught port:317
Sent 238 packet to 10.20.74.106 throught port:318
Sent 239 packet to 10.20.74.106 throught port:319
Sent 240 packet to 10.20.74.106 throught port:320
Sent 241 packet to 10.20.74.106 throught port:321
Sent 242 packet to 10.20.74.106 throught port:322
Sent 243 packet to 10.20.74.106 throught port:323
Sent 244 packet to 10.20.74.106 throught port:324
Sent 245 packet to 10.20.74.106 throught port:325
Sent 246 packet to 10.20.74.106 throught port:326
Sent 247 packet to 10.20.74.106 throught port:327
Sent 248 packet to 10.20.74.106 throught port:328
Sent 249 packet to 10.20.74.106 throught port:329
Sent 250 packet to 10.20.74.106 throught port:330
Sent 251 packet to 10.20.74.106 throught port:331
Sent 252 packet to 10.20.74.106 throught port:332
Sent 253 packet to 10.20.74.106 throught port:333
Sent 254 packet to 10.20.74.106 throught port:334
Sent 255 packet to 10.20.74.106 throught port:335
Sent 256 packet to 10.20.74.106 throught port:336
Sent 257 packet to 10.20.74.106 throught port:337
Sent 258 packet to 10.20.74.106 throught port:338
Sent 259 packet to 10.20.74.106 throught port:339
Sent 260 packet to 10.20.74.106 throught port:340
Sent 261 packet to 10.20.74.106 throught port:341
Sent 262 packet to 10.20.74.106 throught port:342
Sent 263 packet to 10.20.74.106 throught port:343
Sent 264 packet to 10.20.74.106 throught port:344
Sent 265 packet to 10.20.74.106 throught port:345
Sent 266 packet to 10.20.74.106 throught port:346
Sent 267 packet to 10.20.74.106 throught port:347
Sent 268 packet to 10.20.74.106 throught port:348
Sent 269 packet to 10.20.74.106 throught port:349
Sent 270 packet to 10.20.74.106 throught port:350
Sent 271 packet to 10.20.74.106 throught port:351
Sent 272 packet to 10.20.74.106 throught port:352
Sent 273 packet to 10.20.74.106 throught port:353
Sent 274 packet to 10.20.74.106 throught port:354
Sent 275 packet to 10.20.74.106 throught port:355
Sent 276 packet to 10.20.74.106 throught port:356
Sent 277 packet to 10.20.74.106 throught port:357
Sent 278 packet to 10.20.74.106 throught port:358
Sent 279 packet to 10.20.74.106 throught port:359
Sent 280 packet to 10.20.74.106 throught port:360
Sent 281 packet to 10.20.74.106 throught port:361
Sent 282 packet to 10.20.74.106 throught port:362
Sent 283 packet to 10.20.74.106 throught port:363
Sent 284 packet to 10.20.74.106 throught port:364
Sent 285 packet to 10.20.74.106 throught port:365
Sent 286 packet to 10.20.74.106 throught port:366
Sent 287 packet to 10.20.74.106 throught port:367
Sent 288 packet to 10.20.74.106 throught port:368
Sent 289 packet to 10.20.74.106 throught port:369
Sent 290 packet to 10.20.74.106 throught port:370
Sent 291 packet to 10.20.74.106 throught port:371
Sent 292 packet to 10.20.74.106 throught port:372
Sent 293 packet to 10.20.74.106 throught port:373
Sent 294 packet to 10.20.74.106 throught port:374
Sent 295 packet to 10.20.74.106 throught port:375
Sent 296 packet to 10.20.74.106 throught port:376
Sent 297 packet to 10.20.74.106 throught port:377
Sent 298 packet to 10.20.74.106 throught port:378
Sent 299 packet to 10.20.74.106 throught port:379
Sent 300 packet to 10.20.74.106 throught port:380
Sent 301 packet to 10.20.74.106 throught port:381
Sent 302 packet to 10.20.74.106 throught port:382
Sent 303 packet to 10.20.74.106 throught port:383
Sent 304 packet to 10.20.74.106 throught port:384
Sent 305 packet to 10.20.74.106 throught port:385
Sent 306 packet to 10.20.74.106 throught port:386
Sent 307 packet to 10.20.74.106 throught port:387
Sent 308 packet to 10.20.74.106 throught port:388
Sent 309 packet to 10.20.74.106 throught port:389
Sent 310 packet to 10.20.74.106 throught port:390
Sent 311 packet to 10.20.74.106 throught port:391
Sent 312 packet to 10.20.74.106 throught port:392
Sent 313 packet to 10.20.74.106 throught port:393
Sent 314 packet to 10.20.74.106 throught port:394
Sent 315 packet to 10.20.74.106 throught port:395
Sent 316 packet to 10.20.74.106 throught port:396
Sent 317 packet to 10.20.74.106 throught port:397
Sent 318 packet to 10.20.74.106 throught port:398
Sent 319 packet to 10.20.74.106 throught port:399
Sent 320 packet to 10.20.74.106 throught port:400
Sent 321 packet to 10.20.74.106 throught port:401
Sent 322 packet to 10.20.74.106 throught port:402
Sent 323 packet to 10.20.74.106 throught port:403
Sent 324 packet to 10.20.74.106 throught port:404
Sent 325 packet to 10.20.74.106 throught port:405
Sent 326 packet to 10.20.74.106 throught port:406
Sent 327 packet to 10.20.74.106 throught port:407
Sent 328 packet to 10.20.74.106 throught port:408
Sent 329 packet to 10.20.74.106 throught port:409
Sent 330 packet to 10.20.74.106 throught port:410
Sent 331 packet to 10.20.74.106 throught port:411
Sent 332 packet to 10.20.74.106 throught port:412
Sent 333 packet to 10.20.74.106 throught port:413
Sent 334 packet to 10.20.74.106 throught port:414
Sent 335 packet to 10.20.74.106 throught port:415
Sent 336 packet to 10.20.74.106 throught port:416
Sent 337 packet to 10.20.74.106 throught port:417
Sent 338 packet to 10.20.74.106 throught port:418
Sent 339 packet to 10.20.74.106 throught port:419
Sent 340 packet to 10.20.74.106 throught port:420
Sent 341 packet to 10.20.74.106 throught port:421
Sent 342 packet to 10.20.74.106 throught port:422
Sent 343 packet to 10.20.74.106 throught port:423
Sent 344 packet to 10.20.74.106 throught port:424
Sent 345 packet to 10.20.74.106 throught port:425
Sent 346 packet to 10.20.74.106 throught port:426
Sent 347 packet to 10.20.74.106 throught port:427
Sent 348 packet to 10.20.74.106 throught port:428
Sent 349 packet to 10.20.74.106 throught port:429
Sent 350 packet to 10.20.74.106 throught port:430
Sent 351 packet to 10.20.74.106 throught port:431
Sent 352 packet to 10.20.74.106 throught port:432
Sent 353 packet to 10.20.74.106 throught port:433
Sent 354 packet to 10.20.74.106 throught port:434
Sent 355 packet to 10.20.74.106 throught port:435
Sent 356 packet to 10.20.74.106 throught port:436
Sent 357 packet to 10.20.74.106 throught port:437
Sent 358 packet to 10.20.74.106 throught port:438
Sent 359 packet to 10.20.74.106 throught port:439
Sent 360 packet to 10.20.74.106 throught port:440
Sent 361 packet to 10.20.74.106 throught port:441
Sent 362 packet to 10.20.74.106 throught port:442
Sent 363 packet to 10.20.74.106 throught port:443
Sent 364 packet to 10.20.74.106 throught port:444
Sent 365 packet to 10.20.74.106 throught port:445
Sent 366 packet to 10.20.74.106 throught port:446
Sent 367 packet to 10.20.74.106 throught port:447
Sent 368 packet to 10.20.74.106 throught port:448
Sent 369 packet to 10.20.74.106 throught port:449
Sent 370 packet to 10.20.74.106 throught port:450
Sent 371 packet to 10.20.74.106 throught port:451
Sent 372 packet to 10.20.74.106 throught port:452
Sent 373 packet to 10.20.74.106 throught port:453
Sent 374 packet to 10.20.74.106 throught port:454
Sent 375 packet to 10.20.74.106 throught port:455
Sent 376 packet to 10.20.74.106 throught port:456
Sent 377 packet to 10.20.74.106 throught port:457
Sent 378 packet to 10.20.74.106 throught port:458
Sent 379 packet to 10.20.74.106 throught port:459
Sent 380 packet to 10.20.74.106 throught port:460
Sent 381 packet to 10.20.74.106 throught port:461
Sent 382 packet to 10.20.74.106 throught port:462
Sent 383 packet to 10.20.74.106 throught port:463
Sent 384 packet to 10.20.74.106 throught port:464
Sent 385 packet to 10.20.74.106 throught port:465
Sent 386 packet to 10.20.74.106 throught port:466
Sent 387 packet to 10.20.74.106 throught port:467
Sent 388 packet to 10.20.74.106 throught port:468
Sent 389 packet to 10.20.74.106 throught port:469
Sent 390 packet to 10.20.74.106 throught port:470
Sent 391 packet to 10.20.74.106 throught port:471
Sent 392 packet to 10.20.74.106 throught port:472
Sent 393 packet to 10.20.74.106 throught port:473
Sent 394 packet to 10.20.74.106 throught port:474
Sent 395 packet to 10.20.74.106 throught port:475
Sent 396 packet to 10.20.74.106 throught port:476
Sent 397 packet to 10.20.74.106 throught port:477
Sent 398 packet to 10.20.74.106 throught port:478
Sent 399 packet to 10.20.74.106 throught port:479
Sent 400 packet to 10.20.74.106 throught port:480
Sent 401 packet to 10.20.74.106 throught port:481
Sent 402 packet to 10.20.74.106 throught port:482
Sent 403 packet to 10.20.74.106 throught port:483
Sent 404 packet to 10.20.74.106 throught port:484
Sent 405 packet to 10.20.74.106 throught port:485
Sent 406 packet to 10.20.74.106 throught port:486
Sent 407 packet to 10.20.74.106 throught port:487
Sent 408 packet to 10.20.74.106 throught port:488
Sent 409 packet to 10.20.74.106 throught port:489
Sent 410 packet to 10.20.74.106 throught port:490
Sent 411 packet to 10.20.74.106 throught port:491
Sent 412 packet to 10.20.74.106 throught port:492
Sent 413 packet to 10.20.74.106 throught port:493
Sent 414 packet to 10.20.74.106 throught port:494
Sent 415 packet to 10.20.74.106 throught port:495
Sent 416 packet to 10.20.74.106 throught port:496
Sent 417 packet to 10.20.74.106 throught port:497
Sent 418 packet to 10.20.74.106 throught port:498
Sent 419 packet to 10.20.74.106 throught port:499
Sent 420 packet to 10.20.74.106 throught port:500
Sent 421 packet to 10.20.74.106 throught port:501
Sent 422 packet to 10.20.74.106 throught port:502
Sent 423 packet to 10.20.74.106 throught port:503
Sent 424 packet to 10.20.74.106 throught port:504
Sent 425 packet to 10.20.74.106 throught port:505
Sent 426 packet to 10.20.74.106 throught port:506
Sent 427 packet to 10.20.74.106 throught port:507
Sent 428 packet to 10.20.74.106 throught port:508
Sent 429 packet to 10.20.74.106 throught port:509
Sent 430 packet to 10.20.74.106 throught port:510
Sent 431 packet to 10.20.74.106 throught port:511
Sent 432 packet to 10.20.74.106 throught port:512
Sent 433 packet to 10.20.74.106 throught port:513
Sent 434 packet to 10.20.74.106 throught port:514
Sent 435 packet to 10.20.74.106 throught port:515
Sent 436 packet to 10.20.74.106 throught port:516
Sent 437 packet to 10.20.74.106 throught port:517
Sent 438 packet to 10.20.74.106 throught port:518
Sent 439 packet to 10.20.74.106 throught port:519
Sent 440 packet to 10.20.74.106 throught port:520
Sent 441 packet to 10.20.74.106 throught port:521
Sent 442 packet to 10.20.74.106 throught port:522
Sent 443 packet to 10.20.74.106 throught port:523
Sent 444 packet to 10.20.74.106 throught port:524
Sent 445 packet to 10.20.74.106 throught port:525
Sent 446 packet to 10.20.74.106 throught port:526
Sent 447 packet to 10.20.74.106 throught port:527
Sent 448 packet to 10.20.74.106 throught port:528
Sent 449 packet to 10.20.74.106 throught port:529
Sent 450 packet to 10.20.74.106 throught port:530
Sent 451 packet to 10.20.74.106 throught port:531
Sent 452 packet to 10.20.74.106 throught port:532
Sent 453 packet to 10.20.74.106 throught port:533
Sent 454 packet to 10.20.74.106 throught port:534
Sent 455 packet to 10.20.74.106 throught port:535
Sent 456 packet to 10.20.74.106 throught port:536
Sent 457 packet to 10.20.74.106 throught port:537
Sent 458 packet to 10.20.74.106 throught port:538
Sent 459 packet to 10.20.74.106 throught port:539
Sent 460 packet to 10.20.74.106 throught port:540
Sent 461 packet to 10.20.74.106 throught port:541
Sent 462 packet to 10.20.74.106 throught port:542
Sent 463 packet to 10.20.74.106 throught port:543
Sent 464 packet to 10.20.74.106 throught port:544
Sent 465 packet to 10.20.74.106 throught port:545
Sent 466 packet to 10.20.74.106 throught port:546
Sent 467 packet to 10.20.74.106 throught port:547
Sent 468 packet to 10.20.74.106 throught port:548
Sent 469 packet to 10.20.74.106 throught port:549
Sent 470 packet to 10.20.74.106 throught port:550
Sent 471 packet to 10.20.74.106 throught port:551
Sent 472 packet to 10.20.74.106 throught port:552
Sent 473 packet to 10.20.74.106 throught port:553
Sent 474 packet to 10.20.74.106 throught port:554
Sent 475 packet to 10.20.74.106 throught port:555
Sent 476 packet to 10.20.74.106 throught port:556
Sent 477 packet to 10.20.74.106 throught port:557
Sent 478 packet to 10.20.74.106 throught port:558
Sent 479 packet to 10.20.74.106 throught port:559
Sent 480 packet to 10.20.74.106 throught port:560
Sent 481 packet to 10.20.74.106 throught port:561
Sent 482 packet to 10.20.74.106 throught port:562
Sent 483 packet to 10.20.74.106 throught port:563
Sent 484 packet to 10.20.74.106 throught port:564
Sent 485 packet to 10.20.74.106 throught port:565
Sent 486 packet to 10.20.74.106 throught port:566
Sent 487 packet to 10.20.74.106 throught port:567
Sent 488 packet to 10.20.74.106 throught port:568
Sent 489 packet to 10.20.74.106 throught port:569
Sent 490 packet to 10.20.74.106 throught port:570
Sent 491 packet to 10.20.74.106 throught port:571
Sent 492 packet to 10.20.74.106 throught port:572
Sent 493 packet to 10.20.74.106 throught port:573
Sent 494 packet to 10.20.74.106 throught port:574
Sent 495 packet to 10.20.74.106 throught port:575
Sent 496 packet to 10.20.74.106 throught port:576
Sent 497 packet to 10.20.74.106 throught port:577
Sent 498 packet to 10.20.74.106 throught port:578
Sent 499 packet to 10.20.74.106 throught port:579
Sent 500 packet to 10.20.74.106 throught port:580
PASSED writing report...
Running test that does nothing...
This test did nothing

--------------------
needless.nothing
--------------------
This test does absolutely nothing
--------------------
See log above
--------------------
RESULT pass needless.nothing Nothing happened

--------------------
needless.script.kiddie
--------------------
I found a script on the internet, now it's a DAQ test
--------------------
See log above
--------------------
RESULT pass needless.script.kiddie The server is now down. hooray

```

## Report complete


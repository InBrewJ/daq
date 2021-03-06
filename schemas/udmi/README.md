# UDMI Schema

The Universal Device Management Interface (UDMI) provides a high-level specification for the
management and operation of physical IoT systems. This data is typically exchanged
with a cloud entity that can maintain a "digital twin" or "shadow device" in the cloud.
Nominally meant for use with [Googe's Cloud IoT Core](https://cloud.google.com/iot/docs/),
as a schema it can be applied to any set of data or hosting setup. Additionally, the schema
has provisions for basic telemetry ingestion, such as datapoint streaming from an IoT device.

By deisgn, this schema is intended to be:
* <b>U</b>niversal: Apply to all subsystems in a building, not a singular vertical solution.
* <b>D</b>evice: Operations on an IoT _device_, a managed entity in physical space.
* <b>M</b>anagement: Focus on device _management_, rather than command & control.
* <b>I</b>nterface: Define an interface specification, rather than a client-library or
RPC mechanism.

See the associated [UDMI Tech Stack](TECH_STACK.md) for details about transport mechanism
outside of the core schema definition.

## Use Cases

The essence behind UDMI is an automated mechanism for IoT system management. Many current
systems require direct-to-device access, such as through a web browser or telnet/ssh session.
These techniques do not scale to robust managed ecosystems since they rely too heavily on
manual operation (aren't automated), and increase the security exposure of the system
(since they need to expose these management ports).

UDMI is intended to support a few primary use-cases:
* _Telemetry Ingestion_: Ingest device data points in a standardized format.
* _Device Testability_: e.g. Trigger a fake alarm to test reporting mechanims.
* _Commissioning Tools_: Streamline complete system setup and install.
* _Operational Diagnostics_: Make it easy for system operators to diagnoe basic faults.
* _Status and Logging_: Report system operational metrics to hosting infrastructure.
* _Key Rotation_: Manage encryption keys and certificates in accordance with best practice.
* _Credential Exchange_: Bootstrap higher-layer authentication to restricted resources.
* _Firmware Updates_: Initiate, monitor, and track firmware updates across an entire fleet
of devices.

All these situations are conceptually about _management_ of devices, which is conceptually
different than the _control_ or _operation_. These concepts are similar to the _management_,
_control_, and _data_ planes of
[Software Defined Networks](https://queue.acm.org/detail.cfm?id=2560327).
Once operational, the system should be able to operate completely autonomoulsy from the
management capabilities, which are only required to diagnose or tweak system behavior.

## Design Philiosphy

In order to provide for management automation, UDMI strives for the following principles:
* <b>Secure and Authenticated:</b> Requires a propertly secure and authenticated channel
from the device to managing infrastructure.
* <b>Declarative Specification:</b> The schema describes the _desired_ state of the system,
relying on the underlying mechanisms to match actual state with desired state. This is
conceptually similar to Kubernetes-style configuraiton files.
* <b>Minimal Elegant Design:</b> Initially underspecified, with an eye towards making it easy to
add new capabilities in the future. <em>It is easier to add something than it is to remove it.</em>
* <b>Reduced Choices:</b> In the long run, choice leads to more work
to implement, and more ambiguity. Strive towards having only _one_ way of doing each thing.
* <b>Structure and Clarity:</b> This is not a "compressed" format and not designed for
very large structures or high-bandwidth streams.
* <b>Property Names:</b>Uses <em>snake_case</em> convention for property names.
* <b>Resource Names:</b> Overall structure (when flattened to paths), follows the
[API Resource Names guidline](https://cloud.google.com/apis/design/resource_names).

## Schema Structure

Schemas are broken down into several top-level sub-schemas that are invoked for
different aspects of device management:
* Device _state_ ([example](state.tests/example.json)), sent from device to cloud,
defined by [<em>state.json</em>](state.json). There is one current 'state' message per device,
which is considered 'sicky' until a new state message is sent.
* Device _config_ ([example](config.tests/example.json)), passed from cloud to device,
defined by [<em>config.json</em>](config.json). There is one active 'config' message per device,
which should be considered current until a new config is recevied.
* Streaming _pointset_ ([example](pointset.tests/example.json)) from device to cloud,
defined by [<em>pointset.json</em>](pointset.json).
* Monitoring _logentry_ messages ([example](logentry.tests/example.json)) from devices,
defined by [<em>logentry.json</em>](logentry.json).
* Message _envelope_ ([example](envelope.tests/example.json)) for server-side
attributes, defined by [<em>envelope.json</em>](envelope.json).
* Device _metadata_ ([example](metadata.tests/example.json)) stored _about_ a device,
but not directly available to the device, defined by [<em>metadata.json</em>](metadata.json).
* Device _properties_ ([example](properties.tests/example.json)) which is used for
configuring a system (e.g., when registering a device with the cloud),
defined by [<em>properties.json</em>](properties.json).

A device client implementation will typically only be aware of the _state_, _config_,
_points_, _logentry_ messages, while all others are server-side only.

## Validation

To verify correct operation of a real system, follow the instructions outlined in the
[validator subsystem docs](../../docs/validator.md), which provides for a suitable
communication channel. Additional sample messages are easy to include in the regression
suite if there are new cases to test.

## Message Detail Notes

### State Message

* See notes below about 'State status' fields.
* There is an implicit minimum update interval of _one second_ applied to state updates, and it
is considered an error to update device state more often than that.
* `last_config` should be the timestamp _from_ the `timestamp` field of the last successfully
parsed `config` message.

### Config Message

* `max_update_ms`: Maximum time betwen telemetry updates. The system should proactively send an
update often enough to make sure it happens before this time. Typically, this means that the
entire necessary data set can be sent perodically at this interval.
* `min_update_ms`: Minimum time between point updates. Updates that happen faster than this time
(e.g. due to _cov_ events) should be coalessed so that only the most recent update is sent.
* `force_value`: Override value for a point to be used during diagnostics and diagnosis. Should
override any operational values, but not override alarm conditions.
* `min_loglevel`: Indicates the minimum loglevel for reporting log messages below which log entries
should not be sent. See note below for a description of the level value.

### Logentry Message

* See notes below about 'logentry entries' fields.

### State status and logentry entries fields

The State and Logentry messages both have `status` and `entries` sub-fields, respectivly, that
follow the same structure.
* State `status` entries represent 'sticky' conditions that persist until the situation is cleared,
e.g. "device disconnected".
* A `statuses` entry is a map of 'sticky' conditions that are keyed on a value that can be
used to manage updates by a particular (device dependent) subsystem.
* Logentry `entries` fields are transitory event that happen, e.g. "connection failed".
* The log `entries` field is an array that can be used to collaesce multiple log updates into
one message.
* Config parse errors should be represented as a system-level device state `status` entry.
* The `message` field sould be a one-line representation of the triggering condition.
* The `detail` field can be multi-line and include more detail, e.g. a complete program
stack-trace.
* The `category` field is a device-specific representation of which sub-system the message comes
from. In a Java environment, for example, it would be the fully qualified path name of the Class
triggering the message.
* A `status` or `statuses` `timestamp` field should be the timestamp the condition was triggered,
or most recently updated. It might be different than the top-level message `timestamp` if the
condition is not checked often or is sticky until it's cleared.
* A logentry `entries` `timestamp` field is the time that the event occured, which is potentially
different than the top-level `timestamp` field (which is when the log was sent).
* The status `level` should conform to the numerical
[Stackdriver LogEntry](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity)
levels. The `DEFAULT` value of 0 is not allowed (lowest value is 100, maximum 800).

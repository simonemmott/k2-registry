# K2 Registry

The K2 Registry is a simple framework for creating python registries.

## Design

Click [here](./docs/design/design.md) for the design details of the K2 Registry

## Installation

The K2 Registry is available via `pip` and is installed using `pip install k2-registry`

## Usage

### Add A Global Registration

Global registrations are applied to all items registered with all K2 Registry instances

The code snippet below shows how to define a registration function and register it as a global registration

```python
from k2.registry import registration

@registration()
def registerClass(cls):
    ...
    
```






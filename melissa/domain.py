import typing

# integer number (0, inf(
PositiveInteger = typing.NewType('PositiveInteger', int)

DamagePoints = typing.NewType('DamagePoints', float)

DamagedComponents = typing.NewType('DamagedComponents', typing.Mapping[str, PositiveInteger])

RepairTime = typing.NewType('RepairTime', float)

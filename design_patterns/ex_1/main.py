from design_patterns.ex_1.factories.modern_factory import ModernFactory
from design_patterns.ex_1.factories.victorian_factory import VictorianFactory

factory = VictorianFactory()

print(factory.create_sofa())
print(factory.create_table())
print(factory.create_sofa())
print(factory.create_chair())


modern_factory = ModernFactory()
print(modern_factory.create_table())


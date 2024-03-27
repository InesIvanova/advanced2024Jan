from design_patterns.ex_1.factories.abstract_furntiture_factory import AbstractFactory
from design_patterns.ex_1.furnitures.chair import Chair
from design_patterns.ex_1.furnitures.sofa import Sofa
from design_patterns.ex_1.furnitures.table import Table


class VictorianFactory(AbstractFactory):
    def create_sofa(self):
        return Sofa("Victorian")

    def create_chair(self):
        return Chair("Victorian")

    def create_table(self):
        return Table("Victorian")

import unittest
from pktools.PKVar import PKVar
from hypothesis import strategies, given, settings
import logging

logger = logging.getLogger('PKTools.PKVar')
logging.basicConfig()
logger.setLevel('DEBUG')

class PKVarTest(unittest.TestCase):
    @settings(max_examples=2E3)
   
    @given(val = strategies.floats(max_value=1E8), err = strategies.floats(min_value=0, max_value=1E4),
           val_2 = strategies.floats(max_value=1E8), err_2 = strategies.floats(min_value=0, max_value=1E4)
           )
    def test_pkvar_add(self, val, err, val_2, err_2):
        var_1 = PKVar(val, err)
        var_2 = PKVar(val_2, err_2)

        total = var_1 + var_2

        self.assertEqual(var_1.getVal()+var_2.getVal(), val+val_2)
        self.assertEqual(var_1.getError()+var_2.getError(), err+err_2)

    @given(val = strategies.floats(min_value=1E400, max_value=1E1000), err = strategies.floats(min_value=1E400, max_value=1E1000),
           val_2 = strategies.floats(min_value=1E400, max_value=1E1000), err_2 = strategies.floats(min_value=1E400, max_value=1E1000)
           )

    def test_pkvar_big_add(self, val, err, val_2, err_2):
        var_1 = PKVar(val, err)
        var_2 = PKVar(val_2, err_2)

        def try_add():
            return var_1 + var_2

        self.assertRaises(OverflowError, try_add)

if __name__ == "__main__":
    unittest.main()

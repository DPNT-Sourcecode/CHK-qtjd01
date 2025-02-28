from solutions.SUM import sum_solution
import pytest



class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_out_of_range(self):
        with pytest.raises(ValueError):
            sum_solution.compute(101, 2)

    def test_sum_input_not_int(self):
        with pytest.raises(ValueError):
            sum_solution.compute(1, "2")

    def test_sum_input_float(self):
        with pytest.raises(ValueError):
            sum_solution.compute(1, 2.0)




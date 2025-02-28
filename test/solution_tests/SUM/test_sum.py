from solutions.SUM import sum_solution
import pytest


class TestSum():
    def test_sum(self):
        assert sum_solution.sum_solution(1, 2) == 3

    def test_sum_out_of_range(self):
        with pytest.raises(ValueError) as excinfo:
            sum_solution.sum_solution(101, 2)
        assert "Input out of range" in str(excinfo.value)

    def test_sum_input_not_int(self):
        with pytest.raises(ValueError) as excinfo:
            sum_solution.sum_solution(1, "2")
        assert "Input not an integer" in str(excinfo.value)

    def test_sum_input_float(self):
        with pytest.raises(ValueError) as excinfo:
            sum_solution.sum_solution(1, 2.0)
        assert "Input not an integer" in str(excinfo.value)




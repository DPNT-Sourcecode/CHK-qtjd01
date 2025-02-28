from solutions.SUM import sum_solution
import pytest



class TestSum():
    def test_sum(self):
        assert sum_solution.sum_solution(1, 2) == 3

    def test_sum_out_of_range(self, capsys):
        with pytest.raises(ValueError):
                sum_solution.sum_solution(101, 2)
                assert "Input out of range" in capsys.readouterr().err

    def test_sum_input_not_int(self, capsys):
        with pytest.raises(ValueError):
                sum_solution.sum_solution(1, "2")
                assert "Input not an integer" in capsys.readouterr().err

    def test_sum_input_float(self, capsys):
        with pytest.raises(ValueError):
            sum_solution.sum_solution(1, 2.0)
            assert "Input not an integer" in capsys.readouterr().err





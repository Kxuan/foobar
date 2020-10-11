import sys
import os
import unittest

sys.path.append(os.getcwd())

import solution


class WidgetTestCase(unittest.TestCase):
    def test_s(self):
        self.assertEqual(solution.solution('1'), 0)
        self.assertEqual(solution.solution('2'), 1)
        self.assertEqual(solution.solution('3'), 2)
        self.assertEqual(solution.solution('4'), 2)
        self.assertEqual(solution.solution('5'), 3)
        self.assertEqual(solution.solution('6'), 3)
        self.assertEqual(solution.solution('7'), 4)
        self.assertEqual(solution.solution('8'), 3)
        self.assertEqual(solution.solution('9'), 4)
        self.assertEqual(solution.solution('10'), 4)
        self.assertEqual(solution.solution('11'), 5)
        self.assertEqual(solution.solution(
            '179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137216'),
            1024)
if __name__ == '__main__':
    unittest.main()

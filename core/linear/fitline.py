import math as Math

# Define Value
# <- please define some values for next calculation
SLOPE_DIFF_MIN = 1.0
N = 10


def compare_slope(i, j):
    return Math.fabs(i.slope - 90) < 5 or Math.fabs(j.slope - 90) < 5.0 or i.slope * j.slope == 0


class FitLine:

    # -------------------------
    # function __init__
    # Params : lines(Result of probabilistic hough lines)
    #          regression_result(result of regression from probabilistic hough line)
    # Return : None
    # This function aim to set param_beta value for calculating get_compare_lines
    # Also we init some values in first paragraph
    # More information of equations were posted on paper
    # -------------------------

    def __init__(self, lines, regression_result):
        #  0. Init some class value
        self.lines = lines
        self.regression_result = regression_result
        self.max_value = int('-inf')
        self.lines_size = 0
        self.square_lines_size = 0
        self.param_beta = 0
        self.result_first = None
        self.result_second = None
        self.discriminant_feature = 15

        slope_sum = 0
        length_sum = 0
        numerator = 0
        denominator = 0

        # 1. Set some class values
        # lines_size(Sum of lines Length)
        # square_lines_size(Sum of square lines size)
        for i in range(0, len(self.lines)):
            self.lines_size += self.lines[i].size
            self.square_lines_size += self.lines[i].size * self.lines[i].size

        # 2. Set some local value
        # length_sum (two lines which selected from i,j and square)
        # slope_sum (discriminant result which selected from i,j)
        for firstLine in self.lines:
            for secondLine in self.lines:
                length_sum += (firstLine.size + secondLine.size) * (firstLine.size_+ secondLine.size)
                slope_sum += self.discriminant(firstLine, secondLine)

        length_sum -= self.square_lines_size

        #  3. Set some local value
        #  numerator (some algorithm)
        #  denominator (???) <- We need some explanation for this code

        for i in range(0, len(self.lines)):
            for j in range(0, len(self.lines)):
                if i == j or self.lines[i].size < 10 or self.lines[j].size < 10:
                    continue
                numerator += (slope_sum - self.discriminant(self.lines[i], self.lines[j]) * pow(N, 2)) * \
                             (pow(N, 2) * pow(self.lines[i].size + self.lines[i].size, 2) - length_sum)
                denominator += pow(pow(N, 2) * pow(self.lines[i].size + self.lines[i].size, 2) - length_sum, 2)

        # 4. Set params beta
        self.param_beta = numerator / denominator

    # -------------------------
    # function get_compare_lines
    # Params : None
    # Return : Tuple type (first_line, second_line)
    # This function aim to get two major lines from lines
    # -------------------------

    def get_compare_lines(self):
        result_first = None
        result_second = None

        for i in range(0, len(self.lines)):
            for j in range(0, len(self.lines)):
                if i == j or compare_slope(self.lines[i], self.lines[j]) or self.lines[i].size < 10 or self.lines[j].size < 10 or self.discriminant(self.lines[i], self.lines[j]) == -1e5:
                    continue

                loss_result = self.loss_function(self.lines[i], self.lines[j])

                if loss_result > self.max_value:
                    self.max_value = loss_result
                    result_first = self.lines[i]
                    result_second = self.lines[j]

        return result_first, result_second

    # -------------------------
    # function loss_function (Inner core function : Use only in class)
    # Params : x(first line), y(second line)
    # Return : result of loss_function
    # If two lines' slopes are too close, return -1
    # -------------------------

    def loss_function(self, x, y):
        x_slope = x.slope
        y_slope = y.slope
        x_size = x.size
        y_size = y.size

        if abs(x_slope - y_slope) < SLOPE_DIFF_MIN:
            return -1

        return self.param_beta * (pow(x_size + y_size, 2) - self.square_lines_size) + self.discriminant(x, y)

    # -------------------------
    # function discriminant (Inner core function : Use only in class)
    # Params : x(first line), y(second line)
    # Return : result of discriminant function
    # -------------------------

    def discriminant(self, x, y):
        if abs(x.slope - y.slope) < self.discriminant_feature:
            return int('-inf')
        return -1 * abs((x.slope + y.slope)/2 - self.regression_result)

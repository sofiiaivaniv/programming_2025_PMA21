class Vec:
    def __init__(self, nums):
        self.nums = nums

    def __str__(self):
        return " ".join(map(str, self.nums))

    def add(self, other):
        return Vec([self.nums[i] + other.nums[i] for i in range(len(self.nums))])

    def sub(self, other):
        return Vec([self.nums[i] - other.nums[i] for i in range(len(self.nums))])

    def mul(self, other):
        return Vec([self.nums[i] * other.nums[i] for i in range(len(self.nums))])

    def div(self, other):
        result = []
        for i in range(len(self.nums)):
            if other.nums[i] != 0:
                result.append(self.nums[i] / other.nums[i])
            else:
                result.append("inf")
        return Vec(result)


def load_vectors(file_name):
    with open(file_name, "r") as f:
        lines = [l.strip() for l in f if l.strip()]
    if len(lines) < 2:
        print("Error: not enough vectors in file")
        exit()
    v1 = Vec([float(x) for x in lines[0].split()])
    v2 = Vec([float(x) for x in lines[1].split()])
    return v1, v2


def save_vectors(file_name, sum_v, diff_v, prod_v, div_v):
    with open(file_name, "w") as f:
        f.write("Sum:\n" + str(sum_v) + "\n")
        f.write("Difference:\n" + str(diff_v) + "\n")
        f.write("Product:\n" + str(prod_v) + "\n")
        f.write("Division:\n" + str(div_v) + "\n")


if __name__ == "__main__":
    v1, v2 = load_vectors("vectors.txt")
    print("Vectors:")
    print("V1:", v1)
    print("V2:", v2)

    sum_v = v1.add(v2)
    diff_v = v1.sub(v2)
    prod_v = v1.mul(v2)
    div_v = v1.div(v2)

    print("\nSum:", sum_v)
    print("Difference:", diff_v)
    print("Product:", prod_v)
    print("Division:", div_v)

    save_vectors("out.txt", sum_v, diff_v, prod_v, div_v)
    print("\nResults saved in out.txt")
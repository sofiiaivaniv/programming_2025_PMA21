file = open("vectors.txt", "r")
lines = file.readlines()
file.close()
if len(lines) < 2:
    print("Error: The file must contain at least two vectors.")
    exit()

v1 = list(map(float, lines[0].split()))
v2 = list(map(float, lines[1].split()))
print("Vectors:")
print("V1 =", v1)
print("V2 =", v2)
sum_result = [v1[i] + v2[i] for i in range(len(v1))]
diff_result = [v1[i] - v2[i] for i in range(len(v1))]
prod_result = [v1[i] * v2[i] for i in range(len(v1))]
div_result = [v1[i] / v2[i] if v2[i] != 0 else "inf" for i in range(len(v1))]

print("\nSum:", sum_result)
print("Difference:", diff_result)
print("Product:", prod_result)
print("Division:", div_result)

file_out = open("out.txt", "w")
file_out.write("Sum:\n" + " ".join(map(str, sum_result)) + "\n")
file_out.write("Difference:\n" + " ".join(map(str, diff_result)) + "\n")
file_out.write("Product:\n" + " ".join(map(str, prod_result)) + "\n")
file_out.write("Division:\n" + " ".join(map(str, div_result)) + "\n")
file_out.close()
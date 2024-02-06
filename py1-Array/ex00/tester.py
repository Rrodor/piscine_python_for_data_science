from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]

errHeight = [2.71, 1.15, 1.71]
errWeight = [165.3, 38.4]

err2Height = ["hey", "bonjour"]
err2Weight = [2.71, "bonjour"]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

errBmi = give_bmi(errHeight, errWeight)
print(errBmi, type(errBmi))
print(apply_limit(errBmi, 26))

err2Bmi = give_bmi(err2Height, err2Weight)
print(err2Bmi, type(err2Bmi))
print(apply_limit(err2Bmi, 26))

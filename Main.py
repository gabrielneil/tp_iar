import csv
import random
import numpy as np

# vars definition
x0 = []
x1 = []
x2 = []
x3 = []
x4 = []
y = []
w = []
u = []
errors = []
deltaW = []

# csv files reference
with open('X_train.csv', 'r') as x_train, open('Y_train.csv', 'r') as y_train:
    csv_x_train = csv.reader(x_train)
    csv_y_train = csv.reader(y_train)

    # loading X arrays
    for line in csv_x_train:
        x0.append(line[0])
        x1.append(line[1])
        x2.append(line[2])
        x3.append(line[3])
        x4.append(line[4])

        # loading Y array
        yAux = []
    for line in csv_y_train:
        yAux.append(line)

y = np.array(yAux)

# init random weights
for x in range(5):
    w.append(random.random())

# calculate
for x in range(x0.__len__()):
    oK = (float(x0[x]) * float(w[0])) + (float(x1[x]) * float(w[1])) + (float(x2[x]) * float(w[2])) + (
            float(x3[x]) * float(w[3])) + (float(x4[x]) * float(w[4]))
    u.append(oK)
    error = float(y[x]) - oK
    errors.append(error)
    preDeltaW = (0.2 * error)

print(errors)

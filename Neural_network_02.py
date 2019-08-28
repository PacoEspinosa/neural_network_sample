# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 21:01:58 2019

@author: fespinosa
"""

import numpy as np

class NeuralNetwork():
    
    def __init__(self):
        # seeding for random number generation
        np.random.seed(1)
        
        #converting weights to a 3 by 1 matrix with values from -1 to 1 and mean of 0
        self.synaptic_weights = 2 * np.random.random((13, 1)) - 1

    def sigmoid(self, x):
        #applying the sigmoid function
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        #computing derivative to the Sigmoid function
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        
        #training the model to make accurate predictions while adjusting weights continually
        for iteration in range(training_iterations):
            #siphon the training data via  the neuron
            output = self.think(training_inputs)

            #computing error rate for back-propagation
            error = training_outputs - output
            
            #performing weight adjustments
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))

            self.synaptic_weights += adjustments

    def think(self, inputs):
        #passing the inputs via the neuron to get output   
        #converting values to floats
        
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output


if __name__ == "__main__":

    #initializing the neuron class
    neural_network = NeuralNetwork()

    print("Beginning Randomly Generated Weights: ")
    print(neural_network.synaptic_weights)

    #training data consisting of 4 examples--3 input values and 1 output
    training_inputs = np.array(
            [
[3047,3176,11.7500,0.0125,9.4262,25,3,35,2.1277,0.7143,1.5198,3,7],
[3047,3201,12.7692,0.0136,9.7204,1,3,35,0.0783,0.0286,0.0022,1,21],
[3047,3201,12.7692,0.0136,9.7204,2,3,35,0.1566,0.0571,0.0089,1,15],
[3047,3201,12.7692,0.0136,9.7204,3,3,35,0.2349,0.0857,0.0201,1,13],
[3068,3201,12.8333,0.0136,10.1146,4,3,35,0.3117,0.1143,0.0356,1,12],
[3068,3201,12.8333,0.0136,10.1146,5,3,35,0.3896,0.1429,0.0557,1,11],
[3068,3201,12.8333,0.0136,10.1146,6,3,35,0.4675,0.1714,0.0801,1,6],
[3068,3201,12.8333,0.0136,10.1146,7,3,35,0.5455,0.2000,0.1091,2,24],
[3068,3201,12.8333,0.0136,10.1146,8,3,35,0.6234,0.2286,0.1425,2,24],
[3068,3201,12.8333,0.0136,10.1146,9,3,35,0.7013,0.2571,0.1803,2,22],
[3068,3201,12.8333,0.0136,10.1146,10,3,35,0.7792,0.2857,0.2226,2,19],
[3068,3201,12.8333,0.0136,10.1146,11,3,35,0.8571,0.3143,0.2694,2,16],
[3068,3201,12.8333,0.0136,10.1146,12,3,35,0.9351,0.3429,0.3206,2,15],
[3068,3201,12.8333,0.0136,10.1146,13,3,35,1.0130,0.3714,0.3762,2,13],
[3068,3201,12.8333,0.0136,10.1146,14,3,35,1.0909,0.4000,0.4364,2,14],
[3068,3201,12.8333,0.0136,10.1146,15,3,35,1.1688,0.4286,0.5009,2,13],
[3068,3201,12.8333,0.0136,10.1146,16,3,35,1.2468,0.4571,0.5699,2,12],
[3068,3201,12.8333,0.0136,10.1146,17,3,35,1.3247,0.4857,0.6434,2,10],
[3068,3201,12.8333,0.0136,10.1146,18,3,35,1.4026,0.5143,0.7214,2,6],
[3068,3201,12.8333,0.0136,10.1146,19,3,35,1.4805,0.5429,0.8038,2,3],
[3068,3201,12.8333,0.0136,10.1146,20,3,35,1.5584,0.5714,0.8905,2,2],
[3068,3201,12.8333,0.0136,10.1146,21,3,35,1.6364,0.6000,0.9818,2,1],
[3068,3222,13.4615,0.0143,9.9585,1,3,35,0.0743,0.0286,0.0021,1,22],
[3068,3222,13.4615,0.0143,9.9585,2,3,35,0.1486,0.0571,0.0085,1,18],
[3068,3222,13.4615,0.0143,9.9585,3,3,35,0.2229,0.0857,0.0191,1,14],
[3073,3222,12.8333,0.0136,10.1146,4,3,35,0.3117,0.1143,0.0356,1,9],
[3073,3222,12.8333,0.0136,10.1146,5,3,35,0.3896,0.1429,0.0557,1,5],
[3073,3222,12.8333,0.0136,10.1146,6,3,35,0.4675,0.1714,0.0801,1,2],
[3073,3222,12.8333,0.0136,10.1146,7,3,35,0.5455,0.2000,0.1091,2,24],
[3073,3222,12.8333,0.0136,10.1146,8,3,35,0.6234,0.2286,0.1425,2,23],
[3077,3222,13.5455,0.0144,10.2723,9,3,35,0.6644,0.2571,0.1708,2,17],
[3077,3222,13.5455,0.0144,10.2723,10,3,35,0.7383,0.2857,0.2109,2,12],
[3077,3232,13.2500,0.0141,9.8837,1,3,35,0.0755,0.0286,0.0022,1,19],
[3077,3232,13.2500,0.0141,9.8837,2,3,35,0.1509,0.0571,0.0086,1,16],
[3097,3232,14.0909,0.0150,9.9037,3,3,35,0.2129,0.0857,0.0182,1,14],
[3097,3232,14.0909,0.0150,9.9037,4,3,35,0.2839,0.1143,0.0324,1,11],
[3097,3232,14.0909,0.0150,9.9037,5,3,35,0.3548,0.1429,0.0507,1,4],
[3097,3232,14.0909,0.0150,9.9037,6,3,35,0.4258,0.1714,0.0730,1,2],
[3097,3232,14.0909,0.0150,9.9037,7,3,35,0.4968,0.2000,0.0994,2,22],
[3097,3232,14.0909,0.0150,9.9037,8,3,35,0.5677,0.2286,0.1298,2,18],
[3097,3232,14.0909,0.0150,9.9037,9,3,35,0.6387,0.2571,0.1642,2,18],
[3097,3241,13.6667,0.0145,9.5859,1,3,35,0.0732,0.0286,0.0021,1,26],
[3097,3242,12.6923,0.0135,9.8088,1,1,35,0.0788,0.0286,0.0023,1,21],
[3097,3242,12.6923,0.0135,9.8088,2,1,35,0.1576,0.0571,0.0090,1,14],
[3097,3244,11.9286,0.0127,9.8450,1,1,35,0.0838,0.0286,0.0024,1,22],
[3097,3244,11.9286,0.0127,9.8450,2,1,35,0.1677,0.0571,0.0096,1,17],
[3097,3244,11.9286,0.0127,9.8450,3,1,35,0.2515,0.0857,0.0216,1,11],
[3097,3244,11.9286,0.0127,9.8450,4,1,35,0.3353,0.1143,0.0383,1,9],
[3097,3244,11.9286,0.0127,9.8450,5,1,35,0.4192,0.1429,0.0599,1,5],
[3097,3244,11.9286,0.0127,9.8450,6,1,35,0.5030,0.1714,0.0862,1,1],
[3097,3250,11.5333,0.0122,9.6254,1,1,35,0.0867,0.0286,0.0025,1,23],
[3097,3250,11.5333,0.0122,9.6254,2,1,35,0.1734,0.0571,0.0099,1,15],
[3097,3250,11.5333,0.0122,9.6254,3,1,35,0.2601,0.0857,0.0223,1,12],
[3097,3253,11.0000,0.0117,9.5459,1,1,35,0.0909,0.0286,0.0026,1,23],
[3104,3254,9.8125,0.0104,9.5343,1,1,35,0.1019,0.0286,0.0029,1,25],
[3104,3254,9.8125,0.0104,9.5343,2,1,35,0.2038,0.0571,0.0116,1,15],
[3104,3254,9.8125,0.0104,9.5343,3,1,35,0.3057,0.0857,0.0262,1,6],
[3104,3254,9.8125,0.0104,9.5343,4,1,35,0.4076,0.1143,0.0466,1,4],
[3104,3254,9.8125,0.0104,9.5343,5,1,35,0.5096,0.1429,0.0728,1,4],
[3104,3254,9.8125,0.0104,9.5343,6,1,35,0.6115,0.1714,0.1048,2,24],
[3104,3254,9.8125,0.0104,9.5343,7,1,35,0.7134,0.2000,0.1427,2,19],
[3111,3254,10.0000,0.0106,9.8184,8,1,35,0.8000,0.2286,0.1829,2,17],
[3111,3254,10.0000,0.0106,9.8184,9,1,35,0.9000,0.2571,0.2314,2,15],
[3111,3263,9.9375,0.0105,9.5097,1,1,35,0.1006,0.0286,0.0029,1,23],
[3111,3264,9.4118,0.0100,9.4624,1,1,35,0.1062,0.0286,0.0030,1,24],
[3111,3264,9.4118,0.0100,9.4624,2,1,35,0.2125,0.0571,0.0121,1,19],
[3111,3264,9.4118,0.0100,9.4624,3,1,35,0.3187,0.0857,0.0273,1,9],
[3111,3264,9.4118,0.0100,9.4624,4,1,35,0.4250,0.1143,0.0486,1,9],
[3115,3264,9.5625,0.0102,9.7338,5,1,35,0.5229,0.1429,0.0747,1,5],
[3115,3264,9.5625,0.0102,9.7338,6,1,35,0.6275,0.1714,0.1076,2,25],
[3115,3264,9.5625,0.0102,9.7338,7,1,35,0.7320,0.2000,0.1464,2,22],
[3115,3264,9.5625,0.0102,9.7338,8,1,35,0.8366,0.2286,0.1912,2,17],
[3120,3264,9.9333,0.0105,9.9429,9,1,35,0.9060,0.2571,0.2329,2,14],
[3120,3273,9.8750,0.0105,9.6299,1,1,35,0.1013,0.0286,0.0029,1,20],
[3120,3273,9.8750,0.0105,9.6299,2,1,35,0.2025,0.0571,0.0116,1,13],
[3120,3275,9.4118,0.0100,9.5243,1,1,35,0.1062,0.0286,0.0030,1,20],
[3120,3275,9.4118,0.0100,9.5243,2,1,35,0.2125,0.0571,0.0121,1,16],
[3155,3275,9.6875,0.0103,9.7514,3,1,35,0.3097,0.0857,0.0265,1,10],
[3155,3275,9.6875,0.0103,9.7514,4,1,35,0.4129,0.1143,0.0472,1,8],
[3155,3275,9.6875,0.0103,9.7514,5,1,35,0.5161,0.1429,0.0738,1,3],
[3155,3275,9.6875,0.0103,9.7514,6,1,35,0.6194,0.1714,0.1062,2,24],
[3155,3275,9.6875,0.0103,9.7514,7,1,35,0.7226,0.2000,0.1445,2,23],
[3155,3275,9.6875,0.0103,9.7514,8,1,35,0.8258,0.2286,0.1888,2,19],
[3155,3275,9.6875,0.0103,9.7514,9,1,35,0.9290,0.2571,0.2388,2,14],
[3155,3284,9.6471,0.0102,9.4616,1,1,35,0.1037,0.0286,0.0030,1,23],
[3155,3285,9.1667,0.0097,9.4060,1,1,35,0.1091,0.0286,0.0031,1,19],
[3155,3285,9.1667,0.0097,9.4060,2,1,35,0.2182,0.0571,0.0125,1,12],
[3155,3285,9.1667,0.0097,9.4060,3,1,35,0.3273,0.0857,0.0280,1,7],
[3155,3285,9.1667,0.0097,9.4060,4,1,35,0.4364,0.1143,0.0499,1,7],
[3155,3285,9.1667,0.0097,9.4060,5,1,35,0.5455,0.1429,0.0780,1,2],
[3155,3285,9.1667,0.0097,9.4060,6,1,35,0.6545,0.1714,0.1122,2,18],
[3155,3285,9.1667,0.0097,9.4060,7,1,35,0.7636,0.2000,0.1527,2,18],
[3155,3285,9.1667,0.0097,9.4060,8,1,35,0.8727,0.2286,0.1995,2,18],
[3155,3293,9.1053,0.0097,9.1588,1,1,35,0.1098,0.0286,0.0031,1,22],
[3155,3293,9.1053,0.0097,9.1588,2,1,35,0.2197,0.0571,0.0125,1,12],
[3155,3293,9.1053,0.0097,9.1588,3,1,35,0.3295,0.0857,0.0282,1,8],
[3155,3293,9.1053,0.0097,9.1588,4,1,35,0.4393,0.1143,0.0502,1,4],
[3155,3293,9.1053,0.0097,9.1588,5,1,35,0.5491,0.1429,0.0785,1,2],
[3155,3293,9.1053,0.0097,9.1588,6,1,35,0.6590,0.1714,0.1130,2,19],
[3155,3293,9.1053,0.0097,9.1588,7,1,35,0.7688,0.2000,0.1538,2,15],
[3155,3293,9.1053,0.0097,9.1588,8,1,35,0.8786,0.2286,0.2008,2,12],
[3155,3293,9.1053,0.0097,9.1588,9,1,35,0.9884,0.2571,0.2541,2,10],
[3155,3293,9.1053,0.0097,9.1588,10,1,35,1.0983,0.2857,0.3138,2,9],
[3155,3293,9.1053,0.0097,9.1588,11,1,35,1.2081,0.3143,0.3797,2,9],
[3155,3293,9.1053,0.0097,9.1588,12,1,35,1.3179,0.3429,0.4519,2,6]
           ]
            )

    training_outputs = np.array([
	[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1]
            ]).T

    #training taking place
    neural_network.train(training_inputs, training_outputs, 150000)

    print("Ending Weights After Training: ")
    print(neural_network.synaptic_weights)

    user_input_01 = str(input("User Input One: "))
    user_input_02 = str(input("User Input Two: "))
    user_input_03 = str(input("User Input Three: "))
    user_input_04 = str(input("User Input Four: "))
    user_input_05 = str(input("User Input Five: "))
    user_input_06 = str(input("User Input Six: "))
    user_input_07 = str(input("User Input Seven: "))
    user_input_08 = str(input("User Input Eigth: "))
    user_input_09 = str(input("User Input Nine: "))
    user_input_10 = str(input("User Input Ten: "))
    user_input_11 = str(input("User Input Eleven: "))
    user_input_12 = str(input("User Input Twelve: "))
    user_input_13 = str(input("User Input Thirteen: "))
    
    print("Considering New Situation: ", user_input_01, user_input_02, user_input_03, user_input_04, user_input_05,
                                         user_input_06, user_input_07, user_input_08, user_input_09, user_input_10,
                                         user_input_11, user_input_12, user_input_13)
    print("New Output data: ")
    print(neural_network.think(np.array([user_input_01, user_input_02, user_input_03, user_input_04, user_input_05,
                                         user_input_06, user_input_07, user_input_08, user_input_09, user_input_10,
                                         user_input_11, user_input_12, user_input_13])))
    print("Wow, we did it!")
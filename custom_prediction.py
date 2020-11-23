from imageai.Prediction.Custom import CustomImagePrediction
import os

execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "idenprof_061-0.7933.h5")) #this is a path to a custom trained model
prediction.setJsonPath(os.path.join(execution_path, "model_class.json")) # link to the model AI json
prediction.loadModel(num_objects=10)

predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "4.jpg"), result_count=5) # 4.jpg is an image , am using for testing.

for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction + " : " + eachProbability)
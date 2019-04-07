import glob
import json
import sys

from watson_developer_cloud import VisualRecognitionV3

# classify all images in the folder with watson
def ask_watson_list(user_input=None):
    resp_l = []

    # target the specified file
    if user_input:
        target = user_input
    # classify all files in ./images/ folder
    else:
        target = './images/*.JPG'

    for file_path in glob.glob(target):

        with open(file_path, 'rb') as images_file:

            classes = visual_recognition.classify(
                images_file,
                threshold='0.7', # adjust this if you have to
                classifier_ids=["DDSBoxClassifier_218103930"]).get_result()

        resp = json.loads(json.dumps(classes, indent=2))

        classified_classes = resp['images'][0]['classifiers'][0]['classes']
        best_class = None
        best_score = float("-inf")
        for classf in classified_classes:
            if classf["score"] > best_score:
                best_class = classf["class"]
                best_score = classf["score"]

        # add tuple (img file path, classification)
        # 1 -> foco
        # 0 -> hop
        # -1 -> negative
        if best_class == 'Foco':
            resp_l.append((file_path, 1))
        elif best_class == 'Hop':
            resp_l.append((file_path, 0))
        else:
            # could not classify correctly with threshold
            resp_l.append((file_path, -1))

    return resp_l


visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='GuxXSF39chR9aY-sDfObQ4DbAv4gp3mbTJ69zeEfpb37')
# 
# if len(sys.argv) <= 2:
#     # print the result of classifying all images in `./images/*.JPG`
#     # make sure all images in the folder have the extension `.JPG` exactly
#     if len(sys.argv) == 1:
#         result = ask_watson_list()
#         print(result)
#     # print the specified image file classification
#     else:
#         result = ask_watson_list(sys.argv[1])
#         print(result[0])
#
# else:
#     print("You need to specify a path of an image file to classify (or classify everything in ./images/)")

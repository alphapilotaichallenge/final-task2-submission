# final-task2-submission

## 1 PDF file describing their algorithm in a 2-page Technical Report
## 1 zipped archive named ‘submission’ with maximum upload size of 250MB
In the folder named ‘submission’, at the highest level of the directory, please include the following:

### generate_results.py
Within this script, teams need to define their algorithm within the GenerateFinalDetections() class in the predict(self,img) function. This function is called within the generate_submission.py test script that reads all test images, imports and calls a team’s algorithm, and outputs labels for all images in a JSON file.
### requirements.txt
A file which lists libraries that need to be installed for an algorithm’s source code to run.
Other code
### Teams can include additional code in the directory as needed for your algorithms to run. This can be compiled libraries, source code, etc.
Teams SHOULD NOT include any of the following in their submitted archive:
Any code not needed for their algorithms to run
generate_submission.py as AlphaPilot will run our own version of this code
Scoring scripts as AlphaPilot will run our own version of this code

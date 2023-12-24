from students import students
from professors import professors
from databaseConnection import *

c = connection.cursor()

class stream():
    def __init__(self, streamName, streamID, streamDescription):
        self.streamName = streamName
        self.streamID = streamID
        self.streamDescription = streamDescription
    
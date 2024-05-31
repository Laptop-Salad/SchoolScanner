# Consumers/ReportGenerator
from Consumers.Consumer import Consumer
from Producers.GenerateReport import GenerateReport

class ReportGenerator(Consumer):
    """
    This is subscribed to the GenerateReport producer
    """
    subscribers = []

    def __init__(self, api_service):
        self.api_service = api_service

    def update(self, producer, *args):
        if isinstance(producer, GenerateReport):
            report = {
                       "data": [
                         {
                           "scatter-chart": {
                             "data": [
                               [
                                 [
                                   8,
                                   23
                                 ],
                                 100
                               ]
                             ],
                             "name": "Correlation between student punctuality and performance",
                             "x-axis": {
                               "name": "Punctuality",
                               "type": "entrytime"
                             },
                             "y-axis": {
                               "name": "Performance",
                               "type": "points"
                             }
                           },
                           "stacked-bar-chart": {
                             "name": "Punctuality throughout the week",
                             "data": [
                               {
                                 "name": "Late",
                                 "data": [
                                   1,
                                   5,
                                   10,
                                   2,
                                   9
                                 ]
                               },
                               {
                                 "name": "On time",
                                 "data": [
                                   99,
                                   95,
                                   90,
                                   98,
                                   91
                                 ]
                               }
                             ],
                             "x-axis": {
                               "categories": [
                                 "Monday",
                                 "Tuesday",
                                 "Wednesday",
                                 "Thursday",
                                 "Friday"
                               ]
                             }
                           }
                         }
                       ],
                       "name" : "Test 1 Week Report 2"
                     }

            self.api_service.post_report(report)



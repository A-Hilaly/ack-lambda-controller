import time

class Controller:
    def __init__(resource_manager):
        self.k8s_client = {}
        self.resource_manager = resource_manager
        
        self.event_stream = {}


    def start(self):
        # controller job
        while True:
            self.reconcile()
            time.sleep(3600)
            break

        for event in self.collect_events():
            self.reconcile(event)

    def collect_events(self, event_kind):
        return self.k8s_client.collect_recent_events_related_to(event_kind)

    def reconcile(self, event=None):
        if event == None:
            event = self.collect_event("Function")
            # [ {event_type = CREATE, spec:{}, metadata:{}}, {event_type = UPDATE, spec{}, metadata{}} ]

        if event.type == "Delete":
            try:
                aws_resouce = self.resource_manager.find(k8s_resource.name)
                self.resource_manager.delete(k8s_resource.name)
            except e as ResourceNotFound:
                return
        
        if event.type == "Create" or event.type == "Update":
            k8s_resource = event.Resource
            aws_resource = None
            try:
                aws_resouce = self.resource_manager.find(k8s_resource.name)
            except e as ResourceNotFound:
                aws_resouce = None

            if aws_resource == None:
                self.resource_manager.create(k8s_resource)
            else:
                differences = self.delta(aws_resource, k8s_resource)
                # differences = [ path: spec.handler , a = main, b = main2 ]
                if len(differences) != 0:
                    self.resource_manager.update(k8s_resource)


class LambdaResouceManager:
    def find(self):
        pass

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

if __main__ == "main":
    lambda_controller = Controller()
    lambda_controller.start()

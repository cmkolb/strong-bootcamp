class LogLinearModel(object):
    def __init__(self, n_epochs=10, l2=0):
        """
        Initialize the model.
        :param n_epochs:
        :param l2:
        """
        self.n_epochs = n_epochs

    def train(self):
        """
        Train the model. No response is required.
        """
        pass

    def validate(self):
        """
        Validate the model. Requires a response with the metrics defined in bootcamp.yml.
        """
        return {
            'AUC': .66
        }

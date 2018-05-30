from pathlib import Path
from eve import Eve
from awesomeio import settings
from awesomeio.hello import hello_endpoint

SETTINGS_PATH = Path(settings.__file__)


class AwesomeApp(Eve):

    def run(self, *args, **kwargs):
        self._bootstrap_custom_endpoints()
        self._bootstrap_events()
        super().run(*args, **kwargs)

    def _bootstrap_custom_endpoints(self):

        @self.route('/hello', methods=['GET'])
        def _():
            return hello_endpoint()

    def _bootstrap_events(self):
        pass


def main():
    app = AwesomeApp(settings=str(SETTINGS_PATH))
    app.run(host="0.0.0.0")


if __name__ == '__main__':
    main()

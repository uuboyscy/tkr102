class Crawler:
    def __init__(self: Crawler):
        pass

    def extract_process(self) -> str:
        pass

    def transform_process(self, extract_output: str) -> str:
        pass

    def load_to_destination(self, transformed_output: str) -> None:
        pass

    def run():
        extract_output = Crawler.extract_process()
        transformed_output = Crawler.transform_process(extract_output)
        Crawler.load_to_destination(transformed_output)

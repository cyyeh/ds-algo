# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        if not self.finish_time:
            self.finish_time.append(request.arrived_at + request.time_to_process)
            response = Response(False, request.arrived_at)
        else:
            for packet_finish_time in self.finish_time:
                if packet_finish_time <= request.arrived_at:
                    self.finish_time = self.finish_time[1:]
                else:
                    break

            if len(self.finish_time) == self.size:
                response = Response(True, -1)
            else:
                if self.finish_time:
                    response = Response(False, self.finish_time[-1])
                    self.finish_time.append(self.finish_time[-1] + request.time_to_process)
                else:
                    response = Response(False, request.arrived_at)
                    self.finish_time.append(request.arrived_at + request.time_to_process)

        return response


def process_requests(requests, buffer):
    return [buffer.process(request) for request in requests]


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()

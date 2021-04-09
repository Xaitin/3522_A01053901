import city_processor
from threading import Thread
import threading
import time


class CityOverheadTimeQueue:
    def __init__(self):
        self._data_queue = list()
        self.access_queue_lock = threading.Lock()

    def put(self, t: city_processor.CityOverheadTimes) -> None:
        with self.access_queue_lock:
            self._data_queue.insert(0, t)

    def get(self) -> city_processor.CityOverheadTimes:
        with self.access_queue_lock:
            data = self._data_queue[0]
            del self._data_queue[0]
            return data

    def __len__(self) -> int:
        with self.access_queue_lock:
            return self._data_queue.__len__()


class ProducerThread(Thread):
    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        super(ProducerThread, self).__init__()
        self.city_list = cities
        self.city_queue = queue

    def run(self) -> None:
        count = 0
        for city in self.city_list:
            count += 1
            self.city_queue.put(city_processor.ISSDataRequest.get_overhead_pass(city))
            if count % 5 == 0:
                time.sleep(1)


class ConsumerThread(Thread):
    def __init__(self, queue: CityOverheadTimeQueue):
        super(ConsumerThread, self).__init__()
        self.city_queue = queue
        self.data_incoming = True

    def run(self) -> None:
        while self.data_incoming or self.city_queue.__len__() > 0:
            if self.city_queue.__len__() == 0:
                time.sleep(0.75)
            print(self.city_queue.get())
            time.sleep(0.5)


def main():
    CD = city_processor.CityDatabase("city_locations.xlsx")
    cities = list()
    for city in CD.city_db:
        cities.append(city)
    a_third = int(cities.__len__() / 3)
    first_third = cities[0: a_third]
    second_third = cities[a_third + 1: a_third * 2]
    third_third = cities[a_third * 2 + 1: cities.__len__()]

    queue = CityOverheadTimeQueue()
    PT1 = ProducerThread(first_third, queue)
    PT2 = ProducerThread(second_third, queue)
    PT3 = ProducerThread(third_third, queue)
    CT = ConsumerThread(queue)
    PT1.start()
    PT2.start()
    PT3.start()
    CT.start()
    PT1.join()
    PT2.join()
    PT3.join()
    CT.data_incoming = False


if __name__ == '__main__':
    main()

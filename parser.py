import json
import math


def parser(iperf_result):
    return list(map(lambda interval: parse_interval(interval), json.loads(iperf_result.stdout)["intervals"]))


def parse_interval(interval):
    interval_sum = interval["sum"]
    return {
        "Interval": f"{interval_sum['start']:.{1}f}-{interval_sum['end']:.{1}f}",
        "Transfer": float(f"{interval_sum['bytes'] / math.pow(10, 6):.{2}f}"),
        "Transfer_unit": "MBytes",
        "Bandwidth": float(f"{interval_sum['bits_per_second'] / math.pow(10, 6):.{2}f}"),
        "Bandwidth_unit": "Mbits/sec"
    }


def parse_error(iperf_result):
    json_result = json.loads(iperf_result.stdout)
    return json_result["error"]

